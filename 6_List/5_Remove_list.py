# Remove list items:
"""
    The list class methods remove() and pop() both can remove an item from a list. The difference between them is that remove() removes the object given as argument, 
    while pop() removes an item at the given index.
"""

# Using Remove():
"The following example shows how you can use the remove() method to remove list items −"
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

# Using Pop():
"The following example shows how you can use the pop() method to remove list items −"
list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

# Using del:
"Python has the *del* keyword that deletes any Python object from the memory."
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)

# Using slice:
list2 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list2)
del list2[0:2]
print ("List after deleting: ", list2)