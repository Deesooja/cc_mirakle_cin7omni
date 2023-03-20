# Generated by Django 4.1.7 on 2023-03-20 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Customer', max_length=255)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('address_1', models.CharField(max_length=500)),
                ('address_2', models.CharField(max_length=500, null=True)),
                ('address_3', models.CharField(max_length=500, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zip', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('country_iso', models.CharField(max_length=5, null=True)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MIRAKLE', 'MIRAKLE'), ('CIN7', 'CIN7')], max_length=10)),
                ('type', models.CharField(choices=[('SOURCE', 'SOURCE'), ('DESTINATION', 'DESTINATION')], max_length=50)),
                ('code', models.CharField(max_length=255, null=True)),
                ('display_name', models.CharField(max_length=255)),
                ('isConnected', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, null=True)),
                ('client_id', models.CharField(max_length=255, null=True)),
                ('client_secret', models.CharField(max_length=255, null=True)),
                ('token_id', models.CharField(max_length=1000)),
                ('token_secret', models.CharField(max_length=1000, null=True)),
                ('refresh_token', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='CUSTOMER', max_length=25)),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('api_id', models.CharField(max_length=255, null=True)),
                ('api_code', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('currency', models.CharField(max_length=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.address')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.platform')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=255)),
                ('api_code', models.CharField(max_length=255, null=True)),
                ('api_status', models.CharField(max_length=50)),
                ('discount_percent', models.CharField(max_length=10, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('payment_status', models.CharField(max_length=20, null=True)),
                ('isFulfilled', models.BooleanField(default=False)),
                ('api_created_at', models.DateTimeField(null=True)),
                ('api_updated_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.platformcustomer')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.platform')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isSyncOrder', models.BooleanField(default=False)),
                ('isCreateOrder', models.BooleanField(default=False)),
                ('isSyncFulfillment', models.BooleanField(default=False)),
                ('isUseDefaultCustomerEmail', models.BooleanField(default=False)),
                ('default_customer_email', models.CharField(default='Customer', max_length=255)),
                ('sync_orders_created_after', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformSyncData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('synced_at', models.DateTimeField(null=True)),
                ('sync_updated_at', models.DateTimeField(null=True)),
                ('api_message', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
                ('value', models.FloatField()),
                ('currency_iso', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('display_name', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('api_id', models.CharField(db_index=True, max_length=255)),
                ('api_code', models.CharField(max_length=255, null=True)),
                ('api_status', models.CharField(max_length=50)),
                ('sku', models.CharField(db_index=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.platform')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformOrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=255, null=True)),
                ('paid_amount', models.FloatField()),
                ('paid_on', models.DateTimeField()),
                ('payment_mode', models.CharField(max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.platformorder')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformOrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=255)),
                ('sku', models.CharField(db_index=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('product_api_id', models.CharField(max_length=255, null=True)),
                ('product_api_variation_id', models.CharField(max_length=255, null=True)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.platformorder')),
                ('platform_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.platformproduct')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PlatformOrderLineItemPrice', to='apps.price')),
                ('tax_price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PlatformOrderLineItemtax', to='apps.price')),
            ],
        ),
        migrations.AddField(
            model_name='platformorder',
            name='shipping_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ShippingPriceOrder', to='apps.price'),
        ),
        migrations.AddField(
            model_name='platformorder',
            name='tax_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TaxPriceOrder', to='apps.price'),
        ),
        migrations.AddField(
            model_name='platformorder',
            name='total_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TotalPriceOrder', to='apps.price'),
        ),
        migrations.AddField(
            model_name='platformorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platform',
            name='credentials',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.platformcredentials'),
        ),
        migrations.AddField(
            model_name='platform',
            name='settings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.platformsettings'),
        ),
        migrations.AddField(
            model_name='platform',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
