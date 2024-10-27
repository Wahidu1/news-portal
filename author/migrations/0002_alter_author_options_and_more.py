# Generated by Django 5.1.2 on 2024-10-24 19:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={},
        ),
        migrations.RemoveIndex(
            model_name="author",
            name="author_auth_email_48340d_idx",
        ),
        migrations.RemoveField(
            model_name="author",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="author",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="author",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this author belongs to.",
                related_name="author_set",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="author",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="author",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="author",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this author.",
                related_name="author_permission_set",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="author",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
