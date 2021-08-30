# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import Currency
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _('Country'), 'field': 'country'},
    {'string': _('Courrency'), 'field': 'name'},
    {'string': _('Alias'), 'field': 'alias'},
    {'string': _('Simbol'), 'field': 'symbol'},
    {'string': _('Position'), 'field': 'position'},
]

OBJECT_FORM_FIELDS = ['country', 'name', 'alias', 'symbol', 'position']


class CurrencyListView(LoginRequiredMixin, FatherListView):
    model = Currency
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class CurrencyDetailView(LoginRequiredMixin, FatherDetailView):
    model = Currency
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class CurrencyCreateView(LoginRequiredMixin, FatherCreateView):
    model = Currency
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CurrencyUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = Currency
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class CurrencyDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = Currency


class CurrencyAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo Currency
    """
    def get_queryset(self):
        queryset = Currency.objects.all(active=True)
        if self.q:
            queryset = queryset.filter(Q(name__icontains=self.q) | Q(country__name__icontains=self.q))
        return queryset
