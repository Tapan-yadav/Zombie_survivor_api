# Generated by Django 4.1.6 on 2023-03-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survivor",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=100)),
                ("longitude", models.FloatField()),
                ("latitude", models.FloatField()),
                ("is_infected", models.BooleanField()),
                ("count_reports", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Survivor",
                "verbose_name_plural": "Survivors",
            },
        ),
    ]
