# Generated by Django 5.1.2 on 2024-10-24 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0005_comment_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="name",
        ),
    ]
