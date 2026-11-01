#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter

M = 7
N = 1 << (2*M)

def tribes_truth():
    out = []
    for x in range(N):
        hit = False
        for b in range(M):
            if ((x >> (2*b)) & 3) == 3:
                hit = True
                break
        out.append(1 if hit else -1)
    return out

def fwht_int(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def pow2_frac(k):
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))

def floor_log2_frac(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if pow2_frac(k) > x:
        k -= 1
    while pow2_frac(k+1) <= x:
        k += 1
    return k

def ln_interval_unit(y, terms=48):
    assert Fraction(1) <= y <= Fraction(2)
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zpow = z
    s = Fraction(0)
    for j in range(terms):
        s += zpow / (2*j+1)
        zpow *= z2
    lo = 2*s
    # positive tail bounded geometrically
    hi = lo + 2*zpow / ((2*terms+1)*(1-z2))
    return lo, hi

LN2_LO, LN2_HI = ln_interval_unit(Fraction(2), 64)

def log2_interval(x, terms=48):
    assert x > 0
    if x < 1:
        lo, hi = log2_interval(1/x, terms)
        return -hi, -lo
    k = floor_log2_frac(x)
    y = x / pow2_frac(k)
    assert 1 <= y < 2
    llo, lhi = ln_interval_unit(y, terms)
    return Fraction(k) + llo/LN2_HI, Fraction(k) + lhi/LN2_LO

W = fwht_int(tribes_truth())
assert sum(w*w for w in W) == N*N
counts = Counter(abs(w) for w in W if w)
expected = {
    12010: 1,
    1458: 21,
    486: 189,
    162: 945,
    54: 2835,
    18: 5103,
    6: 5103,
    2: 2187,
}
assert counts == expected

den = N*N
pnum = [w*w for w in W]

# Folded influence; every coordinate is symmetric and below 1/2.
inf0 = Fraction(sum(pnum[s] for s in range(N) if s & 1), den)
assert inf0 == Fraction(729, 8192)
J = 14*inf0
assert J == Fraction(5103,4096)

# Entropy interval from exact spectral groups.
Hlo = Fraction(0)
Hhi = Fraction(0)
for w, count in counts.items():
    mass = Fraction(count*w*w, den)
    lo, hi = log2_interval(Fraction(den, w*w))
    Hlo += mass*lo
    Hhi += mass*hi

# Zero-shift and singleton self-XOR data.
c0 = Fraction(sum(x*x for x in pnum), den*den)
ci = Fraction(sum(pnum[s]*pnum[s ^ 1] for s in range(N)), den*den)
Ai = Fraction(sum(abs(W[s]*W[s ^ 1]) for s in range(N)), den)
c1 = 14*ci

assert c0 == Fraction(79770364087,274877906944)
assert ci == Fraction(2457872343,274877906944)
assert Ai == Fraction(7363629,16777216)
assert Ai/ci == Fraction(165494784,3371567)

L0lo, L0hi = log2_interval(1/c0)
L1lo, L1hi = log2_interval(Ai/ci)

# For F = g^{\otimes 3}, exact tensor formulas:
# b0(F)/3 = c0^3 log2(1/c0)
# sum_singletons b_e(F)/3
#   = c0^2 * c1 * [log2(Ai/ci) + 2 log2(1/c0)].
# Hence R_*(F)/(3J(g)) = [H(g) - ...]/J(g).
Rper_lo = (
    Hlo
    - c0**3 * L0hi
    - c0**2 * c1 * (L1hi + 2*L0hi)
)
Rper_hi = (
    Hhi
    - c0**3 * L0lo
    - c0**2 * c1 * (L1lo + 2*L0lo)
)
ratio_lo = Rper_lo / J
ratio_hi = Rper_hi / J

assert ratio_lo > Fraction(65,16)  # 4.0625
assert ratio_lo > 4

print("PASS")
print("seed=width-2 tribes with 7 blocks (14 variables)")
print("walsh_abs_counts=", dict(sorted(counts.items(), reverse=True)))
print("J_seed_exact=", J)
print("H_seed_interval=[%.15f, %.15f]" % (float(Hlo), float(Hhi)))
print("H_seed_over_J_interval=[%.15f, %.15f]" % (float(Hlo/J), float(Hhi/J)))
print("c0_exact=", c0)
print("ci_exact=", ci)
print("Ai_exact=", Ai)
print("Ai_over_ci_exact=", Ai/ci)
print("Rstar_tensor_cube_over_J_interval=[%.15f, %.15f]" % (float(ratio_lo), float(ratio_hi)))
print("certified_strict_lower_bound=65/16=%.10f" % float(Fraction(65,16)))
print("Therefore R_*(g^{tensor 3}) > 4 J(g^{tensor 3}).")
print("Since R_* <= T2, T2(g^{tensor 3}) > 4 J(g^{tensor 3}) as well.")
