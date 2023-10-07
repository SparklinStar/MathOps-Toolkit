def newton_sqrt(number, iterations=10):
    # Step 1: Initialize the initial guess for the square root (x).
    x = 1.0
    
    # Step 2: Perform the Newton-Raphson method for a specified number of iterations.
    for _ in range(iterations):
        # Step 3: Calculate the new approximation for the square root using the formula.
        x = 0.5 * (x + number / x)
    
    # Step 4: Return the final approximation for the square root.
    return x
