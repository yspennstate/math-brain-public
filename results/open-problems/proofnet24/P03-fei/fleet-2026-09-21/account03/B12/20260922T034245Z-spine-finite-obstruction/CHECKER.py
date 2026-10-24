#!/usr/bin/env python3
"""Dependent exact-arithmetic checker for account03/B12 finite spine obstruction.

This checker consumes the certified interval/state constants from the completed
account02/B17 distinguished-spine theorem.  It does not re-run its source-core
logarithm enclosure.  It verifies the new Lipschitz transfer arithmetic, exact
spine state recurrences, finite F3/F4 ratio enclosures, strict finite gains, and
the balanced-uniform gate-margin lower bound.
"""
from fractions import Fraction as F

alpha = F(9,256)
D0 = F(133,128)
C0 = F(16137,2500)  # 6.4548
AND_MARGIN = F(43974201,10**10)

# account02/B17 certified source-valid F1 state and F2 interval.
c1 = F(14593,65536)
I1 = F(68013,32768)
R2L = F("6.5218511190811741401649047123071878637276611493668")
R2U = F("6.5218511190811741401649047123167742489206633278087")

# account02/B17 certified fixed-point and forcing intervals.
cstarL = F(22266585228,10**11)
cstarU = F(22266585229,10**11)
TstarL = F("6.5218511673423727025654896282010361877746102003501")
TstarU = F("6.5218511673532720920534233991583790594494969981239")

# New analytic lemma in REPORT.md: |K'(b)|<19 on 0.0024<=b<=0.0025.
K_LIPSCHITZ = F(19)

def step_c(c):
    return (F(57) + c**4)/256

def step_I(I,c):
    S = 1+c+c**2+c**3
    Dnext = D0 + alpha*(I-1)*S
    return 1+Dnext, D0/Dnext

def T_bounds_from_fixed_point(c):
    b = c**4
    assert F(24,10000) < b < F(25,10000)
    dist = max(abs(b-cstarL**4), abs(b-cstarU**4))
    err = F(128,133)*K_LIPSCHITZ*dist
    return TstarL-err, TstarU+err, err

def dec_floor(x,d=60):
    scale = 10**d
    q = x.numerator*scale//x.denominator
    return f"{q//scale}.{q%scale:0{d}d}"

def dec_ceil(x,d=60):
    scale = 10**d
    q = (x.numerator*scale+x.denominator-1)//x.denominator
    return f"{q//scale}.{q%scale:0{d}d}"

# Source-constant arithmetic used by the new derivative lemma.
# Peer source certifies sum_S |Q_S|=1584.
core_derivative_bound = F(6*1584,512)       # 18.5625
scalar_derivative_bound = alpha * F(72,400) # <0.00633
assert core_derivative_bound + scalar_derivative_bound < 19

# Exact spine states through F4.
c2 = step_c(c1)
I2, lam1 = step_I(I1,c1)
c3 = step_c(c2)
I3, lam2 = step_I(I2,c2)
c4 = step_c(c3)
I4, lam3 = step_I(I3,c3)

T2L,T2U,e2 = T_bounds_from_fixed_point(c2)
R3L = (1-lam2)*R2L + lam2*T2L
R3U = (1-lam2)*R2U + lam2*T2U
assert R3L > R2U

T3L,T3U,e3 = T_bounds_from_fixed_point(c3)
R4L = (1-lam3)*R3L + lam3*T3L
R4U = (1-lam3)*R3U + lam3*T3U
assert R4L > R3U

# Arity recurrence from the consumed Boolean construction.
n1 = 162
n2 = 36*n1-27
n3 = 36*n2-27
n4 = 36*n3-27
assert (n2,n3,n4)==(5805,208953,7522281)

cG4L = 4*(R4L-C0)
assert cG4L > AND_MARGIN
assert cG4L/AND_MARGIN > 60

print("PASS")
print("scope=dependent exact arithmetic from account02/B17 certified source intervals")
print("Kprime_bound", str(core_derivative_bound + scalar_derivative_bound), "< 19")
print("c2", dec_floor(c2,70))
print("c3", dec_floor(c3,70))
print("lambda2", dec_floor(lam2,70))
print("lambda3", dec_floor(lam3,70))
print("T2_transfer_error_upper", dec_ceil(e2,70))
print("T3_transfer_error_upper", dec_ceil(e3,70))
print("R3_lower", dec_floor(R3L,60))
print("R3_upper", dec_ceil(R3U,60))
print("R3_gain_over_R2_upper", dec_floor(R3L-R2U,60))
print("R4_lower", dec_floor(R4L,60))
print("R4_upper", dec_ceil(R4U,60))
print("R4_gain_over_R3_upper", dec_floor(R4L-R3U,60))
print("F4_arity", n4)
print("cG_F4_lower", dec_floor(cG4L,60))
print("cG_over_AND_margin_lower", dec_floor(cG4L/AND_MARGIN,30))
print("full_FEI=OPEN_NOT_PROVED")
