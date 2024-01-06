"""
    Introduction to Python default parameters
    -----------------------------------------
    When you define a function, you can specify a default value for each parameter.

    To specify default values for parameters, you use the following syntax:

    Syntax:
    -------
    * def function_name(param1, param2=value2, param3=value3, ...):

    In this syntax, you specify default values (value2, value3, …) for each parameter using the assignment operator (=).

    When you call a function and pass an argument to the parameter that has a default value, the function will use that argument instead of the default value.

    However, if you don’t pass the argument, the function will use the default value.

    To use default parameters, you need to place parameters with the default values after other parameters. Otherwise, you’ll get a syntax error.

    For example, you cannot do something like this:
    
    Syntax:
    -------
    * def function_name(param1=value1, param2, param3):          # Error:

    Place default parameters after the non-default parameters.

"""

# Example for default parameter:

def great(name, message="Hi"):
    return f"{message} - {name}"


print(great("Thillai"))     # Hi - Thillai
print(great("Shanmugam","Hello")) # Hello - Thillai


# Example Multiple default parameter:

def great_2(name="Thillai",message="Hi"):
    print(f"{message}-{name}")

great_2()                                           # Hi - Thillai
great_2("Thillai Shanmugam","Hello")                # Hello - Thillai Shnamugam
great_2(name="TT")                                  # TT - Hi