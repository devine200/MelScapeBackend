# Generated by Django 4.2.16 on 2024-11-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutHeroSection",
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
                ("header", models.CharField(max_length=200)),
                ("cover_photo", models.ImageField(upload_to="about")),
            ],
        ),
        migrations.CreateModel(
            name="AboutIntroSection",
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
                ("detail_top", models.TextField()),
                ("detail_bottom", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ContactInfo",
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
                ("facebook_link", models.CharField(max_length=300)),
                ("twitter_link", models.CharField(max_length=300)),
                ("instagram_link", models.CharField(max_length=300)),
                ("email_1", models.CharField(max_length=300)),
                ("email_2", models.CharField(max_length=300)),
                ("phone_number", models.CharField(max_length=300)),
                ("calendly_link", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="CoreServices",
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
                ("header", models.CharField(max_length=200)),
                ("details", models.TextField()),
                ("icon_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="CTADescription",
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
                ("header", models.CharField(max_length=200)),
                ("details_top", models.TextField(default="")),
                ("details_bottom", models.TextField(default="")),
                ("is_aligned_left", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="HowWeCanHelpSection",
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
                ("icon", models.ImageField(upload_to="help")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="InstagramPost",
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
                ("post_name", models.CharField(max_length=200)),
                ("post_link", models.CharField(max_length=300)),
                ("post_image", models.ImageField(upload_to="instagram")),
            ],
        ),
        migrations.CreateModel(
            name="LandingHeroSection",
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
                ("header", models.CharField(max_length=300)),
                ("details", models.TextField(default="")),
                ("first_button_text", models.CharField(max_length=50)),
                ("first_button_link", models.CharField(max_length=200)),
                ("second_button_text", models.CharField(max_length=50)),
                ("second_button_link", models.CharField(max_length=200)),
                ("cover_photo", models.ImageField(upload_to="landing")),
                ("slogan_header", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="StepsToEarn",
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
                ("cover_photo", models.ImageField(upload_to="earn")),
                ("step_text", models.CharField(max_length=50)),
                ("cta_button_link", models.CharField(max_length=200)),
            ],
        ),
    ]
