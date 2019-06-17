# codetest
This single file is my answer to the code test I was assigned. 

# Below is the exact prompt that I was given, with an answer to the given question at the end of the prompt: 

Thanks for taking the time to do the exercise! Please complete the following in a dynamic language:

1) In the attached file (w_data.dat), you’ll find daily weather data.   Download this text file, then write a program to output the day number (column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the third column).

2) The attached soccer.dat file contains the results from the English Premier League.  The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

q) Is the way you wrote the second program influenced by writing the first?

a) I read both of the prompts and realized that there were a lot of similarities between the two, even though the info needed from both of these files were in different column numbers in both of the dat files. Once I got down the basic skeleton of the code, such as the logic, I just had to generalize the code, and tried to abstract the process away from the user as much as possible. As long as the user could find which column numbers he wanted to compare, and which column he wanted the result from, the user could input those 3 parameters, preceded by the file_name, to see the result. This way, the user could use the same files to find the lowest spread between other columns that all contained numbers, too. I could have hard-coded this, but the minimal extra effort the user would take to run the program would drastically increase the program's power outside the scope of just this problem.

How to use: 
1) run program
2) enter a string of this format on the commandline:
file_name columntocompare1 columntocompare2 desiredresultcolumn
# --> Here are the two inputs required to answer questions 1 and 2:
1) w_data.dat 2 3 1
2) soccer.dat 7 9 2

I designed some run-time error handling in case the user wishes to use this program for other dat files. 

Notes: This program runs with a few assumptions. First of all, the inputted file is separated into columns like the ones provided 
as samples. Second, the two columns that are menat to be compared have all inputs composed of strings that contain numbers. Third, each
row that consist of real data starts off with the first element in the corresponding row being a number (things like '1', '1.', '1*', '/1', etc will be interpreted as '1', while 'abc', 'xy', 'z', will be invalid inputs for comparison). I used some error-handling to print error messages that the use can hopefully use to enter a valid input to use the program. 


