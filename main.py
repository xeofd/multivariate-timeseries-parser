# main.py - this is core runner file. run this to start the app

# imports
import time
import processes.app as app
from processes.monitor import Monitor

# start the app
if __name__ == "__main__":

    # begin main app
    print("Starting app...")
    time.sleep(1)

    app.run()

    # set previous data for passing to data

    # begin monitor
    print("Starting directory monitor...")
    print("Monitoring /TAR_DIR_1...")
    monitor = Monitor("./TAR_DIR_1/Static_Data.csv")
    monitor.run()
