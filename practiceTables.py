from random import randint, shuffle, gauss
from math import sqrt, ceil, floor
from pdb import set_trace as ppp


def gcd(aa,bb):
    # debug
    # a = aa
    # b = bb
    cc = aa
    while aa != 0:
        cc = aa
        aa = bb%aa
        bb = cc
        # Proxy for gcd:
        #print(bb)
    # For debug:
    #print("({},{}) = {}".format(a, b, bb))
    return bb

def isPrime(n):
    if n == 2:
        return True
    lim = ceil(sqrt(n))
    nn = 1
    while nn <= lim:
        bb = gcd(nn, n)
        nn += 1
        if bb > 1:
            return False
    return True

def getDivisors(nn):
    lis = []
    lim = ceil(nn/2)
    i = 2
    #ppp()
    while i <= lim:
        bb = nn%i
        if bb == 0:
            lis.append(i)
        i += 1
        bb = 1
        #print(bb)
    return lis



def test(nn):
    lis = getDivisors(nn)
    ind1, ind2 = getIndices(len(lis))
    #print("length was {}. Indices were {}, {}".format(len(lis), ind1, ind2))
    #print("divisors were {} and {}.".format(lis[ind1], lis[ind2]))
    return lis[ind1]*lis[ind2]

def getIndices(nn):
    if nn == 1:
        return 0,0
    # Even number of divisors
    if nn%2 == 0:
        lim = nn/2
        ind1 = randint(0,lim)
        ind2 = nn - ind1 - 1
    # Odd number of divisors
    else:
        lim = (nn+1)/2
        ind1 = randint(0,lim)
        ind2 = nn - ind1 - 1
    return ind1, ind2
        
def newMultPrac(upper):
    target = 3
    while isPrime(target):
        target = randint(3, upper)
    lis = getDivisors(target)
    ind1, ind2 = getIndices(len(lis))
    return lis[ind1], lis[ind2]

def buildMultPrac(center):
    upper = center**gauss(2,.3)
    op1 = center #ceil(gauss(center, center**(-3)))
    op2 = randint(2, 12) #int(upper//op1)
    lis = [op1,op2]
    shuffle(lis)
    a = lis[0]
    b = lis[1]
    return a,b

def multPrac(upper, center):
    a = randint(2,upper)
    b = randint(2,upper)
    if a*b > 100:
        a,b = multPrac(upper)
    return (a, b)

def divPrac(upper):
    a = randint(2,9)
    b = randint(2,9)
    while a*b > upper:
        a = randint(2,9)
        b = randint(2,9)
    lis = [a*b, b]
    #shuffle(lis)
    return lis

def processList(lis):
    try:
        newLis = lis.split(',')
        lis = []
        for item in newLis:
            lis.append(int(item))
        return lis
    except:
        print("error in process list")

if __name__ == "__main__":
    try:
        if input("Choose m or d: ").upper() == 'D': 
            while(True):
                upper = int(input("Choose an upper bound: "))
                num = int(input("Number of practice problems: "))
                for i in range(0,num):
                    a,b = divPrac(upper)
                    formatLength = len(str(upper))
                    formatString = "{:" + str(formatLength) +"} ÷ {:" + str(formatLength -1) + "} = "
                    print(formatString.format(a,b))
        
        else:
            while(True):
                upper = input("Choose a factor, or list of factors (use ',' to separate): ")
                upper = processList(upper)
                #center = int(input("Choose a center for operand 1: "))
                num = int(input("Number of practice problems: "))
                for i in range(0,num):
                    shuffle(upper)
                    #a,b = newMultPrac(upper[0])
                    a,b = buildMultPrac(upper[0])
                    formatLength = len(str(upper[0]))
                    formatString = "{:" + str(formatLength) +"} x {:" + str(formatLength) + "} = "
                    print(formatString.format(a,b))
    except ValueError:
            print("Goodbye!!!")
