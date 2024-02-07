from django.urls import path

from .views import BlogView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('list/', BlogView.as_view(), name='list'),
    path('detail/', BlogDetailView.as_view(), name='detail'),
]