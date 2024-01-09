# 2) Remove Dicitionary:
#------------------------
"""
    1. Using del keyword-----> del dict['key']
    2. Using pop()-----------> dict.pop('key)
    3. Using popitem---------> val = dict.popitem()
    4. Using Clear()---------> dict.clear()
"""

# 1. Using del keyword:
#----------------------
"Python's del keyword deletes any object from the memory. Here we use it to delete a key-value pair in a dictionary."
dict    = {"one":1,"two":2,"Three":3,"Four":4}
dict_2  = {1:"One"}
print("Before delete:",dict) #Before delete: {'one': 1, 'two': 2, 'Three': 3, 'Four': 4}
del dict['one']
print("After delete:",dict) #After delete: {'two': 2, 'Three': 3, 'Four': 4}
# del dict_2
# print(dict_2)   # "The del keyword with the dict object itself removes it from memory."


# 2. Using Pop() method:
#----------------------
"The pop() method of dict class causes an element with the specified key to be removed from the dictionary."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)  #numbers dictionary before pop operation: {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
val = numbers.pop(20)
print ("numbers dictionary after pop operation: \n", numbers) #numbers dictionary after pop operation: {10: 'Ten', 30: 'Thirty', 40: 'Forty'}
print ("Value popped: ", val)

# 3. Using Popitem() method:
#---------------------------
"The popitem() method in dict() class doesn't take any argument. It pops out the last inserted key-value pair, and returns the same as a tuple"
numbers = {10:"Ten",20:"Twenty",30:"Thirty",40:"Fourty"}
print("numbers dictionary before popitem operation: \n", numbers) #numbers dictionary before pop operation: {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty'}
val = numbers.popitem()
print ("numbers dictionary after popitem operation: \n", numbers) #numbers dictionary after pop operation: {10: 'Ten', 20: 'Twenty', 30: 'Thirty'}
print ("Value popped: ", val)   #Value popped:  (40, 'Fourty')

# 4. Using Clear() method:
#------------------------
"The clear() method in dict class removes all the elements from the dictionary object and returns an empty object."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers) # numbers dictionary before clear method: {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers) # numbers dictionary after clear method: {}