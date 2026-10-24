#!/usr/bin/env python3
"""Exact arithmetic gate for multiplicative-subgroup-invariant periodic T(523)."""
from math import isqrt, comb
P=523
PHI=P-1

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def row_patterns(d):
    lim=isqrt(P)
    # Normalize T_0(0)=+1. Then r_0 == 1 (mod d), while r_1,r_2,r_3 == 0 (mod d).
    r0vals=[r for r in range(-lim,lim+1) if (r-1)%d==0]
    rvals=[r for r in range(-lim,lim+1) if r%d==0]
    out=set()
    for r0 in r0vals:
        for r1 in rvals:
            for r2 in rvals:
                rem=P-r0*r0-r1*r1-r2*r2
                if rem<0:
                    continue
                a=isqrt(rem)
                for r3 in ({a,-a} if a else {0}):
                    if r3%d==0 and r3*r3==rem:
                        out.add((r0,tuple(sorted((abs(r1),abs(r2),abs(r3))))))
    return sorted(out)

Ds=divisors(PHI)
print('p',P)
print('p_minus_1',PHI)
print('divisors',Ds)
survive=[]
for d in Ds:
    if d==1:
        continue
    pats=row_patterns(d)
    print('d',d,'patterns',pats)
    if pats:
        survive.append(d)
print('nontrivial_surviving_subgroup_orders',survive)
assert survive==[3,9]

p9=row_patterns(9)
assert p9==[(19,(0,9,9))],p9
print('d9_unique_normalized_rowsums',(19,9,9,0))
# At d=9 the orbit imbalances are z=(2,1,1,0), up to the allowed
# permutation/sign normalizations. Thus
# a0=2+2*x0, a1=1+2*x1, a2=1+2*x2, a3=2*x3 and sum a_i=58,
# so x0+x1+x2+x3=27: C(30,3)=4060 ordered support profiles.
profiles=comb(30,3)
assert profiles==4060
print('d9_nonzero_orbit_count',58)
print('d9_ordered_support_profiles',profiles)
print('d9_support_parameterization','(a0,a1,a2,a3)=(2+2x0,1+2x1,1+2x2,2x3), sum x_i=27')

# Independent sanity checks matching the written proof.
for d in Ds:
    if d>1 and d%2==0:
        assert not row_patterns(d)
for d in Ds:
    if d>=29 and d%2==1:
        assert not row_patterns(d)
print('parity_and_magnitude_eliminations','PASS')
print('ALL_EXACT_T523_PROFILE_GATE_CHECKS_PASSED')
