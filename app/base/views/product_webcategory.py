# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Localfolder Library
from ...base.models import product_webcategory
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

OBJECT_FORM_FIELDS = ['name', 'parent_id']


class ProductWebCategoryListView(LoginRequiredMixin, FatherListView):
    model = product_webcategory
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class ProductWebCategoryDetailView(LoginRequiredMixin, FatherDetailView):
    model = product_webcategory
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ProductWebCategoryCreateView(LoginRequiredMixin, FatherCreateView):
    model = product_webcategory
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductWebCategoryUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = product_webcategory
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ProductWebCategoryDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = product_webcategory
