from django.contrib import admin
from .models import Genre, FilmWork, GenreFilmWork, PersonFilmWork, Person


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)

    # Отображение полей в списке
    list_display = (
        'title',
        'type',
        'creation_date',
        'rating',
    )

    # Фильтрация в списке
    list_filter = (
        'type',
        'creation_date',
        'rating',
    )

    # Поиск по полям
    search_fields = ('title', 'description', 'id')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline,)

    list_display = (
        'name',
        'description',
    )

    list_filter = ('name',)

    search_fields = ('name', 'description', 'id')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonFilmWorkInline,)

    list_display = (
        'full_name',
    )

    list_filter = (
        'full_name',
    )

    search_fields = ('full_name', 'id')
