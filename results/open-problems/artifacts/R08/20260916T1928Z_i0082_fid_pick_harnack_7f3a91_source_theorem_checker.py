#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
import sympy as sp

# Exact symbolic boundary derivative identities for nu_r.
x,r=sp.symbols('x r', positive=True)
A=r/x+(1-r)*sp.log(x/(1-x))
Ap=sp.factor(sp.diff(A,x))
assert sp.simplify(Ap-(x-r)/(x**2*(1-x)))==0

r0=Fraction(1,1000)
A2=Fraction(1,1)/(4*r0*(1-2*r0))
A3=4-8*r0

# Elementary exact certificate log(499)<7 from e^7 > sum_{0}^7 7^n/n! >499.
partial=sum((Fraction(7)**n/Fraction(factorial(n))) for n in range(8))
assert partial == Fraction(47273,72)
assert partial > 499

# Use the classical rational bounds 3 < pi < 22/7.
# beta=pi*(999/1000); M=-1/2+(999/1000)log(499).
beta_lower=Fraction(2997,1000)
beta2_upper=Fraction(484,49)  # (22/7)^2
first_den_upper=4*r0*r0+beta2_upper
assert first_den_upper < 10
M_upper=Fraction(13,2)  # follows from log499<7
second_den_upper=M_upper*M_upper+beta2_upper
assert second_den_upper < Fraction(209,4)

# Global half-plane Harnack lower:
# L >= beta^4/[4(4r^2+beta^2)(M^2+beta^2)].
L_crude=beta_lower**4/(4*Fraction(10)*Fraction(209,4))
assert L_crude > Fraction(3,100)

# A domain-exhaustion Harnack constant may therefore be chosen >3/100.
assert A2*Fraction(3,100) > A3

# Exact cross-ratio identity underlying the half-plane Harnack estimate.
X0,Y0,X2,Y2=sp.symbols('X0 Y0 X2 Y2', real=True, positive=True)
num=(X2-X0)**2+(Y2-Y0)**2
den=(X2-X0)**2+(Y2+Y0)**2
assert sp.expand(den-num)==4*Y0*Y2

print("r=1/1000")
print("exp7_partial_0_to_7=",partial,">499")
print("global_Harnack_crude_lower=",L_crude,">3/100")
print("A2=",A2,"A3=",A3)
print("A2*(3/100)>A3 = PASS")
print("boundary_derivative_identity = PASS")
print("cross_ratio_identity = PASS")
print("ALL_SOURCE_THEOREM_EXACT_CHECKS_PASS")
