from django.db import models
from .persons import Person


class Company(Person):
    dummy = models.CharField(max_length=40)
