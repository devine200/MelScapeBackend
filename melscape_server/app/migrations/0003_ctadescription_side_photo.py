# Generated by Django 4.2.16 on 2024-11-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_ctadescription_cta_button_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ctadescription",
            name="side_photo",
            field=models.ImageField(blank=True, upload_to="CTA"),
        ),
    ]
