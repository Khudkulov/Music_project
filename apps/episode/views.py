from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Episode, EpisodeComment, EpisodeFilter, EpisodeLike
from apps.blog.models import Category, Tag
from .forms import EpisodeForm



class EpisodeListView(ListView):
    queryset = Episode.objects.all()
    paginate_by = 25

    def get_categories(self):
        return Category.objects.all()

    def get_tags(self):
        return Tag.objects.all()

    def get_episode_filter(self):
        return EpisodeFilter.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = self.get_categories()
        ctx['tags'] = self.get_tags()
        ctx['episode_filter'] = self.get_episode_filter()

        return ctx

class EpisodeDetailView(DetailView):
    queryset = Episode.objects.all()
    slug_field = 'slug'

    def get_categories(self):
        return Category.objects.all()

    def get_tags(self):
        return Tag.objects.all()

    def get_comments(self):
        return EpisodeComment.objects.filter(episode=self.get_object(), parent__isnull=True).order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = self.get_categories()
        ctx['tags'] = self.get_tags()
        ctx['comments'] = self.get_comments()

        return ctx

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        comment = request.POST.get('comment')
        pid = request.GET.get('pid', None)
        if comment:
            instance = self.get_object()
            user = request.user
            EpisodeComment.objects.create(episode_id=instance.id, author_id=user.id, parent_id=pid, comment=comment)
            return redirect(".#comments")
        messages.error(request, "Comment is empty")
        return redirect('.')




class EpisodeAddView(View):
    template_name = 'episode/add_music.html'
    form_class = EpisodeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        ctx = {
            'form': form
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            episode = form.save(commit=False)
            episode.author = request.user
            episode.save()
            episode.filter.add(EpisodeFilter.objects.get(filter='.mine'))
            messages.success(request, 'New music successfully added')
            return redirect('episode:list')

        raise ValidationError(f"{form.errors}")



class LikeRedirectView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    def get(self, request, *args, **kwargs):
        eid = self.kwargs.get('eid')
        path = request.GET.get('next')
        if request.user.episodelike_set.filter(episode_id=eid).exists():
            request.user.episodelike_set.filter(episode_id=eid).delete()
            messages.success(request, 'disliked')
        else:
            EpisodeLike.objects.create(author_id=request.user.id, episode_id=eid)
            messages.success(request, 'liked')
        return redirect(path)

