#!/usr/bin/env python
"""
Checks validity of error messages and
gives user commands to execute the program
from the other file on either w_data.dat
or soccer.dat
"""

import subprocess
import sys

WRONG_INPUT_ERROR = """enter these args 'myscript.py soccer' or
'myscript.py w_data' to get the answer to problems 
1 or 2 with respect to the prompt"""


def user_commands(input_string):
    """
    :param input_string:
    :return string:

    takes in 'soccer' or 'w_data' input
    to give corresponding output based on
    soccer.dat or w_data.dat
    """
    temp_string = 'python minspread.py '
    if input_string == 'soccer':
        temp_string += 'soccer.dat 7 9 2'
    elif input_string == 'w_data':
        temp_string += 'w_data.dat 2 3 1'

    my_process = subprocess.Popen(temp_string, stdout=subprocess.PIPE)
    out, err = my_process.communicate()
    print 'Output: ' + str(out)
    print 'Errors: ' + str(err)


def main():
    """
    user should type into command line:
    python testing.py soccer
    OR
    python testing.py w_data
    if they dont do that, they will receive an error message.
    minspread.py has much more comprehensive error checking
    but that will not be necessary to demonstrate through
    the use of just this program, as this program
    ensures that at the highest level, the user knows
    two simple commands that will get them their results
    """
    # check to see if user entered exactly 2 args, one for python program, other for command
    if len(sys.argv) != 2:
        sys.exit(WRONG_INPUT_ERROR)

    my_command = str(sys.argv[1])

    if my_command == 'w_data' or my_command == 'soccer':
        user_commands(my_command)
    else:
        sys.exit(WRONG_INPUT_ERROR)


main()
