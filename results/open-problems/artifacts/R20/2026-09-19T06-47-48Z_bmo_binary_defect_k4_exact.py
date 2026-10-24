#!/usr/bin/env python3
"""Exact self-check for the R20 BMO terminal-handoff stress test.

This checks only the finite statement used to falsify the *binary-defect
subroute* on an all-direct cubic K4.  It is not a counterexample to the BMO
conjecture.  For eps_v in {0,1}, the deficit-color at v is

    T_v = 3 eps_v + sum_{u~v} eps_u.

On K4 this equals E + 2 eps_v, where E=sum eps, hence at most two distinct
values occur.  The exhaustive loop below checks all 2^4 assignments with
integer arithmetic.
"""
from itertools import product

V = range(4)
E = [(u, v) for u in V for v in V if u < v]

proper = []
for eps in product((0, 1), repeat=4):
    total = sum(eps)
    T = [3 * eps[v] + sum(eps[u] for u in V if u != v) for v in V]
    assert T == [total + 2 * eps[v] for v in V]
    if all(T[u] != T[v] for u, v in E):
        proper.append((eps, tuple(T)))

print("graph=K4")
print("binary_assignments_tested=16")
print(f"proper_binary_defect_assignments={len(proper)}")
print("formula_verified=T_v=sum(eps)+2*eps_v")
print("VERDICT=PASS_BINARY_SUBROUTE_OBSTRUCTION" if not proper else "VERDICT=FAIL")
