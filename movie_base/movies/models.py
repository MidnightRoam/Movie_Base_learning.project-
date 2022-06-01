import uuid
from datetime import date

from django.db import models
from django.urls import reverse


class MovieCategory(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    """Genres"""
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Actor(models.Model):
    """Actors and directors"""
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description", blank=True)
    short_description = models.CharField("Short description", max_length=350, blank=True)
    image = models.ImageField("Image", upload_to="actors/", blank=True)
    career = models.CharField("Career in the film industry", max_length=250, blank=True)
    height = models.FloatField("Height", blank=True)
    genres = models.ManyToManyField(Genre, max_length=250, blank=True)
    born_date = models.DateField("Date of born", default=date.today)
    url = models.SlugField(max_length=160, unique=True)
    published = models.BooleanField("Published", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Movie(models.Model):
    """Movie"""
    title = models.CharField("Title", max_length=150)
    tagline = models.CharField("Tagline", max_length=150, default='')
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date", default=2022)
    country = models.CharField("Country", max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actors", related_name="film_actors")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premiere = models.DateField("World premiere", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="specify the amount in dollars")
    fees_in_usa = models.PositiveIntegerField(
        "Fees in USA", default=0, help_text="specify the amount in dollars"
    )
    fees_in_world = models.PositiveIntegerField(
        "Fees in world", default=0, help_text="specify the amount in dollars"
    )
    category = models.ForeignKey(
        MovieCategory, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    published = models.BooleanField("Published", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    """Shots from movie"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Shot from movie"
        verbose_name_plural = "Shots from movie"


class RatingStar(models.Model):
    """Star of rating"""
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Star of rating"
        verbose_name_plural = "Stars of rating"


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    """Reviews"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
