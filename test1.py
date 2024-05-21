#NumPy - Ndarray Object:

import numpy as np

"""
    NumPy, which stands for Numerical Python, is an open-source Python library consisting of multidimensional and single-dimensional array elements.
    It's a standard that computes numerical data in Python. NumPy is most widely used in almost every domain where numerical computation is 
    required, like science and engineering; hence, the NumPy API functionalities are highly utilized in data science and scientific 
    Python packages, 
    including Pandas, SciPy, Matplotlib, scikit-learn, scikit-image, and many more.
"""
#----------------------------------------------------
# ndarray is created using an array function in NumPy 
arr_1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_1)    #OP:[1 2 3 4 5 6 7 8 9]
#----------------------------------------------------

#----------------------------------------------------
# create one-dimensonal array
arr_1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr_1)    #OP:[[1 2][3 4]]
#----------------------------------------------------

#----------------------------------------------------
# create Two-dimensonal array
arr_2 = np.array([[1,2],[3,4]])
print(arr_2)    #OP:[[1 2 3 4 5]]
#----------------------------------------------------

#-------------------------------------------------------------------------
# create  array using minimum dimensions 
arr_3 = np.array([1,2,3,4,5],ndmin=2)   #ndmin=2 means two dimension array
print(arr_3)
#-------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# create array using dtype parameter 
arr_4 = np.array([1,2,3],dtype=complex) #dtype = complex means that array contain complex value
arr_5 = np.array([1,2,3],dtype=float)
print(arr_4)    #OP:[1.+0.j 2.+0.j 3.+0.j]
print(arr_5)    #OP:[1. 2. 3.]
#----------------------------------------------------------------------------------------------