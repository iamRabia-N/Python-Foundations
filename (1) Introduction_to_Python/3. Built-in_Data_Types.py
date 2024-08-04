'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Built-in Data Types
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# Built-in data types are those that are pre-installed in the interpreter. 
# They are split into two categories:
# Immutable Data Types: These objects values cannot be changed. Examples of immutable data types are strings, numbers and tuples.
# Mutable Data Types: These objects can be changed. Examples of mutable data types are lists and dictionaries.

# It is sometimes required to use the special data type "None" to assign a null value to a variable. 


''' 
Numbers 
___________
'''

# Python's numeric data types include integer, floating-point, hexadecimal (base 16) and octal (base 8). 
# Examples of these data types are 25, 10.5, 0xB3 and 045 respectively.

# Numerous operations with numbers are possible in Python among which few are mentioned below:
# 1. It can write equations:
print (3*(3.0/45)) # Output: 0.2

# 2. It can execute functions:
print (round(12.35, 1)) #Output: 12.3

# 3. It can perform comparisons: 
x = 4
print (0, x, 10) # Output: True

# 4. It can perform binary operations like masking and shifting. For example:
print (15<<2) # Output: 60
print (2|1) # Output: 3

# 5.  Python allows for long integers of any size. Put a "L" at the end of the integer to tell Python that it should treat it as a long integer


''' 
Strings
___________
'''

# Python defines a string as a sequence of characters. As a result, whenever you use the string for example "Apple", Python internally treats it as the sequence ["A", "P", "P", "L", "E"]. The initial indexer value is always zero. As a result, in order to access the letter "A," you have to type "print (Apple[0])" and so on. We can access all of the other elements using the same concept.
# The following are examples of few string operators: 
print (len("computer"))    # Get its length (Output: 8)
print ("Hello" + "World")  # concatenation (Output: HelloWorld)
print ("Name " * 2) # repetition (Output: Name Name)

OS = "MacBook"
print (OS[1])   # indexing (Output: a)
print (OS[-1])  # indexing backward (Output: k) 
print (OS[1:3]) # slicing (Output: ac)
# When slicing, it isn't necessary to include both first and last elements. Whenever you omit one of the elements, it is presumed that you want everything in that direction. 
print (OS[1:])   # (Output: acBook)
print (OS[:3] ) # (Output: Mac)

# There are many other functions of string which you can explore. 
