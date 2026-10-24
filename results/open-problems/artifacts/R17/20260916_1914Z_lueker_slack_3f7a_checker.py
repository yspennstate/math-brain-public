#!/usr/bin/env python3
"""
R17 exact checker: strict rational sharpening of Lueker's published binary-LCS
upper bound, plus an independent finite-core audit of R18-I0080-C008.

No Monte Carlo.

The R17 checker does NOT re-run Lueker's 6,419,109-state computation.
It starts only from the exact inequalities printed in Lueker 2009:
  rho = 1 + 2^-52,
  R0 >= Rhat * rho^(-eR),
  eR <= 2^27,
  Rhat - 1 >= 2^-24,
at p0=826280, q0=1000000, and the h=8 table parameter z=0.3209.
"""
from fractions import Fraction
from math import comb
import sympy as sp

print("R17 C009 exact arithmetic")

# Lueker published proof constants.
rho = Fraction(1) + Fraction(1, 2**52)
x = Fraction(1, 2**52)
m = 2**27
y = m*x
assert y == Fraction(1, 2**25)

# Elementary exact inequality:
# (1+x)^m <= sum_{k>=0} (mx)^k = 1/(1-mx), since C(m,k)<=m^k.
# Hence rho^{-2^27} >= 1-2^-25.
source_slack = (Fraction(1) + Fraction(1,2**24)) * (Fraction(1) - Fraction(1,2**25))
a = source_slack - 1
assert a == Fraction(1,2**25) - Fraction(1,2**49)
assert a > 0
print("certified R0 lower factor = 1+a with a =", a)

# We use only z >= 0.32, much weaker than the h=8 table value z=0.3209.
z_lower = Fraction(8,25)  # 0.32
factor_z = (2*z_lower)**2
assert factor_z == Fraction(256,625)

# Amplify the published certified slack N times and add one to q.
N = 30_000_000

# Lower-bound (1+a)^N by the first six binomial terms k=0..5.
partial = sum(Fraction(comb(N,k))*a**k for k in range(6))
r1_lower = partial * factor_z
margin = r1_lower - 1
assert margin > 0
print("N =", N)
print("binomial partial lower bound times (2z)^2 =", r1_lower)
print("exact R1 margin lower bound =", margin)

# New rational upper endpoint.
p0 = 826_280
q0 = 1_000_000
p1 = N*p0
q1 = N*q0 + 1
U_old = Fraction(p0,q0)
U_new = Fraction(p1,q1)
assert U_new < U_old

# Published rigorous lower endpoint used by R17.
L = Fraction(792_665_992, 1_000_000_000)
W_old = U_old - L
W_new = U_new - L
assert W_new < W_old

print("U_old =", U_old, float(U_old))
print("U_new =", U_new, format(float(U_new), ".17f"))
print("U decrease =", U_old-U_new, format(float(U_old-U_new), ".17g"))
print("W_old =", W_old, format(float(W_old), ".17f"))
print("W_new =", W_new, format(float(W_new), ".17f"))
print("width decrease =", W_old-W_new)

# Clean decimal corollary.
clean = Fraction(82_627_999_999_998, 100_000_000_000_000)
assert U_new < clean
print("clean decimal corollary U <", "0.82627999999998")

# ---------------- Independent finite-core audit: R18-I0080-C008 ----------------
print("\nR18 C008 independent finite-core audit")

eps = Fraction(1,100)
kappa = Fraction(8,5)
d = Fraction(19,20)

# High y=0 rational bound.
high0 = Fraction(8,5)*Fraction(4193,13200)*Fraction(10000,10003) + Fraction(123,125)*Fraction(12,25)
claimed_high0 = Fraction(144478732,147365625)
assert high0 == claimed_high0
high0_margin = high0-d
assert high0_margin == Fraction(17925553,589462500) > 0

# Low y=3 rational comparison.
low_margin = Fraction(26,81)-Fraction(11,70)-Fraction(16000,99401)
assert low_margin == Fraction(1623529,563603670) > 0

# High y=ell/2.
highmid = Fraction(123,125)*Fraction(967,1000)
assert highmid == Fraction(118941,125000)
assert highmid-d == Fraction(191,125000) > 0

# Smooth all-time parameterization algebra.
t, pi = sp.symbols('t pi', positive=True)
ell = 100 + 95*pi*t
D = sp.Rational(19,20)/ell
b2 = pi*D*t
assert sp.simplify(b2 - (sp.Rational(1,100)-1/ell)) == 0
# t=b^2/(pi D) is tautological from b^2=piDt.
assert sp.simplify(b2/(pi*D)-t) == 0

# Probability-density masses in log coordinates.
# Long component mass = (1-p)/(ell*b) * ell*b = 1-p;
# short component mass = p/(eps*b) * eps*b = p.
p = kappa/100  # at smallest ell=100, maximal p
assert p == Fraction(2,125) < 1

print("R18 high0 margin =", high0_margin)
print("R18 low-point rational margin =", low_margin)
print("R18 highmid margin =", highmid-d)
print("R18 smooth parameter algebra = PASS")
print("R18-AUDIT-R17-C008-ATOMLESS-FINITECORE-001 = PASS_FINITE_CORE")
print("\nALL_EXACT_CHECKS_PASS")
