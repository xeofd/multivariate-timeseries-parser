# data-generator.py
# this is used to make a csv of random time incremented data.

# imports
import csv
import datetime
from random import seed
from random import random
from pathlib import Path

## randomiser to get random variables
seed(1)

def randomiser():
    value = random() * 10
    return value

# time incrementer
def time_inc(prev_time):
    new_time = prev_time + datetime.timedelta(seconds=1)
    return new_time

# build runner
def run():

    # find path to directory across platform
    path_parent = Path("data-generator.py").parent
    path = str(path_parent) + "/TAR_DIR_1/Static_Data.csv"

    ## create & open csv file
    with open(path, 'w', newline='') as file:

        print("begin random data generator...")

        # set initial time
        time = datetime.datetime(2000, 1, 1, 00, 00, 00)

        # begin writer
        writer = csv.writer(file)
        writer.writerow(["v1", "v2", "v3", "time"])
        for _ in range(1000000):
            if _ % 100000 == 0:
                print(str(_) + " rows done...")
            
            time = time_inc(time)
            writer.writerow([randomiser(), randomiser(), randomiser(), time])
        
        print("done!")
        print("file can be found at ../TAR_DIR_1/Static_Data.csv")

def auto_generator(read_from, write_to):

    # set data to write
    write_data = []

    with open(read_from, "r", newline="") as file:

        reader = csv.reader(file, delimiter="\n")
        for row in reader:
            write_data.append(row)

    # set file to write to
    with open(write_to, "w", newline="") as file:
        writer = csv.writer(file)
        for _ in range(301):
            writer.writerow([write_data[_]])