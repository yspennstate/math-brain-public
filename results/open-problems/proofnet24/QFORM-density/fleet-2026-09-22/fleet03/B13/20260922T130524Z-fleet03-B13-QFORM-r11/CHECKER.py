#!/usr/bin/env python3
"""Deterministic sanity checker for the target-level separated-branch witness.

The proof in REPORT.md is analytic.  This script only checks the explicit R=2
geometry and computes the positive-branch mass by deterministic midpoint
quadrature.
"""
import math

R = 2.0
N = 700

a = math.sqrt(R*R - 0.5)
b = math.sqrt(R*R + 0.25)
L = b-a
gap = 2*a
support_total = 2*L
lb = 0.25*(math.sqrt(33.0/8.0)-2.0)

assert support_total < 1.0
assert gap > 1.0
assert lb > 0.0

h = 1.0/N
M = 0.0
for i in range(N):
    x = -0.5 + (i+0.5)*h
    for j in range(N):
        y = -0.5 + (j+0.5)*h
        s = x*x+y*y
        M += math.sqrt(R*R+0.25-s)-math.sqrt(R*R-s)
M *= h*h

print(f"positive_band_left={a:.15f}")
print(f"positive_band_right={b:.15f}")
print(f"support_total_length={support_total:.15f}")
print(f"band_gap={gap:.15f}")
print(f"analytic_positive_mass_lower_bound={lb:.15f}")
print(f"midpoint_N={N}")
print(f"M_positive_branch={M:.15f}")
print(f"two_branch_mass={2*M:.15f}")
print("PASS=True")
