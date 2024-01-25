#2. Accessing Tuples:
"""
    In Python, Tuple is a sequence. Each object in the list is accessible with its index. 
    The index starts from "0". Index or the last item in the tuple is "length-1". 
    To access values in tuples, use the square brackets for slicing along with the index or indices to obtain value available at that index.

    Syntax:
    -------
    * obj = tuple(i)

"""
#--------------------------------------------------------------------------------------------------------------------------------
# Example-1:
"Put the index inside square brackets to retrieve the item at its position."
tuple_1 = ("Thillai","Tamil","Sudharsan","Venkat")
tuple_2 = (1,2,3,4,5,6)

print(tuple_1(0))  # Thillai
print(tuple_1(-1)) # 6

#----------------------------------------------------------------------------
#Extracting a Subtuple from a Tuple
"""
    The slice operator extracts a subtuple from the original tuple.
    Syntax:
    --------
        * Subtup = tup1[i:j]
    Parameters
    ----------
    i − index of the first item in the subtup

    j − index of the item next to the last in the subtup

    This will return a slice from ith to (j-1)th items from the tup1.
"""
#-----------------------------------------------------------------------------
# Example-2:
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)

print(tup1[0:4]) # (a,b,c,d)
print(tup1[:4])  # (a,b,c,d)
print(tup1[0:])  # (a,b,c,d)
print(tup1[-1:0]) #()
print(tup1[-1:]) #d
print(tup1[0:-2]) # a,b,