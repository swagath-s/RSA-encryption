from step2 import *

#TEXT to number is untested!!!

def is_prime(num):
    
    if num == 1 or num ==2:
        return {1:False, 2:True}[num]
    
    if num%2:
        for i in range(3, num/2, 2):
            if not num%i:
                return False
    else:
        return False
    return True


def input_primes(p, q):
    for i in (p, q):
        if is_prime(i):
            print i, "is prime. Accepted."
        else:
            print i, "isn't prime. Try again."
            break
    if is_prime(p) and is_prime(q):
        do_the_thing(p, q)
        
