#!/usr/bin/env python3
"""Exact symbolic comparison for the I0048 preferential-attachment threshold screen.

This checks only the finite algebra used in the accompanying R08 report.  It
compares one fixed-outdegree affine preferential-attachment model with one
affine conditionally-independent-edge preferential-attachment model after
matching their power-law exponent tau=4.

Literature formulas are inputs, not proved by this script:
  FPA: Hazra--van der Hofstad--Ray,
       pi_c = delta/[2(m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)))]
       for delta>0.
  BPA: van der Hofstad, Theorem 9.15 for f(k)=gamma*k+beta,
       pi_c = (1/(2 gamma)-1)(sqrt(1+gamma/beta)-1)
       for gamma<1/2.
"""
import sympy as sp

m = sp.Integer(2)
delta = sp.Integer(2)
gamma = sp.Rational(1, 3)
beta = sp.Integer(1)

tau_fpa = sp.Integer(3) + delta / m
tau_bpa = sp.Integer(1) + 1 / gamma

pi_fpa = sp.simplify(
    delta
    / (
        2
        * (
            m * (m + delta)
            + sp.sqrt(m * (m - 1) * (m + delta) * (m + 1 + delta))
        )
    )
)
pi_bpa = sp.simplify(
    (1 / (2 * gamma) - 1) * (sp.sqrt(1 + gamma / beta) - 1)
)

expected_fpa = sp.Rational(1, 3) - sp.sqrt(10) / 12
expected_fpa_alt = 1 / (8 + 2 * sp.sqrt(10))
expected_bpa = -sp.Rational(1, 2) + sp.sqrt(3) / 3
threshold_gap = sp.simplify(pi_bpa - pi_fpa)
expected_gap = -sp.Rational(5, 6) + sp.sqrt(10) / 12 + sp.sqrt(3) / 3

assert tau_fpa == 4
assert tau_bpa == 4
assert sp.simplify(pi_fpa - expected_fpa) == 0
assert sp.simplify(pi_fpa - expected_fpa_alt) == 0
assert sp.simplify(pi_bpa - expected_bpa) == 0
assert sp.simplify(threshold_gap - expected_gap) == 0
assert sp.simplify(threshold_gap > 0) is sp.true

print("I0048 EXACT THRESHOLD COMPARISON")
print(f"tau_FPA = {tau_fpa}")
print(f"tau_BPA = {tau_bpa}")
print(f"pi_FPA = {pi_fpa}")
print(f"pi_BPA = {pi_bpa}")
print(f"pi_BPA - pi_FPA = {threshold_gap}")
print(f"pi_FPA ~= {sp.N(pi_fpa, 18)}")
print(f"pi_BPA ~= {sp.N(pi_bpa, 18)}")
print("PASS exact symbolic checks")
