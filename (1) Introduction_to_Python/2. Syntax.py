'''
------------
Basic Syntax
-------------
'''

# Let's start interacting with Python by printing "Hello World!" on the screen.
print ("Hello World!")
# In Python, print () is used to display content on the screen. Semicolon at the end of line is not required but small brackets required in print statement. 

# Example 02
x = 2+8
x*2
print (x) 


''' 
Few points to keep in mind about variables in Python:
_________________________________________________________
'''

# 1.	Declaring the type of a variable is not required in Python. Because it is reinitialized every time a value is given to it, the same variable name can have different types at different times, as seen in the following example:
a = "I am learning Python"
print (a)
# Output: I am learning Python

a = 1250
print (a)
# Output: 1250

# 2.	It is a case-sensitive language. It means variables names should be corrected right in order for them to work right. For example:
a = "I am learning Python"
print (a)  # Output: I am learning Python
print (A)  # Output: NameError: name 'A' is not defined

# 3.	In variables, you have to understand the concepts of keywords, identifiers, and literals.
# Keywords are predefined, reserved words that are used in Python programming and have special significance to the compiler.
# Identifiers: Variables, classes, and methods are given names using identifiers.
# Literals: The value assigned to an identifier or variable.


''' 
How to add comments in Python?
_________________________________________________________
'''

# There are two types of comments we can add in python:
# 1.	Single-line Comments
# # comment here
# Put "#" in start of the line to comment it.

# 2.	Multi-Line Comments
# 	Use multiple "#" at start of each line to comment a paragraph or multi-lines.
# Example: 
# # You can comment multi-
# # line text by using 
# # multiple number sign 
# # multiple times 
# # at 
# # start of each
# # line

# 	Use single or double quotations at start and end of line to comment it.
# Example:
# 'You can comment multi- line text by using multiple number sign single or double quotation at start and end of text that wants to be commented'

# 	Use ''' ''' and put content in between these 3-single-quotation.
# Example:
# '''
# You can comment multi- line text by using 3-single quotations at start and end of text that wants to be commented
# '''

''' 
why we need comments in code?
_________________________________________________________
'''

# 1. If you are working in a team and want to leave a coding suggestion for your colleague to continue the work, you can do so using comments.
# 2. If you have any code improvement ideas that you would like to see implemented in the future, leave them in the comments for your future self.
# 3. To improve code readability (by adding comments that explain what the code is doing in each area).



