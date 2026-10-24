#!/usr/bin/env python3
"""Exact combinatorial audit for the source-unit depth-6 reduction.

After fixing the mandatory source weight 1, write the remaining five positive
integer weights as u=(u1,...,u5). Old collisions are homogeneous relations
 eps.u=0. New collisions created by the unit anchor are unit-gap relations
 eps.u=1. This script counts the primitive relation types and S5 orbit keys.
No floating point arithmetic is used.
"""
from itertools import product

N = 5
vecs = list(product((-1, 0, 1), repeat=N))
mixed = [v for v in vecs if 1 in v and -1 in v]

# Homogeneous collision hyperplanes eps.u=0 identify eps and -eps.
def canonical_pm(v):
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    raise ValueError("zero vector")

hom = sorted({canonical_pm(v) for v in mixed})
hom_orbits = sorted({tuple(sorted((v.count(1), v.count(-1)))) for v in hom})

# Oriented mixed unit-gap hyperplanes eps.u=1 do NOT identify eps and -eps,
# because the right-hand side fixes the orientation.
unit_mixed = mixed
unit_mixed_orbits = sorted({(v.count(1), v.count(-1)) for v in unit_mixed})

# One-sided unit-gap equations sum_{i in A} u_i=1 are source-feasible over
# positive integers only when A is a singleton and that coordinate equals 1.
unit_singletons = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
unit_singleton_orbits = {(1, 0)}

assert len(mixed) == 180
assert len(hom) == 90
assert hom_orbits == [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)]
assert len(unit_mixed) == 180
assert unit_mixed_orbits == [
    (1,1),(1,2),(1,3),(1,4),
    (2,1),(2,2),(2,3),
    (3,1),(3,2),(4,1),
]
assert len(unit_singletons) == 5
assert len(hom) + len(unit_mixed) + len(unit_singletons) == 275
assert len(hom_orbits) + len(unit_mixed_orbits) + len(unit_singleton_orbits) == 17

print("EXACT INTEGER AUDIT")
print("dimension_after_anchor=5")
print("homogeneous_collision_hyperplanes=90")
print("homogeneous_S5_orbits=6")
print("homogeneous_orbit_keys=", hom_orbits)
print("oriented_mixed_unit_gap_hyperplanes=180")
print("oriented_mixed_unit_gap_S5_orbits=10")
print("oriented_mixed_unit_gap_orbit_keys=", unit_mixed_orbits)
print("source_feasible_one_sided_unit_gap_hyperplanes=5")
print("source_feasible_one_sided_unit_gap_S5_orbits=1")
print("total_source_anchored_primitive_hyperplanes=275")
print("total_source_anchored_primitive_S5_orbit_types=17")
print("OVERALL PASS")
