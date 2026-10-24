#!/usr/bin/env python3
from fractions import Fraction as Q

# D0008 exact self-check for the source-valid n=3 checkpoint
# P_* = (2/5) Unif[-1,-1/2] + (3/5) Unif[-1,2].
# Its density is 1 on [-1,-1/2] and 1/5 on (-1/2,2].

cells = [
    (Q(-1), Q(-1,2)),
    (Q(-1,2), Q(0)),
    (Q(0), Q(1,2)),
    (Q(1,2), Q(1)),
    (Q(1), Q(3,2)),
    (Q(3,2), Q(2)),
]
target = [Q(1), Q(1,5), Q(1,5), Q(1,5), Q(1,5), Q(1,5)]

# Each segment is t -> (1-t)A+tB, t~Unif[0,1], then a uniform
# random permutation of the coordinates is applied.
segments = [
    ("S0", Q(3,5), (Q(-1),Q(-1),Q(2)), (Q(-1,2),Q(-1,2),Q(1))),
    ("S1", Q(3,10), (Q(-1),Q(0),Q(1)), (Q(1,2),Q(-1),Q(1,2))),
    ("S2", Q(1,10), (Q(-1),Q(1,2),Q(1,2)), (Q(0),Q(0),Q(0))),
]

def projection_density(A,B):
    out = [Q(0) for _ in cells]
    for i in range(3):
        assert A[i] != B[i]
        lo, hi = min(A[i],B[i]), max(A[i],B[i])
        length = hi-lo
        for j,(c0,c1) in enumerate(cells):
            if c0 >= lo and c1 <= hi:
                out[j] += Q(1,3)/length
    return out

assert sum(w for _,w,_,_ in segments) == 1
mixture = [Q(0) for _ in cells]
for name,w,A,B in segments:
    assert sum(A) == 0
    assert sum(B) == 0
    d = projection_density(A,B)
    mass = sum(d[j]*(cells[j][1]-cells[j][0]) for j in range(len(cells)))
    assert mass == 1
    print(name, "weight", w, "projection_density", *d)
    for j in range(len(cells)):
        mixture[j] += w*d[j]

assert mixture == target
assert sum(target[j]*(cells[j][1]-cells[j][0]) for j in range(len(cells))) == 1
mean = sum(
    target[j]*(cells[j][1]**2-cells[j][0]**2)/2
    for j in range(len(cells))
)
assert mean == 0

# Verify the stated mixture-of-uniforms representation of P_* exactly.
# (2/5)U[-1,-1/2] contributes density 4/5 on the first cell;
# (3/5)U[-1,2] contributes density 1/5 on every half-unit cell.
assert Q(2,5) / Q(1,2) + Q(3,5) / Q(3) == 1
assert Q(3,5) / Q(3) == Q(1,5)

print("mixture_density", *mixture)
print("target_mean", mean)
print("weights_sum", sum(w for _,w,_,_ in segments))
print("D0008 P-STAR THREE-SEGMENT EXACT CHECK PASSED")
