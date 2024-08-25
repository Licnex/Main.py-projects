def ldr(list):
  """Removes duplicates by using a for loop"""
  new_list= []
  for current_item in list:
    if current_item not in new_list:
      new_list.append(current_item)
    return new_list
def project_euler_1():
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
    print(get_multiples(3,5,1000))
def project_euler_2():
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
    print(4000000)
def project_euler_3():
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
def project_euler_4():
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
    print(find_largest_palindrome(1000))
def project_euler_5():
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
    print(lcm_upto(20))
def project_euler_6():   
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
    print(sum_square_difference(100))
def project_euler_7():
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
def project_euler_8():
    def find_max_product(num_adj, number):
        final_result = 0
        for i in range(len(number) - num_adj + 1):
            product = 1
            for j in range(num_adj):
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
    print(find_max_product(13, '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'))   
def project_euler_9():
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
    print(PythagoreanTriplet_finder(1000))
def project_euler_10():
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
    print(Sum_of_primes(2000000))
#There you go Daoud, I did them ;)
def project_euler_11():
        def largest_product_string_list2d(list2d_str, num_adjacent):
            def turn_string_to_list2d(list2d_str):
                """Turns a string of numbers into a 2D list"""
                list2d = []
                for line in list2d_str.splitlines():
                    row = []
                    for num in line.split():
                        row.append(int(num))
                    list2d.append(row)
                return list2d

            def largest_product_in_list2d(list2d, num_adjacent):
                """Finds the largest product of a number of adjacent numbers in a 2d list/ grid."""
                final_result = 0

                def horizontal_max(list2d, num_adjacent):
                    result = 0
                    for row in list2d:
                        for i in range(len(row) - num_adjacent + 1):
                            product = 1
                            for j in range(num_adjacent):
                                product *= row[i + j]
                            if product > result:
                                result = product
                    return result

                def vertical_max(list2d, num_adjacent):
                    result = 0
                    for col in range(len(list2d[0])):  # Iterate through columns
                        for row in range(len(list2d) - num_adjacent + 1):
                            product = 1
                            for k in range(num_adjacent):
                                product *= list2d[row + k][col]
                            if product > result:
                                result = product
                    return result

                def diagonal_right_max(list2d, num_adjacent):
                    result = 0
                    for row in range(len(list2d) - num_adjacent + 1):
                        for col in range(len(list2d[row]) - num_adjacent + 1):
                            product = 1
                            for k in range(num_adjacent):
                                product *= list2d[row + k][col + k]
                            if product > result:
                                result = product
                    return result

                def diagonal_left_max(list2d, num_adjacent):
                    result = 0
                    for row in range(len(list2d) - num_adjacent + 1):
                        for col in range(num_adjacent - 1, len(list2d[row])):
                            product = 1
                            for k in range(num_adjacent):
                                product *= list2d[row + k][col - k]
                            if product > result:
                                result = product
                    return result

                final_result = max(
                    horizontal_max(list2d, num_adjacent),
                    vertical_max(list2d, num_adjacent),
                    diagonal_right_max(list2d, num_adjacent),
                    diagonal_left_max(list2d, num_adjacent)
                )

                return final_result

            list2d = turn_string_to_list2d(list2d_str)
            return largest_product_in_list2d(list2d, num_adjacent)
        print(largest_product_string_list2d(
        """
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
        """, 4))
def project_euler_12():
    def devisable_triangle_number(devisable):
        """Calculates the nth triangle number that is divisible by a number of times"""
        devisable -= 1 #fix the bug ❌
                       #alter the code to work with the bug ✅
        num_of_divisors = 0
        triangle_number = 1
        current_triangle_num = 1
        while num_of_divisors < devisable:
            num_of_divisors = 0 # Reset divisor count for each new triangle number 
                                # Headache of overengineering had been fixed (for now)
            triangle_number = sum(range(2, current_triangle_num)) + 1
            for i in range(2, triangle_number):
                if triangle_number % i == 0 :
                    num_of_divisors += 1
            current_triangle_num += 1
        return triangle_number        
    print(devisable_triangle_number(500))
project_euler_12() #inefficient, gonna work on that
