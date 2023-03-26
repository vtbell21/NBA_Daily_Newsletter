import time
import datetime
import os

# set the time you want the script to run
run_time = datetime.time(hour=21, minute=57, second=0)

while True:
    # calculate the number of seconds until the scheduled time
    today = datetime.datetime.today()
    scheduled_time = datetime.datetime.combine(today, run_time)

    if scheduled_time < today:
        scheduled_time += datetime.timedelta(days=1)

    time_to_wait = (scheduled_time - today).seconds
    # wait until the scheduled time
    time.sleep(time_to_wait)
    # once time.sleep() finishes, an email will be sent
    os.system('python data_configuration.py')
    os.system('python email.py')
