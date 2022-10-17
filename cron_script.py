from crontab import CronTab


my_cron = CronTab(user=True)

#  Create a new job and specify which script should be executed
job = my_cron.new(command='/usr/bin/python3 /home/darik/Desktop/script.py')
job.setall('0 0 1 * *')  # specify the job interval
my_cron.write()