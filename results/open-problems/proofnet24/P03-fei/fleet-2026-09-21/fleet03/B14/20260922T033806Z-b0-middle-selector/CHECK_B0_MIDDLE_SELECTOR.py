#!/usr/bin/env python3
from fractions import Fraction as F
import itertools

A = {0,1,2,3,4,5,8,10}

def insert_bit(y, j, b, n=4):
    x=0; k=0
    for i in range(n):
        bit = b if i==j else ((y>>k)&1)
        if i != j:
            k += 1
        x |= bit<<i
    return x

def support_child(j,b):
    return {y for y in range(8) if insert_bit(y,j,b) in A}

# Exact cofactor identities for middle pivots.
assert support_child(2,0) == {0,1,2,3,4,6}
assert support_child(2,1) == {0,1}
assert support_child(3,0) == {0,1,2,3,4,5}
assert support_child(3,1) == {0,2}

def pieces(a,b,t,d):
    q=1-t
    # pivot x2
    delta2 = d*(1-a) + (1-d)*b
    L2 = t*q*delta2*(1-delta2)
    B2 = d*(1-d)*(q*a*(1-a) + t*b*(1-b))
    # pivot x3
    delta3 = a*(1-t) + t*(1-b)
    L3 = d*(1-d)*delta3*(1-delta3)
    B3 = t*q*((1-d)*b*(1-b) + d*a*(1-a))
    X = t*q*d*(1-d)*(1-a-b)**2
    W = L2+B2
    return delta2,delta3,L2,B2,L3,B3,X,W

grid=[F(k,7) for k in range(1,7)]
cases=0
min_two_local_ratio=None
argmin=None
for a,b,t,d in itertools.product(grid, repeat=4):
    delta2,delta3,L2,B2,L3,B3,X,W=pieces(a,b,t,d)
    assert L3 == B2 + X
    assert L2 == B3 + X
    assert W == L3+B3
    assert L2+L3 == W+X
    assert 2*max(L2,L3) >= W
    if W:
        ratio=max(L2,L3)/W
        if min_two_local_ratio is None or ratio < min_two_local_ratio:
            min_two_local_ratio=ratio; argmin=(a,b,t,d,L2,L3,W,X)
    cases += 1

# Uniform anchor for the stable candidate inherited in LIMIT-PRIME-GATE-LIFT-v1.
C0=F("6.4548")
Cstar=F("6.5218512")
astar=4*(Cstar-C0)
assert astar == F("0.2682048")
gamma_quarter_RO=C0-2
gamma_quarter_star=gamma_quarter_RO+astar*F(3,16)
local_uniform=gamma_quarter_RO-F(1,2)*C0-1+astar*F(1,16)
child_uniform=Cstar-2-gamma_quarter_star
root_uniform=F(3,2)*Cstar-3-Cstar
assert local_uniform == F("0.2441628")
assert child_uniform == F("0.0167628")
assert root_uniform == F("0.2609256")
assert root_uniform == local_uniform + child_uniform

print("PASS")
print("truth_support", sorted(A))
print("pivot2_children", sorted(support_child(2,0)), sorted(support_child(2,1)))
print("pivot3_children", sorted(support_child(3,0)), sorted(support_child(3,1)))
print("exact_grid_cases", cases)
print("min_grid_max_local_over_global", min_two_local_ratio)
print("argmin_grid", argmin)
print("selector_theorem", "max(L2,L3) >= W/2")
print("cross_identity", "L3=B2+X; L2=B3+X; W=B2+B3+X")
print("C0", C0, float(C0))
print("Cstar", Cstar, float(Cstar))
print("astar", astar, float(astar))
print("uniform_local_corrected", local_uniform, float(local_uniform))
print("uniform_child_defect", child_uniform, float(child_uniform))
print("uniform_root_defect", root_uniform, float(root_uniform))
