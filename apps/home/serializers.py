from rest_framework import serializers
from apps.models import PlatformOrderLineItem
from django.contrib.auth.models import User
from apps.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class PlatformCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformCredentials
        fields = ['id', 'identifier', 'client_id', 'client_secret','token_id','token_secret','refresh_token']

class PlatformSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformSettings
        fields = ['id', 'isSyncOrder', 'isCreateOrder', 'isSyncFulfillment','isUseDefaultCustomerEmail','default_customer_email','sync_orders_created_after']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'user', 'name', 'type','code','display_name','credentials','settings','isConnected','isActive','created_at','updated_at']