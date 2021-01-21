# plotter.py 
# this is used to read through the dataset and generate a plot of the data.

# imports 
import sys
import pandas as pd
import matplotlib.pyplot as plt

# read through data-set
csv_data = pd.read_csv('TAR_DIR_1/Static_Data.csv')

# break data into small chunks for plotter
def data_set(data, postion=None, start=None, end=None):
    if postion == "start":
        # if specified postion is start pull {x} rows from start of data
        return csv_data.head(int(start))
    elif postion == "end":
        # if specified postion is end pull {x} rows from end of data
        return csv_data.tail(int(start))
    elif postion == "custom":
        # if specified postion is custom pull rows between {x} & {y}
        return csv_data.iloc[int(start):int(end)]
    else:
        # default behaviour - pull first 10 rows of data
        return csv_data.head(10)

# generate plot
def plot_gen(plot_data):
    ax = plt.gca()

    plot_data.plot(kind="scatter", x="time", y="v1", ax=ax)
    plot_data.plot(kind="scatter", x="time", y="v2", color="red", ax=ax)
    plot_data.plot(kind="scatter", x="time", y="v3", color="green", ax=ax)
    plt.show()

# runner script
def run(data):

    # generate plot data
    if len(sys.argv) > 1:
        
        if len(sys.argv) > 3:
            plot_data = data_set(data, sys.argv[1], sys.argv[2], sys.argv[3])
        else:
            plot_data = data_set(data, sys.argv[1], sys.argv[2])

    else:
        plot_data = data_set(data)

    # build and open plot
    plot_gen(plot_data)

# run script
run(csv_data)