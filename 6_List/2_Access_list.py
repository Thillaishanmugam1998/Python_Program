# Access list items:
"""
    In Python, a list is a sequence. Each object in the list is accessible with its index. The index starts from 0. 
    Index or the last item in the list is "length-1". 
    To access the values in a list, use the square brackets for slicing along with the index or indices to obtain value available at that index.

    The slice operator fetches one or more items from the list. Put index on square brackets to retrieve item at its position.
    
    Syntax:
    ------
    obj = list1[i]
"""

# Access list using index[]:
#---------------------------
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[2])
print("Item at negative index:",list2[-1]) 


# Access list using slicing method():
#------------------------------------
print(list1[0:5])
print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list1[:2])
print ("Items from index 2 to last in list3", list1[2:-1])
print ("Items from index 0 to index last in list4", list1[:])