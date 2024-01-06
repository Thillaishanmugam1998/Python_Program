"""
    Introduction to Python logical operators
    Sometimes, you may want to check multiple conditions at the same time. To do so, you use logical operators.

    Python has three logical operators:

    * and
    * or
    * not

    The precedence of the logical operator from the highest to lowest: not, and, and or
"""

# 1. and Operator:
"Syntax: a and b"
"The and operator checks whether two conditions are both True simultaneously:"

price = 9.99
print(price>9 and price<10) # True

# 2. or Operator:
"Syntax: a or b"
"Similar to the and operator, the or operator checks multiple conditions. But it returns True when either or both individual conditions are True:"

price =10
print(price<9 or price<=10) # True

# 3. not Operator:
"Syntax: a not b"
"The not operator applies to one condition. And it reverses the result of that condition, True becomes False and False becomes True."
price = 10
print(price<=10)        # True
print(not price<=10)    # False