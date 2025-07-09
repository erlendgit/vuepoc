import uuid

from django.db import models


class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
