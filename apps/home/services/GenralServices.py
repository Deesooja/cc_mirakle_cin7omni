
from apps.models import *
from django.contrib.auth.models import User
from apps.home.serializers import *
def platrform_data_check_and_create_new_data(data):
    response={}
    user_id=data.get('user')
    platform_credentials_id = data.get('credentials')
    platform_settings_id = data.get('settings')

    if not User.objects.filter(id=user_id).exists():
        response['massage']="user id not exists"
        response['status'] =False
        response['data'] = []
        return response
    

    
    if not PlatformCredentials.objects.filter(id=platform_credentials_id).exists():
        response['massage'] = "platform_credentials id not exists"
        response['status'] = False
        response['data'] = []
        return response


    
    if not PlatformSettings.objects.filter(id=platform_settings_id).exists():
        response['massage'] = "platform_settings id not exists"
        response['status'] = False
        response['data'] = []
        return response

    response['massage'] = "OK"
    response['status'] = True
    response['data'] = data
    return response

def create_address_json_from_mirakle(order):
    address_json={
        "first_name":order['customer']['shipping_address'].get('firstname'),
        "last_name": order['customer']['shipping_address'].get('lastname'),
        "address_1": order['customer']['shipping_address'].get('street_1'),
        "address_2": order['customer']['shipping_address'].get('street_2'),
        "address_3": None,
        "city": order['customer']['shipping_address'].get('city'),
        "state": order['customer']['shipping_address'].get('state'),
        "zip": order['customer']['shipping_address'].get('zip_code'),
        "country": order['customer']['shipping_address'].get('country'),
        "country_iso": order['customer']['shipping_address'].get('country_iso_code'),
        "phone": order['customer']['shipping_address'].get('phone'),
    }
    return address_json


def create_price_json_from_mirakle(order):

    price_json={
        "tax_price":{
            "type": "tax_price",
            "value": order['order_lines'][0]['commission_taxes'][0]['amount'],
            "currency_iso": order["currency_iso_code"]
        },
        "price": {
            "type": "price",
            "value": order['order_lines'][0]['price'],
            "currency_iso": order["currency_iso_code"]
        },
        "shipping_price": {
            "type": "shipping_price",
            "value": order['order_lines'][0]['shipping_price'],
            "currency_iso": order["currency_iso_code"]
        }

    }
    return price_json

def create_platform_customer_json_from_mirakle(order,address_id,platform_id):

    platform_customer_json={
        "platform": platform_id,
        "name": order['customer']['firstname']+order['customer']['lastname'],
        "display_name": order['customer']['firstname']+order['customer']['lastname'],
        "address": address_id,
        "email": order['customer_notification_email'],
        "api_id": order['customer']['customer_id'],
        "api_code": None,
        "currency": order['currency_iso_code'],
        "created_at": order['created_date'],
        "updated_at": order['last_updated_date']
    }
    return platform_customer_json

def create_platform_product_json_from_mirakle(order,platform_id,user_id,price_id):

    platform_product_json={
        "platform": platform_id,
        "user": user_id,
        "name": order['order_lines'][0]['product_title'],
        "display_name": order['order_lines'][0]['product_title'],
        "quantity": order['order_lines'][0]['quantity'],
        "api_id": order['order_lines'][0]['order_line_id'],
        "api_code": None,
        "api_status": None,
        "sku": order['order_lines'][0]['product_sku'],
        "price": price_id
    }
    return platform_product_json

def create_platform_product_order_json_from_mirakle(order,user_id,customer_id,platform_id,total_price_id,tax_price_id,shipping_price_id):

    platform_product_order_json={
        "platform": platform_id,
        "user": user_id,
        "api_id": order.get('order_id'),
        "customer": customer_id,
        "api_code": order.get("commercial_id"),
        "api_status": order.get('order_state'),
        "total_price": total_price_id,
        "shipping_price": shipping_price_id,
        "tax_price": tax_price_id,
        "discount_percent": None,
        "isPaid": False,
        "payment_status": None,
        "isFulfilled": None,
        "api_created_at":order.get('created_date'),
        "api_updated_at":order.get('last_updated_date')
    }
    return platform_product_order_json

def create_platform_order_payment_json_from_mirakle(order,platform_id):

    platform_order_payment_json={
        "platform_order": platform_id,
        "api_id": order.get("transaction_number"),
        "paid_amount": order.get("price"),
        "paid_on": order.get("transaction_date"),
        "payment_mode": order.get("paymentType")
    }
    return platform_order_payment_json

