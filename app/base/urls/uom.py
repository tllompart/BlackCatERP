"""The store routes
"""
# Django Library
from django.urls import path

# Localfolder Library
from ..views.units import (
    unitsAutoComplete, unitsCreateView, unitsDeleteView, unitsDetailView, unitsListView,
    unitsUpdateView)

app_name = 'PyUom'

urlpatterns = [
    path('', unitsListView.as_view(), name='list'),
    path('add/', unitsCreateView.as_view(), name='add'),
    path('<int:pk>/', unitsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', unitsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', unitsDeleteView.as_view(), name='delete'),
    # ==================== Auto completado de Productos ==================== #
    path('autocomplete', unitsAutoComplete.as_view(), name='autocomplete'),
]
