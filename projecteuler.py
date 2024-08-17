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
    """writing this down for daoud: my line of thinking was to first check the first num_of_digits
      and if the result was greater than the current result, update it.
        Then for each digit, check the product multiplication of those digits was greater than the current max product.
        if it wasn't, move 1 step ahead so if digit1 * digit 2 was less than digit2 * digit 3 then max result would then 
        be digit 2 * digit 3(assuming num_of digits is two), this would go on until we have reached the last digit of the 
        large number.what you see here is me trying to implement this line of thinking"""

print(find_max_product(13, "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")) 
# expected output:5832 
