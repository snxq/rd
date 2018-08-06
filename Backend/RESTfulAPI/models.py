from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=128)


class Picture(models.Model):
    name = models.CharField(default='', max_length=64)
    source = models.URLField(default='')
    tag = models.ManyToManyField("Tag")

