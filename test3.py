#NumPy - Array Attributes

import numpy as np

#---------------------------------------------------------------------------
"""
    In this chapter, we will discuss the various array attributes of NumPy.
    "ndarray.shape"
"""
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[1,2],[3,4,5],[6,7,8,9]])

print(arr1.shape)   #OP:(4,)
print(arr2.shape)   #OP:(2, 3)
print(arr3.shape)   #OP:(3,)

arr2.shape = (3,2)
print(arr2) #[[1 2][3 4][5 6]]

arr1_cpy = arr1.reshape(2,2)
print(arr1_cpy) #[[1 2][3 4]]
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
"""
    This array attribute returns the number of array dimensions.
    " ndarray.ndim "
"""
arr1 = np.arange(24)
print(arr1.ndim)

#reshape it
arr2 = arr1.reshape(2,4,3)
print(arr2.ndim)
print(arr2)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
"""
    This array attribute returns the length of each element of array in bytes.
    "numpy.itemsize"
"""
# dtype of array of int64 [8 byte]
arr = np.array([1,2,3])
print(arr.itemsize)

# dtype of array of int8 [1 byte]
arr2 = np.array([1,2,3],dtype=np.int8)
print(arr2.itemsize)

# dtype of array of float32 [4 byte]
arr3 = np.array([1,2,3],dtype=np.float32)
print(arr3.itemsize)
#-----------------------------------------------------------------------------