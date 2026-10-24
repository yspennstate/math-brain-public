#!/usr/bin/env python3
"""Exact self-check for PROB10-03 R14 boundary-obstruction iteration.

Exact parts:
  1. symbolic limit A0(p,D)=T_D/c_D -> (1-p^2)/4 as D->1;
  2. rational Riemann/exponential bounds 13/20 < Q(1)/phi(1) < 33/50;
  3. exact algebra turning those Mills-ratio bounds into p_*<1/4 and
     V_{p_*}<2 mu_1(1-p_*^2);
  4. frozen rigorous bracket arithmetic.

No floating-point value is used as a theorem premise.
"""
from fractions import Fraction as F
import sympy as sp

# --- deterministic second-full limit ---
p,D,g=sp.symbols("p D g", positive=True)
q=p*D**2
gp=(1-q)/(2*D*(1-p))
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
T=(sp.Rational(1,2)*(1-p*q)*c-gp
   +sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g)
A0=sp.simplify(sp.diff(T,D)/sp.diff(c,D))
A0_lim=sp.simplify(sp.limit(A0,D,1,dir="-"))
assert sp.simplify(A0_lim-(1-p**2)/4)==0
print("A0_LIMIT_PASS", A0_lim)

# --- exact rational Mills-ratio sandwich at x=1 ---
# r = Q(1)/phi(1) = int_1^infty exp(-(t^2-1)/2) dt.
# Also r = 1 - int_1^infty exp(-(t^2-1)/2)/t^2 dt.
# On [1,4] both integrands are decreasing. For a>=0 and m>a,
# (1-a/m)^m < exp(-a). Right-endpoint lower Riemann sums therefore
# give exact lower bounds for both positive integrals.
n=400
m=1000
h=F(3,400)
S1=F(0)
S2=F(0)
for j in range(1,n+1):
    t=F(1)+j*h
    a=(t*t-1)/2
    assert 0 <= a < m
    e_lb=(1-a/F(m))**m
    S1 += h*e_lb
    S2 += h*e_lb/(t*t)

assert S1 > F(13,20)
assert S2 > F(17,50)
# Hence r>S1>13/20 and r=1-I2<1-S2<33/50.
print("MILLS_LOWER_SUM", float(S1), ">", 13/20)
print("MILLS_IBP_SUM", float(S2), ">", 17/50)
print("MILLS_SANDWICH_PASS", "13/20 < r < 33/50")

# --- exact consequences for the B->0 candidate ---
r=sp.symbols("r", positive=True)

# u=(G-1)_+ Hermite weights:
# s0/phi(1)^2=(1-r)^2, s2/phi(1)^2=1/2.
# At p=1/4, G(p)<=s0-s2/4. The lower Mills bound implies negativity.
assert F(49,400) < F(1,8)
print("PSTAR_BOUND_ALGEBRA_PASS", "(1-r)^2 < 49/400 < 1/8, so p_*<1/4")

# W=(G-1)_+^2:
# mu1/phi(1)=2r-1, E[W^2]/phi(1)=10r-6.
# E[W^2] < (15/8) mu1 is exactly equivalent to r<33/50.
expr=sp.simplify(sp.Rational(15,8)*(2*r-1)-(10*r-6))
assert sp.simplify(expr-(33-50*r)/8)==0
print("FOURTH_MOMENT_ALGEBRA_PASS", expr)

# Combined strict inequality:
# p_*<1/4 => 2 mu1(1-p_*^2) > (15/8)mu1
# and V_p<=E[W^2] < (15/8)mu1.
assert 2*(1-F(1,4)**2) == F(15,8)
print("BOUNDARY_INCOMPATIBILITY_PASS",
      "V_p* < 15/8 mu1 < 2 mu1(1-p_*^2)")

# Frozen source bracket.
aL=F(630297437506,10**11)
aU=F(1278437096216,10**11)
W=aU-aL
assert W==F(64813965871,10**10)
print("FROZEN_METRIC_WIDTH", float(W))
print("ALL_EXACT_CHECKS_PASS")
