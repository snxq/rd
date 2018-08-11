from uuid import uuid4

from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_time = models.DateTimeField(default=timezone.now)
    name = models.CharField(unique=True, max_length=128)


class Picture(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_time = models.DateTimeField(default=timezone.now)
    name = models.CharField(default='', max_length=64)
    source = models.URLField(default='')
    tags = models.ManyToManyField("Tag")
