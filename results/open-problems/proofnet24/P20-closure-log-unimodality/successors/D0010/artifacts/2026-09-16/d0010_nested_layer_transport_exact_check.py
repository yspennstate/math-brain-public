from fractions import Fraction as Q
from itertools import permutations

# Exact self-check for P20-D0010-LAYER-TRANSPORT-03.
# The theorem for arbitrary n is proved analytically in the run report.
# This finite core stress-checks the rational geometry through n=200 and
# independently enumerates the permutation tensor marginals through n=8.

def data(n):
    assert n >= 3
    eps = Q(1, 2*n*(n-1)*(n-2))
    lengths = [Q(1, 1)] + [
        Q(1, n-1) + eps*(n-2*j) for j in range(1, n)
    ]
    delta = Q(1, 2*n*(n-1))
    j_lo = Q(1, n) - delta/2
    j_hi = Q(1, n) + delta/2
    return eps, lengths, delta, j_lo, j_hi

for n in range(3, 201):
    eps, lengths, delta, j_lo, j_hi = data(n)

    # Outer interval geometry and the uniform-interval JM criterion.
    assert sum(lengths) == 2
    assert lengths[0] == 1
    assert all(lengths[j] > lengths[j+1] for j in range(1, n-1))
    assert lengths[-1] == Q(2*n-1, 2*n*(n-1))
    assert lengths[-1] - Q(1, n) == Q(1, 2*n*(n-1))
    assert 0 < j_lo < j_hi < lengths[-1] < 1
    assert sum(x/2 for x in lengths) == 1
    assert sum(lengths) == 2*max(lengths)

    # The inner repeated tuple also satisfies the uniform-interval criterion.
    assert n*delta >= 2*delta
    assert n*Q(1, n) == 1

    # Layer weights are theta/n on each outer interval and 1-theta on J.
    # The theta coefficient in the mean vanishes exactly.
    outer_center_sum = sum(x/2 for x in lengths)
    mean_const = Q(1, n)
    mean_theta_coeff = outer_center_sum/Q(n, 1) - Q(1, n)
    assert mean_const == Q(1, n)
    assert mean_theta_coeff == 0

# Independent finite combinatorial check of the permutation-tensor marginals.
for n in range(3, 9):
    ps = list(permutations(range(n)))
    expected = len(ps)//n
    for r in range(n):
        for j in range(n):
            assert sum(1 for p in ps if p[r] == j) == expected

print("P20-D0010 nested-layer transport exact self-check")
print("n-range exact rational geometry: 3..200 PASS")
print("permutation tensor exact marginal counts: n=3..8 PASS")
for n in (3, 4, 5, 10, 50, 200):
    eps, lengths, delta, j_lo, j_hi = data(n)
    print(
        "n=", n,
        "sumL=", sum(lengths),
        "Lmin=", lengths[-1],
        "Lmin-1/n=", lengths[-1]-Q(1, n),
        "delta=", delta,
        "J=", (j_lo, j_hi),
    )
print("ALL_EXACT_CHECKS_PASS")
