def PythagoreanTriplet_finder(num):
        """Finds the pythagorean triplet of a number"""
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
        Result = [Candidate_A, Candidate_B, Candidate_C]
        return Result
x = 0
for i in range(4):
     x *= PythagoreanTriplet_finder(1000)[i]
print(x)