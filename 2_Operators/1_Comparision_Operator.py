"""
    Introduction to Python comparison operators:
    -------------------------------------------
    In programming, you often want to compare a value with another value. To do that, you use comparison operators.

    Python has six comparison operators, which are as follows:

    * Less than ( < )
    * Less than or equal to (<=)
    * Greater than (>)
    * Greater than or equal to (>=)
    * Equal to ( == )
    * Not equal to ( != )
    These comparison operators compare two values and return a boolean value, either True or False.

    You can use these comparison operators to compare both numbers and strings.
"""
# 1. Less than(<):
"Syntax: Lefside value < Right side value"
"he Less Than operator (<) compares two values and returns True if the value on the left is less than the value on the right. Otherwise, it returns False:"

print(10<20)        # True
print("ax"<"az")    # True
print("a"<"z")      # True

# 2. Less than or equal to (<=):
"Syntax: Lefside value <= Right side value"
"The less than or equal to operator compares two values and returns True if the left value is less than or equal to the right value. Otherwise, it returns False:"

print(10<=20)       # True
print("ax"<="az")   # True
print("a"<="a")     # True

# 3. Greater than operator (>):
"Syntax: left_value > right_value"
"The greater than the operator (>) compares two values and returns True if the left value is greater than the right value. Otherwise, it returns False:"

print(50>20)     # True
print("a">"z")   # False
print("za">"az") # True

# 4. Greater than or equal to (>=):
"Syntax: left_value >= right_value"
"The greater than or equal to operator (>=) compares two values and returns True if the left value is greater than or equal to the right value. Otherwise, it returns False:"

print(50>=50)    # True
print("z">="z")  # True

# 5. Equal to ( == ):
"Syntax: left_value == right_value"
"The equal to operator (==) compares two values and returns True if the left value is equal to the right value. Otherwise, it returns False :"

print(5==5)          # True
print("App"=="app")  # False
print("app"=="app")  # True

# 6. Not equal to ( != ):
"Syntax: left_value != right_value"
"The not equal to operator (!=) compares two values and returns True if the left value isn’t equal to the right value. Otherwise, it returns False."

print(5!=5)         # False
print("app"!="App") # True