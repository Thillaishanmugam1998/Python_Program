# Sort:
"""
    The sort() method of list class rearranges the items in ascending or descending order with the use of lexicographical ordering mechanism. 
    The sorting is in-place, in the sense the rearrangement takes place in the same list object, and that it doesn't return a new object.

    Syntax
    ------
    list1.sort(key, reverse)

    Parameters
    ---------
    Key − The function applied to each item in the list. The return value is used to perform sort. Optional

    reverse − Boolean value. If set to True, the sort takes place in descending order. Optional

    This method returns None.
"""

list_1 = [8,4,9,1,2,0]
list_1.sort()
print(list_1)
list_1.sort(reverse=True)
print(list_1)


# Example 2
# In this example, the str.lower() method is used as key parameter in sort() method.

list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)


# Example 3
# Let us use a user-defined function as the key parameter in sort() method. The myfunction() uses % operator to return the remainder, based on which the sort is done.

def myfunction(x):
   return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)

