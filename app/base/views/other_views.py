# Furture Library
from __future__ import unicode_literals

# Django Library
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

# Localfolder Library
from ..forms import InitForm
# from ..models import (
#    BaseConfig, Bi, Company, Currency, Meta, Parameter, Partner,
#    Sequence, ERPUser, WebsiteConfig, WParameter)

from ..models import (
    BaseConfig, Company, Currency, Partner,
    Sequence, ERPUser, WebsiteConfig)


def IndexEasy(request):
    if BaseConfig.objects.all().exists():
        template = 'base/index.html'
    else:
        template = 'base/install.html'
    context = {}
    if request.method == 'POST':
        context['form'] = InitForm(request.POST)
        if context['form'].is_valid():
            name = context['form'].cleaned_data.get('name')
            country = context['form'].cleaned_data.get('country')
            currency = Currency.objects.get(country=country)
            email = context['form'].cleaned_data.get('email')
            password = context['form'].cleaned_data.get('password')
            company = Company.create(name, country, currency, 1)

            BaseConfig.create(company)
            WebsiteConfig.create(company.id)

            # Creo el usuario admin y automaticamente se crea su partner
            ERPUser.create(email, 'User', email, password, 1, 1, 1, company)

            # Creo el usuario anonimous y su partner
            ERPUser.create('Anonimous', 'User', 'anonimous@pyerp.cl',
                           password, 0, 0, 0, company)

            """Read Data """
            #Meta.LoadData('data', company.id)
            Sequence.LoadData('data', company.id)
            #WParameter.LoadData('data', company.id)
            #Parameter.LoadData('data', company.id)
            Partner.LoadData('data', company.id)
            #Bi.LoadData('data', company.id)

            """Read Data Demo """
            # PyMeta.LoadData(demo)

            # user = PyUser.objects.create_user(user_name, None, password)
            # user.is_staff = True
            # user.is_superuser = True
            # user.is_active = True
            # user.first_name = 'Admin'
            # user.last_name = 'User'
            # user.save()

            return HttpResponseRedirect(reverse_lazy('User:login'))
    else:
        context['form'] = InitForm()

    return render(request, template, context)
