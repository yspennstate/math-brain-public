#!/usr/bin/env python3
"""Exact necessary endpoint-sum enumeration for a Turyn-type TT(172).

For TT(n) sequences X,Y,Z,W of lengths n,n,n,n-1 satisfying
N_X(j)+N_Y(j)+2N_Z(j)+2N_W(j)=0 for j>=1,
put x=sum X, y=sum Y, z=sum Z, w=sum W. Summing autocorrelations gives
x^2+y^2+2z^2+2w^2 = 6n-2.
For n=172, x,y,z are even and w is odd. We enumerate all absolute-value
quadruples, quotienting only the X<->Y symmetry by x<=y.
This is a necessary-condition reduction only, not a TT(172) existence search.
"""
from math import isqrt
n=172
target=6*n-2
sol=[]
for x in range(0,n+1,2):
    for y in range(x,n+1,2):
        for z in range(0,n+1,2):
            rem=target-x*x-y*y-2*z*z
            if rem<=0 or rem%2:
                continue
            w2=rem//2
            w=isqrt(w2)
            if w*w==w2 and (w&1) and w<=n-1:
                sol.append((x,y,z,w))
assert len(sol)==len(set(sol))
for q in sol:
    x,y,z,w=q
    assert x<=y and x%2==y%2==z%2==0 and w%2==1
    assert x*x+y*y+2*z*z+2*w*w==target
print(f"turyn_type_n={n}")
print(f"induced_T_sequence_length=3n-1={3*n-1}")
print(f"induced_hadamard_order=4(3n-1)={4*(3*n-1)}")
print(f"endpoint_sum_target=6n-2={target}")
print(f"absolute_endpoint_quadruple_count_mod_XY_swap={len(sol)}")
for i,q in enumerate(sol,1):
    print(f"{i:02d}: {q}")
print("EXACT_ENUMERATION_PASSED")
print("SCOPE: necessary TT(172) endpoint sums only; no existence/nonexistence conclusion.")
