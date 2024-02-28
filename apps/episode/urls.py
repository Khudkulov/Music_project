from django.urls import path

from .views import EpisodeListView, EpisodeDetailView, EpisodeAddView, LikeRedirectView

app_name = 'episode'

urlpatterns = [
    path('list/', EpisodeListView.as_view(), name='list'),
    path('detail/<slug:slug>/', EpisodeDetailView.as_view(), name='detail'),
    path('add/', EpisodeAddView.as_view(), name='add_music'),
    path('like/<int:eid>', LikeRedirectView.as_view(), name='like'),
]
