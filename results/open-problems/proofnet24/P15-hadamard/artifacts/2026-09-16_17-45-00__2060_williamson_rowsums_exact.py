#!/usr/bin/env python3
"""Exact k=0 Fourier/row-sum necessary-condition check for Williamson order 515.

If symmetric circulant +/-1 matrices A,B,C,D of order n are Williamson,
then applying AA^T+BB^T+CC^T+DD^T=4n I to the all-ones vector gives
    a^2+b^2+c^2+d^2 = 4n,
where a,b,c,d are the four row sums.  For odd n every row sum is odd.
We enumerate absolute row sums modulo permutation/negation by
0<a<=b<=c<=d.  Passing this test is only a necessary condition.
"""
from math import isqrt
n=515
target=4*n
sol=[]
limit=isqrt(target)
for a in range(1,limit+1,2):
    for b in range(a,limit+1,2):
        if a*a+b*b>target: break
        for c in range(b,limit+1,2):
            rem=target-a*a-b*b-c*c
            if rem<0: break
            d=isqrt(rem)
            if d<c or d%2==0: continue
            if d*d==rem:
                sol.append((a,b,c,d))
assert len(sol)==len(set(sol))
for q in sol:
    assert all(x>0 and x%2 for x in q)
    assert tuple(sorted(q))==q
    assert sum(x*x for x in q)==target
print(f'williamson_sequence_length={n}')
print(f'induced_hadamard_order={4*n}')
print(f'row_sum_square_target={target}')
print(f'absolute_rowsum_quadruple_count_mod_permutation_sign={len(sol)}')
for i,q in enumerate(sol,1): print(f'{i:02d}: {q}')
print('EXACT_ENUMERATION_PASSED')
print('SCOPE: k=0 Williamson row-sum necessary condition only; no Williamson(515) existence/nonexistence conclusion.')
