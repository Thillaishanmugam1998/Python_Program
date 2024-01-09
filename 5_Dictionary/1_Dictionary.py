"""
    Dictionary is one of the built-in data types in Python. Python's dictionary is example of mapping type. 
    A mapping object 'maps' value of one object with another.

    In a language dictionary we have pairs of word and corresponding meaning. 
    Two parts of pair are key (word) and value (meaning). Similarly, Python dictionary is also a collection of key:value pairs. 
    The pairs are separated by comma and put inside curly brackets {}.

    To establish mapping between key and value, the colon ':' symbol is put between the two.
"""

# Example-1:
capitals = {"Tamilnadu":"chennai","Karnataka":"Bangalore","kerala":"Thiruvananthapuram"}
numbers  = {10:"Sachin",45:"Rohit",7:"Dhoni",18:"Kolhi"}
marks    = {"Thillai":100,"Tamil":200}

print(capitals)
print(numbers)
print(marks)

# Example-2:
"* Only a number, string or tuple can be used as key. All of them are immutable *"
d_1 = {"Name":"Thillai"}
d_2 = {10:"Sachin"}
d_3 = {(5,4,4):"Tuple"}
d_4 = {("Tuple","tupe-2"):20}
print(d_1,d_2,d_3,d_4)

# Example-3:
"* Python doesn't accept mutable objects such as list as key, and raises TypeError. *"
# d_5 = {[1,2,3,4]:"List"}
# print(d_5)   # Type Error 'List'

# Example-4:
"* You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary. *"
"Key-unic , value-dupilicate"
d_6 = {"Team":"MI","Ipl":"MI","Champions":"MI"}
d_7 = {"Team":"MI","Team":"CSK","Team":"RCB"}
print(d_6,d_7)

#---------------------------------------------------------------------------------------------------------------------------
# 1) Operation of dictionary:
#---------------------------
# 1. Extract/assign the value mapped with key
d_8 = {1:"one",2:"Two",3:"Three"}
d_9 = {4:"Four",5:"Five"}
d_8[3]="THREE"
print(d_8[1])
print(d_8[2])
print(d_8)

# 2. Union of two dictionary objects, retuning new object
#--------------------------------------------------------
# d_10 = d_8|d_9
# print(d_10)

# 3. Augmented dictionary union operator
#---------------------------------------
# d1 = {'a': 2, 'b': 4, 'c': 30}
# d2 = {'a1': 20, 'b1': 40, 'c1': 60}
# d1|=d2; print (d1)
#------------------------------------------------------------------------------------------------------------------------------

# 2) Access dictionary items:
#----------------------------
# 1. Using []
print(d_8[1])
print(d_9[5])    # If key not present give Error

# 2. Using get() method
print(d_8.get(2))
print(d_9.get(4))
#------------------------------------------------------------------------------------------------------------------------------

# 3) Change Dictionary Items:
#----------------------------
"Apart from the literal representation of dictionary, where we put comma-separated key:value pairs in curly brackets, we can create dictionary object with built-in dict() function."

d1 = dict()    # To create empty dictionary
print(d1) 

d2 = dict([(1,"one"),(2,"Two"),(3,"Three")])  # list of tupes to dict
print(d2)

d3 = dict(((1,2),(3,4),(5,6))) # Tupes of Tupes to dict
print(d3)

d4 = dict(a=5,b=10) # keyword argument to dict
print(d4)
#---------------------------------------------------------------------------------------------------------------------------------

