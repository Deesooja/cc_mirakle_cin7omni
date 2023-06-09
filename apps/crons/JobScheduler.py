from django_cron import CronJobBase, Schedule
from apps.home.jobs.SyncOrdersFromPlatformjob import SyncOrdersFromPlatformJob



class SyncOrdersFromPlatform(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.sync_orders_from_platform'

    def do(self):
        print("Starting job")
        SyncOrdersFromPlatformJob.checkAndStartSyncThread()
        print("Done")