import schedule
import time
import os

# Gets the number of cores present in system
cpus = os.cpu_count()

def run() :

    # Runs program based on host os
    if (os.name == "nt") :
        os.system("python new_main.py")
    else :
        os.system("python3 new_main.py") 

# Scheduler has been set to run everyday at 0000 hrs
schedule.every().day.do(run)

while True :

    schedule.run_pending()
    time.sleep(1)