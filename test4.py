#NumPy - Array Creation Routines
import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------
"""
    A new ndarray object can be constructed by any of the following array creation routines or using a low-level ndarray constructor.
    "numpy.empty(shape,dtype,order)"
"""

#create an empty one-dimensonal array
arr = np.empty(1,dtype=np.int32)
print(arr)
print(arr.ndim)

#create an two-dimensonal array
arr = np.empty((2,2),dtype=float)
print(arr)
print(arr.ndim)
#------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------
"""
    "numpy.zeros"
    Returns a new array of specified size, filled with zeros.
"""
#create an one-dimensonal array with default value zeros
arr = np.zeros(5)
print(arr)
print(arr.ndim)

#create an Two-dimensonal array with default value zeros
arr = np.zeros((2,2),dtype=float)
print(arr)
print(arr.ndim)
#------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------
"""
    "numpy.onces"
    Returns a new array of specified size, filled with onces.
"""
#create an one-dimensonal array with default value onces
arr = np.ones(5)
print(arr)
print(arr.ndim)

#create an Two-dimensonal array with default value onces
arr = np.ones((2,2),dtype=float)
print(arr)
print(arr.ndim)

#create an Two-dimensonal array with default value onces with custom dtype
arr = np.ones((2,2),dtype=[('x','i1'),('y','i1')])
print(arr)
print(arr.ndim)
#------------------------------------------------------------------------------------------------------------------------------------