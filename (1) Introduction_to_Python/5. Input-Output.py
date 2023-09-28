'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Input and Output
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
# Python, like any other language, allows you to collect user input and show information to user.
# Let's understand this concept with the following example: 
x = input ("Enter your first name: \n") 
print ("Your Name is ", x)

# It should be noted that the input prompt can be anything, including empty.

# When a user enters 5, x is correctly handled as a number. The user must explicitly input the quotations to make x into a string.
# You can use the raw_input function to solve this issue.

# It should be noted that the print command requires commas to separate objects:
print ("Name", "sketch")
# Output: Name sketch


''' 
Displaying Information 
_________________________

'''
# The sys module in Python provides access to the three built-in file objects. They are used by the interpreter to provide input and output functionality. They are referred to as sys.stdin, sys.stdout, and sys.stderr.
# Print statements are mapped to sys.stdout. As a result, they send the textual representation of objects to the standard output stream:
# import sys 
sys.stdout.write("Writing data with built-in file object. \n") 
# Output: Writing data with built-in file object


''' 
Formatting Operations
_________________________

'''
# Python's formatting operations are identical to the C language's printf() function. Consider the following example:
print ("Eng. Zoi is here!")
# What if you don't want the name to be hard-coded inside the string? Compare the preceding line of code to the following:
# print (" Eng. %s, is here!" % someone)
print (" Eng. %s, is here!" % "Zoi")
# The sequence of the elements has no impact on the final output. Consequently, stating:
# print (" Eng. %s" % someone)
print (" Eng. %s" % "Zoi")
# is the same as:
# print (someone % "Eng. %s")

# The sample below demonstrates how Python handles multiple format arguments. 
print ("The %s with %i multiple format arguments" % ("Example", 2))


# Table 2.2. Formatting Operators Table
# ____________________________________________________________________________________________________________________________
# Formatting Operator 	   Description
# ____________________________________________________________________________________________________________________________

#       %d 	                decimal integer
#       %i 	                decimal integer
#       %u 	                unsigned integer
#       %o 	                octal integer
#       %x 	                hexadecimal integer
#       %X 	                hexadecimal integer (uppercase letters)
#       %f 	                floating point as [-]m.dddddd
#       %e 	                floating point as [-]m.dddddde±xx
#       %E 	                floating point as [-]m.ddddddE±xx
#       %g, %G 	                floating point where the exponent is less than -4 or greater than the precision
#       %s 	                any printable object (such as strings)
#       %c 	                a single character
#       %% 	                the literal %

# Another basic example is as follows:
value = 150
print ("The value is %d" % value)
# Output: The value is 150

# Following that, there are various unique ways to format operations by inserting unique characters between the formatting operator and the % literal. We must first initialize several variables before proceeding with the examples.

int_var = 3
float_var = 13.5 
string_var = "Hello" 
dict = {"xx":13, "yy":1.5, "zz":"world"}
# 1. You can put dictionary key names in parenthesis.
print ("%(zz)s" % dict) # Output: world

# 2. You can left align the string block by using the - literal.
print ("%-8dend" % float_var)  # Output: 13 

# 3. You can show both positive and negative number signs by using the + literal.
print ("%+d" % int_var)   # Output: +3 

# 4. If you enter a zero, you will get a zero-filling.
print ("%08d " % int_var)   # Output: 00000003 

# 5. Strings with the widest possible field
print ("%0.2s" % string_var)  # Output: He

# 	precision (floating-point values) + period (.)
print ("%0.2f" % float_var)  # Output: 13.50

# 	Minimum digit count (integer)
print ("%0.10f" % int_var)  # Output: 3.0000000000
