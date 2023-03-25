from rest_framework.views import APIView
from apps.home.serializers import *
from apps.models import *
from .services.DataBaseServices import *
from .services.GenralServices import *
from .response import endpointResponse
from .services.MirakleServices import MirakleServices
from apps.home.jobs.SyncOrdersFromPlatformjob import SyncOrdersFromPlatformJob
from django.middleware.csrf import get_token
from django.db.models import Q

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


    def __helper(self,platform_object):

        platform_serialized_data = PlatformSerializer(platform_object)

        # platform_serialized_data.data["user"].pop("password")

        return  platform_serialized_data.data

    def get(self,request):

        try:

            user_id=request.query_params.get("user_id",None)

            platform_id = request.query_params.get("platform_id", None)

            print(platform_id)

            type = request.query_params.get("type",None)

            if platform_id :

                platform_object=Platform.objects.get(id=platform_id) if Platform.objects.filter(id=platform_id).exists() else None

                if platform_object:

                    platform_serialized_data=self.__helper(platform_object)

                    return endpointResponse(status_code=200, massage="Ok", data=platform_serialized_data)

                return endpointResponse(status_code=400, massage="Bad Request", data=[])


            platform_data_list=[]

            query=Q(user=user_id,type=type) if type is not None else Q(user=user_id)

            for platform_object in Platform.objects.filter(query):

                platform_serialized_data=self.__helper(platform_object)

                platform_data_list.append(platform_serialized_data)

            return endpointResponse(status_code=200, massage="Get Method", data=platform_data_list)

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])

    def post(self, request):

        try:

            platform_serialized_data=PlatformSerializer(data=request.data)

            if platform_serialized_data.is_valid():

                platform_serialized_data.save()

                return endpointResponse(status_code=200, massage="Platform  Created", data=platform_serialized_data.data)

            return endpointResponse(status_code=400, massage="Platform  Not Created", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])


    def put(self,request,pk):

        try:

            platform_object=Platform.objects.get(id=pk)

            platform_serialized_data = PlatformSerializer(platform_object,data=request.data)


            if platform_serialized_data.is_valid():

                platform_serialized_data.save()

                return endpointResponse(status_code=200, massage="Platform  Created", data=platform_serialized_data.data)

            return endpointResponse(status_code=400, massage="Platform  Not Created", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])




class CsrfTokenView(APIView):
    def get(self, request):

        csrf_token_dict={}

        csrf_token_dict["csrf_token"]=get_token(request)

        return endpointResponse(status_code=200, massage="OK", data=csrf_token_dict)






class MirakleGetOrdersView(APIView):
    def get(self, request):

        print(get_token(request))

        # SyncOrdersFromPlatformJob.checkAndStartSyncThread()

        # platform=Platform.objects.get(id=5)
        #
        # mirakleServicesObject=MirakleServices(platform)
        #
        # Order_object=mirakleServicesObject.GetOrders()
        #
        # if Order_object.isSuccess:
        #
        #     for order in Order_object.body['orders'][0:2]:
        #
        #         if not PlatformOrder.objects.filter(api_id=order.get("order_id")).exists():
        #
        #             res=mirakleServicesObject.CreateOrdersOnDBTables(order)
        #
        #         else:
        #
        #             res=mirakleServicesObject.UpdateOrdersOnDBTables(order)


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


        return endpointResponse(status_code=200, massage="OK", data=[])

        # return endpointResponse(status_code=200, massage="Not Ok ", data=[])
        
        # return endpointResponse(status_code=400, massage="Bad request", data=[])