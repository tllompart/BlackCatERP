# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import Tax
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Amount"), 'field': 'amount'},
    {'string': _("Include Price"), 'field': 'include_price'},
]

OBJECT_FORM_FIELDS = ['name', 'amount', 'include_price']


class TaxListView(LoginRequiredMixin, FatherListView):
    model = Tax
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class TaxDetailView(LoginRequiredMixin, FatherDetailView):
    model = Tax
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class TaxCreateView(LoginRequiredMixin, FatherCreateView):
    model = Tax
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class TaxUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = Tax
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class TaxDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = Tax


# ========================================================================== #
class TaxAutoComplete(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyPartner
    """
    def get_queryset(self):
        queryset = Tax.objects.filter(active=True)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset
