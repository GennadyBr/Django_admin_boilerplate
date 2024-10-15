import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class CreatedMixin(models.Model):
    # auto_now_add автоматически выставит дату создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class TimeStampedMixin(CreatedMixin):
    # auto_now изменятся при каждом обновлении записи
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    # Типичная модель в Django использует число в качестве id.
    # В таких ситуациях поле не описывается в модели.
    # Вам же придётся явно объявить primary key.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(TimeStampedMixin, UUIDMixin):
    # Первым аргументом обычно идёт человекочитаемое название поля
    name = models.CharField(
        name='name', verbose_name=_('name'), max_length=255
    )
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField(
        name='description', verbose_name=_('description'), blank=True
    )

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме.
        # Это нужно указать в классе модели
        db_table = "content\".\"genre"
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.name


class Person(TimeStampedMixin, UUIDMixin):
    full_name = models.CharField(
        name='full_name', verbose_name=_('full_name'), max_length=255
    )

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return self.full_name


class FilmWork(TimeStampedMixin, UUIDMixin):
    class Type(models.TextChoices):
        movie = "movie", _('movie')
        tv_show = "tv_show", _('tv_show')

    title = models.CharField(
        name='title', verbose_name=_('title'), max_length=255
    )
    description = models.TextField(
        name='description', verbose_name=_('description'), blank=True
    )
    creation_date = models.DateField(
        name='creation_date',
        verbose_name=_('creation_date'),
        blank=True,
        null=True,
    )
    rating = models.FloatField(
        name='rating',
        verbose_name=_('rating'),
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.CharField(
        name='type',
        verbose_name=_('type'),
        max_length=20,
        choices=Type.choices,
        default=Type.movie,
    )
    # Параметр upload_to указывает,
    # в какой подпапке будут храниться загружемые файлы.
    # Базовая папка указана в файле настроек как MEDIA_ROOT
    file_path = models.FileField(
        name='file_path',
        verbose_name=_('file'),
        blank=True,
        null=True,
        upload_to='movies/',
    )
    genres = models.ManyToManyField(Genre, through='GenreFilmWork')
    person = models.ManyToManyField(Person, through='PersonFilmWork')

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('FilmWork')
        verbose_name_plural = _('FilmWorks')

    def __str__(self):
        return self.title


class GenreFilmWork(UUIDMixin, CreatedMixin):
    film_work_id = models.ForeignKey(
        'FilmWork',
        verbose_name=_('FilmWork'),
        on_delete=models.CASCADE,
        null=True,
    )
    genre_id = models.ForeignKey(
        'Genre',
        verbose_name=_('Genre'),
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('FilmWork genre')
        verbose_name_plural = _('FilmWork genres')


class PersonFilmWork(UUIDMixin, CreatedMixin):
    film_work_id = models.ForeignKey(
        'FilmWork',
        verbose_name=_('FilmWork'),
        on_delete=models.CASCADE,
        null=True,
    )
    person_id = models.ForeignKey(
        'Person', verbose_name=_('Person'), on_delete=models.CASCADE, null=True
    )
    role = models.TextField(name='role', verbose_name=_('Role'), blank=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('Person FilmWork')
        verbose_name_plural = _('Persons FilmWork')

    def __str__(self):
        return self.role
