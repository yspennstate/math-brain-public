#!/usr/bin/env python3
import math
import sympy as sp

# NM13-10 spectral-band critical endpoint checker.

a = sp.symbols("a", positive=True)
ratio = (-sp.Rational(1,4) + a + a**2/2)/a**3
dr = sp.factor(sp.diff(ratio, a))
ac = (-4 + sp.sqrt(22))/2
cstar = sp.simplify(ratio.subs(a, ac))

print("log_ratio_derivative =", dr)
print("log_ratio_critical_a =", ac, "=", float(ac))
print("log_ratio_max =", cstar, "=", float(cstar))
assert sp.simplify(4 - cstar) > 0
print("LOG_DRIFT_CONSTANT_4_PASS")

# Excursion-count prefactor:
# 4 log 2 * [136 p/(1-2^{-p})] <= 544*3*log2/(3/4)
# = 2176 log 2 < 1509.
exc_coarse = 2176 * math.log(2)
print("excursion_count_coarse =", exc_coarse)
assert exc_coarse < 1509
print("EXCURSION_COUNT_1509_PASS")

# Optimized large-effective-rho coefficient.
tail_coeff = 1509 * math.e**2 / 9 + 128 / 36
print("optimized_tail_coeff =", tail_coeff)
assert tail_coeff < 1243
print("TAIL_1243_PASS")

# Small-effective-rho branch.
print("exp(6) =", math.exp(6))
assert math.exp(6) < 1243
print("SMALL_RHO_PASS")

# Rearrangement constant: R_s = 65 sqrt(K) J^(1/3) s^(-1/3) L^(2/3).
rearr = 1243 / 65**3 * (1 + 3*math.log(65) + 2/math.e)**2
print("rearrangement_factor_65sqrtK =", rearr)
assert rearr < 1
print("REARRANGEMENT_65SQRTK_PASS")

# Numerical sanity for the exact calculus majorant.
mx = -1e100
arg = None
for k in range(1, 500000):
    aa = 10**(-6 + 8*k/499999)
    val = (-0.25 + aa + 0.5*aa*aa)/(aa**3)
    if val > mx:
        mx, arg = val, aa
print("grid_log_ratio_max =", mx, "at", arg)
assert mx < 4.0000001
print("GRID_LOG_DRIFT_PASS")

print("DYADIC_BLOCK_CONSTANT =", 65*math.sqrt(2))
print("CHECK_PASS")
