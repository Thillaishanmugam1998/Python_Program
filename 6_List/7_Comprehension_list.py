# Comprehension:
"""
    List comprehension is a very powerful programming tool. It is similar to set builder notation in mathematics. 
    It is a concise way to create new list by performing some kind of process on each item on existing list. 
    List comprehension is considerably faster than processing a list by for loop.
"""

# without list comprehension:
ch = ["g","o","o","l","e"]
ch_2 = []
for char in ch:
    if char not in ("aeiou"):
        ch_2.append(char)
print(ch,ch_2)


# With list comprehension:
ch = ["g","o","o","l","e"]
print([char for char in ch if char not in ("aeiou")])


# List Comprehension Technique
"""We can easily get the same result by a list comprehension technique. A general usage of list comprehension is as follows −
 
Syntax:
-------
listObj = [x for x in iterable]
"""

squares = [x*x for x in range(1,11)]
print (squares)

list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)