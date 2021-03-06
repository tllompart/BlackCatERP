# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import Bi
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Type"), 'field': 'type'},
    {'string': _("Model"), 'field': 'model'},
    {'string': _("Parameter"), 'field': 'parameter'},
    {'string': _("Color"), 'field': 'color'},
    {'string': _("Font Color"), 'field': 'font_color'},
    {'string': _("Icon"), 'field': 'icon'},
    {'string': _("Dashboard"), 'field': 'dashboard'},
    {'string': _("Url"), 'field': 'url'},
]

OBJECT_FORM_FIELDS = ['name', 'type', 'model', 'parameter',
                      'color', 'font_color', 'icon', 'dashboard', 'url']


class BiListView(LoginRequiredMixin, FatherListView):
    model = Bi
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class BiDetailView(LoginRequiredMixin, FatherDetailView):
    model = Bi
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class BiCreateView(LoginRequiredMixin, FatherCreateView):
    model = Bi
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class BiUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = Bi
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class BiDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = Bi
    success_url = 'base:bi'
