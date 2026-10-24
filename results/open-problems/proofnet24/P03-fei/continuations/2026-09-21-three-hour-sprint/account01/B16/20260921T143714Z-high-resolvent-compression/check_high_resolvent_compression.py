from fractions import Fraction
import math
import random


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


# Exact coefficient check of (x+2)^3 - 27x = (x-1)^2(x+8).
lhs = [8, -15, 6, 1]
rhs = poly_mul([1, -2, 1], [8, 1])
assert lhs == rhs


def delta_series(p, R=100):
    return sum(
        ((-1) ** r) * (1 - sum(x ** r for x in p)) / ((r - 1) * 2 ** (r - 1))
        for r in range(2, R + 1)
    )


def delta_closed(p):
    return sum(x * math.log(3 / (2 + x)) for x in p if x > 0)


def entropy_nat(p):
    return -sum(x * math.log(x) for x in p if x > 0)


def c2(p):
    return 1 - sum(x * x for x in p)


tests = [
    [1.0],
    [0.5, 0.5],
    [0.75, 0.25],
    [0.9, 0.05, 0.05],
    [0.97] + [0.03 / 15] * 15,
]

rng = random.Random(20260921)
for n in range(2, 33):
    for _ in range(80):
        a = [rng.expovariate(1) for _ in range(n)]
        s = sum(a)
        tests.append([x / s for x in a])

maxerr = 0.0
worst_inf = 0.0
worst_ent = 0.0
for p in tests:
    ds = delta_series(p)
    dc = delta_closed(p)
    maxerr = max(maxerr, abs(ds - dc))
    influence_envelope = math.log(1.5) * c2(p)
    entropy_envelope = entropy_nat(p) / 3
    assert dc <= influence_envelope + 5e-14, (p, dc, influence_envelope)
    assert dc <= entropy_envelope + 5e-14, (p, dc, entropy_envelope)
    if c2(p) > 1e-15:
        worst_inf = max(worst_inf, dc / influence_envelope if influence_envelope else 0.0)
    if entropy_nat(p) > 1e-15:
        worst_ent = max(worst_ent, dc / entropy_envelope if entropy_envelope else 0.0)

kappa = 2 / 3 + math.atanh(0.5)
floor_inf = kappa - 2 * math.log(1.5)
floor_d3 = floor_inf - 2 ** (3 - 2 ** 3)

print("PASS")
print("probability_vectors", len(tests))
print("max_series_closed_error", repr(maxerr))
print("worst_delta_over_ln15_C2", repr(worst_inf))
print("worst_delta_over_H_over3", repr(worst_ent))
print("two_ln_3_over_2", repr(2 * math.log(1.5)))
print("bank_floor_limit", repr(floor_inf))
print("bank_floor_d3", repr(floor_d3))
