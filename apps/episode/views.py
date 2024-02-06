from msilib.schema import ListView

from django.shortcuts import render
from django.views.generic import TemplateView


class EpisodeListView(TemplateView):
    template_name = 'episode/episodes.html'
