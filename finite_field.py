#!/usr/local/bin/python3

import sys



def primitive_elements(qq):
    primitive = {}
    result = {}

    for j in range(2, qq):
        primitive[j] = [0]*qq
        result[j] = set()
        for i in range ( 1, qq):
            #print("member: ", j, "position: ", i, "residue: ", j**i, (j**i)%qq)
            primitive[j][(j**i)%qq] = 1
            result[j].add((j**i)%qq)
        if sum(primitive[j]) == qq-1:
            print("{} is primitive".format(j))
            print(result[j])
            print('\n')

        else:
            print("Order of element {} is {}".format(j, len(result[j])))
            print(result[j])
            print('\n')

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("usage: 'finite_field.py x' where x is order of finite field under multiplication. Note that x should be prime or a power of a prime, otherwise results are not valid, i.e. this script does not generate Galois fields for p**m.")
    else:
        qq  = int(sys.argv[1])

        primitive_elements(qq)


