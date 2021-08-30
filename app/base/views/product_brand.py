# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import ProductBrand
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class ProductBrandListView(LoginRequiredMixin, FatherListView):
    model = ProductBrand
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ProductBrandDetailView(LoginRequiredMixin, FatherDetailView):
    model = ProductBrand
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ProductBrandCreateView(LoginRequiredMixin, FatherCreateView):
    model = ProductBrand
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductBrandUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = ProductBrand
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductBrandDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = ProductBrand
