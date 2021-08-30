from django.contrib import admin

from .models.product import Product
from .models.product_brand import ProductBrand
from .models.units import Units
from .models.product_category import ProductCategory
from .models.product_category_unit import ProductCategoryUnits
from .models.partner import Partner
from .models.currency import Currency
from .models.country import Country
from .models.company import Company

admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategoryUnits)
admin.site.register(ProductCategory)
admin.site.register(Units)
admin.site.register(Partner)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(Company)
