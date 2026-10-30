#!/usr/bin/env python3
"""Exact arithmetic companion for the fleet03/B12 region-2 v->0 lemma.

This script does not evaluate the transcendental certificate.  It checks only
the rational arithmetic of the analytic proof after the two candidate metadata
facts are supplied:
  tail_slope >= 49/10 and |Ghat'| <= 31.
Those are deliberately weaker than the current candidate log
(tail slope 4.909600 and |Ghat'| <= 30.080).

The analytic proof supplies:
  ln(2) > 2/3,
  ell(v) <= 16/15 for v <= 2^-40,
  -12/ln(2) <= Psi'(z) <= 0 on 0<z<=1/2,
and therefore Phi(p,1-v)/v > 557/5 throughout x>=1,y>=40.
"""
from fractions import Fraction
import json

inv_ln2_upper = Fraction(3, 2)       # ln(2) > 2/3
ell_upper = Fraction(16, 15)         # v<=2^-40<1/16 and ell(v)<=1/(1-v)
Ghat_prime_abs_upper = Fraction(31)
tail_slope_lower = Fraction(49, 10)
K = 40

A_lower = -Ghat_prime_abs_upper * ell_upper * inv_ln2_upper
B_lower = Fraction(2) + tail_slope_lower * K   # b*=8-4/ln2 > 2
C_lower = Fraction(-8)                         # x 2^-x <= 1 for x>=1
D_lower = -8 * inv_ln2_upper                  # (1-v)ell(v)<=1
E_lower = Fraction(-8)
F_lower = -6 * inv_ln2_upper                  # p<=1/2, Psi'>=-12/ln2
R_lower = Fraction(0)                          # Psi(1-v)/v >= 0

total = A_lower+B_lower+C_lower+D_lower+E_lower+F_lower+R_lower
assert A_lower == Fraction(-248, 5)
assert B_lower == Fraction(198)
assert F_lower == Fraction(-9)
assert total == Fraction(557, 5)
assert total > 0

print(json.dumps({
    "status": "PASS_COMPONENT_LEMMA_ARITHMETIC",
    "scope": "region2: x>=1, y=log2(1/v)>=40, pinned M96/K40/c=.003 candidate",
    "candidate_metadata_weakened_assumptions": {
        "abs_Ghat_prime_le": "31",
        "tail_slope_ge": "49/10",
        "K": K
    },
    "analytic_bounds": {
        "inv_ln2_lt": "3/2",
        "ell_v_le": "16/15",
        "Psi_prime_interval": "[-12/ln(2),0]"
    },
    "term_lower_bounds": {
        "A": str(A_lower),
        "B": str(B_lower),
        "C": str(C_lower),
        "D": str(D_lower),
        "E": str(E_lower),
        "F": str(F_lower),
        "R": str(R_lower)
    },
    "Phi_over_v_strict_lower": str(total),
    "Phi_over_v_strict_lower_decimal": float(total),
    "full_FEI_status": "OPEN",
    "brain_assistance_status": "WITHOUT_VERIFIED_BRAIN"
}, indent=2, sort_keys=True))
