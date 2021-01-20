# plotter.py 
# this is used to read through the dataset and generate a plot of the data.

# imports 
import pandas as pd
import matplotlib.pyplot as plt

# read through data-set

data = pd.read_csv('TAR_DIR_1/Static_Data.csv', index_col=0, parse_dates=True)

data.plot.scatter(x="v1", y="time")