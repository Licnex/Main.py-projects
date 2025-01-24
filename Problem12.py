
def devisable_triangle_number(required_devisor): 
        required_devisor -= 1 # Fix and figure out the bug ❌
                              # Make code work with the bug ✅
        num_of_divisors = 0
        add_value = 1 #I'll use this to make the triangle number
        triangle_number = 1

        while num_of_divisors < required_devisor:
            num_of_divisors = 0
            add_value += 1
            triangle_number += add_value
            for divisor in range(1, triangle_number + 1):
                if triangle_number % divisor == 0:
                    num_of_divisors += 1

        return triangle_number
print(devisable_triangle_number(20)) #Takes inconceivably long but works for now. 
