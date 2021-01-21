# runner.py - this is the core python file, run this to start program

# imports
import sys
import plotter
import data_generator

# start script

if __name__ == "__main__":

    # first check if user wants to generate random data and if so generate
    has_input = False

    while has_input != True:
        usr_input = input("Do you want to generate new data? (y/n): ")
        if (usr_input == "y" or usr_input == "n"):
            has_input = True
            break

    if usr_input == "y":
        data_generator.run()

    # generate plotter
    print("generating plot...")

    # plotter can accept args - position: string, start: int, end: int
    # if none given it will run on defaults

    usr_args = []
    has_input = False

    while has_input != True:
        usr_input = input("Do you want to plot specific data? (y/n): ")
        if (usr_input == "y" or usr_input == "n"):
            has_input = True
            break

    if usr_input == "y":
        # get position
        postion_arg = input("Where do you want to pull rows from? (start/end/custom): ")
        usr_args.append(postion_arg)

        # get start or range
        if (postion_arg == "start" or postion_arg == "end"):
            row_arg = input("How many rows to capture? (<100 rows reccomended): ")
            usr_args.append(row_arg)
        else:
            start_arg = input("First row to capture from?: ")
            end_arg = input("Final row to capture? (<100 rows reccomended): ")

            usr_args.append(start_arg)
            usr_args.append(end_arg)
        
        print("generating using custom settings...")
    else:
        print("generating using defaults...")


    if len(usr_args) > 0:
        if len(usr_args) > 2:
            # if position, start and end provided as args
            plotter.run(usr_args[0], usr_args[1], usr_args[2])
        else:
            plotter.run(usr_args[0], usr_args[1])
    else:
        plotter.run()