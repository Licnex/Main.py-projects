def sum_of_digits(number):
        result = 0
        for digit in str(number):
            result += int(digit)
        return result
print(sum_of_digits(2**1000))