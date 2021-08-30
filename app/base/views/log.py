# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from app.base.models.log import Log
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Created On"), 'field': 'created_on'},
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
]

OBJECT_FORM_FIELDS = ['name', 'note']


class LogListView(LoginRequiredMixin, FatherListView):
    model = Log
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class LogDetailView(LoginRequiredMixin, FatherDetailView):
    model = Log
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class LogCreateView(LoginRequiredMixin, FatherCreateView):
    model = Log
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class LogUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = Log
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class LogDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = Log
