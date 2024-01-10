# Change List items:
"""
    List is a mutable data type in Python. It means, the contents of list can be modified in place, after the object is stored in the memory. You can assign a new value at a given index position in the list

    Syntax
    -------
    list1[i] = newvalue
"""

# Example:

list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)

list1 = ['Y', 'Z']
list3[1:3] = list1

print ("List after changing with sublist: ", list3)

list2 = ['Z']
list3[1:3] = list2
print ("List after changing with sublist: ", list3)