from .RestServices import *
from .GenralServices import *
from apps.models import *


class MirakleServices():

    base_url = 'https://marketplace.kingfisher.com/api/'

    def __init__(self, platform):

        self.headers =self.__headers(platform.credentials.token_secret)

        self.platform=platform


    def GetOrders(self)->ApiResponse:
        url=self.base_url+"orders"

        response_object=GetRequest(url=url,headers=self.headers)

        return response_object

    def GetSingleOrders(self,order_id)->ApiResponse:

        url=self.base_url+"orders"+"?order_ids"+order_id

        response_object=GetRequest(url=url,headers=self.headers)

        return response_object

    def GetShipments(self) -> ApiResponse:

        url = self.base_url + "shipments"

        response_object = GetRequest(url=url, headers=self.headers)

        return response_object
    def __headers(self,authorization):

        headers = {
            "Content-Type": "application/json",
            "Authorization": authorization,
        }
        return headers

    @staticmethod
    def CreateOrdersOnDBTables(self,order):
        try:

            res=insert_and_update_orders_data_on_db_tables_from_mirakle(order,self.platform)

            return res

        except Exception as e:
            print(e)

    @staticmethod
    def UpdateOrdersOnDBTables(self,order):
        # try:

        res=insert_and_update_orders_data_on_db_tables_from_mirakle(order, self.platform,update=True)

        print("UpdateOrdersOnDBTables",res)

        return res

        # except Exception as e:
        #     print('UpdateOrdersOnDBTables Exceptions', e)