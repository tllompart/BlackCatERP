from django.db import models
from .basemodel import ERPBase


class Country(ERPBase):
    Name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.Name)

    class Meta:
        verbose_name = ("Country")
        verbose_name_plural = ("Countries")
