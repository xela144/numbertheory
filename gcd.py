
def order(y,z):
    y = abs(y)
    z = abs(z)
    if y>z:
        return y,z
    else:
        return z,y

def gcd(a, b):
    if a == 0 or b == 0:
        print("everything divides 0, but calculating GCD anyway")
    # Make a greater than b, or at least a == b
    (aa,bb) = order(a,b)
    bb, qq, rr = get_remainder(aa,bb)
    count =1 
    while rr != 0:
        bb, qq, rr = get_remainder(bb,rr)
        count +=1
    return bb


# returns (b, q, r) for a = bq + r
def get_remainder(a,b):
    # Not sure what to put for this.
    if a == 0:
        # 0 = b*0 + 0
        return b, 0, 0
    if b == 0:
        # a = 0*q + a
        return 0, 0, a
    qq = 0 
    (aa,bb) = order(a,b)
    def get_remainder_helper(aa,bb, qq):
        r1 = aa-bb
        if r1 < bb:
            qq += 1
            return r1, bb, qq
        else:
            qq += 1
            return get_remainder_helper(r1,bb, qq)
    (rr,bb, qq) = get_remainder_helper(aa,bb,qq)
    aa = bb * qq + rr
    print("returning remainder as", aa, "=", bb, "dot", qq, "plus", rr)
    return bb, qq, rr
#print("gcd of", tup[0], "and", tup[1], "is", d)


# Works much better
def newgcd(aa,bb):
    b = bb
    a = aa
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

# For fun
#tup = (4**6**6, 10**6**6)
#newgcd(tup[0],tup[1])

# recursive not very good with python
def newgcd_rec(aa,bb):
    if aa == 0:
        print(bb)
        return bb
    print(bb)
    return newgcd_rec(bb%aa, aa)

# returns True or False.
#FIXME deal with 0 cases.
def coprime(a,b):
    return newgcd(a,b)<2

# Returns the standard reduced residue system, modulo m
def reduced_residue_system(m):
    rrs = []
    for i in range(1,m):
        if newgcd(i,m) == 1:
            rrs.append(i)
    #print(rrs)
    return(rrs)

# returns the Euler's totient value
def totient(m):
    return len(reduced_residue_system(m))

# scatter plot of the totient values up to m.
def plot_totient(m):
    import matplotlib.pyplot as plt
    import numpy as np
    index = np.arange(1,m)
    tot = np.arange(1,m)
    for i in tot:
        tot[i-1] = totient(i)

    plt.scatter(index,tot)
    plt.show()


