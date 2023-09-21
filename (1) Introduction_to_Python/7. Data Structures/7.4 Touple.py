'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Touple 
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

# A tuple is a collection of Python objects that cannot be changed. The general syntax of a tuple is as follows:
# variable = (element1, element2, …)
# Without the brackets, it seems to be a list. The parentheses in the examples that follow are optional.

tpl = (1,) 
print (tpl) 
# Output: (1,) 

tpl = 1, 
print (tpl) 
# Output: (1,)

tpl = () # this is an empty tuple.
print (tpl) 
# Output: ()

tpl = (1,2,3) 
print (tpl) 
# Output: (1,2,3)

tpl = 1,2,3 
print (tpl) 
# Output: (1,2,3)

# It should be noted that the comma is required when defining a length-1 tuple in the above example. Otherwise, the variable being created would not be of the tuple type. Instead, the interpreter will believe you are attempting to assign a numerical value to the variable.
# A tuple looks just like a list. Tuples are distinct from lists in that they are immutable. You can get around this rule by binding a new structure to the old tuple variable.

tpl = 10,15,20 
tpl = tpl[0],tpl[2] 
print (tpl) 
# Output: (10,20)

# Other Interesting Facts About Tuples
# 1. They allow indexing.
tpl = 10,20,30,40 
print (tpl[1])
# Output: 20

# When you need to return more than one value from a function, you must utilize tuples.
def tuplefunction():
    return (10, 20, 30)

x, y, z = tuplefunction()
print (x, y, z) 
  # Output: 10 20 30
