from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(published=True)


class MovieDetailView(DetailView):
    """Full movie description"""
    model = Movie
    slug_field = "url"


#
# class MovieDetailView(View):
#     """Personal movie page"""
#
#     def get(self, request, movie_slug):
#         movie = Movie.objects.get(url=movie_slug)
#         return render(request, "movies/movie_detail.html", {"movie": movie})
