# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models.basemodel import ERPBase


class PyMessage(ERPBase):
    message = models.TextField(_("Note"))
    user_id = models.ForeignKey('base.ERPUser', null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
