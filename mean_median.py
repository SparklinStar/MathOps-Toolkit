from collections import Counter  # Import Counter from the collections module for finding the mode.

def calculate_mean_median_mode(numbers):
    # Calculate the mean (average) of the numbers.
    mean = sum(numbers) / len(numbers)

    # Calculate the median of the numbers.
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[(n - 1) // 2]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2

    # Calculate the mode (most common value) of the numbers.
    count = Counter(numbers)
    mode_count = max(count.values())
    mode = [number for number, freq in count.items() if freq == mode_count]

    return mean, median, mode

# Example usage:
numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8]
mean, median, mode = calculate_mean_median_mode(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
