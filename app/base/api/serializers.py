"""
**************************************************************************

Serializers for base api

**************************************************************************
"""
from rest_framework import serializers


from ..models.currency import Currency
from ..models.country import Country
from ..models.partner import Partner
from ..models.product import Product
from ..models.product_brand import ProductBrand
from ..models.product_category_unit import ProductCategoryUnits
from ..models.product_category import ProductCategory


class CurrencySerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = Currency
        fields = ('name', 'alias', 'symbol', 'country', 'iso', 'position')


class CountrySerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = Country
        fields = ('name')


class PartnerSerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = Partner
        fields = ('name', 'address', 'address_2', 'country_id', 'city',
                  'phone', 'email', 'customer',
                  'provider', 'for_invoice', 'note', 'not_email', 'parent_id', 'type')


class ProductBrandSerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = ProductBrand
        fields = ('__all__')


class ProductCategoryUnitsSerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = ProductCategoryUnits
        fields = ('__all__')


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = ProductCategory
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = Product
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """
    **************************************************************************


    **************************************************************************

    """

    class Meta:
        model = Product
        fields = ('__all__')
