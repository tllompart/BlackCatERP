# -*- coding: utf-8 -*-
"""
Formularios
"""
# Django Library
from django import forms
from django.utils.translation import ugettext_lazy as _

# Thirdparty Library
from dal import autocomplete

# Localfolder Library
from ..models import Partner


class PartnerForm(forms.ModelForm):
    
    class Meta:
        model = Partner
        fields = [
            'name',
            'phone',
            'email',
            'country_id',
            'city',
            'address',
            'address_2',
            'parent_id',
            'type',
            'customer',
            'provider',
            'for_invoice',
            'not_email',
            'note',
        ]
        widgets = {
            'country_id': autocomplete.ModelSelect2(
                url='PyCountry:autocomplete',
                attrs={
                    'data-placeholder': _('Select country...'),
                    'style': 'width: 100%',
                },
            ),
            'parent_id': autocomplete.ModelSelect2(
                url='PyPartner:autocomplete',
                attrs={
                    'class': 'form-control',
                    'data-placeholder': _('Choose a client ...'),
                    'style': 'width: 100%',
                },
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Note ...'),
                    'style': 'width: 100%',
                    'rows': '1',
                },
            ),
            'type': forms.Select(
                attrs={
                    'class': 'static-select2',
                },
            ),
        }
