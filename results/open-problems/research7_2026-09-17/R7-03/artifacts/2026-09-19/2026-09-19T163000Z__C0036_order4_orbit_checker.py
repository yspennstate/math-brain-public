#!/usr/bin/env python3
"""Exact self-check for the R7-03 C0036 order-four theorem.

This is a SELF-CHECK, not an independent audit.  It uses exact integer orbit
enumeration and SymPy polynomial identities; it does not numerically certify
the all-group source conjecture.
"""

import sympy as sp


def orbit_partition(group_elems, add):
    idx = {g: i for i, g in enumerate(group_elems)}
    all_subsets = list(range(1 << len(group_elems)))

    def translate(mask, g):
        out = 0
        for i, h in enumerate(group_elems):
            if (mask >> i) & 1:
                out |= 1 << idx[add(g, h)]
        return out

    seen = set()
    orbits = []
    for mask in all_subsets:
        if mask in seen:
            continue
        orb = tuple(sorted({translate(mask, g) for g in group_elems}))
        seen.update(orb)
        orbits.append(orb)
    return sorted(orbits, key=lambda o: (o[0].bit_count(), o))


def invariant_upsets(orbits):
    all_subsets = set().union(*(set(o) for o in orbits))
    ans = []
    for orbit_mask in range(1 << len(orbits)):
        event = set()
        for j, orb in enumerate(orbits):
            if (orbit_mask >> j) & 1:
                event.update(orb)
        is_up = True
        for a in event:
            for b in all_subsets:
                if (a & ~b) == 0 and b not in event:
                    is_up = False
                    break
            if not is_up:
                break
        if is_up:
            ans.append(orbit_mask)
    return ans


# Exact orbit-poset enumeration.
z4 = list(range(4))
z4_orbits = orbit_partition(z4, lambda a, b: (a + b) % 4)
z4_upsets = invariant_upsets(z4_orbits)
expected_z4_orbits = [
    (0,),
    (1, 2, 4, 8),
    (3, 6, 9, 12),
    (5, 10),
    (7, 11, 13, 14),
    (15,),
]
expected_z4_upsets = [0, 32, 48, 52, 56, 60, 62, 63]
assert z4_orbits == expected_z4_orbits
assert z4_upsets == expected_z4_upsets

v4 = [(0, 0), (1, 0), (0, 1), (1, 1)]
v4_orbits = orbit_partition(v4, lambda a, b: (a[0] ^ b[0], a[1] ^ b[1]))
v4_upsets = invariant_upsets(v4_orbits)
expected_v4_orbits = [
    (0,),
    (1, 2, 4, 8),
    (3, 12),
    (5, 10),
    (6, 9),
    (7, 11, 13, 14),
    (15,),
]
expected_v4_upsets = [0, 64, 96, 100, 104, 108, 112, 116, 120, 124, 126, 127]
assert v4_orbits == expected_v4_orbits
assert v4_upsets == expected_v4_upsets

# Exact algebra used in the non-cardinality order-four inequalities.
a, b, c, d, x, y = sp.symbols("a b c d x y")
e3 = a*b*c + a*b*d + a*c*d + b*c*d
T = e3 / 4
D_opp = (a + c)*(b + d) / 4
D_adj = ((a + c)*(b + d) + 2*(a*c + b*d)) / 8
D1 = (a + c)*(b + d) / 4
D2 = (a + b)*(c + d) / 4

# Inclusion-exclusion formulas are retained symbolically.
z4_antipodal_event = sp.expand(2*D_opp - a*b*c*d)
z4_adjacent_event = sp.expand(4*D_adj - 4*T + a*b*c*d)
v4_two_matching_event = sp.expand(2*(D1 + D2) - 4*T + a*b*c*d)

# At the AM-GM boundary A=2u, B=2v, u=x^2, v=y^2, the common
# order-four remainder factors as claimed in the proof.
u = x**2
v = y**2
F_boundary = sp.expand(2*(u-v)**2 - 4*u*v*(u+v-2*x*y))
F_factor = sp.expand(2*(x-y)**2*((x+y)**2 - 2*x**2*y**2))
assert sp.expand(F_boundary - F_factor) == 0

# The derivative lower bounds used to minimize F over A>=2u, B>=2v are
# exact elementary identities/inequalities:
#   B-2v^2 >= 2v-2v^2 = 2v(1-v) >= 0,
#   A-2u^2 >= 2u-2u^2 = 2u(1-u) >= 0,
# for 0<=u,v<=1.  The final factor obeys
#   (x+y)^2 >= 4xy >= 2x^2 y^2 for 0<=x,y<=1.

print("C0036 ORDER-4 EXACT SELF-CHECK")
print("Z4_ORBITS=", z4_orbits)
print("Z4_INVARIANT_UPSETS=", z4_upsets)
print("Z4_INVARIANT_UPSET_COUNT=", len(z4_upsets))
print("V4_ORBITS=", v4_orbits)
print("V4_INVARIANT_UPSETS=", v4_upsets)
print("V4_INVARIANT_UPSET_COUNT=", len(v4_upsets))
print("Z4_ANTIPODAL_EVENT_POLY=", z4_antipodal_event)
print("Z4_ADJACENT_EVENT_POLY=", z4_adjacent_event)
print("V4_TWO_MATCHING_EVENT_POLY=", v4_two_matching_event)
print("COMMON_BOUNDARY_FACTOR_IDENTITY=PASS")
print("ALL_EXACT_CHECKS_PASS")
