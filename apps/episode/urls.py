from django.urls import path

from .views import EpisodeListView, EpisodeDetailView

app_name = 'episode'

urlpatterns = [
    path('list/', EpisodeListView.as_view(), name='list'),
    path('detail/', EpisodeDetailView.as_view(), name='detail'),
]
