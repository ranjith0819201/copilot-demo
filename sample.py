def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def find_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value
# Generate a docstring for this function
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (int, float): The first number to multiply.
    b (int, float): The second number to multiply.

    Returns:
    int, float: The product of the two numbers.
    """
    return a * b
    return a * b  

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Copilot: Write a function to check if a list is sorted
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
# Generate a docstring for this function
def divide(a, b):
    """
    Divides the first number by the second number and returns the result.

    Parameters:
    a (int, float): The numerator.
    b (int, float): The denominator.

    Returns:
    float: The result of the division.

    Raises:
    ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
# Generate a docstring for this function
def subtract(a, b):
    """
    Subtracts the second number from the first number and returns the result.

    Parameters:
    a (int, float): The number from which to subtract.
    b (int, float): The number to subtract.

    Returns:
    int, float: The result of the subtraction.
    """
    return a - b
# Generate a docstring for this function
def power(base, exponent):
    """
    Raises the base to the power of the exponent and returns the result.

    Parameters:
    base (int, float): The base number.
    exponent (int, float): The exponent to which the base is raised.

    Returns:
    int, float: The result of raising the base to the power of the exponent.
    """
    return base ** exponent
# Generate a docstring for this function
def modulus(a, b):
    """
    Returns the modulus of the first number by the second number.

    Parameters:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    int: The remainder when a is divided by b.
    """
    return a % b



