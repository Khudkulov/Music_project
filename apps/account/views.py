from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, View
from django.contrib.auth.views import auth_logout
from django.contrib import messages
from .form import UserRegisterForm
from .models import ProfilePicture


class RegistrateView(View):
    template_name = 'account/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if request.FILES:
                ProfilePicture.objects.create(user_id=user.id, picture=request.FILES.get('image'))
                messages.success(request, 'Successfully registered')
        return redirect(reverse_lazy('account:login'))


class LoginView(TemplateView):
    template_name = 'account/login.html'


class LogoutView(View):
    template_name = 'account/log_out.html'

    def get(self, request,  *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('/')
