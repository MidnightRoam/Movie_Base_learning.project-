from django.urls import path

from .views import MoviesView, MovieDetailView, ActorDetailView

urlpatterns = [
    path('', MoviesView.as_view(), name='movie_list'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<slug:slug>/', ActorDetailView.as_view(), name='actor_detail'),
]