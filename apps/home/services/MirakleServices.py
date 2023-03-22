from .RestServices import *
from .GenralServices import *


class MirakleServices():

    base_url = 'https://marketplace.kingfisher.com/api/'

    def __init__(self, platform,order_ids):

        self.headers =self.__headers(platform.credentials.token_secret)

        self.order_ids=order_ids

        self.platform=platform


    def GetOrders(self)->ApiResponse:
        url=self.base_url+"orders"

        response_object=GetRequest(url=url,headers=self.headers)

        return response_object

    def GetSingleOrders(self)->ApiResponse:

        url=self.base_url+"orders"+"?order_ids"+self.order_ids

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


    def CreateOrdersOnDBTables(self):
        response_object=self.GetOrders()
        # for order in response_object.body["orders"]:
        res=insert_orders_data_on_db_tables_from_mirakle(response_object.body["orders"][0],self.platform)
        return res

