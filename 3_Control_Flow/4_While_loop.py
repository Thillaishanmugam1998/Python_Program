"""
    Syntax: While loop:
    -------------------
    while condition:
        Body

"""
# Python while statement allows you to execute a code block repeatedly as long as a condition is True.

# While - loop:
max=5
counter =0
while counter < max:
    print(counter)
    counter+=1    # counter = counter + 1
print("Outer loop")


# while - loop:
command = ''
while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")
