"""uRLs para base
"""
# Django Library
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    # ============================ New URLs ============================ #
    path('', include('app.base.urls.usercustom')),
    path('attribute/', include('app.base.urls.attribute')),
    path('base/', include('app.base.urls.base')),
    path('bi/', include('app.base.urls.bi')),
    path('channel/', include('app.base.urls.channel')),
    path('comment/', include('app.base.urls.comment')),
    path('company/', include('app.base.urls.company')),
    path('country/', include('app.base.urls.country')),
    path('cron/', include('app.base.urls.cron')),
    path('currency/', include('app.base.urls.currency')),
    path('faq/', include('app.base.urls.faq')),
    path('image/', include('app.base.urls.image')),
    path('log/', include('app.base.urls.log')),
    path('meta/', include('app.base.urls.meta')),
    path('page/', include('app.base.urls.page')),
    path('parameter/', include('app.base.urls.parameter')),
    path('partner/', include('app.base.urls.partner')),
    path('plugin/', include('app.base.urls.plugin')),
    path('post/', include('app.base.urls.post')),
    path('product/', include('app.base.urls.product')),
    path('product_brand/', include('app.base.urls.product_brand')),
    path('product_category/', include('app.base.urls.product_category')),
    path('product_category_uom/', include('app.base.urls.product_category_uom')),
    path('product-webcategory/', include('app.base.urls.product_webcategory')),
    path('sequence/', include('app.base.urls.sequence')),
    path('shop/', include('app.base.urls.shop')),
    path('tag/', include('app.base.urls.tag')),
    path('tax/', include('app.base.urls.tax')),
    path('uom/', include('app.base.urls.uom')),
    path('variant/', include('app.base.urls.variant')),
    path('wparameter/', include('app.base.urls.wparameter')),
    path('wpayment/', include('app.base.urls.wpayment')),
    path('email/', include('app.base.urls.email')),
    path('file/', include('app.base.urls.file')),
    path('message/', include('app.base.urls.message')),
    path('note/', include('app.base.urls.note')),
    path('event/', include('app.base.urls.event')),
    path('menu/', include('app.base.urls.menu')),
    path('api/', include('app.base.urls.rest')),
]
