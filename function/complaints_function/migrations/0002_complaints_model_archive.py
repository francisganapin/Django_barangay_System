# Generated by Django 4.2 on 2025-02-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("complaints_function", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaints_model",
            name="archive",
            field=models.BooleanField(default=False),
        ),
    ]
