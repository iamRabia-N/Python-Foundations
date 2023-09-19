'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Control Statements
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
# Control statements defines how the code will be executed. Control statements are categorized into two types which are as follows:
# Selection: Selection statements help in making decision. Examples: if, if/else, if/elif/else, nested if.
# Repetition: Repetition statements help in repeating. Example: for, while


'''
_________________________________________________________________________________________________
Selection Statements (if, if/else, if/elif/else, nested if) 
_________________________________________________________________________________________________


If (One-Way Selection) 
________________________

'''

# It enables us to run a specific piece of code only when a given condition is met or satisfied. A single condition is checked by an if statement. Remember to include a colon at the end of each line containing a statement declaration.

' Syntax '
# if <condition>:
#      <statements>

' Example '
x = 100
if x == 100:
   print('Value "100" is assigned to variable "x"')



''' 
if/else (Two-Way Selection)
_____________________________

'''

# The if-else statement checks the condition and runs the body of if when the test condition is True, but the body of else is executed if the condition is False.

' Syntax '
# if <condition>:
#      <statements>
# [else:
#       <statements>]

' Example '
x = 100
if x == 100:
   print('Value "100" is assigned to x variable.')
else:
   print('Value "100" is not assigned to x variable.')



''' 
if/elif/else
_______________
'''
 
# The general syntax for the if/elif/else statement is as follows: 
# 1: if <condition>:
# 2:     <statements>
# 3: [elif <condition>:
# 4:      <statements>]
# 5: [elif <condition>:
# 6:       pass]
# 7:  …
# 8: [else:
# 9:      <statements>]
# It should be noted that the elif and else clauses are both optional. As shown in lines 3 through 7, using elif is only necessary when dealing with several situations. Line 6 begins with an empty phrase that does nothing. It's called a pass.  Pass is used to indicate upcoming work.

' Example '
x = 100
y = 10
if x == y:
   print("x and y have same values.")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")



''' 
Nested if (Multiple Selections)
__________________________________
'''

# Nested if statements are if statements that are contained within another if statement.
' Example '
x = 1
y = 10
z = 100
if x > y:
   if x > z:
      print("Value of x is large")
   else:
       print("Value of z is large ")
elif y > z:
    print("Value of y is large ")
else:
     print("Value of z is large ")



'''
_________________________________________________________________________________________________
Repition Statements (for, while) 
_________________________________________________________________________________________________


for 
_____
'''

# The for statement creates loops within a sequence (list). Each element in the sequence, in turn, sets a value to a variable. 
# Syntax
# for <variable> in <sequence>:
#         <statements>
# [else: 
#         <statements> ] 
# The else clause is executed only when the for statement is not run at all or after the previous loop has been completed. In other words, unless the break statement is invoked within the loop, the else statement is always executed. 

' Examples '
for n in [2,4,6,8,10]: 
        print (n)
# Output: 2,4,6,8,10
 
t = [(1,3),(5,7),(11,13)] 
for t1, t2 in t: 
      print (t1, t2)
# Output: 1 3 
#         5 7 
#        11 13


''' 
 while  
________
'''
# The while statement creates a loop that performs the statements as long as the condition is true. Syntax
# while <condition>:
#             <statements>
#  [else: 
#            <statements> ]
# The else clause is only invoked if the while statement is not executed or if the final loop has been completed. In other words, unless the break statement is invoked within the loop, the else statement is always executed. 

' Example '
x = 6 
while x > 0: 
       print (x)
       x = x-1 
# Output: 6 5 4 3 2 1
# The pass statement does nothing in the following example, and the condition will always be true. As a result, an infinite loop is implemented. 
while 1: 
   pass 



''' 
 break 
________
'''

# Break/continue are used within the for and while loop types.
# The break clause terminates a loop statement without running the else clause. 

' Example '
for a in [1, 2, 3, 4, 5, 6]: 
      print (x) 
      if x == 4: 
          break 
      else: 
         print ("Completed.")
# Output: 1 2 3  4


''' 
Continue 
__________
'''

# The continue clause skips the rest of the loop block, returning to the top of the loop. 
# Example
for a in [1, 2, 3, 4, 5, 6]: 
      print (x)
      if x == 4: 
          continue 
      else: 
         print ("Completed.") 
# Output: 1 2 3 5


'''
_________________________________
Identation in Python
________________________________
''' 

# Python uses indentation to delimit code chunks. When you indent a block of code, you specify how the statements are organized. It also prevents problems caused by incorrect indentation. The following C or Perl code, for example, appears to be a single if statement, yet the second statement is always executed:
# if (expression) 
#      statement1; 
#       statement2; 

# Python does not have this issue because indentation specifies block structure. 
# Another advantage of this design is that it allows you to reduce the size of your code by utilizing indentation instead of traditional block delimiters. 
# I recommend that you write one sentence per line, with a newline (ENTER) to end each line. If you want to have more than one statement on the same line, use semicolons to divide them, as demonstrated below: 
print ("Children are playing..."); print ("cricket...") 

# Remember to use a backslash at the end of any lines that need to be split into two.


