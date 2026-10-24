#!/usr/bin/env python3
"""Arithmetic certificate for P17-M40 small-magnetic-flux persistence.

This script does NOT prove the localization/gauge theorem.  It only reproduces
its numerical consequences from the already-certified M33 zero-field spectral
margins.
"""
from decimal import Decimal, getcontext

getcontext().prec = 70
pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944592307816")
r = Decimal("0.4")
A = (- (Decimal(1) - 2*r)).exp()  # exp(-(1-2r)) = exp(-0.2)
C = 4*pi*A                         # d_H <= C*sqrt(|b-b'|)

margins = [
    Decimal("0.006936878216966567"),
    Decimal("0.012678591429630874"),
    Decimal("0.012678591429630430"),
    Decimal("0.006936878216966123"),
]

print("A =", A)
print("C = 4*pi*A =", C)
for i, m in enumerate(margins, 1):
    bcrit = (m/C) ** 2
    print(f"bcrit[{i}] =", bcrit)

safe_b = Decimal("4.5e-7")
eps = C * safe_b.sqrt()
print("safe_b =", safe_b)
print("epsilon(safe_b) =", eps)
for i, m in enumerate(margins, 1):
    print(f"remaining_margin[{i}] =", m - eps)

assert all(m - eps > 0 for m in margins)
