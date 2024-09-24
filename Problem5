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