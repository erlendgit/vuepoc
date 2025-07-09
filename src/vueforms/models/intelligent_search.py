from django.db import models


class IntelligentSearchSetup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    shared_secret = models.CharField(max_length=128)
    index_setup = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
