# plotter.py 
# this is used to read through the dataset and generate a plot of the data.

# imports 
import pandas as pd
import matplotlib.pyplot as plt

# read through data-set
csv_data = pd.read_csv('TAR_DIR_1/Static_Data.csv')

# break data into smaller chunks
# doing this as trying to plot all 1 million rows is not feasable

plot_data = csv_data.tail(5) # get final 5 rows

# print(data.keys())

plot_data.plot(x="time", y="v1")
plt.show()
