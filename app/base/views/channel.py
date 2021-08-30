# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import channel
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Code"), 'field': 'code'},
]

OBJECT_FORM_FIELDS = ['name', 'code']


class ChannelListView(LoginRequiredMixin, FatherListView):
    model = channel
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ChannelDetailView(LoginRequiredMixin, FatherDetailView):
    model = channel
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class ChannelCreateView(LoginRequiredMixin, FatherCreateView):
    model = channel
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ChannelUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = channel
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class ChannelDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = channel
