from apps.home.services.MirakleServices import MirakleServices
from apps.models import *
from threading import Thread
# from apps.home.thread import CreateTheads

def __updatePlatformLock(platform, lock=True):
    # platform = Platform.objects.get(pk=platform_id)
    if platform:
        platform.isOrderSyncProcessing = lock
        platform.save()

def syncOrdersFromPlatform(platform):

    __updatePlatformLock(platform,True)

    mirakleServicesObject=MirakleServices(platform)

    apiResponceObject=mirakleServicesObject.GetOrders()

    if apiResponceObject.isSuccess:

        print("apiResponceObject.body[orders]",len(apiResponceObject.body["orders"]))

        for order in apiResponceObject.body["orders"][0:2]:

            if not PlatformOrder.objects.filter(api_id=order.get("order_id")).exists():

                mirakleServicesObject.CreateOrdersOnDBTables(order)

            else:
                mirakleServicesObject.UpdateOrdersOnDBTables(order)
                print("Order already exists")

    __updatePlatformLock(platform,False)

class SyncOrdersFromPlatformJob:

    @staticmethod
    def checkAndStartSyncThread():
        threads_list=[]

        idle_platforms = Platform.objects.filter(isActive=True , type="SOURCE", isOrderSyncProcessing=False )

        for platform in idle_platforms:

            thread = Thread(target=syncOrdersFromPlatform, args=(platform,))

            thread.start()

            threads_list.append(thread)

        for t in threads_list:

            t.join()
