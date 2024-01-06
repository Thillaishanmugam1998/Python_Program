"""
    Syntax: Continue
    ----------------
        * continue
    
    using for loop with continue:
    --------------------------
    for index in range(n):
        if condition:
            continue
    
    using while loop with continue:
    ---------------------------
    while condition:
        if condition:
            continue

"""

# The continue statement is used inside a for loop or a while loop. The continue statement skips the current iteration and starts the next one.

# continue for loop:
for index in range(11):
    if index % 2 :             # "0" means "false" and "1" or "any postive number" means true
        continue
    print(index) # 0 2 4 6 8 10


# continue while loop:
max =10
counter =0
while counter < max:
    counter+=1
    if not counter % 2 :
        continue
    print(counter) # 1 3 5 7 9
    