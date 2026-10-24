#!/usr/bin/env python3
"""Exact rational post-processing for B18 complementary-MUX address tube.

This is NOT a new read-once certificate. It reuses the completed account02/B12
four-step scalar checker formulas solely to strengthen its certified compact
minimum to > 1/64, then checks the rational constants in the new address-tube
argument. All sign decisions below use fractions.Fraction.
"""
from fractions import Fraction
from functools import lru_cache

C = Fraction(3260925607, 500000000)      # 6.521851214
C0 = Fraction(16137, 2500)               # 6.4548
a = 4 * (C - C0)                         # 0.268204856
B = C / 2 + 2
alpha = 2 * (C0 - 4)                     # 4.9096
K = 4 * B - a
c22 = Fraction(111, 50)
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
    loglo, _ = log2_bounds(Fraction(16)/qlo)
    total = alpha*qlo*loglo + c22*qlo - K*qhi*(1-qhi/Fraction(16))
    for j in range(4):
        scale = 2**j
        zlo = qlo/scale
        zhi = qhi/scale
        hlow, _ = h2_bounds(zlo)
        vlo = V(zlo)
        vhi = V(zhi)
        if vlo <= Fraction(1,2) <= vhi:
            hvup = Fraction(1)
        elif vhi <= Fraction(1,2):
            _, hvup = h2_bounds(vhi)
        else:
            _, hvup = h2_bounds(vlo)
        total += scale*(4*hlow - hvup - 2*zhi*C + 2*zlo*zlo*B)
    return total

# Inherited B12 four-step compact branch, with one NEW quantitative assertion.
min_lower = None
min_cell = None
for k in range(11, 1, -1):
    lo = Fraction(1, 2**k)
    hi = Fraction(1, 2**(k-1))
    step = (hi-lo)/128
    for r in range(128):
        qlo = lo + r*step
        qhi = qlo + step
        lower = cell_lower(qlo, qhi)
        assert lower > 0
        if min_lower is None or lower < min_lower:
            min_lower = lower
            min_cell = (qlo, qhi)

assert min_cell == (Fraction(1,2048), Fraction(129,262144))
assert min_lower > Fraction(1,64)

# Small branch from B12: F(q) >= small_constant*q, q<=2^-11.
small_constant = 15*alpha + c22 - K - 8*C
assert small_constant == Fraction(728423179, 250000000)
assert small_constant > Fraction(1,32)

# Hence globally on 0<q<=1/2: F(q) > q/32.
reserve = Fraction(1,32)

# New B18 address tube: |s|<=q^2/8192.
tube_den = 8192

# Source derivative premise |G'|<31 near x=1 and elementary ln2>2/3.
# If |s|<=1/32768, then x-1<1/1000; thus
# |Gamma_0'| < 2*C0 + 31/1000 + 31*(3/2), plus lift derivative < a.
M_bound = 2*C0 + Fraction(31,1000) + Fraction(93,2) + a
assert M_bound < 60

# Two potential moves cost <=120|s|. Relative to q, q<=1/2:
potential_loss = Fraction(60, tube_den)  # 120*(q/8192), max q=1/2

# TV <= 2|s| <= q^2/4096. Fannes:
# H-loss/q <= (q/4096) log2(61440/q^2), increasing in q<=1/2.
# At q=1/2 this is < (1/8192)*18 = 9/4096 because 245760<2^18.
entropy_loss = Fraction(9,4096)
assert 245760 < 2**18

net = reserve - potential_loss - entropy_loss
assert potential_loss == Fraction(15,2048)
assert net == Fraction(89,4096)
assert net > 0

print("PASS")
print("candidate_C", float(C))
print("compact_min_gt_1_over_64", True)
print("global_midline_reserve", "F(q)>q/32")
print("source_derivative_M_bound_lt_60", True)
print("address_tube", "|t-1/2|<=q^2/8192")
print("potential_loss_over_q_le", f"{potential_loss.numerator}/{potential_loss.denominator}")
print("entropy_loss_over_q_lt", f"{entropy_loss.numerator}/{entropy_loss.denominator}")
print("net_slack_over_q_gt", f"{net.numerator}/{net.denominator}")
print("classification", "exact-rational post-processing plus new analytic tube constants")
