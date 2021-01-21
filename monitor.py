# monitor.py - this file holds the runner for the directory monitor to check for new files

# imports
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# runner
def run():
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    path = "./TAR_DIR_1"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()