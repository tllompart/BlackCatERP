# Django Library
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .basemodel import ERPBase
from .product_category_unit import ProductCategoryUnits

TYPE_CHOICE = (
    ("bigger", "Bigger"),
    ('reference', 'Reference'),
    ('smaller', 'Smaller'),
)


class Units(ERPBase):
    name = models.CharField(_("Name"), max_length=255)
    ratio = models.DecimalField(
        _("Ratio"), max_digits=10, decimal_places=2, default=1)
    round = models.DecimalField(
        _("Ratio"), max_digits=10, decimal_places=2, default=0.01)
    type = models.CharField(_("type"), choices=TYPE_CHOICE,
                            max_length=64, default='consu')
    category_id = models.ForeignKey(
        ProductCategoryUnits, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")
