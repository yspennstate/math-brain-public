#!/usr/bin/env python3
"""Exact symbolic checks for PROB20-07 final B1 two-cycle closure.

This script checks algebra only. Inequality signs used in the proof are
explained in the accompanying report.
"""

import sympy as sp

A, B, X, Y, S, P = sp.symbols("A B X Y S P", real=True)
a = sp.Rational(1, 12)
b = sp.Rational(3, 4)

SX = X + Y
PX = X * Y
Cxy = 1 - SX
txy = (Cxy - B) / (A - B)

x1, y1 = X, Y
x2 = txy * (A + Y)
y2 = txy * (A + X)
x3 = (1 - txy) * (B + Y)
y3 = (1 - txy) * (B + X)

r1 = Y / X
r2 = (A + X) / (A + Y)
r3 = (B + X) / (B + Y)

Ux = [x1**2, 2*x1*x2, 2*x1*x3, x2**2, 2*x2*x3, x3**2]
Uy = [y1**2, 2*y1*y2, 2*y1*y3, y2**2, 2*y2*y3, y3**2]

assert sp.simplify(r1*r2 - 1 + A*(X-Y)/(X*(A+Y))) == 0
assert sp.simplify(r1*r3 - 1 + B*(X-Y)/(X*(B+Y))) == 0

lam22 = sp.simplify(r2**2)
src22 = sp.simplify((Uy[4]-lam22*Ux[4]) + (Uy[5]-lam22*Ux[5]))
claim_src22 = ((X-Y)*(A-Cxy)*(A*(2-SX)+SX*Cxy+2*PX)/(A+Y)**2)
assert sp.simplify(src22-claim_src22) == 0

tgt22 = sp.simplify((X-a)-lam22*(Y-a))
claim_tgt22 = ((X-Y)*(A**2+2*a*A-PX+a*SX)/(A+Y)**2)
assert sp.simplify(tgt22-claim_tgt22) == 0

C = 1-S
D = b*(A-C)*(A*(2-S)+S*C+2*P) - (A**2+2*a*A-P+a*S)
Dmax = sp.factor(D.subs(P,S**2/4))
claim_Dmax = -sp.Rational(1,24)*(2*A+S)*(9*A*S-6*A+9*S**2-33*S+20)
assert sp.simplify(Dmax-claim_Dmax) == 0

L = (9*S**2-33*S+20)/(6-9*S)
claim_L_gap = (9*S**2-6*S+2)/(3*(2-3*S))
assert sp.simplify((L-3)-claim_L_gap) == 0

lam12 = sp.simplify(r1*r2)
src12 = sp.simplify((Uy[2]-lam12*Ux[2]) + (Uy[3]-lam12*Ux[3]) + (Uy[4]-lam12*Ux[4]) + (Uy[5]-lam12*Ux[5]))
claim_src12 = ((X-Y)*(A*(1+PX)+PX*SX)/(X*(A+Y)))
assert sp.simplify(src12-claim_src12) == 0

T1 = sp.simplify((X-a)-lam12*(Y-a))
claim_T1 = ((X-Y)*(A*(SX-a)+PX)/(X*(A+Y)))
assert sp.simplify(T1-claim_T1) == 0

T2 = sp.simplify((x2-a)-lam12*(y2-a))
claim_T2 = ((X-Y)*(txy*(A**2-PX)-a*A)/(X*(A+Y)))
assert sp.simplify(T2-claim_T2) == 0

T3 = sp.simplify((x3-a)-lam12*(y3-a))
claim_T3 = -((X-Y)*(txy*(A**2-PX)-A*(Cxy-a)+PX)/(X*(A+Y)))
assert sp.simplify(T3-claim_T3) == 0

t = (1-S-B)/(A-B)
E = sp.expand(12*t*(A**2-P) + A*(12*S-11-9*P) + P*(12-9*S))
poly = sp.factor((A-B)*E)

N0 = sp.expand(A**2*(1-9*P) + A*P*(12-9*S) - 12*P*(1-S))
N1 = sp.expand(A*(11-12*A-12*S+9*P) + 9*P*S)
assert sp.simplify(poly-(N0+B*N1)) == 0

Sv = sp.Rational(2,5)
Yv = sp.Rational(9,50)
Xv = Sv-Yv
Av = sp.Integer(4)
Bv = -sp.Rational(1,100)
Cv = 1-Sv
tv = (Cv-Bv)/(Av-Bv)

xv = [Xv, tv*(Av+Yv), (1-tv)*(Bv+Yv)]
yv = [Yv, tv*(Av+Xv), (1-tv)*(Bv+Xv)]
rv = [sp.simplify(yv[i]/xv[i]) for i in range(3)]

assert all(v >= a for v in xv+yv)
assert rv[0] < 1 < rv[1] <= rv[2]
assert rv[0]*rv[1] < 1
assert 1 < rv[0]*rv[2] < rv[1]**2

Pv = Xv*Yv
Ev = sp.simplify(E.subs({S:Sv,P:Pv,A:Av,B:Bv}))
assert Ev > 0

print("ALL EXACT B1 CLOSURE CHECKS PASSED")
