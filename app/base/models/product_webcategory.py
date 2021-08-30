# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .basemodel import ERPBase


class ProductWebCategory(ERPBase):
    name = models.CharField(max_length=40)

    parent_id = models.ForeignKey(
        'self', null=True, blank=True, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return '%s%s' % (self.parent_id and ('[%s] ' % self.parent_id) or '', self.name)

    class Meta:
        verbose_name = _("ProductWebCategory")
        verbose_name_plural = _("ProductWebCategory")
