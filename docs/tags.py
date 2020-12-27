from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase, TagBase


class MyCustomTag(TagBase):
    name = models.CharField(max_length=140)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # REQ01: I want to use a ForeignKey instead of a generic one
    content_object = models.ForeignKey('docs.Document', on_delete=models.CASCADE)
    # REQ02: I want to use a custom tag model
    tag = models.ForeignKey(
        MyCustomTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")