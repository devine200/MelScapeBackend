# Generated by Django 4.2.16 on 2024-11-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_blogcategory_blogcomment_alter_faq_category_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="cover_photo",
            field=models.ImageField(blank=True, null=True, upload_to="blog"),
        ),
    ]