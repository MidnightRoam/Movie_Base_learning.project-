from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Actor


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(published=True)


class MovieDetailView(DetailView):
    """Personal movie page"""
    model = Movie
    slug_field = "url"


class ActorDetailView(DetailView):
    """Personal actor or director page"""
    model = Actor
    slug_field = "url"
