# Python - Copy Dictionaries:
#---------------------------

# Example-1:
d1={1:"one",2:"Two"}
d2={}
d3={}
print("Before copy dict to dict :",d2)
d2=d1
print("After copy dict to dict :",d2)
d3 = d1.copy()
print(d3)

#------------------------------------------

# Python Nested Dictionaries:
#----------------------------
"""
A Python dictionary is said to have a nested structure if value of one or more keys is another dictionary. 
A nested dictionary is usually employed to store a complex data structure.
"""

marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}

for student, subjects in marklist.items():
    print(f"Student: {student}")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    print("------------")


for k,v in marklist.items():
   print (k, ":", v)

print(marklist.get("Mahesh"))
print(marklist.get("Mahesh")["Phy"])
print(marklist["Mitchell"])
print(marklist["Mitchell"]["maths"])

#------------------------------------------------------------------------------------------------------------
# Dictionary Methods():
#----------------------
"""
1	dict.clear()

Removes all elements of dictionary dict.

2	dict.copy()

Returns a shallow copy of dictionary dict.

3	dict.fromkeys()

Create a new dictionary with keys from seq and values set to value.

4	dict.get(key, default=None)

For key key, returns value or default if key not in dictionary.

5	dict.has_key(key)

Returns true if a given key is available in the dictionary, otherwise it returns a false.

6	dict.items()

Returns a list of dict's (key, value) tuple pairs.

7	dict.keys()

Returns list of dictionary dict's keys.

8	dict.pop()

Removes the element with specified key from the collection

9	dict.popitem()

Removes the last inserted key-value pair

10	dict.setdefault(key, default=None)

Similar to get(), but will set dict[key]=default if key is not already in dict.

11	dict.update(dict2)

Adds dictionary dict2's key-values pairs to dict.

12	dict.values()

Returns list of dictionary dict's values.
"""