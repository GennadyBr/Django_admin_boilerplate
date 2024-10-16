# Generated by Django 4.2.16 on 2024-10-15 09:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
            sql="CREATE SCHEMA content;",
        ),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'title',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                (
                    'description',
                    models.TextField(blank=True, verbose_name='Описание'),
                ),
                (
                    'creation_date',
                    models.DateField(
                        blank=True, null=True, verbose_name='Дата создания'
                    ),
                ),
                (
                    'rating',
                    models.FloatField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name='Рейтинг',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=[('movie', 'фильм'), ('tv_show', 'сериал')],
                        default='movie',
                        max_length=20,
                        verbose_name='Тип',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Кинопроизведение',
                'verbose_name_plural': 'Кинопроизведения',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=255, verbose_name='Название'),
                ),
                (
                    'description',
                    models.TextField(blank=True, verbose_name='Описание'),
                ),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'full_name',
                    models.CharField(max_length=255, verbose_name='ФИО'),
                ),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('role', models.TextField(blank=True, verbose_name='Роль')),
                (
                    'film_work',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='movies.filmwork',
                        verbose_name='Кинопроизведение',
                    ),
                ),
                (
                    'person',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='movies.person',
                        verbose_name='Персона',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Персона кинопроизведения',
                'verbose_name_plural': 'Персоны кинопроизведения',
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'film_work',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='movies.filmwork',
                        verbose_name='Кинопроизведение',
                    ),
                ),
                (
                    'genre',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='movies.genre',
                        verbose_name='Жанр',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Жанр кинопроизведения',
                'verbose_name_plural': 'Жанры кинопроизведения',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(
                through='movies.GenreFilmWork', to='movies.genre'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(
                through='movies.PersonFilmWork', to='movies.person'
            ),
        ),
    ]
