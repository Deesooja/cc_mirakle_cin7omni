
from django.urls import path, re_path
from apps.home.views import *


urlpatterns = [

    path('credentials', PlatformCredentialsView.as_view(), name="platform_credential"),
    path('settings', PlatformSettingsView.as_view(), name="platform_settings"),
    path('create', PlatformView.as_view(), name="platform_create"),

    # re_path(r'^product-details/(?P<product_id>\w+)/$', views.productDetails, name="product-details"),
    # re_path(r'^product-group-details/(?P<product_group_id>\w+)/$', views.productGroupDetails, name="product-group-details"),

]
