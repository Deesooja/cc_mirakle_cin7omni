from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Address)
admin.site.register(Price)
admin.site.register(PlatformCredentials)
admin.site.register(PlatformSettings)
admin.site.register(Platform)
admin.site.register(PlatformSyncData)
admin.site.register(PlatformCustomer)
admin.site.register(PlatformProduct)
admin.site.register(PlatformOrder)
admin.site.register(PlatformOrderPayment)
admin.site.register(PlatformOrderLineItem)
