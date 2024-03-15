'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                Modules and Packages 
---------------------------------------------------------------------------------------------------------------------------------------------------------------


_________________________________________________________________________________________________
Modules
_________________________________________________________________________________________________
'''

# A module is a collection of classes, functions and variables stored in a text file. Modules can be written in Python or C. A module's global namespace is created and imported using the syntax shown below:
# import <module> 
# It is also possible to import many modules at the same time with just one import statement as shown below:
# import m1, m2, m3
# Some Python modules are always available. Others (including yours) are files that must be imported (in most situations, those files end in.py or.pyc). A file must be saved in one of the folders mentioned in the sys.path variable before it is imported.


# If you want your module to be both runnable and importable, add something like the following line of code at the end of the file:
# If __name__ == "__main__": your_function()

# You can find out what is in a module by typing:
# dir(<module>)
# For example:
import math
dir(math)


'''
_________________________________________________________________________________________________
Packages
_________________________________________________________________________________________________
'''

# A package is a collection of modules that are all located in the same directory. Package names must be subdirectories of a directory in the sys.path variable.
# A package directory must include at least one empty __init__.py file and may include subpackages (subdirectories). Each subdirectory must also have an empty __init__.py file.

# For example:
# import a.b
# The module a.b in the above line specifies a submodule named b within the package a.

# When you import a package, its subpackages are not all imported at the same time. That must be stated directly in the __init__.py file.
# It would be equivalent to including the following line in your package's __init__.py file:
# import subpackage1, subpackage2, subpackage3

# Keep in mind that Python uses the paths contained in sys.path to locate modules and packages. This variable is a basic list, just like any other and you can add whatever directory you want to it. To view the current contents of this variable, type sys.path at the prompt of your interpreter.
# The ability to rename modules when importing them is a new feature included in release 2.0. This can be done in two ways:
# import module as newname
# or
# from module import name as newname
# This functionality corresponds to the following code:
# import module newmodule = module del module

'''
Built-In Methods
_________________
'''
# All of these built-in functions are part of the __builtin__ module and can be used after you've created a module or package called m.
m.__dict__ # lists the module dictionary
m.x = m.__dict__["x"] # provides access to a specific attribute
m.__doc__ # returns the documentation string
m.__name__ # returns the name of the module
m.__file__ # returns the file name
m.__path__ # returns the fully qualified package name
from in Contrast to import


# The main reason that you don't want to do from <module> import * is to avoid namespace clashing.

import package1.string 
print (package1.string.join(list))
# The previously mentioned example retrieves the module string from the package package1.

from package1 import string 
print (string.join(list))
#To use the string module, you must reference its objects by typing string.object>. When importing a module from a package, use this notation.

'''
Releasing and Reloading Modules
________________________________
'''

# You can remove a module from system memory at any time after it has been imported.
# For example:
import string, sys 
lst = ["a","b","c","d"] 
print (string.join(lst,"-")) 
del string 
del sys.modules["string"]

# You can easily find out what modules have been imported by typing:
sys.modules.key() ['os.path', 'operator', 'os', 'exceptions', '__main__', 'ntpath', 'strop', 'nt', 'sys', '__builtin__', 'site', 'signal', 'UserDict', 'string', 'stat', 'cmath']
