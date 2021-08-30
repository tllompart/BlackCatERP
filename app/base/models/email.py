# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library

from .partner import Partner
from .basemodel import ERPBase

TYPE_CHOICE = (
    ("received", "Received"),
    ('sent', 'sent')
)


class Email(ERPBase):
    title = models.CharField(_("Title"), max_length=255)
    content = models.TextField(_("Content"))
    partner_id = models.ForeignKey(Partner, null=True, blank=True, on_delete=models.PROTECT,related_name='+')
    type = models.CharField(_("type"), choices=TYPE_CHOICE, max_length=64)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
