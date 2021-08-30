from django.db import models
from django.utils.translation import ugettext_lazy as _

from .basemodel import ERPBase
from .country import Country

POSITION_CHOICE = (
    ("before", "Antes de la Cantidad"),
    ('after', 'Después de la Cantidad'),
)


class Currency(ERPBase):
    name = models.CharField('Name', max_length=40)
    alias = models.CharField('Alias', max_length=40)
    symbol = models.CharField('Symbol', max_length=15)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    iso = models.CharField(max_length=30)
    position = models.CharField(
        choices=POSITION_CHOICE, max_length=64, default='after')

    def __str__(self):
        return "{} ({})".format(self.name, self.country)

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
