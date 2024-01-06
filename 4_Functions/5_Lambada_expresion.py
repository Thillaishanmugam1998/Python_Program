"""
    Sometimes, you need to write a simple function that contains one expression. 
    However, you need to use this function once. And it’ll unnecessary to define that function with the def keyword.

    That’s where the Python lambda expressions come into play.

    What are Python lambda expressions
        Python lambda expressions allow you to define anonymous functions.

        Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

        A lambda expression typically contains one or more arguments, but it can have only one expression.

        The following shows the lambda expression syntax:

    lambda parameters: expression:
    ------------------------------
        lambda parameters: expression
    
    It’s equivalent to the following function without the "anonymous" name:
    -----------------------------------------------------------------------
        def anonymous(parameters):
            return expression
"""