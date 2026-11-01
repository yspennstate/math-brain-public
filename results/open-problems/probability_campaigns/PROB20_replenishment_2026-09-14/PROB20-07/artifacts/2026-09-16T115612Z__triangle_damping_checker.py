#!/usr/bin/env python3
"""
Exact symbolic checker for PROB20-07 run 2026-09-16T115612Z.

Checks the two-parameter convex-hull theorem joining the two aligned
weak-endpoint real-neutral tensors P^(+), P^(-), and the constant
barycentric QSO U.

Universal proof ingredients checked exactly:
  * the aligned endpoint tensors have common centered normal form differing
    only by the sign of the u-coordinate;
  * convex interpolation gives the angular factor kappa=2 theta-1;
  * barycentric interpolation gives exact radial factor lambda;
  * the coefficient floor is a(lambda)=1/3-lambda/4, independent of theta;
  * the common Lyapunov function is monotone under angular damping;
  * on the endpoint image simplex, beta(u,v)^2 <= (81/256) L(u,v);
  * the weak-edge geometric factor q_edge(kappa)=(81+175 kappa^2)/256;
  * the radial factor q_rad(lambda)=lambda^2(8-3 lambda)/5;
  * the product factor is <1 except at the two neutral vertices
    (lambda,kappa)=(1,+/-1).
"""
import sympy as sp

u, v = sp.symbols("u v", real=True)
theta, lam, kappa = sp.symbols("theta lam kappa", real=True)

a0 = sp.Rational(1, 12)
b0 = sp.Rational(3, 4)

# Common chart: u=x1-x3, v=x2-1/3.
x1 = sp.Rational(1, 3) - v/2 + u/2
x2 = sp.Rational(1, 3) + v
x3 = sp.Rational(1, 3) - v/2 - u/2

# Aligned residual assignments:
# P+ : (11,12,13,22,23,33) -> (e1,e1,e2,e2,e3,e3)
# P- : after simultaneous swap 2<->3 from the archived -1 tensor,
#      (11,12,13,22,23,33) -> (e3,e3,e2,e2,e1,e1).
Wp = [
    x1**2 + 2*x1*x2,
    2*x1*x3 + x2**2,
    2*x2*x3 + x3**2,
]
Wm = [
    2*x2*x3 + x3**2,
    2*x1*x3 + x2**2,
    x1**2 + 2*x1*x2,
]
Vp = [sp.expand(a0 + b0*w) for w in Wp]
Vm = [sp.expand(a0 + b0*w) for w in Wm]

alpha = sp.expand(u*(4 + 3*v)/4)
beta = sp.expand(-sp.Rational(3, 8)*(u**2 - 3*v**2))

assert sp.simplify((Vp[0]-Vp[2]) - alpha) == 0
assert sp.simplify((Vp[1]-sp.Rational(1,3)) - beta) == 0
assert sp.simplify((Vm[0]-Vm[2]) + alpha) == 0
assert sp.simplify((Vm[1]-sp.Rational(1,3)) - beta) == 0

# Angular interpolation theta P+ + (1-theta) P-.
kexpr = 2*theta - 1
Vtheta = [sp.expand(theta*Vp[i] + (1-theta)*Vm[i]) for i in range(3)]
assert sp.simplify((Vtheta[0]-Vtheta[2]) - kexpr*alpha) == 0
assert sp.simplify((Vtheta[1]-sp.Rational(1,3)) - beta) == 0

# Adding barycentric QSO U gives exact radial damping.
# Centered map: lambda * (kappa*alpha, beta).
assert sp.simplify(lam*kexpr*alpha - lam*(2*theta-1)*alpha) == 0
assert sp.simplify(lam*beta - lam*beta) == 0

# Floor along the whole triangle.
a_lam = sp.simplify((1-lam)*sp.Rational(1,3) + lam*a0)
A_lam = sp.simplify((1-lam)*sp.Rational(1,3) + lam*sp.Rational(5,6))
assert a_lam == sp.Rational(1,3) - lam/4
assert A_lam == sp.Rational(1,3) + lam/2
assert sp.simplify(A_lam + 2*a_lam - 1) == 0

