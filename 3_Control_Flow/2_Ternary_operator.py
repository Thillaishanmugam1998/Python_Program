"""
    Syntax: Ternary Operator
    ------------------------------------------------------
    * value_if_true if condition else value_if_false
"""
# 1. Without Ternary Operator:

age = int(input('Enter Your age: '))

if age >=18:
    print("Ticket price is 20")
else:
    print("Ticket price is 5")


# 2. With Ternary Operator:

age = int(input("Enter the age: "))

print("Ticket price is 20") if age>=18 else print("Ticket price is 5")
