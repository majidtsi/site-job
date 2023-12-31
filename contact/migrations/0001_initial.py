# Generated by Django 4.2.4 on 2023-08-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Info",
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
                ("place", models.CharField(max_length=50)),
                (
                    "phone_number",
                    models.CharField(help_text="1234363783", max_length=20),
                ),
                (
                    "email",
                    models.EmailField(help_text="lucio@exemple.com", max_length=254),
                ),
            ],
            options={
                "verbose_name": "Info",
                "verbose_name_plural": "Infos",
            },
        ),
    ]
