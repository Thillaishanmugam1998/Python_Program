# Python - Dictionary View Objects:
"""
    The items(), keys() and values() methods of dict class return view objects. 
    These views are refreshed dynamically whenever any change occurs in the contents of their source dictionary object.
    1. items()-----> Obj = dict.items()
    2. keys()------> Obj = dict.keys()
    3. valuse()

"""

# 1. items():
#-----------
"The items() method returns a dict_items view object. It contains a list of tuples, each tuple made up of respective key, value pairs."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

# 2. Keys():
#-----------
"""The keys() method of dict class returns dict_keys object which is a list of all keys defined in the dictionary. 
It is a view object, as it gets automatically updated whenever any update action is done on the dictionary object"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.keys()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({60:"Sixty"})
print ("View automatically updated")
print (obj)

# 3. Values():
#-------------
"The values() method returns a view of all the values present in the dictionary. The object is of dict_value type, which gets automatically updated."
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.values()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({100:"Hundred"})
print ("View automatically updated")
print (obj)