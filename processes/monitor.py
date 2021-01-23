# monitor.py - this file holds the class for the directory monitor and class for the event handler

# imports
import sys
import time
from pathlib import Path
import processes.events as event_func
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# find path to csv across platform
path_parent = Path("monitor.py").parent
path = str(path_parent) + "/TAR_DIR_1"

# build monitor class
class Monitor:

    # set directory
    WATCH_DIR = path

    def __init__(self, prev_data):
        self.observer = Observer()
        self.prev_data = prev_data

    def run(self):
        # set event handler
        event_handler = Handler(self.prev_data)

        # set observer schedule
        self.observer.schedule(event_handler, self.WATCH_DIR, recursive=True)

        # start observer
        self.observer.start()

        try:
            while True:
                # every 5 seconds check for changes
                time.sleep(5)
        except:
            self.observer.stop()
            print("Monitor stopped...")
        
        self.observer.join()

# build handler class
class Handler(FileSystemEventHandler):

    def __init__(self, prev_data):
        self.prev_data = prev_data

    def on_any_event(self, event):
        
        # if directory based event ignore
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            ## when create even called stop the monitor and run the file created event func
            print("File created!")

        elif event.event_type == 'modified':
            ## when modify event called stop the monitor and run the file modified function
            event_func.on_modify(self.prev_data, event.src_path)
