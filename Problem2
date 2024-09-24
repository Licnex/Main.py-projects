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

print(fib_gen_even(4000000))