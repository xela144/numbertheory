#!/usr/bin/python3

'''
Task:
"Create a random number generator in Python and share your project on any public repository before the start of the meetup.  The project must accept two inputs of type integer: minimum and maximum.  It must return a random integer between the minimum and maximum values, inclusive.  The project can use any user interface."

===

Implements a linear congruential generator X_{n+1} = (aX_n +c) mod m

where

0 < m           modulus
0 < a < m       multiplier
0 < c < m       incrementor
0 < X_0 < m     The seed

===

To maximize the period of the pseudo-random number generator, we must have that 

i.   gcd(m,c) = 1
ii.  a - 1 = product of prime factors of m
iii. if a - 1 mod 4 == 0, then m mod 4 == 0.
'''

from practiceTables import gcd, isPrime, getDivisors
import time
from math import floor, ceil, sqrt, log

class randrand():
    def __init__(self):
        self.modulus = 0
        self.multiplier = 0
        self.incrementer = 0
        self.theSeed = 0
        self.currentRand = 0
        self.prevRand = 0
        self.upper = 0
        self.lower = 0

    # Set up the parameters for the linear congruence generator
    def setLinearConGen(self):
        self.setMod()
        self.setInc()
        self.setMult()
        self.setTheSeed()
        self.prevRand = self.theSeed

    # Set the seed based on the hash of the system time
    def setTheSeed(self):
        firstSeed = self.getTimeSeed()
        while firstSeed < self.upper:
            firstSeed *= firstSeed + 1
        self.theSeed = firstSeed % self.modulus

    # This seed is a hash of the system clock, stringified
    def getTimeSeed(self):
        timeSeed = floor(time.time()*1234567)
        hashhh = hash(str(floor(timeSeed)))
        # We want the absolute value
        if hashhh < 0:
            hashhh = -hashhh
        return hashhh

    # The modulus. Should be bigger than the upper bound
    def setMod(self):
        upper = self.upper
        self.modulus = floor(upper*log(upper))


    # The incrementor
    def setInc(self):
        modulus = self.modulus
        # First candidate for incrementor
        inc = floor(modulus * log(modulus))

        # Ensure the incrementor and modulus are relatively prime
        while not self.coprime(inc, modulus):
            inc += 1
            print(inc)
        # Store to class
        self.incrementor = inc
    
    # Boolean, returns True for relatively prime numbers
    def coprime(self, a,b):
        if a*b == 0:
            print("coprime error: Zero case not implemented")
            return
        return gcd(a,b)<2


    # The multiplier, c, and the modulus, m, must be relatively prime for
    # guarantees on the strength of the randomness.
    # Warning: This code takes some time for large numbers!!!
    def setMult(self):
        if self.incrementor == 0:
            print("Error, must set incrementor before setting multiplier")
            return
        
        modulus = self.modulus
        # Get the product of all the prime factors of the modulus
        product = 1
        modFourFlag = modulus % 4 == 0
        for prime in getDivisors(modulus):
            product *= prime
        
        # If modulus is divisible by four, so is product - 1
        product *= (1 + 2*int(modFourFlag))

        self.multiplier = product + 1 

        
    def getRandom(self):
        # These parameters are used to generate the next pseudo random number
        X = self.prevRand
        a = self.multiplier
        m = self.modulus
        c = self.incrementor
        # Now get the next random number in the sequence
        X_next = (X*a+c)%m
        self.prevRand = X_next

        # Make sure that the value we return is in the correct range
        nextRand = X_next % self.upper
        if nextRand < self.lower:
            nextRand = self.getRandom()
        return nextRand

    
if __name__ == "__main__":
    try:
        randgen = randrand()
        #if input("Enter a lower bound ")
        print("Random number generator. Type 'q' to quit.")
        print("Please be nice (i.e. don't enter lower > upper or things of that sort)")
        print("This is a pseudo-random generator. A list of random", 
                "numbers will be generated based off a seed. This first step will take",
                "some time for large upper bounds, as prime factors are calculated. This",
                "is necessary for guarantees on the length the period, but for faster "
                "algorithms this constraint can be relaxed at the price of a shorter "
                "period. After this initial calculation the subsequent random numbers",
                "are easily calculated.\n")

        print("And one more thing: if the lower bound is close to the upper bound, this",
              " will also weaken the randomness of the generator by shortening the period.")
        
        print("\nThe name of the algorithm is 'Linear Congruence Generator'")
        while(True):

            # Get the user input
            randgen.upper = int(input("Choose an upper bound: "))
            randgen.lower = int(input("Choose a lower bound: "))

            # Initialize the linear congruence generator list
            randgen.setLinearConGen()

            # Generate a random number, then print
            theRandomNumber = randgen.getRandom()
            print("RandomNumber was: {}".format(theRandomNumber))
            if input("Continue? Type y or n: ").upper() == 'Y':
                while True:
                    theRandomNumber = randgen.getRandom()
                    print("RandomNumber was: {}".format(theRandomNumber))
                    if input("Press return to continue, or enter another character to re-seed ") == '':
                        continue
                    else:
                        break 

    # Allow user to error out to quit        
    except ValueError:
            print("Goodbye!!!")
