'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Ranges
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


# A range is a list of integers. This data structure is provided by the built-in function range().
#---------- 1st Method
r = range(10,15) 
print (list(r))   #Output: [11, 12, 13, 14, 15]

#---------- 2nd Method
for i in range(10,15):
    print(i, end=" ")    

# Output: 10 11 12 13 14


# When the first parameter is omitted, it is presumed to be zero.
r = range(5) 
print (list(r))     # Output: [0,1,2, 3, 4]

# The interval between the list components is specified as a third input to the range() function.
r = range(2,20,2) 
print (list(r))  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Here's an example of going backward:
r = range(6, 2,-1) 
print (list(r))  # Output: [6, 5, 4, 3,]

# The xrange() function only computes the values when they are accessed. Instead of storing a lengthy list of numbers in a variable, this function returns an XrangeType object.
for n in xrange(12):
     print (n)                # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# The preceding illustration still applies when using the range() function, but it stores the entire list in memory.
# As you will see in the following section, it is possible to assign a reference to the xrange() function's return value to a variable. Note that we are only storing a reference to the function; we are not storing any values.
List1 = xrange(12)
print (List1)  # Output:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

# However, you can use the tolist() method to later transform this reference into a genuine list.
List1.tolist() 
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
