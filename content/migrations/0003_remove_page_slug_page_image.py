# Generated by Django 5.1.2 on 2024-10-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_remove_photogallery_date_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="page",
            name="slug",
        ),
        migrations.AddField(
            model_name="page",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="pages/"),
        ),
    ]
