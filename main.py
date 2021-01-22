# main.py - this is core runner file. run this to start the app

# imports
import processes.app as app
import processes.monitor as monitor
import time

# start the app
if __name__ == "__main__":

    # begin
    print("Starting app...")
    time.sleep(1)

    app.run()

    print("Starting directory monitor...")
    print("Monitoring /TAR_DIR_1...")
    monitor.run()
