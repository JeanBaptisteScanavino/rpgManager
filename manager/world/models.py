from django.db import models


class Regions(models.Model):
    name = models.CharField(max_length=240, verbose_name="Nom de la région")
    visited = models.BooleanField(default=False, verbose_name="Déjà visitée")
    religion = models.CharField(
        max_length=240, null=True, blank=True, verbose_name="Religion principale"
    )
    politic = models.CharField(
        max_length=240, null=True, blank=True, verbose_name="Sytème politique"
    )
    chief = models.CharField(
        max_length=240, null=True, blank=True, verbose_name="Chef connu"
    )
    region_maps_url = models.CharField(
        max_length=240, null=True, blank=True, verbose_name="Lien vers la carte"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    history_in_campaign = models.TextField(
        null=True, blank=True, verbose_name="Activité importante lié à la campagne"
    )
