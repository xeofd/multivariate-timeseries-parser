# events.py - this file contains the functions to run when the monitor calls events

# imports
import re
import processes.plotter as plotter
import processes.data_generator as dg
import processes.user_input as user_input

regex_pattern = "[\./][/]"

# on create event
def create(path):
    # strip path of punctuation and set directory and file_name
    result = re.split(regex_pattern, path)

    # inform user of new data set
    print("New data set found! Generating new plot...")
    plotter.run(result[0], result[1], "end", 5)

# on modify event
def modify(path):
    # strip path of punctuation and set directory and file_name
    result = re.split(regex_pattern, path)

    # inform user of new data set
    print("Data set modified! Generating new plot...")
    plotter.run(result[0], result[1], "end", 5)