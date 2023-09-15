# Define a function called 'division' that takes two arguments, 'x' and 'y'
def division(x, y):
    # Check if 'y' is equal to 0
    if y == 0:
        # If 'y' is 0, return the string "ERROR" (division by zero is undefined)
        return "ERROR"
    else:
        # If 'y' is not 0, return the result of 'x' divided by 'y'
        return x / y

# Assert statements are used to test the 'division' function
# They check if the function behaves as expected for specific inputs

# Assert that division(2, 1) should return 2 and so on...
assert division(2, 1) == 2
assert division(0, 5) == 0
assert division(1, 2) == 0.5
assert division(1, 0) == "ERROR"
