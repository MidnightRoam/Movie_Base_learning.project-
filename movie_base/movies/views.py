from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie, Actor, MovieCategory
from .forms import ReviewForm


class MoviesView(ListView):
    """List of published movies"""
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
