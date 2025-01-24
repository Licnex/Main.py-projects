def Gen_nth_prime(num):
        """Finds the nth prime number."""
        if num == 1:
            return 2 
        primes = [2]
        prime_candidate = 3
        
        def is_prime(candidate):
            """Check if a number is prime."""
            for prime in primes:
                if prime * prime > candidate: # Simple optimization i made thanks to last week
                    break
                if candidate % prime == 0:
                    return False
            return True
        
        while len(primes) < num: # I know you said that I should avoid while loops but 
                                #  I didn't see a way to avoid them in this case
            if is_prime(prime_candidate):
                primes.append(prime_candidate)
            prime_candidate += 2
        return primes[-1]
print(Gen_nth_prime(10001))