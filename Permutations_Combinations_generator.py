from math import factorial  # Import the factorial function from the math module.

# Function to calculate permutations (n choose r).
def permutations(n, r):
    # Use the factorial function to calculate the factorial of n and (n-r).
    numerator = factorial(n)
    denominator = factorial(n - r)
    
    # Calculate and return the result as the ratio of the factorials.
    result = numerator // denominator
    return result

# Function to calculate combinations (n choose r).
def combinations(n, r):
    # Use the factorial function to calculate the factorials of n, r, and (n-r).
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    
    # Calculate and return the result as the ratio of the factorials.
    result = numerator // denominator
    return result
