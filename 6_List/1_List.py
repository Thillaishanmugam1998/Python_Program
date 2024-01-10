# List:
"""
    List is one of the built-in data types in Python. 
    A Python list is a sequence of comma separated items, enclosed in square brackets [ ]. 
    The items in a Python list need not be of the same data type.

    In Python, a list is a sequence data type. It is an ordered collection of items. Each item in a list has a unique position index, 
    starting from 0.

    A list in Python is similar to an array in C, C++ or Java. However, the major difference is that in C/C++/Java, 
    the array elements must be of same type. 
    On the other hand, Python lists may have objects of different data types.

    A Python list is mutable. Any item from the list can be accessed using its index, and can be modified. 
    One or more objects from the list can be removed or added. A list may have same item at more than one index positions.
"""

#Example:
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]


# Python list operation:
print(list1+list2) # concadination of two list
print("Rohan" in list1) # member ship
print([5]*5) # Repedation
