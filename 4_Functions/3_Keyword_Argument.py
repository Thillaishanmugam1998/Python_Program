# 1. Keyword Argument:

def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
print(net_price)                         # 90.0

"""
In the get_net_price(100, 0.1) function call, we pass each argument as a positional argument. 
In other words, we pass the price argument first and the discount argument second.

However, the function call get_net_price(100, 0.1) has a readability issue. Because by looking at that function call only, 
you don’t know which argument is price and which one is the discount.

On top of that, when you call the get_net_price() function, you need to know the position of each argument.

If you don’t, the function will calculate the net_price incorrectly. For example:
"""

net_price = get_net_price(0.1, 100)
print(net_price)            # -9.99

"""
To improve the readability, Python introduces the keyword arguments.

The following shows the keyword argument syntax:

Syntax:
-------
fn(parameter1=value1,parameter2=value2)
"""

net_price = get_net_price(price=100, discount=0.1)
print(net_price)                        #90.0

# 2. Keyword Argument and default Parameter:

def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

print(get_net_price(100))
print(get_net_price(2000,tax=5))
print(get_net_price(40,discount=90,tax=7))
# print(get_net_price(100,discount=3,4)) # Error after keyword agrument cannot apper positional argument