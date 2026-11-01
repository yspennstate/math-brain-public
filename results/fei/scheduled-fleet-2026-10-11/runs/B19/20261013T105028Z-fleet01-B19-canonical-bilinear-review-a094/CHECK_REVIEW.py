#!/usr/bin/env python3
"""Independent B19 reconstruction of the canonical-root claim and scope test.

The finite countercertificate uses exact Walsh probabilities and rational
outward intervals for every logarithm; it does not import the author's
checker.
"""

from fractions import Fraction
from functools import lru_cache
from math import comb, log2


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for base in range(0, len(a), 2 * h):
            for j in range(base, base + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a


def truth_matrix(rows, avec=0, bvec=0):
    r = len(rows)
    out = []
    for mask in range(1 << (2 * r)):
        x = mask & ((1 << r) - 1)
        y = mask >> r
        bilinear = sum(((x >> i) & 1) * ((rows[i] & y).bit_count() & 1)
                       for i in range(r))
        exponent = (bilinear + (avec & x).bit_count()
                    + (bvec & y).bit_count() + int(y == 0)) & 1
        out.append(1 if exponent == 0 else -1)
    return out


def restrict(values, coordinate, bit):
    n = len(values).bit_length() - 1
    ans = []
    for short in range(1 << (n - 1)):
        low = short & ((1 << coordinate) - 1)
        high = short >> coordinate
        full = low | (bit << coordinate) | (high << (coordinate + 1))
        ans.append(values[full])
    return ans


def spectral_probabilities(values):
    npoints = len(values)
    return [Fraction(w * w, npoints * npoints) for w in fwht(values)]


def upper_caps(p):
    q = list(p)
    n = len(p).bit_length() - 1
    for i in range(n):
        for s in range(1 << n):
            if not ((s >> i) & 1):
                q[s] += q[s | (1 << i)]
    return q


def upper_u_float(values):
    p = spectral_probabilities(values)
    cap = upper_caps(p)
    return sum(float(ps) * log2(float(cap[s] / ps))
               for s, ps in enumerate(p) if ps)


def influence(values, coordinate):
    n = len(values).bit_length() - 1
    disagree = sum(values[x] != values[x ^ (1 << coordinate)]
                   for x in range(1 << n))
    return Fraction(disagree, 1 << n)


@lru_cache(None)
def ln_interval(x, target_bits=220):
    """Rational outward interval for ln(x), for rational x >= 1."""
    assert x >= 1
    if x == 1:
        return Fraction(0), Fraction(0)
    z = (x - 1) / (x + 1)
    z2 = z * z
    total = Fraction(0)
    power = z
    k = 0
    target = Fraction(1, 1 << target_bits)
    while True:
        total += power / (2 * k + 1)
        next_power = power * z2
        # Tail <= next_power/(2k+3) * 1/(1-z^2).
        tail = next_power / (2 * k + 3) / (1 - z2)
        if 2 * tail < target:
            return 2 * total, 2 * (total + tail)
        power = next_power
        k += 1


LN2 = ln_interval(Fraction(2))


@lru_cache(None)
def log2_interval(x):
    lo, hi = ln_interval(x)
    # All quantities are nonnegative, so these quotient corners are outward.
    return lo / LN2[1], hi / LN2[0]


def upper_u_interval(values):
    p = spectral_probabilities(values)
    cap = upper_caps(p)
    lo = Fraction(0)
    hi = Fraction(0)
    for s, ps in enumerate(p):
        if not ps:
            continue
        ell, ehi = log2_interval(cap[s] / ps)
        lo += ps * ell
        hi += ps * ehi
    return lo, hi


def frac_decimal(x, digits=24):
    scale = 10 ** digits
    q = (x.numerator * scale) // x.denominator
    return f"{q // scale}.{q % scale:0{digits}d}"


def cap_scalar(d, h):
    return d - h - sum(comb(h, j) * log2(1 - 2 ** (-(d - j)))
                       for j in range(h))


checks = 0
max_canonical = (-1.0, None)

# Independent full truth-table reconstruction of every canonical affine
# orientation through rank four.
for r in range(1, 5):
    rows = tuple(1 << i for i in range(r))
    for avec in range(1 << r):
        for bvec in range(1 << r):
            f = truth_matrix(rows, avec, bvec)
            p = spectral_probabilities(f)
            assert all(q == Fraction(1, 1 << (2 * r)) for q in p)
            checks += 1
            infs = [influence(f, i) for i in range(2 * r)]
            assert all(q == Fraction(1, 2) for q in infs)
            checks += 2 * r
            root_u = upper_u_float(f)
            assert abs(root_u - r) < 2e-12
            charges = []
            for i in range(2 * r):
                child_mean = sum(upper_u_float(restrict(f, i, b))
                                 for b in (0, 1)) / 2
                delta = root_u - child_mean
                charges.append(delta)
                if i < r:
                    d = r - 1
                    h = avec.bit_count() - ((avec >> i) & 1)
                    formula = 1 + cap_scalar(d, h) / (2 ** r)
                    assert abs(delta - formula) < 4e-12
                    assert delta <= 1.5 + 4e-12
                else:
                    assert abs(delta - 1) < 4e-12
                checks += 2
            ratio = sum(charges) / float(sum(infs))
            assert ratio <= 2.5 + 4e-12
            checks += 1
            max_canonical = max(max_canonical, (ratio, (r, avec, bvec)))

# Check the scalar inequality separately well beyond the truth-table range.
for d in range(257):
    for h in range(d + 1):
        c = cap_scalar(d, h)
        assert -1e-12 <= c <= 2 ** d + 1e-10 * max(1, 2 ** d)
        checks += 1

# Scope falsifier: an invertible, non-monomial 3x3 bilinear matrix.
rows = (0b111, 0b101, 0b011)
f = truth_matrix(rows, avec=0b111, bvec=0)
root_lo, root_hi = upper_u_interval(f)
root_p = spectral_probabilities(f)
assert all(q == Fraction(1, 64) for q in root_p)
infs = [influence(f, i) for i in range(6)]
total_i = sum(infs)
assert total_i == 3
g_lo = Fraction(0)
g_hi = Fraction(0)
child_intervals = []
for i in range(6):
    u0 = upper_u_interval(restrict(f, i, 0))
    u1 = upper_u_interval(restrict(f, i, 1))
    child_intervals.append((u0, u1))
    # Correct signed interval subtraction.
    g_lo += root_lo - (u0[1] + u1[1]) / 2
    g_hi += root_hi - (u0[0] + u1[0]) / 2

margin_lo = g_lo - Fraction(5, 2) * total_i
margin_hi = g_hi - Fraction(5, 2) * total_i
assert margin_lo > Fraction(627, 1000)
checks += 4

print(f"PASS independent_checks={checks}")
print(f"canonical_max_G_over_I={max_canonical[0]:.15f} at r,a,b={max_canonical[1]}")
print("canonical_scope=all affine orientations through rank 4; scalar d<=256")
print("scope_falsifier_rows=[0b111,0b101,0b011] a=0b111 b=0")
print(f"scope_falsifier_I={total_i}")
print(f"scope_falsifier_G_interval=[{frac_decimal(g_lo)}, {frac_decimal(g_hi)}]")
print(f"scope_falsifier_G_over_I_interval=[{frac_decimal(g_lo/total_i)}, {frac_decimal(g_hi/total_i)}]")
print(f"scope_falsifier_G_minus_5I_over_2_interval=[{frac_decimal(margin_lo)}, {frac_decimal(margin_hi)}]")
print("scope_falsifier_certificate=RIGOROUS_RATIONAL_OUTWARD_INTERVAL")
