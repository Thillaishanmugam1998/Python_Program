# Add items in list:
"""
    There are two methods of the list class, append() and insert(), that are used to add items to an existing list.
"""

# Example-1:
#------------
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)

# Example-2:
#------------
"The insert() method inserts the item at a specified index in the list."
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)