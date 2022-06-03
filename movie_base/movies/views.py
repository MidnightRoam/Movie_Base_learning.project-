from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Actor, MovieCategory, Genre
from .forms import ReviewForm


class GenreYear:
    """Genres and release dates of movies"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(published=True).values("year")


class MovieView(GenreYear, ListView):
    """List of published movies"""
    model = Movie
    queryset = Movie.objects.filter(published=True)


class MovieDetailView(GenreYear, DetailView):
    """Personal movie page"""
    model = Movie
    slug_field = "url"


class ActorDetailView(GenreYear, DetailView):
    """Personal actor or director page"""
    model = Actor
    slug_field = "url"


class AddReview(View):
    """Reviews"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class FilterMoviesView(GenreYear, ListView):
    """Filter movies by genre, year"""
    def get_queryset(self):
        if self.request.GET.getlist("year") and self.request.GET.getlist("genre"):
            queryset = Movie.objects.filter(
                year__in=self.request.GET.getlist("year"),
                genres__in=self.request.GET.getlist("genre")
            )
        else:
            queryset = Movie.objects.filter(
                Q(year__in=self.request.GET.getlist("year")) |
                Q(genres__in=self.request.GET.getlist("genre"))
            )
        return queryset