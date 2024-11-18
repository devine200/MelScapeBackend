# Generated by Django 4.2.16 on 2024-11-13 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_blogpost_cover_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogImage",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="blog")),
            ],
        ),
        migrations.AddField(
            model_name="blogcomment",
            name="post",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="app.blogpost",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blogpost",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
