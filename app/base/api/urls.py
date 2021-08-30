"""
**************************************************************************
URLS for BlackCat ERP
**************************************************************************
"""

from django.urls import path

from .views import CurrencyListview, CurrencyDetailview, CountryListview, CountryDetailview

urlpatterns = [
    path('currency/', CurrencyListview.as_view()),
    path('currency/<pk>', CurrencyDetailview.as_view()),
    path('country/', CountryListview.as_view()),
    path('country/<pk>', CountryDetailview.as_view()),
]
