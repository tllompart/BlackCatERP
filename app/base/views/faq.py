# Django Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..models import faq
from .web_father import (
    FatherCreateView, FatherDeleteView, FatherDetailView, FatherListView,
    FatherUpdateView)

OBJECT_LIST_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Content"), 'field': 'content'},
]

OBJECT_FORM_FIELDS = ['name', 'content']


class FaqListView(LoginRequiredMixin, FatherListView):
    model = faq
    template_name = 'base/list.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}

class FaqDetailView(LoginRequiredMixin, FatherDetailView):
    model = faq
    template_name = 'base/detail.html'
    extra_context = {'fields': OBJECT_LIST_FIELDS}


class FaqCreateView(LoginRequiredMixin, FatherCreateView):
    model = faq
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FaqUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = faq
    fields = OBJECT_FORM_FIELDS
    template_name = 'base/form.html'


class FaqDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = faq
