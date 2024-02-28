from django import template

from apps.episode.models import EpisodeLike

register = template.Library()

@register.filter(name='user_likes_episode')
def user_likes_episode(eid, user_id):
    return EpisodeLike.objects.filter(episode_id=eid, author_id=user_id).exists()
