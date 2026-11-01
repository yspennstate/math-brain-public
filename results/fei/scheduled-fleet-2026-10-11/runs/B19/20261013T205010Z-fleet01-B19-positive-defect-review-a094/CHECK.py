#!/usr/bin/env python3
"""Independent audit of the B05 positive point-defect tower theorem.

The analytic theorem is checked through an exact rational certificate for its
small-margin calculus step.  Finite Walsh reconstructions use integer/Fraction
arithmetic for spectra and influences and 100-digit Decimal only for logs.
This code is independent of the author's checker structure.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from math import exp, log, log2
import random

getcontext().prec = 100
LN2 = Decimal(2).ln()
SEED = 0xB19A094D
rng = random.Random(SEED)
C = Fraction(8, 3)


def exact_scalar_certificate():
    checks = 0

    # e^(3/4): lower Taylor sum through degree 3.
    x = Fraction(3, 4)
    term = Fraction(1)
    low3 = term
    for n in range(1, 4):
        term *= x / n
        low3 += term
    assert low3 == Fraction(269, 128)
    assert low3 > Fraction(7, 4)
    checks += 2

    # Upper Taylor sum through degree 4 plus a geometric tail.  Starting at
    # degree 5, successive ratios are at most 1/8.
    term = Fraction(1)
    partial4 = term
    for n in range(1, 5):
        term *= x / n
        partial4 += term
    term5 = term * x / 5
    exp_upper = partial4 + term5 / (1 - Fraction(1, 8))
    assert exp_upper < Fraction(17, 8)
    checks += 1

    # Exact surrogate bounds for a(0.49) and exact a(0.51).
    # sqrt(51)>7.1 and sqrt(51)<7.2 are checked by squaring.
    assert 51 * 100 > 71 * 71
    assert 51 * 25 < 36 * 36
    a49_upper = Fraction(2401, 1490) / Fraction(71, 10)
    a49_lower = Fraction(2401, 1490) / Fraction(36, 5)
    assert a49_upper < Fraction(23, 100)
    assert Fraction(17, 8) * a49_upper < Fraction(1, 2)
    assert Fraction(7, 4) * a49_lower > Fraction(1, 4)
    checks += 5

    a51 = Fraction(2601, 10570)
    assert low3 * a51 > Fraction(1, 2)
    assert Fraction(17, 8) * a51 < 1
    checks += 2

    # log_2(16/9)>33/40 and ln 2>56/81.
    assert 2**127 > 3**80
    ln2_lower = Fraction(2, 3) + Fraction(2, 81)
    assert ln2_lower == Fraction(56, 81)
    checks += 2

    slope_lower = (Fraction(99, 160) - Fraction(7, 4)
                   - Fraction(81, 448) - Fraction(1, 100))
    assert slope_lower == Fraction(-14807, 11200)
    assert slope_lower > Fraction(-4, 3)
    margin = slope_lower - Fraction(-4, 3)
    assert margin == Fraction(379, 33600)
    checks += 3
    return checks, slope_lower, margin


def fwht_int(values):
    a = list(map(int, values))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a


def caps(probs):
    out = list(probs)
    n = len(out).bit_length() - 1
    for j in range(n):
        b = 1 << j
        for s in range(1 << n):
            if not s & b:
                out[s] += out[s | b]
    return out


def U(values):
    N = len(values)
    w = fwht_int(values)
    p = [Fraction(a * a, N * N) for a in w]
    q = caps(p)
    total = Decimal(0)
    for ps, qs in zip(p, q):
        if not ps:
            continue
        ratio = Decimal(qs.numerator) * Decimal(ps.denominator) / (
            Decimal(qs.denominator) * Decimal(ps.numerator))
        total += (Decimal(ps.numerator) / Decimal(ps.denominator)) * ratio.ln() / LN2
    return total


def influence(values):
    n = len(values).bit_length() - 1
    N = len(values)
    return sum((Fraction(sum(values[x] != values[x ^ (1 << j)] for x in range(N)), N)
                for j in range(n)), Fraction(0))


def mean(values):
    return Fraction(sum(values), len(values))


def tensor(f, g):
    return tuple(f[x] * g[y] for y in range(len(g)) for x in range(len(f)))


def activate(q):
    # Low selector bit: branch 0 is q, branch 1 is +1.
    return tuple(q[x >> 1] if not (x & 1) else 1 for x in range(2 * len(q)))


def point_defect(r):
    return tuple(-1 if x == 0 else 1 for x in range(1 << r))


def restrict(f, coordinate, bit):
    n = len(f).bit_length() - 1
    out = []
    for z in range(1 << (n - 1)):
        lo = z & ((1 << coordinate) - 1)
        hi = z >> coordinate
        out.append(f[lo | (bit << coordinate) | (hi << (coordinate + 1))])
    return tuple(out)


def R(t):
    t = Decimal(t.numerator) / Decimal(t.denominator) if isinstance(t, Fraction) else Decimal(str(t))
    if t == 0:
        u = Decimal(0)
    else:
        u = t * t * (Decimal(1) / (t * t)).ln() / LN2
    xp, xm = (1 + t) / 2, (1 - t) / 2
    e1 = xp * xp * (Decimal(1) / (xp * xp)).ln() / LN2 if xp else Decimal(0)
    e2 = xm * xm * (Decimal(1) / xm).ln() / LN2 if xm else Decimal(0)
    return e1 + e2 - u / 2 + (1 - t * t) / 4


def point_stats(r):
    p = Fraction(1, 1 << r)
    beta = 1 - 2 * p
    iq = 2 * r * p
    b = Decimal(beta.numerator) / Decimal(beta.denominator)
    uq = b * b * (Decimal(1) / (b * b)).ln() / LN2
    uq += Decimal((2 * r * p * beta).numerator) / Decimal((2 * r * p * beta).denominator)
    return beta, uq, iq


def tower(base, ranks):
    out = [activate(tensor((-1, 1), base))]
    for r in ranks:
        out.append(activate(tensor(point_defect(r), out[-1])))
    return out


def leaf_average(f, depth):
    if depth == 0 or len(f) == 1 or rng.random() < 0.31:
        return U(f), 1
    j = rng.randrange(len(f).bit_length() - 1)
    a, na = leaf_average(restrict(f, j, 0), depth - 1)
    b, nb = leaf_average(restrict(f, j, 1), depth - 1)
    return (a + b) / 2, na + nb


exact_checks, slope_bound, slope_margin = exact_scalar_certificate()

# Independent scalar diagnostics over the whole interval.
scalar_grid = 0
min_slope = (1e9, None)
max_scaled_R = (-1e9, None)
for j in range(1, 100000):
    t = j / 100000
    rp = ((1 + t) / 2 * log2(4 / (1 + t) ** 2)
          - (1 - t) / 2 * log2(2 / (1 - t))
          - t * log2(1 / t ** 2) - (1 - t) / (4 * log(2)) - t / 2)
    rv = float(R(Fraction(j, 100000)))
    min_slope = min(min_slope, (rp, t))
    max_scaled_R = max(max_scaled_R, (rv / (1 - t), t))
    assert rp > -4 / 3
    assert rv <= 4 * (1 - t) / 3 + 1e-13
    scalar_grid += 2

# Point-defect formulas, including direct Walsh reconstruction for small ranks.
point_checks = 0
max_point_ratio = (Decimal(0), None)
for r in range(2, 257):
    beta, uq, iq = point_stats(r)
    ratio = uq / (Decimal(iq.numerator) / Decimal(iq.denominator))
    if ratio > max_point_ratio[0]:
        max_point_ratio = (ratio, r)
    assert uq <= 2 * (Decimal(iq.numerator) / Decimal(iq.denominator))
    if r <= 9:
        q = point_defect(r)
        assert abs(U(q) - uq) < Decimal("1e-90")
        assert influence(q) == iq
        assert mean(q) == beta
        point_checks += 3
    point_checks += 1

bases = []
for n in range(3):
    for mask in range(1 << (1 << n)):
        bases.append(tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n)))
for _ in range(40):
    bases.append(tuple(rng.choice((-1, 1)) for _ in range(8)))

direct_checks = recurrence_checks = endpoint_checks = 0
max_recurrence_error = Decimal(0)
saved_towers = []
for base in bases:
    n = len(base).bit_length() - 1
    sequences = [(), (2,), (3,), (4,), (2, 2), (2, 3), (3, 2)] if n <= 2 else [(), (2,), (3,), (2, 2)]
    ub, ib = U(base), influence(base)
    for seq in sequences:
        layers = tower(base, seq)
        prev = None
        for d, f in enumerate(layers, 1):
            uf, inf = U(f), influence(f)
            direct_checks += 1
            if d == 1:
                eu = Decimal(1) + ub / 2
                ei = Fraction(1) + ib / 2
            else:
                r = seq[d - 2]
                beta, uq, iq = point_stats(r)
                t = beta * mean(prev)
                eu = U(prev) / 2 + uq / 2 + R(t)
                ei = influence(prev) / 2 + iq / 2 + (1 - t) / 2
            err = abs(uf - eu)
            max_recurrence_error = max(max_recurrence_error, err)
            assert err < Decimal("1e-88")
            assert inf == ei
            recurrence_checks += 2
            if ub <= Decimal(C.numerator) / Decimal(C.denominator) * Decimal(ib.numerator) / Decimal(ib.denominator):
                assert uf <= Decimal(C.numerator) / Decimal(C.denominator) * Decimal(inf.numerator) / Decimal(inf.denominator) + Decimal("1e-88")
                endpoint_checks += 1
            prev = f
        if len(layers[-1]) <= 4096:
            saved_towers.append(layers[-1])

# Long nonstationary sequences, with ranks selected independently through 128.
state_checks = 0
for base in bases:
    u = Decimal(1) + U(base) / 2
    i = Fraction(1) + influence(base) / 2
    m = Fraction(1, 2)
    for _ in range(300):
        r = rng.randint(2, 128)
        beta, uq, iq = point_stats(r)
        t = beta * m
        u = u / 2 + uq / 2 + R(t)
        i = i / 2 + iq / 2 + (1 - t) / 2
        m = (1 + t) / 2
        assert u <= Decimal(C.numerator) / Decimal(C.denominator) * Decimal(i.numerator) / Decimal(i.denominator) + Decimal("1e-85")
        state_checks += 1

# Independent pruned-tree and common-terminal-factor checks.
tree_checks = tensor_checks = leaves_seen = 0
cores = [(-1,), (-1, 1), (-1, -1, -1, 1), (-1, 1, 1, -1)]
for f in saved_towers[:100]:
    ci = Decimal(C.numerator) / Decimal(C.denominator) * Decimal(influence(f).numerator) / Decimal(influence(f).denominator)
    for _ in range(4):
        leaves_u, nl = leaf_average(f, 4)
        assert U(f) - leaves_u <= ci + Decimal("1e-85")
        leaves_seen += nl
        tree_checks += 1
    for h in cores:
        leaf_u, _ = leaf_average(f, 3)
        root = U(tensor(f, h))
        assert abs(root - U(f) - U(h)) < Decimal("1e-88")
        assert abs((root - leaf_u - U(h)) - (U(f) - leaf_u)) < Decimal("1e-88")
        tensor_checks += 2

print(f"seed={SEED}")
print(f"exact_scalar_certificate_checks={exact_checks}")
print(f"slope_lower_bound={slope_bound} margin_over_minus_4_3={slope_margin}")
print(f"scalar_grid_checks={scalar_grid} min_slope={min_slope}")
print(f"max_R_over_one_minus_t={max_scaled_R}")
print(f"point_defect_checks={point_checks} max_ratio=({max_point_ratio[0]}, rank={max_point_ratio[1]})")
print(f"direct_tower_checks={direct_checks}")
print(f"recurrence_checks={recurrence_checks} endpoint_checks={endpoint_checks}")
print(f"long_nonstationary_checks={state_checks}")
print(f"pruned_tree_checks={tree_checks} leaves_seen={leaves_seen}")
print(f"tensor_identity_checks={tensor_checks}")
print(f"max_recurrence_error={max_recurrence_error}")
print("formal_verdict=ACCEPT_AT_STATED_THEOREM_SCOPE")
print("a023_first_revelation_credit=NOT_ESTABLISHED")
print("full_fei=OPEN")
print("PASS")
