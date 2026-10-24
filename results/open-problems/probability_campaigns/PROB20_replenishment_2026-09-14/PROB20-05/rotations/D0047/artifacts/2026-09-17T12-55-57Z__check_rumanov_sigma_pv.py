#!/usr/bin/env python3
"""
D0047 exact symbolic self-check for the source-side Rumanov one-pole reduction.

Checks algebraic consequences of specializing Rumanov's governing system
(2.24),(2.25) to the beta=2 Brownian-carousel real-line PDE after
r=s/2, t=-log r. This is a self-check, not an independent audit and
does not prove that the physical carousel boundary-value solution lies
in the one-pole Lax family.
"""
import sympy as sp

x,t=sp.symbols("x t")
r=sp.Function("r")(t)
Q=sp.Function("Q")(t)
J0=sp.Function("J0")(t)
sigma=1+x**2
v=2*x-r*sigma
bp=-sigma/(x-Q)
subs_rt={sp.diff(r,t):-r}

rho=sp.simplify((bp+v)/sigma)
rho_target=-1/(x-Q)+2*x/sigma-r
assert sp.simplify(rho-rho_target)==0

qdot=sp.diff(Q,t)
J=-r*x-qdot/(x-Q)+J0
assert sp.simplify(sp.diff(rho_target,t).subs(subs_rt)+sp.diff(J,x))==0

b1=sp.simplify((sp.diff(bp,x)-bp*rho_target-J)/2)
b1_target=-(J0+r*Q)/2+(qdot-r*(1+Q**2))/(2*(x-Q))
assert sp.simplify(b1-b1_target)==0

res=(sp.diff(b1,t)+sigma*sp.diff(b1,x,2)+v*sp.diff(b1,x)
     -(2*sp.diff(bp,x)-(sp.diff(sigma,x)/sigma)*bp)*b1)
res=sp.simplify(res.subs(subs_rt))
poly=sp.Poly(sp.cancel(-2*(x-Q)**2*res),x)
c2,c1,c0=[sp.factor(c) for c in poly.all_coeffs()]

J0dot=sp.diff(J0,t)
Qdd=sp.diff(Q,t,2)
J0dot_target=r*Q-r**2*(1+Q**2)
assert sp.simplify(c2.subs(J0dot,J0dot_target))==0

J0_target=sp.Rational(1,2)*(r**2*(1+Q**2)-2*r*Q-qdot**2/(1+Q**2))
Qdd_target=Q*qdot**2/(1+Q**2)+r*(1+Q**2)*(r*Q-1)
assert sp.simplify(c1.subs({J0dot:J0dot_target,J0:J0_target,Qdd:Qdd_target}))==0
assert sp.simplify(c0.subs({J0dot:J0dot_target,J0:J0_target,Qdd:Qdd_target}))==0

J0diff=sp.diff(J0_target,t).subs({sp.diff(r,t):-r,sp.diff(Q,t,2):Qdd_target})
assert sp.simplify(J0diff-J0dot_target)==0

y=sp.Function("y")(t)
yd=sp.diff(y,t)
ydd=sp.diff(y,t,2)
q_sub=sp.sinh(y)
qd_sub=sp.cosh(y)*yd
qdd_sub=sp.sinh(y)*yd**2+sp.cosh(y)*ydd
eq_y=sp.simplify((qdd_sub-Qdd_target.subs({Q:q_sub,qdot:qd_sub}))/sp.cosh(y))
eq_y_target=ydd-r*sp.cosh(y)*(r*sp.sinh(y)-1)
assert sp.simplify(sp.expand_trig(eq_y-eq_y_target))==0

R=sp.symbols("R", positive=True)
Y=sp.Function("Y")(R)
Yr=sp.diff(Y,R)
Yrr=sp.diff(Y,R,2)
C=sp.cosh(Y)
S=sp.sinh(Y)
Yrr_rule=S*C-C/R-Yr/R

Sigma=sp.Rational(1,4)*R**2*(Yr**2-C**2)
Sig1=sp.simplify(sp.expand_trig(sp.diff(Sigma,R).subs(Yrr,Yrr_rule)))
Sig1_target=-sp.Rational(1,2)*R*C*(C+Yr)
assert sp.simplify(Sig1-Sig1_target)==0

Sig2=sp.simplify(sp.expand_trig(sp.diff(Sig1_target,R).subs(Yrr,Yrr_rule)))
Sig2_target=-sp.Rational(1,2)*R*S*(C+Yr)**2
assert sp.simplify(Sig2-Sig2_target)==0

Rsig_minus=sp.simplify(R*Sig1_target-Sigma)
Rsig_minus_target=-sp.Rational(1,4)*R**2*(C+Yr)**2
assert sp.simplify(sp.expand_trig(Rsig_minus-Rsig_minus_target))==0

sigma_pv=sp.expand((R*Sig2_target)**2
    +4*Rsig_minus_target*(Rsig_minus_target+Sig1_target**2))
assert sp.simplify(sp.factor(sigma_pv))==0

a,b=sp.symbols("a b")
P=1+a*R+b*R**2
Q_R=P/R
Qdot_R=P/R-sp.diff(P,R)
J0_R=sp.Rational(1,2)*(R**2*(1+Q_R**2)-2*R*Q_R-Qdot_R**2/(1+Q_R**2))
Sigma_R=sp.simplify(-(J0_R+R*Q_R)/2)
assert sp.simplify(sp.limit(Sigma_R/R,R,0)+a)==0

print("Rumanov conservation-law specialization: PASS")
print("one-pole b_plus/b1 reduction: PASS")
print("J0 first integral and Q ODE: PASS")
print("Q=sinh(y) auxiliary equation: PASS")
print("sigma-PV identity from auxiliary equation: PASS")
print("small-r branch Sigma/r -> -a: PASS")
print("D0047 RUMANOV ONE-POLE SIGMA-PV EXACT CHECK PASSED")