def create_platform_order_line_item_json_from_mirakle(order,platform_order_id,platform_product_id,price_id,tax_price_id):

    platform_order_line_item_json={
        "platform_order": platform_order_id,
        "platform_product": platform_product_id,
        "api_id": order["order_lines"][0].get("order_line_id"),
        "sku": order["order_lines"][0].get("product_sku"),
        "name": order["order_lines"][0].get("product_title"),
        "price": price_id,
        "tax_price": tax_price_id,
        "product_api_id": order["order_lines"][0].get("order_line_id"),
        "product_api_variation_id": None,
        "quantity": order["order_lines"][0].get("quantity")
    }
    return platform_order_line_item_json

 # <-------------------Insert_orders_data_on_db_tables_from_mirakle------------------->
def insert_orders_data_on_db_tables_from_mirakle(order,platform_object):
    required_dict={}
    required_dict["user_id"]=platform_object.user.id
    required_dict["platform_id"]=platform_object.id

    # <-------------------Address------------------->
    address_json=create_address_json_from_mirakle(order)

    address_serialized_data=AddressSerializer(data=address_json)

    address_serialized_data.is_valid()

    print(address_serialized_data.errors)
    if address_serialized_data.is_valid():
        address_serialized_data.save()
        required_dict["address_id"]=address_serialized_data.data.get('id')
    else:
        return "Check address"

    # <-------------------Price------------------->
    price_json=create_price_json_from_mirakle(order)
    for price_type in ['price','tax_price','shipping_price']:

        price_serialized_data=PriceSerializer(data=price_json[price_type])
        price_serialized_data.is_valid()
        print(price_serialized_data.errors)

        if price_serialized_data.is_valid():

            price_serialized_data.save()
            required_dict[price_type+"_id"] =price_serialized_data.data.get('id')
        else:
            return "check price"+price_type

    # <-------------------Platform Customer------------------->
    platform_customer_json=create_platform_customer_json_from_mirakle(order,required_dict["address_id"],required_dict["platform_id"])

    platform_customer_serialized_data=PlatformCustomerSerializer(data=platform_customer_json)

    platform_customer_serialized_data.is_valid()
    print(platform_customer_serialized_data.errors)

    if platform_customer_serialized_data.is_valid():
        platform_customer_serialized_data.save()
        required_dict["platform_customer_id"] =platform_customer_serialized_data.data.get("id")
    else:
        return "check platform_customer"

    # <-------------------Platform Product------------------->
    platform_product_json=create_platform_product_json_from_mirakle(order,required_dict["platform_id"],required_dict["user_id"],required_dict["price_id"])

    platform_product_serialized_data=PlatformProductSerializer(data=platform_product_json)

    platform_product_serialized_data.is_valid()
    print(platform_product_serialized_data.errors)
    if platform_product_serialized_data.is_valid():
        platform_product_serialized_data.save()
        required_dict["platform_product_id"] = platform_product_serialized_data.data.get("id")
    else:
        return "Check platform_product"

    # <-------------------Platform Order------------------->
    platform_product_order_json=create_platform_product_order_json_from_mirakle(order,user_id=required_dict["user_id"],customer_id=required_dict["platform_customer_id"],platform_id=required_dict["platform_id"],total_price_id=required_dict["price_id"],tax_price_id=required_dict["tax_price"],shipping_price_id=required_dict["shipping_price"])

    platform_product_order_serialized_data=PlatformOrderSerializer(data=platform_product_order_json)

    platform_product_order_serialized_data.is_valid()
    print(platform_product_order_serialized_data.errors)

    if platform_product_order_serialized_data.is_valid():
        platform_product_order_serialized_data.save()
        required_dict["platform_product_order_id"]=platform_product_order_serialized_data.data.get('id')
    else:
        return "Check platform_product_order"

    # <-------------------Platform Order Payment------------------->
    platform_order_payment_json=create_platform_order_payment_json_from_mirakle(order,platform_id=required_dict["platform_id"])

    platform_order_payment_serialized_data=PlatformOrderPaymentSerializer(data=platform_order_payment_json)
    platform_order_payment_serialized_data.is_valid()
    print(platform_order_payment_serialized_data.errors)
    if platform_order_payment_serialized_data.is_valid():
        platform_order_payment_serialized_data.save()
        required_dict["platform_product_order_id"]=platform_order_payment_serialized_data.data.get('id')
    else:
        return "Check platform_order_payment "

    # <-------------------Platform Order Line------------------->
    platform_order_line_item_json=create_platform_order_line_item_json_from_mirakle(order,platform_order_id=required_dict["platform_product_order_id"],platform_product_id=required_dict["platform_product_id"],price_id=required_dict["price_id"],tax_price_id=required_dict["tax_price"])

    platform_order_line_item_serialized_data=PlatformOrderLineItemSerializer(data=platform_order_line_item_json)
    platform_order_line_item_serialized_data.is_valid()
    print(platform_order_line_item_serialized_data.errors)

    if platform_order_line_item_serialized_data.is_valid():
        platform_order_line_item_serialized_data.save()
        required_dict["platform_order_line_item_id"]=platform_order_line_item_serialized_data.data.get("id")
    else:
        return "Check platform_order_line_item "

    return True
