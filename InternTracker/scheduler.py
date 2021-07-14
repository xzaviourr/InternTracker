import schedule
import time
import os

def run() :

    # This is only for windows as for linux python3 needs to be used
    os.system("python main.py") 

# Scheduler has been set to run on every monday
schedule.every().monday.do(run)

while True :

    schedule.run_pending()
    time.sleep(1)