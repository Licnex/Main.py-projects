def find_prime_factors(number):
        """Finds the prime factors for a given number (somehow, doesn't return duplicates)"""
        primes = []
        def prime_check(num):
            i = 2
            for i in range(2,num):
                if num % i == 0 and i!= 0 and i != 1 and i!= num:
                    return False 
        for multiple in range(2,number):
            if number%multiple == 0 and multiple != 0 and  multiple != 1: #checking if the multiple is a multiple of number
                if prime_check(multiple) != False:
                    primes.append(multiple)
        return primes
print(find_prime_factors(600851475143))