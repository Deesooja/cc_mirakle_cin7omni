from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Address(models.Model):
    first_name = models.CharField(max_length=255, null=False, default="Customer")
    last_name = models.CharField(max_length=255, null=True)
    address_1 = models.CharField(max_length=500, null=False)
    address_2 = models.CharField(max_length=500, null=True)
    address_3 = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=255, null=True)
    country_iso = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Price(models.Model):
    type = models.CharField(max_length=25)
    value = models.FloatField(null=False)
    currency_iso = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlatformCredentials(models.Model):
    identifier = models.CharField(max_length=255, null=True)
    client_id = models.CharField(max_length=255, null=True)
    client_secret = models.CharField(max_length=255, null=True)
    token_id = models.CharField(max_length=1000)
    token_secret = models.CharField(max_length=1000, null=True)
    refresh_token = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlatformSettings(models.Model):
    isSyncOrder = models.BooleanField(default=False)
    isCreateOrder = models.BooleanField(default=False)
    isSyncFulfillment = models.BooleanField(default=False)
    isUseDefaultCustomerEmail = models.BooleanField(default=False)
    default_customer_email = models.CharField(max_length=255, null=False, default="Customer")
    sync_orders_created_after = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Platform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, unique=False)
    name = models.CharField(max_length=10, choices=[('MIRAKLE', 'MIRAKLE'), ('CIN7', 'CIN7')])
    type = models.CharField(max_length=10, choices=[('SOURCE', 'SOURCE'), ('DESTINATION', 'DESTINATION')])
    code = models.CharField(max_length=255, null=True)
    display_name = models.CharField(max_length=255)
    credentials = models.OneToOneField(PlatformCredentials, on_delete=models.CASCADE, null=True)
    settings = models.ForeignKey(PlatformSettings, on_delete=models.DO_NOTHING, null=True)
    isConnected = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PlatformSyncData(models.Model):
    api_id = models.CharField(max_length=255, db_index=True, null=True)
    synced_at = models.DateTimeField(null=True)
    sync_updated_at = models.DateTimeField(null=True)
    api_message = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PlatformCustomer(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, db_index=True, unique=False)
    type = models.CharField(max_length=25, null=False, default="CUSTOMER")
    name = models.CharField(max_length=255, null=False)
    display_name = models.CharField(max_length=255, null=False)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)
    email = models.CharField(max_length=255, null=False)
    api_id = models.CharField(max_length=255, null=True)
    api_code = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    currency = models.CharField(max_length=5, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlatformProduct(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_index=True, unique=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    display_name = models.CharField(max_length=500)
    quantity = models.IntegerField()
    api_id = models.CharField(max_length=255, db_index=True)
    api_code = models.CharField(max_length=255, null=True)
    api_status = models.CharField(max_length=50)
    sku = models.CharField(max_length=255, db_index=True)
    price = models.ForeignKey(Price, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




