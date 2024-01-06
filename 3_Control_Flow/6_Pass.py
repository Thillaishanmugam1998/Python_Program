"""
    Syntax: Pass:
    ------------
        * pass
    
    Syntax: If condition - pass:
    ---------------------------
    if condition:
        pass
    
    Syntax: While - pass:
    ---------------------------
    while condition:
        pass
        
    Syntax: For loop - pass:
    ---------------------------
    for index in range(n):
        pass
        
    Syntax: Function - pass:
    ---------------------------
    def function():
        pass
    
    Syntax: Class - pass:
    ---------------------------
    class Stream:
        pass
"""

# The pass statement is a statement that does nothing. It’s just a placeholder for the code that you’ll write in the future.

# When you run the code that contains a pass statement, the Python interpreter will treat the pass statement as a single statement. 
# As a result, it doesn’t issue a syntax error.

# With and Without pass statement:

counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    # implement later         # if i run this code i will got syntax error      (Without pass statement)
    pass                      # with pass statement

