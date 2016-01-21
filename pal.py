'''
Level 1: The palindrome problem

Convert a number to base b, using the division with remainder algorithm:

N  = q1 * b + r0
q1 = q2 * b + r1
q2 = q3 * b + r2
  ...
qn =  0 * b + rn

Now the number in base b is rn..r2r1r0
'''

import sys


def answer(n):
    def convertn(num, base):
        N = num
        bb = base
        qq = N // bb
        rn = N  % bb
        L = [rn]
        rn = 0
        while qq:
            rn = qq  % bb
            qq = qq // bb
            L.append(rn)
        return L
    
    base = 2

    while True:
        L = convertn(n,base)
        if L == L[::-1]:
            print(base)
            break
        else:
            base += 1
        if base > 1000:
            break
        
if __name__ == '__main__':
    answer(int(sys.argv[1]))
