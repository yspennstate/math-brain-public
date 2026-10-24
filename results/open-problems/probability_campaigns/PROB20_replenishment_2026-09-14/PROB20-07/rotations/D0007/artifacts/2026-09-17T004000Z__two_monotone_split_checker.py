#!/usr/bin/env python3
"""Exact rational certificate for D0007's two-monotone-split obstruction at n=28857.

All decisive comparisons use fractions.Fraction and exact integer powers.
No floating point is used in assertions.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

E = 20001
n = 28857
q = (n - 1) // 2
assert n == 2*q + 1

a = Fraction(q, n)
mu = Fraction(1, E + 1)
mu_minus = Fraction(n*mu - 1, n - 1)
mu_plus = Fraction(n*mu + 1, n + 1)

# Exact identity: Wang-Wang decreasing-density mean condition for the
# majority deficiency law on [s,1] is equivalent to s <= mu_minus.
# At s=mu_minus it holds with equality.
s = mu_minus
rhs_majority_at_s = s + (1 - s) / (q + 1)
assert mu_plus == rhs_majority_at_s

# Rational test point below the true extremal-layer cutoff t(s).
r = Fraction(7, 100000)
assert s < r < 1

def G(z):
    """Target deficiency CDF for Beta(1,E): 1-(1-z)^E."""
    return 1 - (1-z)**E

def g(z):
    """Target deficiency density: E(1-z)^(E-1)."""
    return E * (1-z)**(E-1)

def M1(z):
    """Exact truncated first moment integral_0^z u g(u) du."""
    A = 1-z
    return Fraction(1, E+1) - A**E + Fraction(E, E+1)*A**(E+1)

def A_ext(s0, t):
    """Mass of the extremal decreasing minority subdensity through layer t."""
    return G(t) - (t-s0)*g(t)

def M_ext(s0, t):
    """First moment of that extremal subdensity through layer t."""
    return M1(t) - g(t)*(t*t-s0*s0)/2

A_r = A_ext(s, r)
M_r = M_ext(s, r)
target_mass = a
target_moment = a * mu_minus

# Since A_ext(s,t) is strictly increasing in t>s, A_r<a proves the
# true cutoff t(s) lies to the right of r.
assert A_r < target_mass

# Since M_ext(s,t) is strictly increasing in t>s, this exact inequality
# proves the minimum possible minority first moment at mass a is already
# above the required a*mu_minus.
assert M_r > target_moment

getcontext().prec = 40
def dec(fr):
    return Decimal(fr.numerator) / Decimal(fr.denominator)

print("D0007 exact two-monotone-split obstruction certificate")
print(f"E={E}; n={n}; q={q}")
print(f"a=q/n={dec(a)}")
print(f"mu_minus={dec(mu_minus)}")
print(f"mu_plus={dec(mu_plus)}")
print(f"r={dec(r)}")
print(f"A_ext(s,r)-a={dec(A_r-target_mass)}")
print(f"M_ext(s,r)-a*mu_minus={dec(M_r-target_moment)}")
print(f"A comparison numerator sign={-1 if (A_r-target_mass).numerator < 0 else 1}")
print(f"M comparison numerator sign={1 if (M_r-target_moment).numerator > 0 else -1}")
print(f"|A comparison numerator| bit_length={abs((A_r-target_mass).numerator).bit_length()}")
print(f"|M comparison numerator| bit_length={abs((M_r-target_moment).numerator).bit_length()}")
print("majority mean-condition equality at s=mu_minus: PASS")
print("ALL EXACT D0007 TWO-MONOTONE-SPLIT CHECKS PASSED")
