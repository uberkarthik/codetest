# codetest
This minspread.py is my answer to both of the problems in the code test I was assigned. However, I added the myscript.py file to make minspread.py even more usable than it normally would be. I've explained the details below. Please do note that I do, indeed, have one file (minspread.py) as the main logic to answer both problems, and that the myscript.py one is a helper script that increases the  scalability and usability of minspread.py.

# Below is the exact prompt that I was given, with an answer to the given question at the end of the prompt: 

Thanks for taking the time to do the exercise! Please complete the following in a dynamic language:

1) In the attached file (w_data.dat), you’ll find daily weather data.   Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

2) The attached soccer.dat file contains the results from the English Premier League.  The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

q) Is the way you wrote the second program influenced by writing the first?

a) I read both of the prompts and realized that there were a lot of similarities between the two, even though the info needed from both of these files were in different column numbers in both of the dat files. Once I got down the basic skeleton of the code, such as the logic, I just had to generalize the code, and tried to abstract the process away from the user as much as possible. 
# minspread.py:
Previously, I had it so that as long as the user could find which column numbers he wanted to compare, and which column he wanted the result from, the user could input those 3 parameters, preceded by 'python minspread.py file_name', to see the result. This way, the user could use the same files to find the lowest spread between other columns that all contained numbers, too. I could have hard-coded this, but the minimal extra effort the user would take to run the program would drastically increase the program's power outside the scope of just this problem. The program can still be run in such a manner. 
# myscript.py:
Since then, I decided to make it easier on those who decide to test specifically the results for the two provided files. Another way to run my script can be to run 'python myscript.py soccer' or 'python myscript.py w_data'. I did this extra step because it would make it easier/better for scalability and long-term usage. In the future, if the minspread.py scripts needs to be run, it is much easier to remember the word "soccer" or "w_data" rather than all the column numbers of each of the things you want results from. It also enables developers to more easily add and create more recognizable names for each specific scenario that they might code for by adding it into this script. 

# Pylint, PEP8 standards, Hardcoding: 
I used scored 10/10 on pylint, and as far as I could tell, I followed PEP8 standards. I did not hard-code anything in this code, as it dynamically takes in the user input to populate the variables used for main logic. If you notice anything that looks like hard-coding, it is probably used for error-handling purposes. 

How to use: 
1) run program
2) enter a string of this format on the commandline:
file_name columntocompare1 columntocompare2 desiredresultcolumn
# --> Here are the ways required to answer questions 1 and 2:
1) minspread.py 
  
  a) python minspread.py w_data.dat 2 3 1
  
  b) python minspread.py soccer.dat 7 9 2
  
2) myscript.py

  a) python myscript.py w_data
  
  b) python myscript.py soccer
  

I designed some run-time error handling in case the user wishes to use this program for other dat files. 

Notes: This program runs with a few assumptions. First of all, the inputted file is separated into columns like the ones provided 
as samples. Second, the two columns that are meant to be compared have all inputs composed of strings that contain numbers. Third, each
row that consist of real data starts off with the first element in the corresponding row being a number (things like '1', '1.', '1*', '/1', etc will be interpreted as '1', while 'abc', 'xy', 'z', will be invalid inputs for comparison). I used some error-handling to print error messages that the user can hopefully use to enter a valid input to use the program. 


