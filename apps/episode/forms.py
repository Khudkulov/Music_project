
from django import forms

from .models import Episode


class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episode
        fields = ['title', 'filter', 'author', 'image', 'music', 'category', 'tags', 'description']
        exclude = ['author', 'filter']
