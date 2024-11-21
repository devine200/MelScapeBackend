# Generated by Django 4.2.16 on 2024-11-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0017_appointmentbookingrequest"),
    ]

    operations = [
        migrations.RemoveField(model_name="siteinfo", name="twitter_link",),
        migrations.AddField(
            model_name="siteinfo",
            name="linkedin_link",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AddField(
            model_name="siteinfo",
            name="tiktok_link",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="calendly_link",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="email_1",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="email_2",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="facebook_link",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="instagram_link",
            field=models.CharField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="siteinfo",
            name="phone_number",
            field=models.CharField(default="", max_length=300),
        ),
    ]
