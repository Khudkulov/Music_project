from django.urls import path
from .views import EpisodeListView
app_name = 'episode'

urlpatterns = [
    path('episode-list/', EpisodeListView.as_view(), name='episode-list')
]
