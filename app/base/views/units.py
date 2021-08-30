# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import Product, units
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Ratio"), 'field': 'ratio'},
    {'string': _("Rouding"), 'field': 'rouding'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Category"), 'field': 'category_id'},
]

OBJECT_FORM_FIELDS = ['name', 'ratio', 'rouding', 'type', 'category_id']


class unitsListView(LoginRequiredMixin, FatherListView):
    model = units
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class unitsDetailView(LoginRequiredMixin, FatherDetailView):
    model = units
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class unitsCreateView(LoginRequiredMixin, FatherCreateView):
    model = units
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class unitsUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = units
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class unitsDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = units


# ========================================================================== #
class unitsAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        queryset = units.objects.filter(active=True)

        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
