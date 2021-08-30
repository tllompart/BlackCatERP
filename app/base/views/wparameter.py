# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import parameter
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Value"), 'field': 'value'},
]

OBJECT_FORM_FIELDS = ['name', 'value']


class WParameterListView(LoginRequiredMixin, FatherListView):
    model = parameter
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class WParameterDetailView(LoginRequiredMixin, FatherDetailView):
    model = parameter
    template_name = 'base/detail.html'

class WParameterCreateView(LoginRequiredMixin, FatherCreateView):
    model = parameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class WParameterUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = parameter
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'



class WParameterDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = parameter
    success_url = 'base:wparameters'
