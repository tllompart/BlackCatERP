# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.basemodel import ERPBase


class Variant(ERPBase):
    name = models.CharField(_("Name"), max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")
