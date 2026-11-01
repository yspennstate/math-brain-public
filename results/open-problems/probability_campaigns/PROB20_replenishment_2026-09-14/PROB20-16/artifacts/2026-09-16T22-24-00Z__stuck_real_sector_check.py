#!/usr/bin/env python3
"""
PROB20-16 stuck-recovery exact self-check.

This script does NOT certify the global X095 metric and does NOT prove the
remaining finite-separation real-transverse compensation inequality.

It verifies only:
  (1) the conditional-Bernoulli coordinate identities for a real two-site DPP;
  (2) the exact infinitesimal rho->0 compensation determinant identity;
  (3) an exact rational counterexample to the tempting auxiliary coercivity
      S_C(U) >= 2 L(C) b^2 for arbitrary real-symmetric U.
"""
from fractions import Fraction
import sympy as sp

# ---------------------------------------------------------------------
# 1. Conditional Bernoulli coordinates
# ---------------------------------------------------------------------
Y,U,V = sp.symbols("Y U V", positive=True)
X = (1-Y)*U + Y*V
Sedge = Y*(1-Y)*(U-V)

p00 = (1-X)*(1-Y) - Sedge
p10 = X*(1-Y) + Sedge
p01 = (1-X)*Y + Sedge
p11 = X*Y - Sedge

assert sp.simplify(p10/(1-Y) - U) == 0
assert sp.simplify(p00/(1-Y) - (1-U)) == 0
assert sp.simplify(p11/Y - V) == 0
assert sp.simplify(p01/Y - (1-V)) == 0

# ---------------------------------------------------------------------
# 2. Exact local compensation determinant
# ---------------------------------------------------------------------
x,y,r = sp.symbols("x y r", positive=True)
s = r**2
q00 = (1-x)*(1-y)-s
q10 = x*(1-y)+s
q01 = (1-x)*y+s
q11 = x*y-s
L = sp.log(q10*q01/(q00*q11))

# raw real-symmetric affine direction coordinates z=(a,d,b)
# Umat=[[a,b],[b,d]]
T = sp.Matrix([
    [-(1-y), -(1-x), -2*r],
    [ (1-y), -x,      2*r],
    [ -y,     (1-x),  2*r],
    [ y,       x,     -2*r],
])
F = T.T * sp.diag(1/q00,1/q10,1/q01,1/q11) * T
Curv = sp.zeros(3)
# -H'' = Fisher - 2 L det(U) = Fisher -2L(ad-b^2)
Curv[0,1] = Curv[1,0] = -L
Curv[2,2] = 2*L
Smat = sp.simplify(F + Curv)

# In the rho->0 deformation C0=C(x+rho), C1=C(x), the normalized
# real cross-vector W/sqrt(ac rho) has raw coordinate map
# P(u1,u2)=(2u1,0,u2).  Since J=d/dx grad H2 = -Smat[e11,.]
# with the Frobenius off-diagonal factor, the local residual is:
Dloc = sp.Matrix([
    [6*Smat[0,0],              3*Smat[0,2]],
    [3*Smat[0,2], Smat[2,2] + 2*Smat[0,1]],
])
target_det = 36*r**2*y*(1-y)/(q00*q10*q01*q11)
det_diff = sp.factor(sp.together(Dloc.det() - target_det))
assert det_diff == 0

# ---------------------------------------------------------------------
# 3. Exact failure of naive per-endpoint off-diagonal coercivity
# ---------------------------------------------------------------------
xf = Fraction(4,5)
yf = Fraction(4,5)
rf = Fraction(9999,50000)
sf = rf*rf

P00 = (1-xf)*(1-yf)-sf
P10 = xf*(1-yf)+sf
P01 = (1-xf)*yf+sf
P11 = xf*yf-sf
P = [P00,P10,P01,P11]
assert all(p > 0 for p in P)

# Direction U=[[-1,1],[1,-1]], hence det U=0 and b=1.
aa=Fraction(-1); dd=Fraction(-1); bb=Fraction(1)
Q00 = -(1-yf)*aa -(1-xf)*dd - 2*rf*bb
Q10 =  (1-yf)*aa - xf*dd     + 2*rf*bb
Q01 = -yf*aa      +(1-xf)*dd + 2*rf*bb
Q11 =  yf*aa      + xf*dd     - 2*rf*bb
Q=[Q00,Q10,Q01,Q11]
FI = sum(q*q/p for q,p in zip(Q,P))
odds = P10*P01/(P00*P11)

# Exact rational comparisons:
# odds > 8192 = 2^13 => L=log odds > 13 log 2.
# log 2 = 2 atanh(1/3) > 2/3, so 2L > 52/3.
# FI < 52/3.  Hence FI < 2L.
assert odds > 2**13
assert FI < Fraction(52,3)

print("status=PASS")
print("conditional_bernoulli_coordinates=PASS")
print("local_compensation_determinant=36*r^2*y*(1-y)/(p00*p10*p01*p11)")
print("local_compensation_identity=PASS")
print("naive_coercivity_counterexample=PASS")
print("counterexample_x=4/5")
print("counterexample_y=4/5")
print("counterexample_r=9999/50000")
print("counterexample_direction=[[-1,1],[1,-1]]")
print("counterexample_atoms=", ",".join(str(p) for p in P))
print("counterexample_FI=", FI)
print("counterexample_odds=", odds)
print("exact_odds_margin_over_8192=", odds-Fraction(8192,1))
print("exact_52_over_3_minus_FI=", Fraction(52,3)-FI)
print("conclusion=For this direction det(U)=0 and b=1, so S_C(U)=FI<2L; the auxiliary bound S_C(U)>=2L*b^2 is false.")
print("global_X095_metric_certified=False")
