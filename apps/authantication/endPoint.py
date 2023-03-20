

from django.urls import path, re_path
from apps.authantication.views import  *


urlpatterns = [

    path('login', UserAuthanticationLoginView.as_view(), name="login"),
    path('logout', UserLogoutView.as_view(), name="logout"),
    path('register', UserRegistrationView.as_view(), name="register"),

    # re_path(r'^product-details/(?P<product_id>\w+)/$', views.productDetails, name="product-details"),
    # re_path(r'^product-group-details/(?P<product_group_id>\w+)/$', views.productGroupDetails, name="product-group-details"),

]
