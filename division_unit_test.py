def division(x, y):
    """
    Divide two numbers 'x' and 'y'.

    Parameters:
    x (float or int): The numerator.
    y (float or int): The denominator.

    Returns:
    float or str: If 'y' is not zero, returns the result of 'x' divided by 'y'.
                  If 'y' is zero, returns the string "ERROR" (division by zero is undefined).
    """
    if y == 0:
        return "ERROR"
    else:
        return x / y

# Assert statements for testing the 'division' function
assert division(2, 1) == 2
assert division(0, 5) == 0
assert division(1, 2) == 0.5
assert division(1, 0) == "ERROR"
