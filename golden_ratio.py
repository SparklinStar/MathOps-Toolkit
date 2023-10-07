def golden_ratio(iterations=15):
    # Start with an initial approximation of the golden ratio, typically 1.
    ratio = 1

    # Iterate to improve the approximation.
    for _ in range(iterations):
        # The golden ratio is defined as (1 + sqrt(5)) / 2.
        # We can approximate it by adding 1 to the reciprocal of the current approximation.
        # This approach iteratively refines the approximation.
        ratio = 1 + 1 / ratio

    return ratio

# Example usage:
approximations = []
for i in range(1, 16):
    approximation = golden_ratio(i)
    approximations.append(approximation)

print("Approximations of the Golden Ratio:")
for i, approx in enumerate(approximations):
    print(f"Iteration {i+1}: {approx:.16f}")
