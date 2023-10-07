from math import factorial  # Import the factorial function from the math module.

# Function to approximate the sine of an angle using the Maclaurin series.
def sine(x, terms=10):
    result = 0  # Initialize the result to 0.

    for n in range(terms):
        # Calculate the current term in the Maclaurin series.
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        
        # Add the current term to the result.
        result += term

    return result  # Return the final approximation of sine(x).
