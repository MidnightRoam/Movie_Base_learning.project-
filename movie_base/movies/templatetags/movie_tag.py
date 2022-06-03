from django import template

from movies.models import MovieCategory, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """Conclusion all categories"""
    return MovieCategory.objects.all()


@register.inclusion_tag('movies/tags/latest_added_movies.html')
def get_latest_movies(count=5):
    """Conclusion latest added movies"""
    movies = Movie.objects.order_by("-id")[:count]
    return {'latest_movies': movies}
