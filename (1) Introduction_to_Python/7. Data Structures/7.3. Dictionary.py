'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Dictionary (hash tables)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

'''

# Dictionaries demonstrate Python's single mapping type. They represent finite sets of items with almost arbitrary indexes. 
# Dictionaries in Python are sometimes known as associative arrays or hash tables. A dictionary's general syntax is as follows:
# variable = {"key1":"value1", "key2":"value2", …}
# Dictionaries are always surrounded by braces. They link key items to value elements—keys and values are separated by a colon.
# A dictionary's values can be any type but its keys must be of an immutable data type (such as strings, numbers or tuples). Because it uses a hash algorithm to accomplish a fast lookup, dictionary keys have no natural order and are always listed in arbitrary order.

# Let us now concentrate on the operations that dictionaries can do. Let's start with a small dictionary.
py_dictionary = {"var1":"integer", "var2":"string", "var3":"float"}
# Now, let's apply some operations to it:
print (py_dictionary["var2"]) # (value lookup) Output: "string"

# py_dictionary["var4"] # raises a KeyError exception

del py_dictionary["var1"] # deletes the key fish 
print (py_dictionary) # Output: {'var2': 'string', 'var3': 'float'}

py_dictionary["var2"] = "bool" # updates an entry
print (py_dictionary)  # Output: {'var2': 'bool', 'var3': 'float'}

py_dictionary["new_var_added"] = "array" # adds an entry
print (py_dictionary)  # Output: {'var2': 'bool', 'var3': 'float', 'new_var_added': 'array'}


print (len(py_dictionary)) # (provides the number of keys) Output: 3


'''
_________________________________________________________________________________________________
Built-In Methods
_________________________________________________________________________________________________
'''

# The following sequence of commands shows the built-in methods that are implemented for dictionaries.

py_dictionary = {"a":10, "b":20, "c":30}
print (py_dictionary.keys()) # creates a list of keys. Very used in for statements. ["a","b","c"]  # Output: dict_keys(['a', 'b', 'c'])

print (py_dictionary.values()) # (creates a list of values) Output: dict_values([10, 20, 30])

print (py_dictionary.items()) # (creates a tuple with the dictionary elements) Output: dict_items([('a', 10), ('b', 20), ('c', 30)])

print (py_dictionary.has_key("a")) # (returns 1 if key exists. Otherwise it returns 0) Output: 1

# dic.get(value, default)
# If key exists, returns its value. Otherwise it returns the second arg. 
print (py_dictionary.get("b", None)) # Output: 20

# dic.update(dictionary)
# adds the dictionary in the argument to the original dictionary. 
py_dictionary.update({"d":40})
print (py_dictionary) # Output: {'a': 10, 'b': 20, 'c': 30, 'd': 40}

newdictionary = py_dictionary.copy() # creates a copy of the dictionary
keys = py_dictionary.keys()
# keys.sort() # sorts the dictionary keys
py_dictionary.clear() # removes all the items from the dictionary.
