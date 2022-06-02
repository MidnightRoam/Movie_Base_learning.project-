from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MovieCategory, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(MovieCategory)
class CategoryAdmin(admin.ModelAdmin):
    """Categories"""
    list_display = ('name', 'url')


class ReviewInLines(admin.TabularInline):
    """Reviews on movie admin-page"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInLines(admin.TabularInline):
    """Movie shots on movie admin-page"""
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Movie shots view"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movies"""
    list_display = ('title', 'category', 'url', 'published', 'get_image')
    list_filter = ('year',)
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInLines, ReviewInLines]
    save_on_top = True
    list_editable = ('published',)
    readonly_fields = ('get_image',)
    fieldsets = (
        ("About movie", {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'), )
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'), )
        }),
        ("Actors", {
            'classes': ('collapse', ),
            'fields': (('actors', 'directors', 'genres', 'category'), )
        }),
        ("Financial", {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'), )
        }),
        ("Options", {
            'fields': (('url', 'published'), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Poster view"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genres"""
    list_display = ('name', 'url')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Movie shots"""
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="80"')

    get_image.short_description = "Movie shots view"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Actors"""
    list_display = ('name', 'url', 'published', 'get_image')
    list_filter = ('age',)
    save_on_top = True
    list_editable = ('published',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Actor image view"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Rating"""
    list_display = ('movie', 'ip')


admin.site.register(RatingStar)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Reviews"""
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.site.site_title = "MovieSearcher"
admin.site.site_header = "MovieSearcher"