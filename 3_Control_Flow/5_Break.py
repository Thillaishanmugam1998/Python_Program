"""
    Syntax: Break:
    --------------
        * break
    
    using for loop with break:
    --------------------------
    for index in range(n):
        if condition:
            break
    
    using while loop with break:
    ---------------------------
    while condition:
        if condition:
            break
"""
# Sometimes, you want to terminate a for loop or a while loop prematurely regardless of the results of the conditional tests.
# In these cases, you can use the break statement:

# Break for loop:
for index in range(11):
    print(index)
    if index!=0 and (index % 5)==0:   # break if (index!=0 and (index % 5)==0) else print(index) Error: break only inside the loop
        break
print("Outside for loop")

# Break Nested for loop:
for x in range(5):
    for y in range(5):
        if y>1:
            break
        print(f"(x:{x},Y:{y})")

# Break while loop:
print("Enter 0 to exit")
while True:
    number = int(input("Enter the number: "))
    if number == 0:
        break
    print(number)