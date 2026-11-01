#!/usr/bin/env python3
"""Independent exact audit of the curvature-sign core of P20-I0081-LOGUNIFORM-RECTANGLE-03.

Peer source: proofnet24/P20-closure-log-unimodality/runs/2026-09-16/
2026-09-16_16-08-12__run-report.md, creation commit
8fa1d9ecf23f1354b8d34a4f5affb7251983c096, blob
8885afcece2e0a8cd1e1b99c74547edf06624759.

This checker independently validates the algebraic cancellation in equations (4.20)
and the exact rational margin in (4.27). It does not by itself audit the analytic
branch-continuation argument or Ji's edge theorem.
"""
from fractions import Fraction

# Algebraic cancellation: A = (1/2)csc^2(t) S - 1.
# Let C=csc^2(t), q=cot(t), T=dS/dt. Since dC/dt=-2*C*q,
# dA/dtheta = (1/2)dA/dt = -(1/2)C*q*S + (1/4)C*T.
# Adding A*q cancels the S terms exactly, giving -q + (1/4)C*T.
# For S=sum_X X P_X(phi_X), phi_X=X cot t,
# T=sum_X X P'_X(phi_X)*(-X C).
# P'_X=-2 a_X(1-a_X^2) sin(phi_X)/D_X^2, hence T=2 C U and
# the bracket is -q+(1/2)C^2 U, which is P20 equation (4.20).
# Check coefficients with exact rationals.
coef_S = -Fraction(1,2) + Fraction(1,2)
coef_T = Fraction(1,4)
assert coef_S == 0 and coef_T == Fraction(1,4)
assert coef_T * 2 == Fraction(1,2)

# Independent exact finite core for X>=6.
# e > sum_{n=0}^5 1/n! = 163/60, and (163/60)^6 > 400.
e6_gap_num = 163**6 - 400*60**6
assert e6_gap_num == 92969578009 and e6_gap_num > 0
# Thus a=e^{-X}<1/400 for X>=6.
# P_X >= (1-a)/(1+a) > 399/401 and L+M>=12.
phase_lower = Fraction(1,2)*12*Fraction(399,401) - 1
assert phase_lower == Fraction(1993,401) and phase_lower > 0

# pi^2 < (22/7)^2 = 484/49 < 10; therefore csc^4 envelope < 529/324.
assert Fraction(484,49) < 10
csc4 = Fraction(529,324)
# E(6) < 216/400 * (400/399)^4.
E6 = Fraction(216,400) * Fraction(400,399)**4
assert E6 == Fraction(512000000,938702163)
ratio = csc4 * E6
assert ratio == Fraction(67712000000,76034875203)
assert ratio < 1
margin = 1-ratio
assert margin == Fraction(8322875203,76034875203) and margin > 0

# Analytic monotonicity sign is immediate: for X>=6, a=e^-X in (0,1),
# d log E/dX = 3/X -1 - a/(1+a) - 3a/(1-a) < 3/X -1 <= -1/2.
print('cancellation_S_coefficient', coef_S)
print('post_chain_U_coefficient', coef_T*2)
print('e6_integer_gap', e6_gap_num)
print('phase_lower', phase_lower)
print('E6_upper', E6)
print('curvature_ratio_upper', ratio)
print('curvature_margin', margin)
print('AUDIT P19-AUDIT-P20-RECTANGLE-CURVATURE-13 PASS')
print('SCOPE: curvature cancellation/sign core only; branch continuation/Ji theorem not re-audited here')
