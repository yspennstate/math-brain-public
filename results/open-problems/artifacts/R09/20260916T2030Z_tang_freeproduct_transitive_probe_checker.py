#!/usr/bin/env python3
import sympy as sp

p,t,u,v = sp.symbols('p t u v')

# R09 exact checker for Tang Question 4.11, transitive probe.
# Simple Cayley graph G = Cay(C2 * C3, {a,b,b^{-1}}).
# C2 factor block is one simple edge; C3 factor block is one triangle.
F2 = 1-p+p*t
F3 = (1-p)**2 + 2*p*(1-p)**2*t + p**2*(3-2*p)*t**2

assert sp.expand(F2.subs(t,1)) == 1
assert sp.expand(F3.subs(t,1)) == 1

m2 = sp.factor(sp.diff(F2,t).subs(t,1))
m3 = sp.factor(sp.diff(F3,t).subs(t,1))
assert m2 == p
assert sp.expand(m3-2*p*(1+p-p**2)) == 0

# Criticality for the two-type Galton-Watson compiler:
# mean matrix [[0,m2],[m3,0]], so rho^2 = m2*m3.
H = sp.factor(1-m2*m3)
assert H == 2*p**4 - 2*p**3 - 2*p**2 + 1
assert sp.expand(sp.diff(m2*m3,p)-2*p*(2+3*p-4*p**2)) == 0

# Exact rational bracket for the unique root pc in (0,1).
plo = sp.Rational(63727,100000)
phi = sp.Rational(3983,6250) # 0.63728
assert H.subs(p,plo) > 0
assert H.subs(p,phi) < 0

# Fixed-point equations u=F2(v), v=F3(u).
elim = sp.factor(u - F2.subs(t,F3.subs(t,u)))
Q = sp.factor(elim/(u-1))
Q_expected = 2*p**4*u - 3*p**3*u + p**3 - 2*p**2 + 1
assert sp.expand(Q-Q_expected) == 0

u_phys = sp.factor(-(p-1)*(p**2-p-1)/(p**3*(2*p-3)))
v_phys = sp.factor((u_phys-1+p)/p)
assert sp.simplify(u_phys - F2.subs(t,v_phys)) == 0
assert sp.simplify(v_phys - F3.subs(t,u_phys)) == 0
assert sp.factor(1-u_phys) == H/(p**3*(2*p-3))
assert sp.factor(1-v_phys) == H/(p**4*(2*p-3))

theta = sp.factor(1-u_phys*v_phys)
theta2 = sp.factor(sp.diff(theta,p,2))

R = (4*p**9 - 38*p**8 + 106*p**7 - 38*p**6 - 254*p**5
     + 274*p**4 + 171*p**3 - 264*p**2 - 84*p + 126)
theta2_expected = sp.factor(4*(p-1)*R/(p**9*(2*p-3)**4))
assert sp.simplify(theta2-theta2_expected) == 0

# Exact positive Bernstein representation of R on [0,1].
bern_coeffs = [
    sp.Rational(126),
    sp.Rational(350,3),
    sp.Rational(100),
    sp.Rational(2185,28),
    sp.Rational(3464,63),
    sp.Rational(493,14),
    sp.Rational(291,14),
    sp.Rational(413,36),
    sp.Rational(6),
    sp.Rational(3),
]
bern = sum(
    bern_coeffs[j]*sp.binomial(9,j)*p**j*(1-p)**(9-j)
    for j in range(10)
)
assert sp.expand(bern-R) == 0
assert all(c>0 for c in bern_coeffs)

# Prior-art convention sanity check:
# if the order-two generator is counted with its inverse as a parallel edge,
# its effective factor-connection probability is r=1-(1-p)^2.
# This recovers Kozakova's published modular-group critical polynomial.
r_parallel = 1-(1-p)**2
koz_poly = sp.expand(r_parallel*m3-1)
koz_expected = 2*p**5 - 6*p**4 + 2*p**3 + 4*p**2 - 1
assert sp.expand(koz_poly-koz_expected) == 0

# Retained periodic-tree metric sanity.
theta3=2*p**2-p
assert sp.diff(theta3,p,2)==4

print("R09 Tang Q4.11 exact checker")
print("graph = Cay(C2*C3,{a,b,b^{-1}}), simple degree 3")
print("F2 =", sp.factor(F2))
print("F3 =", sp.factor(F3))
print("critical H(p) =", H)
print("pc bracket = (63727/100000, 3983/6250)")
print("physical u =", u_phys)
print("physical v =", v_phys)
print("theta =", theta)
print("theta'' =", theta2_expected)
print("R Bernstein coefficients =", bern_coeffs)
print("all Bernstein coefficients positive => theta''<0 for pc<p<1")
print("parallel-involution convention gives Kozakova polynomial =", koz_poly)
print("retained stem metric remains unbounded above; T3 theta'' =", sp.diff(theta3,p,2))
print("PASS")
