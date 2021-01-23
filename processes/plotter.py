# plotter.py 
# this is used to read through the dataset and generate a plot of the data.

# imports 
import sys
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# watcher


# break data into small chunks for plotter
def data_set(data, postion=None, start=None, end=None):
    if postion == "start":
        # if specified postion is start pull {x} rows from start of data
        return data.head(int(start))
    elif postion == "end":
        # if specified postion is end pull {x} rows from end of data
        return data.tail(int(start))
    elif postion == "custom":
        # if specified postion is custom pull rows between {x} & {y}
        return data.iloc[int(start):int(end)]
    else:
        # default behaviour - pull first 10 rows of data
        return data.head(10)

# generate plot
def plot_gen(plot_data):
    ax = plt.gca()

    plot_data.plot(kind="line", x="time", y="v1", ax=ax)
    plot_data.plot(kind="line", x="time", y="v2", color="red", ax=ax)
    plot_data.plot(kind="line", x="time", y="v3", color="green", ax=ax)
    plt.show()

# runner script
def run(directory, file_name, position=None, start=None, end=None):

    # find path to csv across platform
    path_parent = Path("data-generator.py").parent
    path = str(path_parent) + "/" + directory + "/" + file_name

    # read through data-set
    csv_data = pd.read_csv(path)

    # generate plot data
    if position != None:    
        if end != None:
            # if more than 3 arguments
            plot_data = data_set(csv_data, position, start, end)
        else:
            plot_data = data_set(csv_data, position, start)
    else:
        plot_data = data_set(csv_data)

    # build and open plot
    plot_gen(plot_data)

# {monitor function} - on data modify event call this
def data_update(source_data, new_data):

    # read both sources of data and combine
    source_data = pd.read_csv(source_data)
    new_data = pd.read_csv(new_data)

    data_sets = [source_data, new_data]
    combo = pd.concat(data_sets)

    # plot new data - last 20 items in the new data set
    plot_data = data_set(combo, "end", 20)

    # build new plot
    plot_gen(plot_data)