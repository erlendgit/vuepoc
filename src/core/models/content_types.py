from django.core.exceptions import ValidationError
from django.db import models


class ContentType(models.Model):
    key = models.CharField(max_length=128, editable=True)
    name = models.CharField(max_length=255, unique=True)
    name_plural = models.CharField(max_length=255)

    def clean(self):
        if self.key and self.key != self.key.lower():
            raise ValidationError({"key": "The ID must be in lowercase."})

    def __str__(self):
        return self.name
