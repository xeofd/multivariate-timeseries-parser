# events.py - this file contains the functions to run when the monitor calls events

# imports
import re
from pathlib import Path
import processes.plotter as plotter
import processes.data_generator as dg
import processes.user_input as user_input


# on modify event
def on_modify(prev_path, new_path):

    # inform user of new data set
    print("Data set modified! Generating new plot...")
    plotter.data_update(prev_path, new_path)