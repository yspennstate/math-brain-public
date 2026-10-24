#!/usr/bin/env python3
"""Exact finite arithmetic self-check for the generic single-unit-gap depth-six theorem.

This is NOT the theorem proof. The immutable report supplies the analytic inequalities.
The script checks only the finite orbit list and the rational constants/margins used there.
"""
from fractions import Fraction as F

types = [(1,0)] + [(a,b) for a in range(1,6) for b in range(1,6) if a+b <= 5]
assert len(types) == 11

full = [(a,b) for a,b in types if a+b+1 == 6]
assert full == [(1,4),(2,3),(3,2),(4,1)]

jmap = {(a,b): min(a,b+1) for a,b in full}
assert sorted(set(jmap.values())) == [1,2,3]
assert jmap[(1,4)] == 1
assert jmap[(2,3)] == 2 and jmap[(4,1)] == 2
assert jmap[(3,2)] == 3

j1_log_coeff_bound = F(5,27)
j1_fisher_bound = F(4,1)
j1_total = j1_log_coeff_bound + j1_fisher_bound
assert j1_total == F(113,27)

def qx(p): return 15*p*p - 10*p + 1
def qy(p): return 15*p*p - 20*p + 6
assert qx(F(1,3)) == F(-2,3)
assert qy(F(1,2)) == F(-1,4)
assert qy(F(2,5)) == F(2,5)

j2_total = F(4,3) + F(1,4) + F(1,1)
assert j2_total == F(31,12)

j3_total = F(3,4)
reserve = F(24,1)
margins = {1: reserve-j1_total, 2: reserve-j2_total, 3: reserve-j3_total}
assert margins[1] == F(535,27)
assert margins[2] == F(257,12)
assert margins[3] == F(93,4)
assert all(v > 0 for v in margins.values())

print("OVERALL PASS")
print("feasible_generic_orbit_types =", len(types))
print("types =", types)
print("full_support_types =", full)
print("full_support_symmetry_classes_j =", sorted(set(jmap.values())))
print("j1_danger_bound =", j1_total, "; reserve_margin =", margins[1])
print("j2_danger_bound =", j2_total, "; reserve_margin =", margins[2])
print("j3_danger_bound =", j3_total, "; reserve_margin =", margins[3])
print("qx(1/3) =", qx(F(1,3)))
print("qy(2/5) =", qy(F(2,5)))
print("qy(1/2) =", qy(F(1,2)))
