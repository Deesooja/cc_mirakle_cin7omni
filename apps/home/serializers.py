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
    settings=PlatformSettingsSerializer()
    credentials=PlatformCredentialsSerializer()
    # user=UserSerializer()
    class Meta:
        model = Platform
        fields = ['id', 'user', 'name', 'type','code','display_name','credentials','settings','isConnected','isActive','created_at','updated_at']
        # depth=1

    def create(self, validated_data):

        settings_data = validated_data.pop('settings')

        credentials_data = validated_data.pop('credentials')

        # Create a new PlatformSettings instance and associate it with the Platform
        settings=PlatformSettings.objects.create( **settings_data)

        # Create a new PlatformCredentials instance and associate it with the Platform
        credentials=PlatformCredentials.objects.create( **credentials_data)

        platform = Platform.objects.create(credentials=credentials,settings=settings ,**validated_data)

        return platform

    def update(self, instance, validated_data):
        settings_data = validated_data.pop('settings', {})
        credentials_data = validated_data.pop('credentials', {})

        # Update the Platform instance
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.code = validated_data.get('code', instance.code)
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.isConnected = validated_data.get('isConnected', instance.isConnected)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.isOrderSyncProcessing=validated_data.get('isOrderSyncProcessing', instance.isOrderSyncProcessing)
        instance.save()

        # Update the PlatformSettings instance
        settings_instance = instance.settings
        settings_instance.isSyncOrder = settings_data.get('isSyncOrder', settings_instance.isSyncOrder)
        settings_instance.isCreateOrder = settings_data.get('isCreateOrder', settings_instance.isCreateOrder)
        settings_instance.isSyncFulfillment = settings_data.get('isSyncFulfillment', settings_instance.isSyncFulfillment)
        settings_instance.isUseDefaultCustomerEmail = settings_data.get('isUseDefaultCustomerEmail', settings_instance.isUseDefaultCustomerEmail)
        settings_instance.default_customer_email = settings_data.get('default_customer_email', settings_instance.default_customer_email)
        settings_instance.sync_orders_created_after = settings_data.get('sync_orders_created_after',settings_instance.sync_orders_created_after)
        settings_instance.save()

        # Update the PlatformCredentials instance
        credentials_instance = instance.credentials
        credentials_instance.identifier = credentials_data.get('identifier', credentials_instance.identifier)
        credentials_instance.client_id = credentials_data.get('client_id', credentials_instance.client_id)
        credentials_instance.client_secret = credentials_data.get('client_secret', credentials_instance.client_secret)
        credentials_instance.token_secret = credentials_data.get('token_secret', credentials_instance.token_secret)
        credentials_instance.token_id = credentials_data.get('token_id', credentials_instance.token_id)
        credentials_instance.refresh_token = credentials_data.get('refresh_token', credentials_instance.refresh_token)
        credentials_instance.save()

        return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class PlatformSyncDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformSyncData
        fields = '__all__'

class PlatformCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformCustomer
        fields = '__all__'

class PlatformProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformProduct
        fields = '__all__'

class PlatformOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformOrder
        fields = '__all__'

class PlatformOrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformOrderPayment
        fields = '__all__'

class PlatformOrderLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformOrderLineItem
        fields = '__all__'

