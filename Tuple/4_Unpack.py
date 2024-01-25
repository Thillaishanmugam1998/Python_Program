# 4. Unpack:
"""
The term "unpacking" refers to the process of parsing tuple items in individual variables. In Python, the parentheses are the default delimiters for a literal representation of sequence object.
>>> t1 = (x,y)
>>> t1 = x,y
>>> type (t1)
<class 'tuple'>
"""

#-------------------------------------------------------------------------------------------------------------------
# E-1:
tup1 = (1,2,3,4)
n1,n2,n3,n4 = tup1
n1,n2 = tup1 # ValueError: not enough values to unpack (expected 4, got 2)
print(n1,n2,n3,n4)

#---------------------

# E-2:
tup2 = (1,2,3,4)
x,*y = tup2
a,*b,c = tup2
*n,z,l = tup2
print(x) # 1
print(y) # [2,3,4]
print(a) # 1
print(b) # [2,3]
print(c) # 4
print(n) # [1,2]
print(z) # 3
print(l) # 4

#----------------------

