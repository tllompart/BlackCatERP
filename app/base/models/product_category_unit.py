
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .basemodel import ERPBase


class ProductCategoryUnits(ERPBase):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

    class Meta:
        verbose_name = _("ProductUnit")
        verbose_name_plural = _("ProductUnits")
