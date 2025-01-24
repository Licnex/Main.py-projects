def largest_collatz_sequence(limit):
        """Finds the number under the given limit that produces the longest Collatz sequence.""" 
        def sequence_generator(number):
            """Generates a a collatz sequence as a list from a given number"""
            sequence = []
            while number != 1:
                sequence.append(number)
                if number % 2 == 0:
                    number = number // 2
                else:
                    number = 3 * number + 1
            sequence.append(1)  # Since the sequence always ends with 1 (not including negatives)
            return sequence
        max_length = 0
        result = 0
        for number in range(2, limit):
            seq = sequence_generator(number)
            if len(seq) > max_length:
                max_length = len(seq)
                result = number 
        return result
print(largest_collatz_sequence(1000000))        