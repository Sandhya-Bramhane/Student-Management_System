# Generated by Django 4.2.3 on 2024-02-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0003_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notice",
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
                ("nid", models.IntegerField()),
                ("dt", models.CharField(max_length=20)),
                ("sub", models.CharField(max_length=100)),
                ("dept", models.CharField(max_length=20)),
            ],
        ),
    ]
