from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.html import strip_tags

# from .tasks import send_mail_task


class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'image', 'password1', 'password2']



class MyPasswordResetForm(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):

        subject = loader.render_to_string(subject_template_name, context)
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        plain_message = strip_tags(body)


        send_mail_task.apply_async(("Reset Password", plain_message, [to_email], subject))

