#!/usr/bin/env python3
"""Exact rational interval certificate for the B12 complementary-data MUX theorem.

No external packages. All sign decisions use fractions.Fraction. Logarithms
at rational endpoints are enclosed by the positive atanh series after exact
power-of-two scaling to [1,2].
"""
from fractions import Fraction
from functools import lru_cache

C = Fraction(3260925607, 500000000)   # 6.521851214
C0 = Fraction(16137, 2500)            # 6.4548
a = 4 * (C - C0)                      # 0.268204856
B = C / 2 + 2
alpha = 2 * (C0 - 4)                  # 4.9096
K = 4 * B - a
c22 = Fraction(111, 50)               # 2.22
NTERMS = 14

def ln_1_to_2_bounds(z):
    assert 1 <= z <= 2
    y = (z - 1) / (z + 1)
    y2 = y*y
    term = y
    s = Fraction(0)
    for n in range(NTERMS):
        if n:
            term *= y2
        s += term / (2*n + 1)
    s *= 2
    if y == 0:
        return s, s
    rem = 2 * y**(2*NTERMS + 1) / (2*NTERMS + 1) / (1-y*y)
    return s, s + rem

LN2_LO, LN2_HI = ln_1_to_2_bounds(Fraction(2))

@lru_cache(None)
def ln_bounds(x):
    assert x > 0
    z = x
    k = 0
    while z < 1:
        z *= 2
        k -= 1
    while z >= 2:
        z /= 2
        k += 1
    lo, hi = ln_1_to_2_bounds(z)
    if k >= 0:
        return lo + k*LN2_LO, hi + k*LN2_HI
    return lo + k*LN2_HI, hi + k*LN2_LO

@lru_cache(None)
def log2_bounds(x):
    lo, hi = ln_bounds(x)
    return lo/LN2_HI, hi/LN2_LO

@lru_cache(None)
def h2_bounds(x):
    if x == 0 or x == 1:
        return Fraction(0), Fraction(0)
    assert 0 < x < 1
    lxlo, lxhi = ln_bounds(x)
    lylo, lyhi = ln_bounds(1-x)
    nlo = x*(-lxhi) + (1-x)*(-lyhi)
    nhi = x*(-lxlo) + (1-x)*(-lylo)
    return nlo/LN2_HI, nhi/LN2_LO

def V(x):
    return 4*x*(1-x)

def cell_lower(qlo, qhi):
    # T(q)=q[alpha log2(16/q)+2.22-K(1-q/16)].
    # q log2(16/q) is increasing on (0,1/2].
    loglo, _ = log2_bounds(Fraction(16)/qlo)
    total = alpha*qlo*loglo + c22*qlo - K*qhi*(1-qhi/Fraction(16))

    # Sum_{j=0}^3 2^j R(q/2^j).
    for j in range(4):
        scale = 2**j
        zlo = qlo/scale
        zhi = qhi/scale

        # h2(z) increases on [0,1/2].
        hlow, _ = h2_bounds(zlo)

        vlo = V(zlo)
        vhi = V(zhi)
        # V(z) increases on [0,1/2]. h2 rises to 1/2 then falls.
        if vlo <= Fraction(1,2) <= vhi:
            hvup = Fraction(1)
        elif vhi <= Fraction(1,2):
            _, hvup = h2_bounds(vhi)
        else:
            _, hvup = h2_bounds(vlo)

        # R(z)=4h(z)-h(V_z)-2z C+2z^2 B.
        total += scale*(4*hlow - hvup - 2*zhi*C + 2*zlo*zlo*B)
    return total

# Small-q analytic branch.
small_constant = 15*alpha + c22 - K - 8*C
assert small_constant > 0
assert small_constant == Fraction(728423179, 250000000)

# Exact rational interval cover [2^-11,1/2].
cells = 0
min_lower = None
min_cell = None
m = 128
for k in range(11, 1, -1):
    lo = Fraction(1, 2**k)
    hi = Fraction(1, 2**(k-1))
    step = (hi-lo)/m
    for r in range(m):
        qlo = lo + r*step
        qhi = qlo + step
        lower = cell_lower(qlo, qhi)
        assert lower > 0
        cells += 1
        if min_lower is None or lower < min_lower:
            min_lower = lower
            min_cell = (qlo, qhi, k, r)

assert cells == 1280
assert min_cell[0] == Fraction(1,2048)
assert min_cell[1] == Fraction(129,262144)

print("PASS")
print("candidate_C", float(C))
print("quadratic_lift_a", float(a))
print("B=C/2+2", float(B))
print("alpha", float(alpha))
print("K", float(K))
print("small_branch_constant_exact", f"{small_constant.numerator}/{small_constant.denominator}")
print("small_branch_constant_decimal", format(float(small_constant), ".15f"))
print("interval_cells", cells)
print("min_interval_lower_decimal", format(float(min_lower), ".15f"))
print("min_cell_left", f"{min_cell[0].numerator}/{min_cell[0].denominator}")
print("min_cell_right", f"{min_cell[1].numerator}/{min_cell[1].denominator}")
print("ln2_width_upper", format(float(LN2_HI-LN2_LO), ".3e"))
print("classification", "exact-rational sign certificate for scalar four-step lower envelope; source Gamma tail premise imported")
