#!/usr/bin/env python3
"""Exact self-check for R14 PROB10-03 tail/entropy iteration.

Exact arithmetic verifies:
  * the rational Gaussian-tail envelope constants;
  * the frozen bracket width arithmetic;
  * the stationary entropy-balance H_B algebra.

No numerical scout in this file is promoted to a source endpoint.
"""
from fractions import Fraction as F
import sympy as sp

# e > sum_{k=0}^5 1/k! = 163/60.
series6 = sum((F(1), F(1), F(1,2), F(1,6), F(1,24), F(1,120)), F(0))
assert series6 == F(163,60)

# Since sqrt(2*pi)>2 and e^{-81/2}<e^{-40},
# phi(9) < U := (1/2)(60/163)^40.
U = F(1,2) * F(60,163)**40

# Mills plus Gaussian integration-by-parts recurrence:
# R0 < U/9,
# R2 < (9+1/9)U = (82/9)U,
# R4 < [9^3+3(82/9)]U = (2269/3)U.
# T2,T4 are the corresponding two-sided moments.
T2 = 2 * F(82,9) * U
T4 = 2 * F(2269,3) * U

bounds = {
    "Tail_I": 7*T2,
    "Tail_IB": 3*T2,
    "Tail_IBB": 4*T4,
    "Tail_K": 1600*T2,
    "Tail_KB": 19200*T4,
    "Tail_Kp": 12000*T2,
    "delta_tail_Ip": F(5,6)*1600*T2,
    "delta_tail_IBp": F(5,6)*19200*T4,
}
thresholds = {
    "Tail_I": F(3,10**16),
    "Tail_IB": F(12,10**17),
    "Tail_IBB": F(14,10**15),
    "Tail_K": F(64,10**15),
    "Tail_KB": F(64,10**12),
    "Tail_Kp": F(48,10**14),
    "delta_tail_Ip": F(54,10**15),
    "delta_tail_IBp": F(54,10**12),
}

print("EXACT_GAUSSIAN_TAIL_ENVELOPE")
print("series6", series6)
print("U_phi9", float(U))
print("T2", float(T2))
print("T4", float(T4))
for key in bounds:
    ok = bounds[key] < thresholds[key]
    print(key, repr(float(bounds[key])), "<", repr(float(thresholds[key])), ok)
    assert ok

# Frozen source bracket arithmetic.
aL = F(630297437506,10**11)
aU = F(1278437096216,10**11)
width = aU-aL
assert width == F(64813965871,10**10)
print("FROZEN_METRIC_WIDTH", width, float(width))

# Entropy-balance algebra at an H=0 point.
# L=averaged KL, V=I_BB, M=-I_B, r=A0_D/A0.
L,B,V,M,r,DB = sp.symbols("L B V M r DB", positive=True)
A0 = L/(4*B**2*M)
A0D = r*A0
HB = -B*V + 8*B*M*A0 - 4*B**2*V*A0 + 4*B**2*M*A0D*DB
target = 2*L/B - B*V - L*V/M + L*r*DB
assert sp.simplify(HB-target) == 0
print("ENTROPY_BALANCE_ROOT_IDENTITY_PASS")

print("ALL_EXACT_CHECKS_PASS")
