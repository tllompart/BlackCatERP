# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


from .basemodel import ERPBase


class Event(ERPBase):
    name = models.CharField(_("Name"), max_length=255)
    note = models.TextField(_("Note"))
    begin_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
