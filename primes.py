import math
def is_prime(n):
    if n < 2:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    
    root = math.isqrt(n)
    for i in range(3,root+1,2):
        if n%i == 0:
            return False
    return True

NUMBERS = [142343545456546,5623489562348956,4564385643,4857263485,120742,54679,579348]