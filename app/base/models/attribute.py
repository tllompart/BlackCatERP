# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.variant import Variant
from ..models.basemodel import ERPBase


class Attribute(ERPBase):
    name = models.CharField(_("Name"), max_length=255)
    variant_id = models.ForeignKey(Variant, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("PyAttribute")
