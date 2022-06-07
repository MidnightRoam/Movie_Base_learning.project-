from modeltranslation.translator import register, TranslationOptions
from .models import MovieCategory, Actor, Movie, Genre, MovieShots


@register(MovieCategory)
class MovieCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'short_description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    

@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
