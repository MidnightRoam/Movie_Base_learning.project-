from django.urls import path
from django.contrib.flatpages import views

from .views import MovieView, MovieDetailView, ActorDetailView, AddReview, FilterMoviesView, Search

urlpatterns = [
    path('', MovieView.as_view(), name='movie_list'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('search/', Search.as_view(), name='search'),
    path('about/', views.flatpage, {'url': '/about-us/'}, name='about'),
    # path('json-filter/', JsonFilterMoviesView.as_view(), name='json_filter'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<slug:slug>/', ActorDetailView.as_view(), name='actor_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]