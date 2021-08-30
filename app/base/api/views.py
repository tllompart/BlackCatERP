from .serializers import ProductBrandSerializer, ProductCategoryUnitsSerializer, ProductCategorySerializer
from .serializers import CurrencySerializer, CountrySerializer, PartnerSerializer, ProductSerializer
from ..models.product_category import ProductCategory
from ..models.product_category_unit import ProductCategoryUnits
from ..models.product_brand import ProductBrand
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models.currency import Currency
from ..models.country import Country
from ..models.partner import Partner
from..models.product import Product


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/X-list/',
        'Detail View': '/X-detail/<str:pk>/',
        'Create': '/X-create/',
        'Update': '/X-update/<str:pk>/',
        'Delete': '/X-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def currencyList(request):
    currencies = Currency.objects.all().order_by('-id')
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def currencyDetail(request, pk):
    currencies = Currency.objects.get(id=pk)
    serializer = CurrencySerializer(currencies, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def currencyCreate(request):
    serializer = CurrencySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def currencyUpdate(request, pk):
    currency = Currency.objects.get(id=pk)
    serializer = CurrencySerializer(instance=currency, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def currencyDelete(request, pk):
    curr = Currency.objects.get(id=pk)
    curr.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def countryList(request):
    currencies = Country.objects.all().order_by('-id')
    serializer = CountrySerializer(currencies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def countryDetail(request, pk):
    currencies = Country.objects.get(id=pk)
    serializer = CountrySerializer(currencies, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def countryCreate(request):
    serializer = CountrySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def countryUpdate(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(instance=country, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def countryDelete(request, pk):
    count = Country.objects.get(id=pk)
    count.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def productBrandList(request):
    brands = ProductBrand.objects.all().order_by('-id')
    serializer = ProductBrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductBrandDetail(request, pk):
    brands = ProductBrand.objects.get(id=pk)
    serializer = ProductBrandSerializer(brands, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ProductBrandCreate(request):
    serializer = ProductBrandSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def ProductBrandUpdate(request, pk):
    brands = ProductBrand.objects.get(id=pk)
    serializer = ProductBrandSerializer(instance=brands, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def ProductBrandDelete(request, pk):
    brand = ProductBrand.objects.get(id=pk)
    brand.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def ProductCategoryList(request):
    category = ProductCategory.objects.all().order_by('-id')
    serializer = ProductCategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductCategoryDetail(request, pk):
    category = ProductCategory.objects.get(id=pk)
    serializer = ProductCategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ProductCategoryCreate(request):
    serializer = ProductCategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def ProductCategoryUpdate(request, pk):
    category = ProductCategory.objects.get(id=pk)
    serializer = ProductCategorySerializer(
        instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def ProductCategoryDelete(request, pk):
    category = ProductCategory.objects.get(id=pk)
    category.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def ProductCategoryUnitsList(request):
    category = ProductCategoryUnits.objects.all().order_by('-id')
    serializer = ProductCategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductCategoryUnitsDetail(request, pk):
    category = ProductCategoryUnits.objects.get(id=pk)
    serializer = ProductCategoryUnitsSerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ProductCategoryUnitsCreate(request):
    serializer = ProductCategoryUnitsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def ProductCategoryUnitsUpdate(request, pk):
    category = ProductCategoryUnits.objects.get(id=pk)
    serializer = ProductCategoryUnitsSerializer(
        instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def ProductCategoryUnitsDelete(request, pk):
    category = ProductCategoryUnits.objects.get(id=pk)
    category.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def partnerList(request):
    partners = Partner.objects.all().order_by('-id')
    serializer = ProductBrandSerializer(partners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def partnerDetail(request, pk):
    partners = Partner.objects.get(id=pk)
    serializer = ProductBrandSerializer(partners, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def partnerCreate(request):
    serializer = PartnerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def partnerUpdate(request, pk):
    partners = Partner.objects.get(id=pk)
    serializer = ProductBrandSerializer(instance=partners, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@csrf_exempt
@api_view(['DELETE'])
def partnerDelete(request, pk):
    partner = Partner.objects.get(id=pk)
    partner.delete()

    return Response('Item succsesfully delete!')


@csrf_exempt
@api_view(['GET'])
def productList(request):
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def productUpdate(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@csrf_exempt
@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Item succsesfully delete!')


class CurrencyListview(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyDetailview(RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CountryListview(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailview(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CurrencySerializer


class PartnerListview(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetailview(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
