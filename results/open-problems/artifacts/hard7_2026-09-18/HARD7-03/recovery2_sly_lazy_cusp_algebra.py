from fractions import Fraction as F
import sympy as sp

# HARD7-03 / D0025 recovery-2 exact algebra.
# This checks only finite/rational and symbolic identities used in the report.
# The asymptotic probability argument and theorem proof are written on the report page.

r = F(1, 2)
p_slow = F(1, 2)
p_fast = F(1, 2)
alpha_slow = F(1, 2)
alpha_fast = F(1, 1)

E_inv_alpha = p_slow / alpha_slow + p_fast / alpha_fast
mu = F(1, r) - E_inv_alpha

# A self-contained homogeneous lazy-LPP union bound gives G_unit(0) <= 4:
# 3^n paths and P(Gamma(n,1) >= 4n) <= exp(-n(3-log 4)).
# The exponent after multiplying by 3^n is -(3-log 12)n.
# e^3 > 1 + 3 + 3^2/2! + 3^3/3! = 13 > 12, so 3-log 12 > 0.
exp3_partial = F(1, 1) + F(3, 1) + F(9, 2) + F(27, 6)
assert exp3_partial == F(13, 1)
assert exp3_partial > 12

g_unit_0_lower = F(1, 4)
g_Q_0_lower = r * g_unit_0_lower
delta_lower = mu * g_Q_0_lower

assert E_inv_alpha == F(3, 2)
assert mu == F(1, 2)
assert g_Q_0_lower == F(1, 8)
assert delta_lower == F(1, 16)

# Exact Laplace-transform check of the Sly-type coupling on a fast row:
# W~Exp(1), B~Ber(1/2), E~Exp(1/2), U=B E, independent.
# Then Z=W+U~Exp(1/2).
s = sp.symbols("s", positive=True)
rr = sp.Rational(1, 2)
a = sp.Integer(1)
L_W = a / (a + s)
L_U = rr / a + (1 - rr / a) * rr / (rr + s)
L_Z_target = rr / (rr + s)
assert sp.simplify(L_W * L_U - L_Z_target) == 0

# Exact source-shape secant identity under the K=2 lazy coordinate transform:
# source level set: y(v)=v/G(v), g(y(v))=(1-v)/G(v), g(0)=1/G(0).
v, G0, Gv = sp.symbols("v G0 Gv", nonzero=True)
source_y = v / Gv
source_g = (1 - v) / Gv
source_g0 = 1 / G0
secant = sp.simplify((source_g - source_g0) / source_y)
target = (G0 - Gv) / (G0 * v) - 1
assert sp.simplify(secant - target) == 0

left_endpoint = F(1, 1) - delta_lower
right_endpoint = F(1, 1) + delta_lower
assert left_endpoint == F(15, 16)
assert right_endpoint == F(17, 16)

print("E_INV_ALPHA =", E_inv_alpha)
print("MU =", mu)
print("EXP3_TAYLOR_PARTIAL =", exp3_partial)
print("G_UNIT_0_RECIPROCAL_LOWER =", g_unit_0_lower)
print("G_Q_0_LOWER =", g_Q_0_lower)
print("DELTA_2_Q_CERTIFIED_LOWER =", delta_lower)
print("PLATEAU_INTERVAL =", f"[{left_endpoint}, {right_endpoint}]")
print("FAST_ROW_LAPLACE_COUPLING_IDENTITY = PASS")
print("SOURCE_SECANT_IDENTITY = PASS")
print("ALL_EXACT_CHECKS_PASS = True")
