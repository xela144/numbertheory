#!/usr/local/bin/python3

import sys
import pdb


# Just compute x^n - 1 for x in {1, 2, ... xx} 
def poly_mod(xx, nn):
    while xx:
        mm = (xx**nn - 1)
        print(xx, mm, mm%nn)
        xx -= 1

# Factor x^n - 1 as (x-1)*sum^{x-1}_0 x^i and compute the polynomial
def poly_mod_factor(xx, nn):
    while xx:
        ss = sum([xx**x for x in range(0,nn)])
        prod = (xx - 1) * ss
        print(xx, ss % nn, prod, prod%nn)
        xx -= 1
        
    

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("usage: 'mod_poly.py x n'. For calculating x^n-1 mod n for x in 1..n-1.") 
    else:
        nn  = int(sys.argv[1])
        xx = nn -1
        poly_mod(xx, nn)
        print("\nfactoring out (x - 1):")
        poly_mod_factor(xx, nn)


