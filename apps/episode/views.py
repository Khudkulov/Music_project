from django.views.generic import TemplateView, ListView, DetailView, CreateView


class EpisodeListView(TemplateView):
    template_name = 'episode/episode_list.html'


class EpisodeDetailView(TemplateView):
    template_name = 'episode/episode_detail.html'


class EpisodeAddView(TemplateView):
    template_name = 'episode/episode_add.html'
