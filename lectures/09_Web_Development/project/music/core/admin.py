from django.contrib import admin

from .models import Artist, Genre, Ruble

# Register your models here.


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Ruble)
class RubleAdmin(admin.ModelAdmin):
    pass
