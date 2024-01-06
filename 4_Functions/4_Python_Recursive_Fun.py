"""
    Introduction to recursive functions:
    -------------------------------------
    A recursive function is a function that calls itself until it doesn’t.

    The following fn() function is a recursive function because it has a call to itself:

    Syntax:
    ------
    def function():
        .......
        .......
        function()

    Also, a recursive function needs to have a condition to stop calling itself. So you need to add an if statement like this:

    Syntax:
    -------
    def function():
        ........
        ........
        if condition:
            ......
        else:
            function()

    * A recursive function is a function that calls itself until it doesn’t.
    * And a recursive function always has a condition that stops calling itself.
"""

# Without Recursive Function Example:
# Want to countdown to print 3 to 0:
def countdown(start):
    print(start)

countdown(3) #3
countdown(2) #2
countdown(1) #1
countdown(0) #0

# With Recursive Function Without Condition Example:
def countdown_r(start):
    print(start)
    countdown_r(start-1)

countdown_r(3)               # RecursionError: maximum recursion depth exceeded while calling a Python object


# With Recursive Function With Condition Example:
def countdown_r(start):
    if (start>=0):
        print(start)
        countdown_r(start-1)

countdown_r(3)  

# Sum of sequence without using recursion:
def sum(number):
    total = 0
    for index in range(number+1):
        total=total+index
    return total

print(sum(100))

# sum of sequence with using recursion:
def sum(number):

    if number>0:
        return number + sum(number-1)
    
    return 0

print(sum(100))

# sum of sequence with using recursion:
def sum(number):
    return number+sum(number-1) if number > 0 else  0

print(sum(100))