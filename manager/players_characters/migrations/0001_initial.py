# Generated by Django 4.2.3 on 2023-07-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlayersCharacters",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Nom du personnage"),
                ),
                (
                    "player",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Nom du Joueur"
                    ),
                ),
                (
                    "character_sheet_url",
                    models.CharField(
                        max_length=1080,
                        null=True,
                        verbose_name="Url fiche de personnage",
                    ),
                ),
            ],
        ),
    ]