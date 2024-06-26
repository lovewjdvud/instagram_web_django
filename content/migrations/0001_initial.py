# Generated by Django 4.2.13 on 2024-06-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feed",
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
                ("content", models.TextField()),
                ("image", models.TextField()),
                ("profile_image", models.TextField()),
                ("user_id", models.TextField()),
                ("like_count", models.TextField()),
            ],
        ),
    ]
