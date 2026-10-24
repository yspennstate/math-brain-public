#!/usr/bin/env python3
"""Exact algebra/arithmetic self-check for the 2026-09-19 P0083 P5/cycle run.

This is a SELF-CHECK, not an independent audit and not a numerical proof of the
continuum inequalities.  The report proves the sign implications from the stated
parameter ranges.  This script checks the symbolic identities and the three
rational endpoint comparisons used there.
"""

from fractions import Fraction
import sympy as sp

p, t = sp.symbols("p t", positive=True)
q = p + 1
T = t**q

# H_p(t) and the exact numerator of H'_p after multiplication by the
# positive factor (1+t^(p+1))^2 t^(p+1).
H = (t**(-p) + 2*t - 1) / (1 + T)
H_scaled = sp.simplify(sp.diff(H, t) * (1 + T) ** 2 * t ** (p + 1))
H_expected = (
    t ** (2*p + 1) * ((p + 1) - 2*p*t)
    + (1 - 2*p) * t ** (p + 1)
    - p
)
assert sp.simplify(H_scaled - H_expected) == 0

# M_p(t) and the exact logarithmic-derivative identity used to prove
# strict monotonicity for 1 <= p <= 3 and t >= 1.
D = 1 - t**p + 2*t**(p + 1)
M = (
    t * D * (1 + t**(p + 1)) ** (1/p)
    / (1 + 2*t**(p + 1)) ** ((p + 1)/p)
)
M_log = sp.simplify(t * sp.diff(sp.log(M), t))
M_expected = (
    (2*T - p) / D
    + (p + 1) * (p + (p - 1)*T) / (p * (1 + T) * (1 + 2*T))
)
assert sp.simplify(M_log - M_expected) == 0

# In the only potentially negative first-term case 2A < p, the report
# lower-bounds the logarithmic derivative by a rational expression whose
# numerator is rewritten as the manifestly positive expression below.
A = sp.symbols("A", positive=True)
lower_num = 4*p*A**2 - p**2*A + 2*p*A - A + p
lower_rewrite = A*p*(4*A - p + 2) + (p - A)
assert sp.expand(lower_num - lower_rewrite) == 0

# Exact endpoint comparisons.
h_4over3_gap = Fraction(305, 96) - Fraction(256, 81)
p5_path_gap = Fraction(91, 18) - Fraction(4, 1)
cycle_cube_gap = Fraction(8, 125) - Fraction(1, 16)
assert h_4over3_gap > 0
assert p5_path_gap > 0
assert cycle_cube_gap > 0

print("EXACT_SELF_CHECK_PASS")
print("H_4over3_endpoint_gap =", h_4over3_gap)
print("P5_path_gap_91over18_minus_4 =", p5_path_gap)
print("cycle_cube_gap_8over125_minus_1over16 =", cycle_cube_gap)
print("H_derivative_identity = PASS")
print("M_log_derivative_identity = PASS")
print("M_negative_case_lower_numerator_identity = PASS")
