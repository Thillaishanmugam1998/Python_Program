"""
    Syntax: if condition:
    --------------------
    if condition:
        statement-1
    
    Syntax: if - else:
    ------------------
    if condition:
        True statement
    else:
        False statement
    
    Syntax: if - elif:
    ------------------
    if condition:
        statement-1
    elif condition:
        statement-2
    
    Syntax: if - elif - else:
    -------------------------
    if condition:
        True statement-1
    elif condition:
        True statement-2
    else:
        False statement
"""
# You use the if statement to execute a block of code based on a specified condition.

# 1. If condition:

amount = int(input("Enter the amount\n"))
if amount >=1000:
    print("10% discount") 


# 2. If-else condition:
    
amount = int(input("Enter the amount \t"))
if amount >=1000:
    print("10% discount")
else:
    print("No discount")


# 3. If-elif condition:

amount = int(input("Enter the amount: \t"))
if amount >=1000:
    print("10% discount")
elif amount>=500:
    print("5% discount")


# 4. If-elif-else condition:

amount = int(input("Enter the amount: \t"))
if amount >=1000:
    print("10% discount")
elif amount>=500:
    print("5% discount")
else:
    print("No discount")