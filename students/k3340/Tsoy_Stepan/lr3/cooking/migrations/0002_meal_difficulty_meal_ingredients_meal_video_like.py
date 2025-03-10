# Generated by Django 5.1.6 on 2025-02-13 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cooking", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="difficulty",
            field=models.CharField(
                choices=[("ez", "Easy"), ("md", "Medium"), ("hd", "Hard")],
                default="ez",
                max_length=2,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meal",
            name="ingredients",
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meal",
            name="video",
            field=models.URLField(
                default="https://www.youtube.com/watch?v=EOWa0fmSGs8"
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Like",
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
                ("status", models.BooleanField(default=False)),
                (
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cooking.meal"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
