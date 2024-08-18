def ldr(list):
  """Removes duplicates by using a for loop"""
  new_list= []
  for current_item in list:
    if current_item not in new_list:
      new_list.append(current_item)
    return new_list
def get_multiples(num1, num2, RangeTop):
   """checks for multiples of number in range(1-RangeTop)"""
   multiples = []
   i=1
   for i in range(1,RangeTop):
       if i % num1 == 0 and i != 0:
              multiples.append(i)
       if i % num2 == 0 and i != 0:
              multiples.append(i)
   return multiples
def fib_gen_even(limit):
    """Generates Fibonacci sequence up to a limit and filters out odd numbers"""
    def fib_gen():
      a = 1
      b = 2
      fib_list = [1]
      while b < limit:
          a,b = b, a+b
          fib_list.append(a)
      return fib_list
    def filter_odd(lists):
        """filters out odd numbers"""
        new_list = []
        for current_item in lists:
            if current_item % 2 == 0:
                new_list.append(current_item)
        return new_list
    return filter_odd(fib_gen())
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
def find_largest_palindrome(limit):
    """Find the largest palindrome of two numbers 
    limit being the largest the  numbers can be"""
    num1=1
    num2=2
    palindromes = []
    for num1 in range(1, limit):
        for num2 in range(1,limit):
            if str(num1*num2) == str(num1*num2)[::-1]:
                palindromes.append(num1*num2)
    return max(palindromes) 
def lcm_upto(num):
    """finds the least common multiples of range(1-num)"""
    lcm = 1
    for number in range(1, num):
        if lcm % number > 0:
            for multiplier in range(1, num):
                if (lcm * multiplier) % number == 0:
                    lcm *= multiplier
                    break
    return lcm
def sum_square_difference(RangeTop):
    """Finds the difference between the sum of squares and sum of numbers"""
    def sum_of_squares(RangeTop):
        """squares numbers then adds them"""
        lists = []
        sum_square = 0  
        number = 1
        for number in range(1, RangeTop+1):
            sum_square += (number**2)
        return sum_square
    def sum_of_range_squared(rangeTop):
        """"adds numbers then squares them"""
        sum_of_range= 0
        for number in range(1, rangeTop+1):
            sum_of_range += number
        return (sum_of_range**2)
        
    sum_square_difference= (sum_of_range_squared(RangeTop)-sum_of_squares(RangeTop)) 
    return sum_square_difference
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
def find_max_product(num_of_digits, number):
    final_result = 0
    for i in range(len(number) - num_of_digits + 1):
        product = 1
        for j in range(num_of_digits):
            product *= int(number[i + j])
        if product > final_result:
            final_result = product

    return final_result
    """writing this down for Daoud: my line of thinking was to first check the first num_of_digits
      and if the result was greater than the current result, update it.
        Then for each digit, check the product multiplication of those digits was greater than the current max product.
        if it wasn't, move 1 step ahead so if digit1 * digit 2 was less than digit2 * digit 3 then max result would then 
        be digit 2 * digit 3(assuming num_of digits is two), this would go on until we have reached the last digit of the 
        large number.what you see here is me trying to implement this line of thinking"""
def PythagoreanTriplet_finder(num):
    """Finds the pythagorean triplet of a given number then multiplies the triplets"""
    Candidate_A = 1
    Candidate_B = 2
    Candidate_C = 3
    Triplet_A = 0
    Triplet_B = 0
    Triplet_C = 0
    for Candidate_A in range(num):
        for Candidate_B in range(Candidate_A+1, num):
            for Candidate_C in range(Candidate_B+1, num):
                if Candidate_A**2 + Candidate_B**2 == Candidate_C**2 and Candidate_A+Candidate_B+Candidate_C == num:
                    Candidate_A = Triplet_A
                    Candidate_B = Triplet_B
                    Candidate_C = Triplet_C
    return Triplet_A * Triplet_B * Triplet_C
def Sum_of_primes(limit):
    """Finds the sum of all primes up to a given limit then adds them all up"""
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
#There you go Daoud, I did them

print(Sum_of_primes(2000000))
