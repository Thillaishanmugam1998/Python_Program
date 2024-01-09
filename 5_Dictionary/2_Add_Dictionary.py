# 1) Add Dictionary Items:
#-------------------------
"""
    1. Using the Operator
    ---------------------
The "[]" operator (used to access value mapped to a dictionary key) is used to update an existing key-value pair as well as add a new pair.

    Syntax
    -------
    * dict["key"] = val

    If the key is already present in the dictionary object, 
    its value will be updated to val. If the key is not present in the dictionary, a new key-value pair will be added.
"""
score = {"IND":200}
print(score)
score["IND"] = 500
print(score)
score["AUS"] = 501
print(score)

"""
    2. Using the Update()
    ---------------------
    In this case, the update() method's argument is another dictionary. 
    Value of keys common in both dictionaries is updated. For new keys, key-value pair is added in the existing dictionary

    Syntax
    -------
    * d1.update(d2)
"""
score_1 = {"IND":200,"AUS":500}
score_2 = {"IND":300,"AUS":800,"NZ":0}
print(score_1)
score_1.update(score_2)     #1
print(score_1)
score_3 = [("NZ",400),("SA",0)]
score_1.update(score_3)     #2
print(score_1)
score_1.update(IND=900,AUS=1000)    #3 
print(score_1)

"""
    3. Using the Unpack Operator
    ----------------------------
    The "**" symbol prefixed to a dictionary object unpacks it to a list of tuples, 
    each tuple with key and value. Two dict objects are unpacked and merged together and obtain a new dictionary.
"""

new_dict = {**score_1,**score_2}
print(new_dict)