'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Operators
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# Following few points shows the operators and their precedence in Python:
# 1.	 (), [], {}
#  
# 2.	'Object' 

# 3.	object.attribute, object[i],  function() 
# To access a variable's (object's) properties and methods, use the. (dot) operator. For example:
var1 = ["L", "a", "n", "g,", "u", "a,", "g", "e"]
print ('Value of the variable "var1" before append', var1)
var1.append("s") 
print ('Value of the variable "var1" after append', var1)

# 4.	 +x, -x

# 5.	x**y 

# 6.	x*y, x/y, x%y 

# 7.	x+y, x-y 

# 8.	x<>y 
# These operators provide shifting operations. The << operator ensures left shifting (at bit level) and the >> operator ensures right shifting. 
# For example:
x = 4 # binary representation is 0100
print ("Value of variabe 'x' before shift operator", x)
x = x << 1 # The binary representation will be 1000 8 
print ("Value of variabe 'x' after shift operator", x)

# 9.	x & y 

# 10.	x ^ y The bitwise XOR  

# 11.	x | y The bitwise OR operator 

# 12.	<=, >, >=, ==, !=, <>, is, is not, in, not in 

# 13.	The operators "in and not in" are only used with lists. 

# 14.	The == operator checks for equality whereas the = operator assigns a value to a variable. 

# 15.	 not 

# 16.	and 

# 17.	or


''' 
Augmented Assignment  
_______________________
'''

# With Python 2.0, a complete set of augmented assignment operators are also implemented. This comprises the following symbols: +=, -=, *=, /=, %=, **=, &=, |=, =, »= and «= 
# For example:
x = 5
print ('Before applying augmented assignment', x)

x += 1
print ('After applying augmented assignment',x)

# you can say x += 1 rather than x = x+1.


''' 
Expressions 
______________
'''

# Numerous expressions are supported by Python operators; among which few are as follows: 
# x,y,z = z-x, y*z, x+y   # Parallel assignment: example 1 
# x,y,z = 15,10,5 # Parallel assignment: example 2 
# x,y = y,x # Switching assignments 
# a = b = c = 100  # Multiple assignments 
# string.atof(var2) # Functions support 
# 2 < x < 10 # Multiple range testing 

