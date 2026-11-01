#!/usr/bin/env python3
from itertools import product
from math import log2

SIGNS=(-1,1)

def transformed(a,b,c,d):
    return (a+b,b,c+d-a-b,d-b)

quads=list(product(SIGNS,repeat=4))
diag=[q for q in quads if transformed(*q)[2]==0]
below=[q for q in quads if transformed(*q)[2]==0 and transformed(*q)[0]==0]
above=[q for q in quads if transformed(*q)[2]==0 and transformed(*q)[3]==0]
assert (len(diag),len(below),len(above))==(6,4,4)
print('local_total=16')
print('diag_count=6')
print('below_count=4')
print('above_count=4')
for m in range(1,7):
    N=4**(m*(m-1))*6**m
    n=2*m
    e=n*n-(2*m*(m-1)+m*log2(6))
    rhs=n*n/2-(n/2)*(log2(6)-2)
    assert abs(e-rhs)<1e-12
    print(f'm={m} n={n} family_count={N} normalized_exponent={e/(n*n):.12f}')
print('EXACT_LOCAL_COUNT_AND_EXPONENT_PASS')
