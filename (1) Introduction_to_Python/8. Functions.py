'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Functions and Procedures 
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

# Functions and procedures are code blocks that can be accessed from various places of your code. Python includes numerous built-in functions but you can also write your own functions. Yours are referred to as user-defined functions. Functions and procedures improve the modularity of the program and allow for greater code reuse.
# Procedures are functions that don't return a value. The only distinction between a function and a procedure is that a procedure contains either a return command without parameters (which returns None) or no return statement at all. 
# While functions are running, they generate their own namespace. 
# When you call a function such as function (a,b,c):
# 1. Python searches its namespaces for function to determine whether this is a Python object.
# 2. Python generates a tuple of the arguments supplied. As an example, we have arguments=(a,b,c).
# 3. Python calls the function internally as follows: apply(function,arguments). 


'''
_________________________________________________________________________________________________
Functions
_________________________________________________________________________________________________
'''

# Functions are usually preceded by the abbreviation def. Their end point is determined by the last line of the indented block of code that follows.
# A function's general format is as follows:
# def functionname(arg1, arg2, …): # tuple of arguments
#    "documentation string" # optional
#    <statements>

# Example 01
def addnumbers(x,y):
 print ("This function returns sum!")
 return x + y 

x = addnumbers(3,4)   
print (x)# Output: 7

# Example 01
def name():
 print ("function with no parameters")
 
name()


# Remember that to call a function without arguments, it's necessary to use empty parentheses.
variable = name() # instead of variable = name
print (variable)

# As a matter of fact, remember that you can assign functions to variables.
x = abs
print (x(-2)) # it's the same as saying print abs(-2)
# Output: 2
# x = abs returns the own function, and assigns its value to x.


# Variables that have values assigned to them inside a function always belong to the function namespace. The following example illustrates the concept of how to change a global variable inside a function by using the keyword global.
x = 10
def nudge():
   global x
   x = 20
   return x


'''
_________________________________________________________________________________________________
Python implements procedural abstraction
_________________________________________________________________________________________________
'''

# Python provides this feature by implementing anonymous functions with the keyword lambda. When the function is only an expression, this form of abstraction can be employed. In other words, lambda is just another way to write def with the exception that it doesn't have to be named and that you can just use expressions in it. It is only intended to be a shortcut for writing simple functions.

# Examples
f = lambda x: x * 4 
print (f(20))
# Output: 80

# The previous case can also be written as follows:
def f(x): 
    return x * 4 
print (f(30))
# Output: 120

# Here's another example:
def compose(func1,func2,val): 
  f = lambda x, f1=func1, f2=func2: f1(f2(x)) 
  return f(val)
  
print (compose(chr,abs,-75))
# Output: 'K'

# lambda is very useful for functions—such as map, filter, and reduce—that need a function as an argument.
def listtostring(list): 
  return reduce(lambda string, item: string + chr(item), list, "") 
  
print (listtostring([1,2,3,4,5]))
# Output: "\001\002\003\004\005"


'''
_________________________________________________________________________________________________
Parameters
_________________________________________________________________________________________________
'''

# In Python, all parameters are provided by reference. Modules, classes, instances and other functions can be passed to functions as arguments and dynamically examined. 
def powerdivision(x,y):  #function parameters: "x" and "y"
      return (x/y) 

print (powerdivision(4,2))   # function arguments: "4" and "2"
# Output: 2.0

# Whenever mutable objects (dictionaries and lists) that are transported to a function as arguments change within the function.
a = [10] 
def changelst(argument): 
       argument.append(4.0) 

changelst(a)
print (a)
# Output: a [10, 4.0]


# Default arguments are also allowed by the syntax. If the argument isn't provided, the default value takes place. The default value is optional. Even though its absence doesn't break your program, its presence cuts many lines from your code.
# Examples
a = 5 
def test(b = a):
    print (b)

test() 
# Output: 5 

test(2) 
# Output: 2 

a = 10
test() # Note that the b wasn't reassigned
# Output: 5
# This effect is because the value of a was collected when the function was created.

# In some cases, you cannot pre-identify the number of arguments that you might need. For this kind of situation, you can use the special symbols * and ** next to a generic argument name.
' *args gets a tuple of values in the received order; **args gets a dictionary mapping argumentname:value.'

def displayargs(*args):
    # defines a list of an undefined number of arguments.
    print (args)

displayargs(10,20,30)
# Output: (10, 20, 30)

def add(*args): 
       sum=0
       for arg in args:
           sum=sum+arg
       return sum

add(1,2,3,4) 
# Output: 10 
          
add(1,2,3,4,5,6,7) 
# Output: 28

'''
Returning Values
___________________
'''

# The return expression terminates the execution of a function but when it is followed by an expression, it returns the expression.

def returnargument(x): 
    return x 
# Output: 5 5

# A function can return multiple values by using tuples.
def returntuple(a,b): 
    return (a,b) 

x = 4 
y = 19 
a, b = returntuple(x,y) 
print (a, b)
# Output: 4, 19

# It is also possible for a function to have no return at all. When that happens, the value None is returned.

'''
Built-In Methods
___________________
'''

# When you have a function f, the following built-in methods can be accessed:
f.__doc__ or f.func_doc # "documentation string"
f.__name__ or f.func_name # "function name"
f.func_code # byte-compile code
f.func_defaults # tuple containing the default arguments
f.func_globals # dictionary defining the global namespace


'''
Dynamic Namespace
___________________
'''

# Python allows use of dynamic namespace concepts. When a function, module or class is formed, it specifies its own namespace.
# Python's namespaces are as follows:
# # Built-in names include int, string, def, print and so on. 
# # Global names are declared global and assigned at the module's top level. 
# # Local names—Names assigned within a function
# # When creating code, there are two ways to write an object name. You can use both qualified and unqualified names. Qualified names make use of object namespaces as references such as:
# print (objectnamespace.objectname) 
# # If the object is in your namespace, unqualified names handle scopes.
# For example, print (objectname).

