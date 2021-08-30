import os

from django.db import models
from .basemodel import ERPBase
from .country import Country

from .currency import Currency


class Person(ERPBase):
    name = models.CharField(max_length=40)
    street = models.CharField(max_length=100, blank=True)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    VatId = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40, blank=True)

    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    currency_id = models.ForeignKey(
        Currency, null=True, blank=True, on_delete=models.PROTECT)

    postal_code = models.CharField(max_length=255, blank=True)

    social_facebook = models.CharField(max_length=255, blank=True)
    social_instagram = models.CharField(max_length=255, blank=True)
    social_linkedin = models.CharField(max_length=255, blank=True)
    social_youtube = models.CharField(max_length=255, blank=True)
    social_whatsapp = models.CharField(max_length=255, blank=True)
