# Generated by Django 5.0 on 2025-02-12 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movies',
        ),
    ]
