#!/usr/bin/env python3

"""
This is a short python script to evaluate mathematical expressions in postfix notation
It only works with operators that take 2 arguments at the moment
"""

OPERATOR = {
        # Maths operators
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y,
        '%' : lambda x, y: x % y,
        '//' : lambda x, y: x // y,
        '**' : lambda x, y: x ** y,

        # Bitwise operators
        '^' : lambda x, y: x ^ y,
        '|' : lambda x, y: x | y,
        '&' : lambda x, y: x & y,
        '<<' : lambda x, y: x << y,
        '>>' : lambda x, y: x >> y
        }

def evaluate(expression):
    """
    Evaluates an postfix expression

    Returns the result on success raises SyntaxError when there is an error.
    """

    # Create a new empty stack for each expression and tokenise the expression
    stack = []
    tokens = expression.split()
    for position, token in enumerate(tokens):
        if token in OPERATOR:
            # Check that the stack has at least 2 values for us to use
            if len(stack) < 2:
                error = "There are not sufficient values for operation `{}` at {}. Stack trace: {}".format(token, position, stack)
                raise SyntaxError(error)
            # If we find an operator, retrieve the last 2 items on the stack and use the operation on them
            y, x = stack.pop(), stack.pop()
            result = OPERATOR[token](x, y)
            # Push the result back onto the stack
            stack.append(result)
        elif token.isdigit():
            # If we've found a number, convert it to an int and push it to the stack
            stack.append(int(token))
        else:
            # We've encountered a token that isn't an operand nor operator, fail and print a stack trace.
            error = "Token: `{}` at {} is not a valid token. Stack trace: {}".format(token, position, stack)
            raise SyntaxError(error)

    # If we have anything other than 1 thing on the stack, then the input is bad
    if len(stack) != 1:
        erorr = "Reached end of expression, stack does not have 1 value. Stack trace: {}".format(stack)
        raise SyntaxError(error)
    else:
        return stack.pop()

if __name__ == '__main__':
    import traceback
    import sys

    # Read an expression in
    expression = input("Enter the postfix expression: ")

    # While we have an expression
    while expression:

        # Evaluate the expression and catch SyntaxErrors
        try:
            print("Result:", evaluate(expression))
        except SyntaxError as e:
            traceback.print_exc(file=sys.stderr)

        # Prompt user for input again
        expression = input("Enter the postfix expression: ")
