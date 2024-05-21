#NumPy - Array From Existing Data
import numpy as np

"""
numpy.asarray
This function is similar to numpy.array except for the fact that it has fewer parameters. 
This routine is useful for converting Python sequence into ndarray.

numpy.asarray(a, dtype = None, order = None)

Input data in any form such as list, list of tuples, tuples, tuple of tuples or tuple of lists
"""

#convert list to ndarray
list = [1,2,4,5]
arr = np.asarray(list)
print(arr)

#set dtype
list = [1,2,3,4,5]
arr = np.asarray(list,dtype=float)
print(arr)

#convert tuple to ndarray
tuple = (17,14,19)
arr = np.asarray(tuple)
print(arr)

#convert list of tuple to ndarray
list = [(17,14,19),(19,14,17)]
arr = np.asarray(list)
print(arr)

#convert tuples of tuple to ndarray
tuple = ((17,14,19),(19,14,17))
arr = np.asarray(tuple)
print(arr)