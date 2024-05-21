#NumPy - Data Types

import numpy as np

#--------------------------------------------------------------------------------------------------
# using array-scalar type 
dt = np.dtype(np.int32)
print(dt)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# create structured data-types
dt2 = np.dtype([('age',np.int8)])
print(dt2)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
"""
    The following examples show the use of structured data type. Here, 
    the field name and the corresponding scalar data type is to be declared.
"""
# first create structured data type 
dt3 = np.dtype([('age',np.int8)])

# now apply it to ndarray object 
a = np.array([(10,),(20),(30)],dtype=dt3)
print(a)
print(a['age'])
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
"""
    The following examples define a structured data type called student with a string field 'name', 
    an integer field 'age' and a float field 'marks'. This dtype is applied to ndarray object.
"""
# first create structured data type
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])

# now apply it to ndarray object
studnet_list = np.array([('Thillai',25,99.5),('Shanmugam',21,99.8)],dtype=student)
print(studnet_list)
print(studnet_list[0]['name'])
print(studnet_list[0]['age'])
print(studnet_list[0]['marks'])
print(studnet_list[1]['name'])
print(studnet_list[1]['age'])
print(studnet_list[1]['marks'])
#--------------------------------------------------------------------------------------------------