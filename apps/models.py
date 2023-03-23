from django.db import models
from django.contrib.auth.models import User
from apps.home.services.DataBaseServices import insertDataOnTable


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
    @staticmethod
    def CreatePlatformCredentials(self,data):
        fields = [field.name for field in self._meta.get_fields()]
        platform_credential_object = insertDataOnTable(fields=fields,model=self,data=data)
        return platform_credential_object

    class Meta:
        ordering = ['created_at']

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
    type = models.CharField(max_length=50, choices=[('SOURCE', 'SOURCE'), ('DESTINATION', 'DESTINATION')])
    code = models.CharField(max_length=255, null=True)
    display_name = models.CharField(max_length=255)
    credentials = models.OneToOneField(PlatformCredentials, on_delete=models.CASCADE, null=True)
    settings = models.ForeignKey(PlatformSettings, on_delete=models.DO_NOTHING, null=True)
    isConnected = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isOrderSyncProcessing = models.BooleanField(default=False)
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

class PlatformOrder(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, db_index=True, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, unique=False)
    api_id = models.CharField(max_length=255, null=False)
    customer = models.ForeignKey(PlatformCustomer, null=True, on_delete=models.DO_NOTHING)
    api_code = models.CharField(max_length=255, null=True)
    api_status = models.CharField(max_length=50, null=False)

    total_price = models.ForeignKey(Price, null=False, related_name="TotalPriceOrder", on_delete=models.CASCADE)

    shipping_price = models.ForeignKey(Price, null=True, related_name="ShippingPriceOrder", on_delete=models.CASCADE)

    tax_price = models.ForeignKey(Price, null=True, related_name="TaxPriceOrder", on_delete=models.CASCADE)

    discount_percent = models.CharField(max_length=10, null=True)
    isPaid = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=20, null=True)
    isFulfilled = models.BooleanField(default=False)
    api_created_at = models.DateTimeField(null=True)
    api_updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.api_id

class PlatformOrderPayment(models.Model):
    platform_order = models.ForeignKey(PlatformOrder, on_delete=models.CASCADE, db_index=True, unique=False)
    api_id = models.CharField(max_length=255, null=True)
    paid_amount = models.FloatField(null=False)
    paid_on = models.DateTimeField()
    payment_mode = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PlatformOrderLineItem(models.Model):
    platform_order = models.ForeignKey(PlatformOrder, on_delete=models.CASCADE, db_index=True, unique=False)
    platform_product = models.ForeignKey(PlatformProduct, on_delete=models.DO_NOTHING, null=True)
    api_id = models.CharField(max_length=255, null=False)
    sku = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255, null=False)
    price = models.ForeignKey(Price, on_delete=models.DO_NOTHING, null=True, related_name="PlatformOrderLineItemPrice")
    tax_price = models.ForeignKey(Price, on_delete=models.DO_NOTHING, null=True, related_name="PlatformOrderLineItemtax")
    product_api_id = models.CharField(max_length=255, null=True)
    product_api_variation_id = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
