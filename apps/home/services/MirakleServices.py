from .RestServices import *


class MirakleServices():

    base_url = 'https://marketplace.kingfisher.com/api/'

    def __init__(self, platform,order_ids):

        self.headers =self.__headers(platform.credentials.token_secret)

        self.order_ids=order_ids


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