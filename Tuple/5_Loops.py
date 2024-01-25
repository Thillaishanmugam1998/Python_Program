# 5. Python - Loop Tuples
"""
    You can traverse the items in a tuple with Python's for loop construct. The traversal can be done, using tuple as an iterator or with the help of index.
    Syntax:
    ------
        * for values in tuples:
            ......
            ......
            ......
    """

#E-1:
tuple1 = (1,2,3,4,5,6,7)
for value in tuple1:
    print(value)

for value in range(len(tuple1)):
    print(tuple1(value))
#----------------------------------------------------------

# 6. Python - Join Tuples

# Example:
    t1 = (1,2,3,4)
    t2 = ("one","Twor","Three")
    t3 = t1+t2
    print(t3) # (1,2,3,"one","Two","Three")

    t1+=t2 # t1=t1+t2


    l1 = list(t1)
    l2 = list(t2)
    l1.extend(l2)
    t1 = tuple(l1)

    t3 = sum((t1,t2),())

#----------------------------------------------------------
    
# 7. Tuple Methods
    
"""
    Since a tuple in Python is immutable, the tuple class doesn't define methods for adding or removing items. 
    The tuple class defines only two methods.
"""
# Finding the Index of a Tuple Item

tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("First index of 10:", x)

# Counting Tuple Items

tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("count of 10:", c)