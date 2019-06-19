#!/usr/bin/env python
"""
This single file is my answer to the code test I was assigned.
enter a string of this format on the commandline:
file_name columntocompare1 columntocompare2 desiredresultcolumn
It prints out the desiredcolumn with the lowest spread between
columntocompare1 and columntocompare2, from all of the given rows
"""
import sys
import re

INPUT_MESSAGE = """Enter name of file to parse, followed by which
2 columns numbers to find the difference between them, then which
column you want outputted (separate each entry by a space) \n"""

# stored these messages here for easier test cases; not part of actual logic
ERROR_MESSAGE_1 = 'no such file in the directory'

ERROR_MESSAGE_2 = """incorrect number of parameters;
require 4 params separated by single
space for each; possibly because you
entered consecutive spaces
(dont put space at the end of input)"""

ERROR_MESSAGE_3 = """at least one of the params is empty;
possibly because you entered consecutive spaces/at least
one of the column parameters entered is not a number"""

ERROR_MESSAGE_4 = 'file is empty'

ERROR_MESSAGE_5 = """desiredresultcolumn not a number;
could also be because you entered 
nonnumerical column number input"""

ERROR_MESSAGE_6 = """at least one of the column numbers selected is out
of the range of column numbers in the file"""

ERROR_MESSAGE_7 = """at least one of the columns selected for finding
the difference dont all contain numbers; could also be 
because you entered nonnumerical column number input"""


def has_numbers(input_string):
    """
    :param input_string:
    :return boolean:

    helper function used to filter out rows that dont matter
    (checks if row is numbered, since that's a common feature
    i found between both of the files for the useful rows
    """
    return any(char.isdigit() for char in input_string)


def only_nums(input_string):
    """
    :param input_string:
    :return int:
    input a string, and remove chars other than numbers, then casts to int
    """
    return int(re.sub(r"\D", "", input_string))


def validate():
    """
    :param
    :return int, int, string, list:

    take input, then check input for runtime error-handling
    return the list containing input parameters
    input expects: file_name coltocompare1 coltocompare2 resultcol
    """
    if len(sys.argv) != 5:
        sys.exit(ERROR_MESSAGE_2)

    filename = sys.argv[1]
    colcomp1 = int(sys.argv[2]) - 1
    colcomp2 = int(sys.argv[3]) - 1
    colresult = int(sys.argv[4]) - 1

    try:
        myfile = open(filename)
    except IOError:
        sys.exit(ERROR_MESSAGE_1)
    my_list = []
    # splits file into rows based on new lines
    for i in myfile:
        my_list += [i.split()]

    # run time error handling: if user inputs incorrect input/parameters
    for x_temp in sys.argv:
        if x_temp == '':
            sys.exit(ERROR_MESSAGE_3)

    if not my_list:
        sys.exit(ERROR_MESSAGE_4)

    return colcomp1, colcomp2, colresult, my_list


def main():
    """
    main logic:
    How to use:
    1) run program
    2) enter a string of this format on the commandline:
        file_name columntocompare1 columntocompare2 desiredresultcolumn
        (dont put a space at the end of user input)
    more main logic: ignores empty/non relevant rows
    keeps track of the result based on the lowest spread
    between two cols in that row updates result based on
    max/min spread in current row runs in O(n)/linear time complexity
    """
    colcomp1, colcomp2, colresult, my_list = validate()
    smallest, firstflag = 0, 0
    result = ''

    for x_row in my_list:
        if not x_row:
            continue
        if has_numbers(x_row[0]):
            try:
                tempmax = only_nums(x_row[colcomp1])
                tempmin = only_nums(x_row[colcomp2])
                tempdiff = abs(tempmax - tempmin)
                try:
                    x_row[colresult]
                except ValueError:
                    sys.exit(ERROR_MESSAGE_5)
                except IndexError:
                    sys.exit(ERROR_MESSAGE_6)
                if firstflag == 0:
                    smallest = tempdiff
                    result = x_row[colresult]
                    firstflag = 1
                elif tempdiff < smallest:
                    smallest = tempdiff
                    result = x_row[colresult]
            except IndexError:
                sys.exit(ERROR_MESSAGE_6)
            except ValueError:
                sys.exit(ERROR_MESSAGE_7)

    print result


# runs the main function logic
main()
