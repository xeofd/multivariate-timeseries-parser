# data generator
# this is used to make a csv of random time incremented data.

# imports
from random import seed
from random import random
import csv
import datetime

## randomiser to get random variables
seed(1)

def randomiser():
    value = random() * 10
    return value

# time incrementer
def time_inc(prev_time):
    new_time = prev_time + datetime.timedelta(seconds=1)
    return new_time

## create & open csv file

with open('TAR_DIR_1/Static_Data.csv', 'w', newline='') as file:
    # set initial time
    time = datetime.datetime(2000, 1, 1, 00, 00, 00)

    # begin writer
    writer = csv.writer(file)
    writer.writerow(["v1", "v2", "v3", "time"])
    for _ in range(1000000):
        time = time_inc(time)
        writer.writerow([randomiser(), randomiser(), randomiser(), time])