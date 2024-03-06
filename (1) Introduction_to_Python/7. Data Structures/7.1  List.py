'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Data Structures
---------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# Python supports a wide number of data structures, including lists, tuples, ranges and dictionaries.

'''
________________________________________________________________________________________________
Lists 
_________________________________________________________________________________________________
'''

# Lists are mutable sequences of objects that can be altered after they are generated and are indexed by natural numbers.
# Lists are flexible and simple to create. They are enclosed by brackets:
Lst1 = [1,2,3,4,5]

# A list can contain items with multiple data types:
Lst1 = [1, "Numbers!", 2]

# Lists can also contain other lists.
Lst1 = [1, "Numbers!", [2, 4, 6,"Even!!"]]

# Strings and lists both use the same operators. Forexample, you need to use slice operator to extract a range of elements from a list.
Lst1 = [1, "Numbers!", [2, 4, 6,"Even!!"]]
print (Lst1[1])  # Output: "Numbers!"

# To retrieve elements from lists that are included within other lists, use a pair of brackets to denote each list. Consider the following two examples.
Lst1 = [1, "Numbers!", [2, 4, 6,"Even!!"]]
print (Lst1[2][3])   # Output: " Even!!" 
print (Lst1[2][3][2])    # Output: "e"


# Let's explore a few examples of operations that can be implemented on a list.

''' 
Identifying an Entry
_____________________________
'''

Lst1 = [1, "Numbers!", 2.5]
print ("The index of List's element is ", Lst1.index(2.5))  # Output: 2


''' 
Assigning Values to a List
_____________________________
'''

Lst1 = [1, "Numbers!", [2, 4, 6,"Even!!"]]
print ("Before Assigning Value to the List", Lst1)   # Output: Before Assigning Value to the List [1, 'Numbers!', [2, 4, 6, 'Even!!']]

Lst1[1] = "New Value Added" 
print ("After Assigning Value to the List", Lst1)   # Output: After Assigning Value to the List [1, 'New Value Added', [2, 4, 6, 'Even!!']]



''' 
Assigning Values to a Slice
_____________________________
'''

Lst1 = [1, "Numbers!", [2, 4, 6,"Even!!"], 2, 3]
print (Lst1)  # Output: [1, 'Numbers!', [2, 4, 6, 'Even!!'], 2, 3]

Lst1[1:4] = ["New value added!", ["new list", 100], "New value added!"] 
print (Lst1) # Output: [1, 'New value added!', ['new list', 100], 'New value added!', 3]


''' 
Inserting Values
_____________________________
'''

# The following example starts inserting items at index number 6.
Lst1 = [1,2,3,4,5] 
print (Lst1)  # Output: [1, 2, 3, 4, 5]

Lst1[5:] = ["a", "b", "c", "d", "e"] 
print (Lst1)  # Output: [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

# If the list contained more than six elements, the statement would overwrite a section of it. Keep in mind that you can also add a value to this list as demonstrated in the example below:
Lst1 = [1,2,3,4,5]
print (Lst1)  # Output: [1, 2, 3, 4, 5]

Val = ["a", "b", "c", "d", "e"] 
Lst1.insert(4, Val)
print (Lst1)   # Output: [1, 2, 3, 4, ['a', 'b', 'c', 'd', 'e'], 5]


''' 
Deleting a Value
_____________________________
'''

Lst1 = [1,2,3,4,5]
print (Lst1)  # Output: [1, 2, 3, 4, 5]

del Lst1[-1] 
print (Lst1)  # Output: [1, 2, 3, 4]

del Lst1[0:2] 
print (Lst1)  # Output: [3, 4]


'''
___________________________________________________
Built-In Methods
_____________________________________________________
'''

# To see all of a list's built-in methods, open the interpreter and type dir([]). Some of the methods examples are as follows:
Lst = [0, 1, 2]  
print (Lst)   # Output: [0, 1, 2]

Lst.append(150) # adds element 5 to the list
print (Lst)     # Output: [0, 1, 2, 150]

Lst.append((5, 6)) # appends the tuple (5, 6)
print (Lst)     # Output: [0, 1, 2, 150, (5, 6)]


Lst.pop() # removes the last element of the list
print (Lst)     # Output: [0, 1, 2, 150]


Lst.insert(2, 10) # inserts the element 10 at index number 2
print (Lst)       # Output: [0, 1, 10, 2, 150]


Lst.pop(2)    # removes the element at index 2
print (Lst)   # Output: [0, 1, 2, 150]


Lst.reverse() # reverse the list order
print (Lst)   # Output: [150, 2, 1, 0]


Lst.extend([3, 14, 5]) # adds this list to our original list
print (Lst)  #  Output: [150, 2, 1, 0, 3, 14, 5]

Lst.sort()   # sorts the list elements
print (Lst)  # Output: [0, 1, 2, 3, 5, 14, 150]


Lst = [1, 2, 3, 4, 5, 4]
print (Lst.count(4)) # Output:2


print (Lst.index(5)) # returns the element 5's corresponding index. 
print (Lst.remove(3)) # removes the third element (not the index!!!)

# It should be noted that prior to version 1.5.2, lst.append (1,2) always added a tuple (1,2) to the list lst. When you do that as of release 2.0, you will now encounter a TypeError exception and a notice that says "append requires exactly 1 argument; 2 given." Not to worry! Simply add an additional set of parenthesis, like in lst.append ((1,2)), to correct that.
