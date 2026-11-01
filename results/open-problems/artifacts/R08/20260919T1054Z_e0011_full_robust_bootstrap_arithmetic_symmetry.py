#!/usr/bin/env python3
from fractions import Fraction
from math import log10

OLD = 4642311559640512826443825152
F1 = 7492177630527378997219688448
FULL = 8119101129828730822113361920
NEXT_OLD = 8458449879232610418655494144
assert FULL > F1 > OLD
assert FULL < NEXT_OLD
GAIN = Fraction(FULL, F1)
assert GAIN == Fraction(6002564211340,5539070962521)
P_F1 = Fraction(80668567688839168,9875024747329504587890625)
P_FULL = P_F1 * GAIN
assert P_FULL == Fraction(157353619261751296,17775044545193108258203125)

CORE={(-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(2,0)}
HALO={(0,-2),(0,3),(1,2),(2,1)}
PATCH=CORE|HALO
FIXED={(-1,0),(-1,1)}
TARGET={(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1)}
MATS=[((1,0),(0,1)),((-1,0),(0,1)),((1,0),(0,-1)),((-1,0),(0,-1)),((0,1),(1,0)),((0,-1),(1,0)),((0,1),(-1,0)),((0,-1),(-1,0))]
def lin(p,M):
    x,y=p
    return (M[0][0]*x+M[0][1]*y,M[1][0]*x+M[1][1]*y)
def ap(p,M,t):
    q=lin(p,M); return q[0]+t[0],q[1]+t[1]
syms=[]
for M in MATS:
    MP={lin(p,M) for p in PATCH}
    for a in PATCH:
        for b in MP:
            t=a[0]-b[0],a[1]-b[1]
            if {ap(p,M,t) for p in PATCH}==PATCH and (M,t) not in syms:
                syms.append((M,t))
valid=[]
for M,t in syms:
    f=lambda S:{ap(p,M,t) for p in S}
    if f(CORE)==CORE and f(HALO)==HALO and f(FIXED)==FIXED and f(TARGET)==TARGET:
        valid.append((M,t))
assert len(syms)==4
assert valid==[(((1,0),(0,1)),(0,0))]
RY=(((1,0),(0,-1)),(0,1))
assert RY in syms
M,t=RY
swap_core={p for p in CORE if ap(p,M,t) in HALO}
swap_halo={p for p in HALO if ap(p,M,t) in CORE}
assert swap_core=={(1,-1),(2,0)}
assert swap_halo=={(1,2),(2,1)}

print('PASS exact R08/E0011 unrestricted robust-bootstrap arithmetic/symmetry certificate')
print('full_over_F1_exact=',f'{GAIN.numerator}/{GAIN.denominator}')
print('full_over_F1_decimal=',repr(float(GAIN)))
print('log10_gain=',repr(log10(GAIN.numerator)-log10(GAIN.denominator)))
print('full_bootstrap_probability=',f'{P_FULL.numerator}/{P_FULL.denominator}')
print('full_bootstrap_probability_decimal=',repr(float(P_FULL)))
print('new_log10_Bcat_diagnostic=',repr(-49.89688548885152 + log10(GAIN.numerator)-log10(GAIN.denominator)))
print('full_patch_lattice_isometries=',len(syms))
print('Bellman_partition_preserving_isometries=',len(valid))
print('only_valid_isometry=identity')
print('y_reflection_core_to_halo=',sorted(swap_core))
print('y_reflection_halo_to_core=',sorted(swap_halo))
