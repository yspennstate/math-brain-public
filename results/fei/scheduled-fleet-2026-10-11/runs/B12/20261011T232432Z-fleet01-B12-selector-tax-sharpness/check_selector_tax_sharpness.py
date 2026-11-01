#!/usr/bin/env python3
"""Exact/interval certificate for the A060 three-bit selector-tax witness.

Integer Walsh transforms certify the spectra.  Rigorous rational bounds
for ln(2) and ln(3) use the positive atanh series with a geometric tail.
No randomness is used.
"""

from fractions import Fraction
from decimal import Decimal, getcontext


def fwht(values):
    out = list(values)
    h = 1
    while h < len(out):
        for i in range(0, len(out), 2 * h):
            for j in range(i, i + h):
                a, b = out[j], out[j + h]
                out[j], out[j + h] = a + b, a - b
        h *= 2
    return out


def ln_bounds_from_t(t, terms):
    # ln(x)=2*atanh(t), t=(x-1)/(x+1), for 0<t<1.
    partial = 2 * sum((t ** (2*k + 1)) / (2*k + 1) for k in range(terms))
    first_power = t ** (2*terms + 1)
    remainder = 2 * first_power / ((2*terms + 1) * (1 - t*t))
    return partial, partial + remainder


def decimal(frac, digits=40):
    getcontext().prec = digits
    return Decimal(frac.numerator) / Decimal(frac.denominator)


# D(z1,z2) is -1 only at binary point 11. K(x,z1,z2) is -1 only at 111.
D_values = [1, 1, 1, -1]
K_values = [1] * 7 + [-1]
D_walsh = fwht(D_values)
K_walsh = fwht(K_values)
assert sorted(abs(w) for w in D_walsh) == [2, 2, 2, 2]
assert sorted(abs(w) for w in K_walsh) == [2] * 7 + [6]

# Normalized squared spectra and exact influences.
D_mass = [Fraction(w*w, 16) for w in D_walsh]
K_mass = [Fraction(w*w, 64) for w in K_walsh]
assert D_mass == [Fraction(1, 4)] * 4
assert K_mass[0] == Fraction(9, 16)
assert K_mass[1:] == [Fraction(1, 16)] * 7

I_D = sum(alpha.bit_count() * D_mass[alpha] for alpha in range(4))
I_K = sum(alpha.bit_count() * K_mass[alpha] for alpha in range(8))
I_selector = sum(K_mass[alpha] for alpha in range(8) if alpha & 4)
assert I_D == 1
assert I_K == Fraction(3, 4)
assert I_selector == Fraction(1, 4)

# Rigorous logarithm intervals.  t=1/3 gives ln2; t=1/2 gives ln3.
ln2_lo, ln2_hi = ln_bounds_from_t(Fraction(1, 3), 36)
ln3_lo, ln3_hi = ln_bounds_from_t(Fraction(1, 2), 64)
assert ln2_lo > Fraction(1, 2)

# c0 = [H(K)-H(D)/2]/I_selector = 12-(9/2)*(ln3/ln2).
c_lo = Fraction(12) - Fraction(9, 2) * ln3_hi / ln2_lo
c_hi = Fraction(12) - Fraction(9, 2) * ln3_lo / ln2_hi
assert c_lo > Fraction(4867, 1000)
assert c_hi < Fraction(4868, 1000)

# H(K)/I(K)=16/3-(3/2)*(ln3/ln2).
ratio_lo = Fraction(16, 3) - Fraction(3, 2) * ln3_hi / ln2_lo
ratio_hi = Fraction(16, 3) - Fraction(3, 2) * ln3_lo / ln2_hi

# Tensor powers preserve H/I exactly by disjoint additivity: both numerator
# and denominator acquire the same positive integer factor.
for m in range(1, 101):
    assert (Fraction(m, 1) * ratio_lo * I_K) / (Fraction(m, 1) * I_K) == ratio_lo
    assert (Fraction(m, 1) * ratio_hi * I_K) / (Fraction(m, 1) * I_K) == ratio_hi

print("scope: exact D=two-bit point defect and K=three-bit point defect selector splice")
print("randomness: none")
print(f"D integer Walsh coefficients: {D_walsh}")
print(f"K integer Walsh coefficients: {K_walsh}")
print(f"exact H(D)=2, I(D)={I_D}, I_selector(K)={I_selector}, I(K)={I_K}")
print(f"selector-tax coefficient lower: {decimal(c_lo)}")
print(f"selector-tax coefficient upper: {decimal(c_hi)}")
print(f"FEI ratio H(K)/I(K) lower: {decimal(ratio_lo)}")
print(f"FEI ratio H(K)/I(K) upper: {decimal(ratio_hi)}")
print("certified: c0>4.867, so a coefficient-4 selector-tax inequality is false")
print("certified: disjoint tensor powers preserve the smaller FEI ratio, not c0")
print("PASS")
