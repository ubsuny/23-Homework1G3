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
        # If 'y' is 0, return the string "ERROR" (division by zero is undefined)
        return "ERROR"
    else:
        # If 'y' is not 0, return the result of 'x' divided by 'y'
        return x / y

# Assert statements are used to test the 'division' function
# They check if the function behaves as expected for specific inputs

# Assert that division(2, 1) should return 2 and so on...
# Assert statements for testing the 'division' function
assert division(2, 1) == 2
assert division(0, 5) == 0
assert division(1, 2) == 0.5

# Assert that division(1, 0) should return "ERROR" since it's dividing by zero
assert division(1, 0) == "ERROR"
