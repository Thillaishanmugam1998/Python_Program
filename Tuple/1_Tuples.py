# Tuples:
"""
    Tuple is one of the built-in data types in Python. 
    A Python tuple is a sequence of comma separated items, enclosed in parentheses (). 
    The items in a Python tuple need not be of same data type.
"""
#------------------------------------------------------------------------------------
# Examples:
tuple_1 = ("Thillai","Tamil",17,14,17.14) # hetrogenious
tuple_2 = (1,2,3,4,5) # homogenious 
tuple_3 = ('a','b','c','d')

print(tuple_1)
print(tuple_2)
print(tuple_3)

#-------------------------------------------------------------------------------------
# Tuple Operation:
# concatinate
print((1,2,3)+(4,5,6)) # (1,2,3,4,5,6)
print(("hello")*2) # ("hello","hello")
print(3 in (1,2,3)) # True