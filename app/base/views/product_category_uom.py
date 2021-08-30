# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import product_category_unit
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': 'Name', 'field': 'name'},
]

OBJECT_FORM_FIELDS = ['name']


class ProductCategoryUOMListView(LoginRequiredMixin, FatherListView):
    model = product_category_unit
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ProductCategoryUOMDetailView(LoginRequiredMixin, FatherDetailView):
    model = product_category_unit
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ProductCategoryUOMCreateView(LoginRequiredMixin, FatherCreateView):
    model = product_category_unit
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryUOMUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = product_category_unit
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductCategoryUOMDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = product_category_unit
