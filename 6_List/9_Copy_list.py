# Copy List:

"""
    In Python, a variable is just a label or reference to the object in the memory. Hence, the assignment "lst1 = lst" refers to the same list object in the memory. 
    Take a look at the following example −
"""
# Using Assignment operator:
lst = [10, 20]
print ("lst:", lst, "id(lst):",id(lst))
lst1 = lst
print ("lst1:", lst1, "id(lst1):",id(lst1))

lst[0]=100
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))

# Using Copy method():
lst = [10, 20]
lst1 = lst.copy()
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))

lst[0]=100
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))