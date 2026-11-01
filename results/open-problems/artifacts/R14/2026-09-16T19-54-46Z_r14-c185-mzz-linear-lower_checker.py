#!/usr/bin/env python3
from fractions import Fraction

print("R14-C185 exact arithmetic certificate: MZZ Theorem 4.3 at kappa=-1")

# Exact rational pi enclosure using Machin's formula.
def atan_bounds(x, odd_N):
    if odd_N % 2 == 0:
        odd_N += 1
    def S(N):
        z = Fraction(0)
        for n in range(N + 1):
            t = x ** (2*n + 1) / Fraction(2*n + 1)
            z += t if n % 2 == 0 else -t
        return z
    return S(odd_N), S(odd_N - 1)

aL, aU = atan_bounds(Fraction(1,5), 17)
bL, bU = atan_bounds(Fraction(1,239), 5)
piL = 16*aL - 4*bU
piU = 16*aU - 4*bL

# Certified enclosure for (2*pi)^(-1/2).
cL = Fraction(398942280401432, 10**15)
cU = Fraction(398942280401433, 10**15)
assert 2*piU*cL*cL < 1
assert 2*piL*cU*cU > 1

# Alternating exact-rational enclosure for int_0^1 exp(-t^2/2) dt.
def gauss_int_bounds(a, N_even=28):
    a = Fraction(a)
    def S(N):
        z = Fraction(0)
        fact = 1
        for n in range(N + 1):
            if n:
                fact *= n
            term = a ** (2*n + 1) / (2**n * fact * (2*n + 1))
            z += term if n % 2 == 0 else -term
        return z
    return S(N_even + 1), S(N_even)

iL, iU = gauss_int_bounds(Fraction(1))
# Phi(-1) = 1/2 - (2*pi)^(-1/2) int_0^1 exp(-t^2/2) dt.
PhiL = Fraction(1,2) - cU*iU
PhiU = Fraction(1,2) - cL*iL
assert PhiL > 0

# Rational SAT endpoint chosen strictly below MZZ's delta_lin(-1)=1/Phi(-1).
alpha_L = Fraction(630297437506, 10**11)  # 6.30297437506
assert alpha_L * PhiU < 1

# Retained rigorous R14-C184 upper endpoint.
alpha_U = Fraction(1278437096216, 10**11)  # 12.78437096216
width = alpha_U - alpha_L
assert width == Fraction(648139658710, 10**11)

print("Gaussian CDF enclosure: PASS")
print("  Phi(-1) in [%.18g, %.18g]" % (float(PhiL), float(PhiU)))
print("MZZ strict lower-endpoint inequality: PASS")
print("  alpha_L =", alpha_L, "=", float(alpha_L))
print("  alpha_L * Phi(-1) <= %.18g < 1" % float(alpha_L*PhiU))
print("  1/Phi(-1) in [%.15f, %.15f]" % (float(1/PhiU), float(1/PhiL)))
print("Retained alpha_U =", float(alpha_U))
print("New width =", width, "=", float(width))
print("Width movement:")
print("  before = 10.61241096216")
print("  after  =", float(width))
print("ALL_EXACT_CHECKS_PASS")
