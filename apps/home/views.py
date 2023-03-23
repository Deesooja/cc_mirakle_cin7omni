from rest_framework.views import APIView
from apps.home.serializers import *
from apps.models import *
from .services.DataBaseServices import *
from .services.GenralServices import *
from .response import endpointResponse
from .services.MirakleServices import MirakleServices

class PlatformCredentialsView(APIView):
    def post(self, request):
        try:
            if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

                platform_credentials_serialized_data=PlatformCredentialsSerializer(data=request.data)

                if platform_credentials_serialized_data.is_valid():

                    platform_credentials_serialized_data.save()

                    return endpointResponse(status_code=200, massage="Platform Credentials Created", data=platform_credentials_serialized_data.data)

                return endpointResponse(status_code=400, massage="Platform Credentials Not Created", data=[])

            return endpointResponse(status_code=400, massage="Platform Credentials already exists", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])





class PlatformSettingsView(APIView):
    def post(self, request):

        try:
            # if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

            platform_settings_serialized_data=PlatformSettingsSerializer(data=request.data)

            if platform_settings_serialized_data.is_valid():

                platform_settings_serialized_data.save()

                return endpointResponse(status_code=200, massage="Platform settings Created", data=platform_settings_serialized_data.data)

            return endpointResponse(status_code=400, massage="Platform settings Not Created", data=[])

            # return endpointResponse(status_code=400, massage="Platform Credentials already exists", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])

class PlatformView(APIView):
    def post(self, request):

        try:

            # if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

            response_data=platrform_data_check_and_create_new_data(request.data)

            if response_data['status']:


                platform_serialized_data=PlatformSerializer(data=request.data)

                if platform_serialized_data.is_valid():

                    platform_serialized_data.save()

                    return endpointResponse(status_code=200, massage="Platform  Created", data=platform_serialized_data.data)

                return endpointResponse(status_code=400, massage="Platform  Not Created", data=[])

            return endpointResponse(status_code=400, massage=response_data['massage'], data=[])

            # return endpointResponse(status_code=400, massage="Platform Credentials already exists", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])

class MirakleGetOrdersView(APIView):
    def get(self, request):

        platform=Platform.objects.get(id=5)

        mirakleServicesObject=MirakleServices(platform)

        Order_object=mirakleServicesObject.GetOrders()

        if Order_object.isSuccess:

            for order in Order_object.body['orders'][0:2]:

                if not PlatformOrder.objects.filter(api_id=order.get("order_id")).exists():

                    res=mirakleServicesObject.CreateOrdersOnDBTables(order)

                else:

                    res=mirakleServicesObject.UpdateOrdersOnDBTables(order)


            # address_json=create_address_json(Order_object.body['orders'][0])
            # print(address_json)
            # price_json=create_price_json(Order_object.body['orders'][0])
            # print(price_json)
            # platform_customer_json=create_platform_customer_json(Order_object.body['orders'][0],1,3)
            # print(platform_customer_json)
            # platform_product_json=create_platform_product_json_from_mirakle(Order_object.body['orders'][0], 1, 3, 1)
            # print(platform_product_json)
            # product_order_json=create_platform_product_order_json_from_mirakle(Order_object.body['orders'][0],1,3,1,1,2,3)
            # print(product_order_json)
            # platform_order_payment_json=create_platform_order_payment_json_from_mirakle(Order_object.body['orders'][0],3)
            # print(platform_order_payment_json)
            # platform_order_line_item_json=create_platform_order_line_item_json_from_mirakle(Order_object.body['orders'][0], 3, 1, 1,2)
            # print(platform_order_line_item_json)


            return endpointResponse(status_code=200, massage=res, data=[])

        return endpointResponse(status_code=200, massage="Not Ok ", data=[])
        
        # return endpointResponse(status_code=400, massage="Bad request", data=[])