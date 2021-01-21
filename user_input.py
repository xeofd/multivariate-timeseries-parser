# user_input.py - this file contains functions for accepting user input

# validator
# validator requires two params - txt: string, args: array[string]
def validator(txt, args):

    # set valid input bool
    is_valid = False

    # run loop
    while is_valid != True:
        # Create input string
        usr_input = input(txt)

        # Check user input is valid
        for arg in args:
            if usr_input == arg:
                return usr_input

# static