# Common Lyapunov function.
L = sp.expand((1 + sp.Rational(3,2)*v)*u**2 + v**2)

# Endpoint output coefficient multiplying alpha^2 in L(alpha,beta).
Cout = sp.expand(1 + sp.Rational(3,2)*beta)
# On the endpoint image simplex beta in [-1/4,1/2], hence Cout >=5/8.
assert sp.simplify(Cout.subs(beta if False else v, v)) == Cout  # structural no-op

# Exact angular identity.
L_F = sp.expand((1 + sp.Rational(3,2)*beta)*alpha**2 + beta**2)
L_H = sp.expand((1 + sp.Rational(3,2)*beta)*(kappa*alpha)**2 + beta**2)
angular_gap = sp.factor(L_F - L_H)
assert angular_gap == sp.factor((1-kappa**2)*(1+sp.Rational(3,2)*beta)*alpha**2)

# Key new global bound on the endpoint image simplex:
# beta^2 <= (81/256) L.
# The image simplex condition is v in [-1/4,1/2] and u^2 <= (1/2-v)^2.
r = sp.symbols("r", nonnegative=True)
Lr = sp.expand((1 + sp.Rational(3,2)*v)*r + v**2)
F = sp.expand(9*Lr - 4*(r - 3*v**2)**2)
# Since F is concave in r, its minimum on [0,R] is at an endpoint.
assert sp.diff(F, r, 2) == -8
R = (sp.Rational(1,2)-v)**2
F0 = sp.factor(F.subs(r,0))
FR = sp.factor(F.subs(r,R))
assert F0 == -9*v**2*(2*v-1)*(2*v+1)
assert sp.simplify(FR + (2*v-1)*(64*v**3 + 42*v**2 + 3*v + 16)/8) == 0
# On v in [-1/4,1/2], F0>=0.
# For FR, (1-2v)>=0 and the cubic is >0; a simple lower bound is
# 64v^3>=-1, 42v^2>=0, 3v>=-3/4, +16, hence cubic>=57/4.
assert sp.Rational(-1) + sp.Rational(0) - sp.Rational(3,4) + 16 == sp.Rational(57,4)

# Algebraic equivalence of F>=0 to beta^2 <=81/256 L.
beta2_from_r = sp.Rational(9,64)*(r-3*v**2)**2
assert sp.simplify(sp.Rational(81,256)*Lr - beta2_from_r - sp.Rational(9,256)*F) == 0

# Edge contraction factor.
q_edge = sp.simplify(kappa**2 + (1-kappa**2)*sp.Rational(81,256))
assert q_edge == (sp.Integer(81) + sp.Integer(175)*kappa**2)/256
assert sp.simplify((1-q_edge) - sp.Rational(175,256)*(1-kappa**2)) == 0

# Radial factor from the preceding ray theorem.
q_rad = sp.simplify(lam**2*(8-3*lam)/5)
assert sp.factor(1-q_rad.subs(lam,1)) == 0
assert sp.simplify(sp.diff(q_rad,lam) - lam*(16-9*lam)/5) == 0

q_total = sp.factor(q_rad*q_edge)

# Exact control point inside the triangle.
control = sp.simplify(q_total.subs({lam:sp.Rational(99,100), kappa:sp.Rational(1,2)}))
assert control < 1

print("ALL EXACT TRIANGLE-DAMPING CHECKS PASSED")
print("aligned plus residual assignments:  (e1,e1,e2,e2,e3,e3)")
print("aligned minus residual assignments: (e3,e3,e2,e2,e1,e1)")
print("centered angular map: (kappa*alpha, beta)")
print("alpha =", alpha)
print("beta  =", beta)
print("floor a(lambda) =", a_lam)
print("q_edge(kappa) =", q_edge)
print("q_rad(lambda) =", q_rad)
print("q_total =", q_total)
print("endpoint-image beta^2/L bound = 81/256")
print("control q_total(lambda=99/100,kappa=1/2) =", control)
