def restoring_division(numerator, denominator):
    """
    Perform restoring division between 'numerator' and 'denominator'.

    Parameters:
    numerator (int): The number to be divided.
    denominator (int): The divisor.

    Returns:
    tuple: A tuple containing the quotient and remainder of the division.
           - quotient (int): The result of the division, i.e., how many times the 'denominator' can go into 'numerator'.
           - remainder (int): The remainder left after the division.
    """
    quotient = 0  # Initialize the quotient to zero
    remainder = numerator  # Set the remainder to the numerator initially

    # Perform the division as long as the remainder is greater than or equal to the denominator
    while remainder >= denominator:
        quotient += 1  # Increment the quotient for each successful subtraction
        remainder -= denominator  # Subtract the denominator from the remainder

    # After the loop, 'quotient' holds the number of times 'denominator' went into 'numerator'
    # 'remainder' holds the remaining value after division
    return quotient, remainder

# Example usage:
quotient, remainder = restoring_division(10, 3)
print(f"Quotient: {quotient}, Remainder: {remainder}")  # This will print Quotient: 3, Remainder: 1
