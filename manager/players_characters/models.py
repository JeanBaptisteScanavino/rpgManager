from django.db import models


class PlayersCharacters(models.Model):
    name = models.CharField(verbose_name="Nom du personnage", max_length=255)
    player = models.CharField(verbose_name="Nom du Joueur", max_length=255, null=True, blank=True)
    character_sheet_url = models.CharField(
        verbose_name="Url fiche de personnage", max_length=1080, null=True , blank=True
    )
    # character_sheet_file = models.FileField(verbose_name="Importer une fiche")

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return self.name
