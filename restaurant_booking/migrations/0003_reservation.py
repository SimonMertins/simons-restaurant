# Generated by Django 5.0.1 on 2024-01-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_booking", "0002_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("num_guests", models.IntegerField()),
            ],
        ),
    ]
