#!/usr/bin/env python3
"""R08 independent exact audit of the finite algebra in the newest R09
Tang Q4.11 simple Cayley C2*C3 transitive-subclass theorem.

This checks algebra only; it does not independently establish the global
free-product branching compiler beyond the written graph decomposition.
"""
import sympy as sp

p,t,u,v=sp.symbols("p t u v")

F2=1-p+p*t
F3=(1-p)**2+2*p*(1-p)**2*t+p**2*(3-2*p)*t**2
m2=sp.factor(sp.diff(F2,t).subs(t,1))
m3=sp.factor(sp.diff(F3,t).subs(t,1))
assert sp.factor(m2-p)==0
assert sp.factor(m3-2*p*(1+p-p**2))==0

M=sp.factor(m2*m3)
H=sp.factor(1-M)
assert sp.factor(M-2*p**2*(1+p-p**2))==0
assert sp.factor(H-(2*p**4-2*p**3-2*p**2+1))==0
assert sp.factor(sp.diff(M,p)-2*p*(2+3*p-4*p**2))==0

lo=sp.Rational(63727,100000)
hi=sp.Rational(3983,6250)
assert H.subs(p,lo)>0
assert H.subs(p,hi)<0

eq=sp.factor(u-(1-p+p*F3.subs(t,u)))
target=(u-1)*(2*p**4*u-3*p**3*u+p**3-2*p**2+1)
assert sp.factor(eq-target)==0

us=sp.factor(-(p-1)*(p**2-p-1)/(p**3*(2*p-3)))
vs=sp.factor((p-1)**2*(2*p**3-p**2-2*p-1)/(p**4*(2*p-3)))
assert sp.factor(us-(1-p+p*vs))==0
assert sp.factor(vs-F3.subs(t,us))==0
assert sp.factor((1-us)-H/(p**3*(2*p-3)))==0
assert sp.factor((1-vs)-H/(p**4*(2*p-3)))==0

theta=sp.factor(1-us*vs)
theta_claim=sp.factor(H*(2*p**5-3*p**4-p**3+2*p**2-1)/(p**7*(2*p-3)**2))
assert sp.factor(theta-theta_claim)==0

R=4*p**9-38*p**8+106*p**7-38*p**6-254*p**5+274*p**4+171*p**3-264*p**2-84*p+126
theta2_claim=4*(p-1)*R/(p**9*(2*p-3)**4)
assert sp.factor(sp.diff(theta,p,2)-theta2_claim)==0

b=[
sp.Rational(126),sp.Rational(350,3),sp.Rational(100),sp.Rational(2185,28),
sp.Rational(3464,63),sp.Rational(493,14),sp.Rational(291,14),
sp.Rational(413,36),sp.Rational(6),sp.Rational(3)]
assert all(x>0 for x in b)
bern=sp.expand(sum(b[j]*sp.binomial(9,j)*p**j*(1-p)**(9-j) for j in range(10)))
assert sp.factor(bern-R)==0

print("R08-AUDIT-R09-TANG-Q411-C2C3-TRANSITIVE-04")
print("block_pgfs_means = PASS")
print("critical_polynomial_and_exact_bracket = PASS")
print("fixed_point_elimination_and_physical_candidate_residuals = PASS")
print("theta_closed_form = PASS")
print("theta_second_derivative = PASS")
print("positive_Bernstein_certificate_for_R = PASS")
print("Conclusion: finite algebra supports theta''(p)<0 on the supercritical interval,")
print("given R09's written free-product branching/physical-branch argument.")
print("AUDIT_VERDICT = PASS_FOR_EXACT_FINITE_CORE")
print("ALL_EXACT_CHECKS_PASS")
