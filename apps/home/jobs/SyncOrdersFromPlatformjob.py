from apps.home.services.MirakleServices import MirakleServices
from apps.models import *


def __updatePlatformLock(platform_id, lock=True):
    platform = Platform.objects.get(pk=platform_id)
    if platform:
        platform.isProductUpdateSyncProcessing = lock
        platform.save()

def syncOrdersFromPlatform(platform):
    pass

class SyncOrdersFromPlatformJob:

    @staticmethod
    def checkAndStartSyncThread():
        idle_platforms = Platform.objects.filter(type="SOURCE", isActive=True, isOrderSyncProcessing=False)
        for platform in idle_platforms:

            # thread = Thread(target=syncOrdersFromPlatform, args=(platform, ))
            # thread.start()
