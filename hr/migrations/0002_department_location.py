# Generated by Django 5.0.3 on 2025-07-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hr", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="location",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
