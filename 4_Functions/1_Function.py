"""
    * What is a function
       A function is a named code block that performs a job or returns a value.
    * Why do you need functions in Python
        Sometimes, you need to perform a task multiple times in a program. And you don’t want to copy the code for that same task all over places.

To do so, you wrap the code in a function and use this function to perform the task whenever you need it.

For example, whenever you want to display a value on the screen, you need to call the print() function. Behind the scene, Python runs the code inside the print() function to display a value on the screen.
"""

# 1. Define a function:
def great():
    """ Display the greetings to users"""
    print("Hi")

# Function Defination:
    """
    A function definition starts with the def keyword and the name of the function (greet).

    If the function needs some information to do its job, you need to specify it inside the parentheses (). The greet function in this example doesn’t need any information, so its parentheses are empty.

    The function definition always ends in a colon (:).
    """

# Function Body:
    """
    The text string surrounded by triple quotes is called a docstring. It describes what the function does. Python uses the docstring to generate documentation for the function automatically.

    The line print('Hi') is the only line of actual code in the function body. The greet() function does one task: print('Hi')
    """

# Calling Function:
    """
        When you want to use a function, you need to call it. A function call instructs Python to execute the code inside the function.

        To call a function, you write the function’s name, followed by the information that the function needs in parentheses.

        The following example calls the greet() function. Since the greet() function doesn’t need any information, you need to specify empty parentheses like this:
    """

great()  # Hi


# 2. Passing Information to Python Function:

def great_2(name):
    print(f"Hi {name}")

great_2("Thillai")  # Hi Thillai

firstname = "Shanmugam"
great_2(firstname)  # Hi Shanmugam

# Parameters vs. Arguments
"""
    Sometimes, parameters and arguments are used interchangeably. It’s important to distinguish between the parameters and arguments of a function.

    A parameter is a piece of information that a function needs. And you specify the parameter in the function definition. For example, the greet() function has a parameter called name.

    An argument is a piece of data that you pass into the function. For example, the text string 'Thillai' or the variable Shanmugam is the function argument.
"""

# 3. Returning a value:
"""
    A function can perform a task like the greet() function. Or it can return a value. The value that a function returns is called a return value.

    To return a value from a function, you use the return statement inside the function body.

    * return value
"""
def great_3(name):
    return f"Hi {name}"

result = great_3("Tam")
print(result)       # Hi Tam


# 4. Example Python Function (add):

def addition(num_1,num_2):
    return num_1+num_2

print(addition(5,5)) # 10