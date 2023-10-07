def sieve_of_eratosthenes(limit):
    # Step 1: Create a list (sieve) of Boolean values initialized to True.
    sieve = [True] * (limit + 1)
    
    # Step 2: Set the first two elements (0 and 1) to False since they are not prime.
    sieve[0] = sieve[1] = False
    
    # Step 3: Iterate through the numbers starting from 2 up to the square root of the limit.
    for i in range(2, int(limit**0.5) + 1):
        # Step 4: If the current number (i) is marked as prime, mark its multiples as not prime.
        if sieve[i]:
            for j in range(i**2, limit + 1, i):
                # Mark multiples of i as not prime by setting their values to False.
                sieve[j] = False
    
    # Step 5: Collect the prime numbers (marked as True) into a list.
    primes = [i for i in range(2, limit + 1) if sieve[i]
    
    # Step 6: Return the list of prime numbers.
    return primes
