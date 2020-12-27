from django.db import models
from taggit.managers import TaggableManager

from .tags import UUIDTaggedItem

class Document(models.Model):
    name = models.CharField(max_length=140)

    tags = TaggableManager(through=UUIDTaggedItem)