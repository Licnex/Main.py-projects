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