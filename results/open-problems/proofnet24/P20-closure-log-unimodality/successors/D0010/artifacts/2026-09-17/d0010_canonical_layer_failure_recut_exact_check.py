#!/usr/bin/env python3
from fractions import Fraction as Q

# Target law F_* = (5/6) U[0,3/5] + (1/6) U[0,1].
target_low = Q(14,9)
target_high = Q(1,6)

# Basic target checks.
mass = target_low*Q(3,5) + target_high*Q(2,5)
mean = target_low * (Q(1,2)*Q(3,5)**2) + target_high * (Q(1,2)*(Q(1,1)**2-Q(3,5)**2))
assert mass == 1
assert mean == Q(1,3)

# Canonical nested [0,L] layer decomposition weights.
p_short = Q(5,6)
p_long = Q(1,6)
assert p_short/Q(3,5) + p_long/Q(1,1) == target_low
assert p_long == target_high

# No three canonical labels can have midpoint sum 1.
canonical_sums = []
for k in range(4):  # k copies of L=1, 3-k copies of L=3/5
    Lsum = Q(k,1) + Q(3-k,1)*Q(3,5)
    canonical_sums.append(Lsum)
    assert Lsum != 2  # midpoint sum = Lsum/2, so center sum 1 iff Lsum=2

# Alternative nonnested triple components.
# Each affine coordinate is x(u)=a+b*u for u~U[0,1].
triples = [
    # weight, affine maps, expected interval endpoints
    (Q(1,5),
     [(Q(0),Q(1,5)), (Q(0),Q(1,5)), (Q(1),Q(-2,5))],
     [(Q(0),Q(1,5)), (Q(0),Q(1,5)), (Q(3,5),Q(1))]),
    (Q(8,15),
     [(Q(0),Q(1,5)), (Q(3,5),Q(-2,5)), (Q(2,5),Q(1,5))],
     [(Q(0),Q(1,5)), (Q(1,5),Q(3,5)), (Q(2,5),Q(3,5))]),
    (Q(4,15),
     [(Q(1,5),Q(1,5)), (Q(1,5),Q(1,5)), (Q(3,5),Q(-2,5))],
     [(Q(1,5),Q(2,5)), (Q(1,5),Q(2,5)), (Q(1,5),Q(3,5))]),
]
assert sum(w for w,_,_ in triples) == 1

# Verify each affine coupling has sum identically 1 and each coordinate is uniform
# on the claimed interval (nonzero affine slope, endpoints match).
for w, maps, ints in triples:
    assert sum(a for a,b in maps) == 1
    assert sum(b for a,b in maps) == 0
    for (a,b),(lo,hi) in zip(maps,ints):
        assert b != 0
        e0, e1 = a, a+b
        assert min(e0,e1) == lo and max(e0,e1) == hi

# Cyclic symmetrization: each coordinate receives each interval in a triple
# with probability 1/3. Compute exact density on fifth-cells.
cells = [(Q(i,5),Q(i+1,5)) for i in range(5)]
dens = [Q(0) for _ in cells]
for w, maps, ints in triples:
    for lo,hi in ints:
        L = hi-lo
        for r,(c0,c1) in enumerate(cells):
            # All interval endpoints lie on the fifth grid.
            if c0 >= lo and c1 <= hi:
                dens[r] += w * Q(1,3) / L

assert dens[:3] == [target_low]*3
assert dens[3:] == [target_high]*2

print("P20-D0010 canonical-layer failure / recut rescue exact check")
print("target_mass =", mass)
print("target_mean =", mean)
print("canonical_length_sums =", ",".join(str(x) for x in canonical_sums))
print("mixture_weights =", ",".join(str(w) for w,_,_ in triples))
print("fifth_cell_densities =", ",".join(str(x) for x in dens))
print("ALL_EXACT_CHECKS_PASS")
