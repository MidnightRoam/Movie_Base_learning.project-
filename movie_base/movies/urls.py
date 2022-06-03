from django.urls import path

from .views import MovieView, MovieDetailView, ActorDetailView, AddReview

urlpatterns = [
    path('', MovieView.as_view(), name='movie_list'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('category/<int:category_id/', MovieView.as_view(), name='category'),
    path('actor/<slug:slug>/', ActorDetailView.as_view(), name='actor_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]