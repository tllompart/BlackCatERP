
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


from .basemodel import ERPBase


class Files(ERPBase):
    name = models.CharField(_("Name"), max_length=255)
    content = models.TextField(_("Content"))
    user_id = models.ForeignKey(
        'base.ERPUser',
        null=True,
        blank=True,
        on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")
