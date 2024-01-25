# 3.Update:
"""
    In Python, tuple is an immutable data type. An immutable object cannot be modified once it is created in the memory.
"""
#---------------------------------------------------------------------------------------------------------------------
# E-1:
tuple_1 = ("Thillai","Tamil")
tuple_1[1] = "Shanmugam"
print(tuple_1) # TypeError: 'tuple' object does not support item assignment

#--------------------------------------------------------------------------
# How to Update a Python Tuple?

"""
You can use a work-around to update a tuple. Using the list() function, convert the tuple to a list, perform the desired append/insert/remove operations and then parse the list back to tuple object.
"""

# E-2:
tuple_1 = (1,2,4,6)
list_1 = list(tuple_1)
list_1[2]=3
list_1[3]=4

tuple_1=tuple(list_1) # (1,2,3,4)
