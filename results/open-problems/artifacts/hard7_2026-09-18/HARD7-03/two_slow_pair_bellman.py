from fractions import Fraction as F
from itertools import product

states = list(product(range(3), repeat=2))
c = F(1, 2)
lam = F(71, 219)

# Potential for the controlled two-site block.  State (i,j) means occupancies
# of two consecutive slow K=2 sites.  Left injection intensity may be any
# u in [0,1], the internal jump has rate c=1/2 when allowed, and the right
# exit intensity may be any v in [0,c].
h = {
    (0, 0): F(0),
    (0, 1): F(179, 219),
    (0, 2): F(98, 73),
    (1, 0): F(71, 219),
    (1, 1): F(230, 219),
    (1, 2): F(313, 219),
    (2, 0): F(88, 219),
    (2, 1): F(239, 219),
    (2, 2): F(316, 219),
}

# Stationary law of the extremal open block with maximal injection u=1
# whenever i<2 and maximal exit v=1/2 whenever j>0.
p = {
    (0, 0): F(1, 73),
    (0, 1): F(2, 73),
    (0, 2): F(8, 219),
    (1, 0): F(10, 219),
    (1, 1): F(8, 73),
    (1, 2): F(20, 219),
    (2, 0): F(64, 219),
    (2, 1): F(44, 219),
    (2, 2): F(40, 219),
}


def maximal_transitions(s):
    i, j = s
    out = []
    if i < 2:
        out.append(((i + 1, j), F(1)))
    if i > 0 and j < 2:
        out.append(((i - 1, j + 1), c))
    if j > 0:
        out.append(((i, j - 1), c))
    return out


print("HARD7-03 exact two-slow-site controlled-current certificate")
print(f"lambda={lam}")
print(f"sum_p={sum(p.values())}")
assert sum(p.values()) == 1

balance = {s: F(0) for s in states}
for s in states:
    for t, rate in maximal_transitions(s):
        balance[s] -= p[s] * rate
        balance[t] += p[s] * rate

print("stationary_balance:")
for s in states:
    print(f"  {s}: {balance[s]}")
assert all(v == 0 for v in balance.values())

J = sum(p[s] * c for s in states if s[1] > 0)
print(f"maximal_reservoir_exit_current={J}")
assert J == lam

print("bellman_coefficients:")
for s in states:
    i, j = s
    internal = F(0)
    if i > 0 and j < 2:
        internal = c * (h[(i - 1, j + 1)] - h[s])

    inj_coeff = None
    if i < 2:
        inj_coeff = h[(i + 1, j)] - h[s]
        assert inj_coeff >= 0

    exit_coeff = None
    if j > 0:
        # The +1 is the unit reward for a counted exit.
        exit_coeff = F(1) + h[(i, j - 1)] - h[s]
        assert exit_coeff >= 0

    maximal = internal
    if inj_coeff is not None:
        maximal += inj_coeff
    if exit_coeff is not None:
        maximal += c * exit_coeff
    assert maximal == lam

    print(
        f"  {s}: internal={internal}, inj_coeff={inj_coeff}, "
        f"exit_coeff={exit_coeff}, max={maximal}"
    )

    # Since the dependence on each boundary intensity is affine, endpoint
    # verification plus the nonnegative coefficients certifies every
    # u in [0,1] and v in [0,1/2].
    us = [F(0)] if i == 2 else [F(0), F(1)]
    vs = [F(0)] if j == 0 else [F(0), c]
    for u in us:
        for v in vs:
            value = internal
            if inj_coeff is not None:
                value += u * inj_coeff
            if exit_coeff is not None:
                value += v * exit_coeff
            assert value <= lam

print(f"potential_min={min(h.values())}")
print(f"potential_max={max(h.values())}")
print(
    "finite_time_consequence: E[N_exit(t)] <= (71/219)t + h(X_0) "
    "<= (71/219)t + 316/219"
)
print("ALL_EXACT_CHECKS_PASS")
