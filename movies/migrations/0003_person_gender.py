# Generated by Django 4.2.16 on 2024-10-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_filmwork_certificate_filmwork_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.TextField(
                choices=[('male', 'male'), ('female', 'female')],
                null=True,
                verbose_name='gender',
            ),
        ),
    ]
