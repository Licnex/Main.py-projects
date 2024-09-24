

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