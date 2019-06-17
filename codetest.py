import sys, re

#input expects: file_name coltocompare1 coltocompare2 resultcol
g= raw_input("Enter name of file to parse, followed by which 2 columns numbers to find difference between, then which column you want outputted (separate each entry by a space)")
g = g.split(' ')
g = list(map(str, g))

try: file = open(g[0])
except IOError: sys.exit('no such file in the directory')
mylist = []
smallest, firstflag = 0, 0
result = ''

'''
helper function used to filter out rows that dont matter (checks if row is numbered, since that's a common feature i found between both of the files for the useful rows
input string -> output true/false
'''
def hasNumbers(inputString): return any(char.isdigit() for char in inputString)

'''
input a string, and remove chars other than numbers, then casts to int
input string -> output int(string)
'''
def onlynums(inputString): return int(re.sub("\D", "", inputString))

#splits file into rows based on new lines
for i in file: mylist += [i.split()]


#run time error handling: if user inputs incorrect input/parameters
if len(g) != 4: sys.exit('incorrect number of parameters; require 4 params separated by single space for each; possibly because you entetted consecutive spaces')
for x in g:
    if x == '': sys.exit('at least one of the params is empty; possibly because you enterred consecutive spaces')
if not mylist: sys.exit('file is empty')
for x in mylist:
    if not x: continue
    if hasNumbers(x[0]):
        try:
            onlynums(x[int(g[1]) - 1])
            onlynums(x[int(g[2]) - 1])
            x[int(g[3]) - 1]
        except IndexError:
            sys.exit('at least one of the column numbers selected is out of the range of column numbers in the file')
        except ValueError:
            sys.exit('at least one of the column numbers selected for finding the difference between dont all contain numbers')

'''
main logic: ignores empty/non relevant rows
keeps track of the result based on the lowest spread between two cols in that row
updates result based on max/min spread in current row
runs in O(n)/linear time complexity
'''
for x in mylist:
    if not x: continue
    if hasNumbers(x[0]):
        tempmax = onlynums(x[int(g[1]) - 1])
        tempmin = onlynums(x[int(g[2]) - 1])
        tempdiff = abs(tempmax - tempmin)
        if firstflag == 0:
            smallest = tempdiff
            result = x[int(g[3]) - 1]
            firstflag = 1
        elif tempdiff < smallest:
            smallest = tempdiff
            result = x[int(g[3]) - 1]

print result
