# Generated by Django 5.1.2 on 2024-10-15 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Album",
                "verbose_name_plural": "Albums",
                "db_table": "album",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, unique=True)),
            ],
            options={
                "verbose_name": "Page",
                "verbose_name_plural": "Pages",
                "db_table": "page",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Shortcut",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="shortcuts/"),
                ),
            ],
            options={
                "verbose_name": "Shortcut",
                "verbose_name_plural": "Shortcuts",
                "db_table": "shortcut",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="VideoGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("video_url", models.URLField()),
            ],
            options={
                "verbose_name": "Video Gallery",
                "verbose_name_plural": "Video Galleries",
                "db_table": "video_gallery",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="PhotoGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("images", models.ImageField(upload_to="photo_galleries/")),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photo_galleries",
                        to="content.album",
                    ),
                ),
            ],
            options={
                "verbose_name": "Photo Gallery",
                "verbose_name_plural": "Photo Galleries",
                "db_table": "photo_gallery",
                "managed": True,
            },
        ),
    ]
