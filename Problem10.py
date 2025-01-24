def Sum_of_primes(limit):
    """Finds the sum of all primes up to a given limit"""
    def Gen_Prime(limit):
        """Generates primes up to a given limit and actually uses sieve"""
        is_prime_list = [True] * limit #Creates a list of booleans which are by default set to true
                                #(Saw This when scrolling of youtube, blew my mind)
        is_prime_list[1] = False
        is_prime_list[0] = False # 1 and 0 will mess with the program so it better to just manually change them 
        for number in range(limit):
            if is_prime_list[number] == True: #Checks if the number is marked as true
                for j in range(number*number, limit, number):
                    is_prime_list[j] = False
        primes = []
        for number in range(limit):
            if is_prime_list[number] == True:
                primes.append(number)
        return primes  
    return sum(Gen_Prime(limit))
print(Sum_of_primes(2000000))