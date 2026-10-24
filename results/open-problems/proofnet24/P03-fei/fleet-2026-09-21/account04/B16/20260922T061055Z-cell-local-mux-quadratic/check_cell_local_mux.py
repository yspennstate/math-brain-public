#!/usr/bin/env python3
"""Standard-library checks for account04/B16 cell-local MUX theorem."""
from fractions import Fraction
from math import log, log2
import random

C = Fraction(6521851214, 10**9)
A = Fraction(268204856, 10**9)
INV_LN2_UB = Fraction(10**7, 6931471)
RHO = Fraction(3, 20)

reserve = (C - 6
           - Fraction(31, 2) * INV_LN2_UB * (RHO*RHO/(1-RHO*RHO))
           - A * Fraction(1, 2) * RHO*RHO)
assert reserve == Fraction(1114633887638025857, 271020516100000000000)
assert reserve > 0

allrho = C - 6 - A/2
assert allrho == Fraction(193874393, 500000000)
assert allrho > 0

# Direct affine-cell identity check.
rng = random.Random(160922061055)
max_err = 0.0
for _ in range(20000):
    p = 10 ** rng.uniform(-5.0, -0.3010299956639812)
    rho = rng.uniform(1e-8, 0.8)
    if p*(1+rho) > 0.5:
        p = 0.49/(1+rho)
    sigma = rng.uniform(-30.0, 30.0)
    intercept = rng.uniform(-20.0, 20.0)
    def G(y):
        return intercept + sigma*y
    def gamma0(z):
        return z*G(log2(1/z))
    direct = (gamma0(p)
              - 0.5*gamma0(p*(1-rho))
              - 0.5*gamma0(p*(1+rho)))
    K = (1-rho)*log(1-rho) + (1+rho)*log(1+rho)
    closed = p*sigma*K/(2*log(2))
    max_err = max(max_err, abs(direct-closed))
assert max_err < 2e-13

# K(rho) <= rho^2/(1-rho^2) sanity mesh, kept away from zero
# to avoid subtractive floating-point cancellation. The theorem itself is analytic.
max_ratio = 0.0
for j in range(20,20000):
    rho = j/20000
    K = (1-rho)*log(1-rho) + (1+rho)*log(1+rho)
    ub = rho*rho/(1-rho*rho)
    assert K <= ub + 2e-15
    max_ratio = max(max_ratio, K/ub)

print("CELL_LOCAL_MUX_CHECK PASS")
print("rho_cert", float(RHO))
print("reserve_exact", reserve)
print("reserve_decimal", float(reserve))
print("negative_slope_all_rho_reserve_exact", allrho)
print("negative_slope_all_rho_reserve_decimal", float(allrho))
print("affine_formula_trials", 20000)
print("max_affine_formula_error", max_err)
print("K_bound_mesh_points", 19980)
print("max_K_to_upper_ratio", max_ratio)
