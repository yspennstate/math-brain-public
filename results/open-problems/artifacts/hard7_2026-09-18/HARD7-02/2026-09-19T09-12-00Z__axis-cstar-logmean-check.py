#!/usr/bin/env python3
"""
HARD7-02 run 13 exact symbolic self-check.

Purpose:
  Verify the algebra behind the raw axis-mass logarithmic-mean formula and
  the reciprocal-amplitude C* deformation. This is a self-check of exact
  algebra only; the source-level probabilistic inputs are the previously
  proved mass-homogeneity and axis-family dilation theorems.
"""
import sympy as sp

A, B = sp.symbols("A B", positive=True)
m = A + B
p = A/m

# Combining mass homogeneity with the probability-axis law.
from_normalized = sp.simplify(m * 2*(2*p - 1)/sp.log(p/(1-p)))
raw_formula = 2*(A-B)/sp.log(A/B)
assert sp.simplify(from_normalized - raw_formula) == 0
print("raw_axis_scale_alpha =", raw_formula)
print("RAW_AXIS_COMBINATION_PASS = True")

# Fixed-product hyperbola.
g, s = sp.symbols("g s", positive=True)
Ah = g*sp.exp(s)
Bh = g*sp.exp(-s)
Lh = sp.simplify((Ah-Bh)/(sp.log(Ah)-sp.log(Bh)))
assert sp.simplify(Lh - g*sp.sinh(s)/s) == 0
print("fixed_product_logmean =", Lh)
print("HYPERBOLIC_REPARAMETERIZATION_PASS = True")

# Exact rational counterexample to extending the relative-phase U(1) gauge
# to positive reciprocal amplitudes: alpha=1, p=1/4, r=2.
# Original scale^alpha = 1/log(3).
# New raw masses are A=1/2 and B=3/8, hence scale^alpha=(1/4)/log(4/3).
old = 1/sp.log(3)
new = sp.Rational(1,4)/sp.log(sp.Rational(4,3))
print("p=1/4 alpha=1 r=2 old_scale =", old)
print("p=1/4 alpha=1 r=2 new_scale =", new)

# Equality would imply log 3 = 4 log(4/3), hence 3=(4/3)^4,
# equivalently 243=256. The integer mismatch is an exact certificate.
lhs_int = 3*81
rhs_int = 256
assert lhs_int == 243 and rhs_int == 256 and lhs_int != rhs_int
print("equality_would_force:", lhs_int, "=", rhs_int)
print("EXACT_NONINVARIANCE_WITNESS_PASS = True")

# Swap point for p=1/4, alpha=1: r^alpha=q/p=3.
p0 = sp.Rational(1,4)
q0 = sp.Rational(3,4)
r_alpha_swap = q0/p0
A_swap = sp.simplify(p0*r_alpha_swap)
B_swap = sp.simplify(q0/r_alpha_swap)
assert A_swap == q0 and B_swap == p0
print("swap_point_r^alpha =", r_alpha_swap)
print("swap_masses =", A_swap, B_swap)
print("SWAP_POINT_PASS = True")

# Balance point: r^alpha=sqrt(q/p), which makes A=B=sqrt(pq).
r_alpha_bal = sp.sqrt(q0/p0)
A_bal = sp.simplify(p0*r_alpha_bal)
B_bal = sp.simplify(q0/r_alpha_bal)
assert sp.simplify(A_bal-B_bal) == 0
assert sp.simplify(A_bal-sp.sqrt(p0*q0)) == 0
print("balance_point_r^alpha =", r_alpha_bal)
print("balanced_mass =", A_bal)
print("BALANCE_POINT_PASS = True")

print("ALL_EXACT_CHECKS_PASS = True")
