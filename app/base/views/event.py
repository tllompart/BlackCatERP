# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import event
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Note"), 'field': 'note'},
    {'string': _("Begin Date"), 'field': 'begin_date'},
]

OBJECT_FORM_FIELDS = ['name', 'note', 'begin_date']


class EventListView(LoginRequiredMixin, FatherListView):
    model = event
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class EventDetailView(LoginRequiredMixin, FatherDetailView):
    model = event
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class EventCreateView(LoginRequiredMixin, FatherCreateView):
    model = event
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class EventUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = event
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class EventDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = event
