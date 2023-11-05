'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Encapsulation in Python
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# In Python, all attributes (variables and methods) are essentially public, but certain conventions and techniques can be used to achieve a form of encapsulation.

'''
Single Underscore Convention
____________________________
'''
# Attributes preceded by a single underscore (e.g., _n) are meant to be treated as internal and not intended for external use, though they can still be accessed.


'''
Double Underscore Name Mangling
_______________________________
'''
# Attributes starting with double underscores (e.g., __n) are not explicitly exported and undergo name-mangling as _Class__Variablename when byte-compiled, making them less accessible but not entirely private.
# Example:
class Number:
    def __init__(self, value):
        self._n = value  # Follows the single underscore convention
        self.__n = value  # Utilizes double underscore name mangling

    def __repr__(self):
        return f'{self.__class__.__name__}({self._n})'

    def add(self, value):
        self._n = self._n + value

    def incr(self):
        self._n = self._n + 1

# Interactive Example:
a = Number(20)
a.add(4)
a.incr()

# Accessing _n directly (not recommended but possible)
print(a._n)  # Output: 25

# Changing _n directly
a._n = 30
print(a)

# Accessing __n through name mangling (not truly private)
print(a._Number__n)  # Output: 20


'''
Default Argument for Class Attribute
____________________________________
'''
# Default arguments can be used to store class attributes in the namespace.
# Example:
v = 10

class C:
    def storen(self, n=v):
        return n

objA = C()
print(objA.storen())  # Output: 10

# Modifying v does not affect objA's attribute
v = 20
objB = C()
print(objB.storen())  # Output: 10


'''
 Manipulating Class Attributes
_______________________________
'''
# You can directly access and manipulate internal attributes of an object.

class Fun:
    def __init__(self):
        self.total = None

a = Fun()
b = Fun()
a.total = 2
b.total = 3
print(a.total, b.total)  # Output: 2 3


'''
Hiding Method with Double Underscore
____________________________________
'''
# Methods can be "hidden" by prefixing them with double underscores. To access, create a reference to the method.
# Example:
class C:
    def __a(self):
        print("ni!")

    b = __a  # Reference to the hidden method

a = C()
a.b()  
