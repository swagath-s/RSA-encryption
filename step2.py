from random import *
from gcd_printer import *
from step3 import *


def pick_e(elist):
    """currently picks a value from given list at random."""
    #to do: find ideal characteristics of e and implement testing 
    rng = SystemRandom()
    e = int(rng.random()*len(elist))                #random() generates values in [0, 1]
    return elist[e]                                 #returns value stored at randomly generated index

def generate_elist_pick_e(phi):
    """generates list of co-primes leading up to phi, and calls pick_e to pick one"""
    elist = []
    for i in range(phi):
        if gcd(i, phi)==1:
            elist.append(i)
    return pick_e(elist)

def invert(e, phi):
    """Iterates through set [0, phi) to find d such that d.e = 1 (mod phi).
        In other words, (d.e)%phi = 1"""

    #bruteforce:

    for i in range (phi):
        if (i*e)%phi == 1:
            return i
    
def do_the_thing(p, q):
    n = p*q
    print "n =", n
    phi = (p-1)*(q-1)                                 #from formula
    print "phi =", phi, "(just for testing purposes)"
    e = generate_elist_pick_e(phi)
    print "e =", e
    d = invert(e, phi)                            #calls function that will generate private key
    print "d =", e
    m = raw_input("Ready to encrypt. Input message:\n")
    
    
