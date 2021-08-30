
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from .basemodel import ERPBase


class Log(ERPBase):
    name = models.CharField('Name', max_length=40)
    content = models.TextField("Content", blank=True, null=True)

    


    class Meta:
        ordering = ['pk']
        verbose_name = _("Log")
        verbose_name_plural = _("Logs")
