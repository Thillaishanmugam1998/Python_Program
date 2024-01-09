# Python - Loop Dictionaries
#---------------------------
"""
    Unlike a list, tuple or a string, dictionary data type in Python is not a sequence, as the items do not have a positional index. However, 
    traversing a dictionary is still possible with different techniques.
"""
# Example-1:
#------------
"Running a simple for loop over the dictionary object traverses the keys used in it."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)

# Example-2:
#-----------
"Once we are able to get the key, its associated value can be easily accessed either by using square brackets operator or with get() method."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print(numbers[x])
   print(numbers.get(x))

# Example-3:
#-----------
   "The dict_items object is a list of key-value tuples over which a for loop can be run as follows:"
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print(x)

# Example-4:
#-----------
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x,y in numbers.items():
   print(x,y)

# Example-5:
#-----------
   "Similarly, the collection of keys in dict_keys object can be iterated over."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.keys():
   print(x)

# Example-6:
#-----------
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.values():
   print(x)

# Example-7:
#-----------
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
len = len(numbers)
for index in range(len):
   key   = list(numbers.keys()) 
   value = list(numbers.values())
   print(key[index],value[index])