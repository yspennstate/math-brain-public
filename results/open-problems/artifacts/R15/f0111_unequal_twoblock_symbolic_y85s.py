#!/usr/bin/env python3
import sympy as sp

# Exact symbolic self-check for R15 unequal-amplitude two-block reduction.
# No floating-point sampling is used.

m, d, k, r, s = sp.symbols("m d k r s", real=True)
A, B = sp.symbols("A B", positive=True)

def esimp(expr):
    return sp.simplify(sp.expand(sp.trigsimp(expr).rewrite(sp.exp)))

alpha = m / sp.sinh(m)

# U(s)=A exp((m+d)s)+B exp(-(m-d)s)
U = A*sp.exp((m+d)*s) + B*sp.exp(-(m-d)*s)
ode = sp.diff(U,s,2) - 2*d*sp.diff(U,s) - (m**2-d**2)*U
assert esimp(ode) == 0
print("PASS ODE: U''-2 d U'-(m^2-d^2)U=0")

u0 = A+B
u1 = A*sp.exp(m+d)+B*sp.exp(-(m-d))
up0_direct = (m+d)*A - (m-d)*B
up1_direct = (m+d)*A*sp.exp(m+d) - (m-d)*B*sp.exp(-(m-d))

up0_transfer = d*u0 + alpha*(sp.exp(-d)*u1-u0*sp.cosh(m))
up1_transfer = d*u1 + alpha*(u1*sp.cosh(m)-sp.exp(d)*u0)
assert esimp(up0_transfer-up0_direct) == 0
assert esimp(up1_transfer-up1_direct) == 0
print("PASS endpoint transfer formulas")

# Normalize S(0)=1, C=k, S(1)=r; hence U0=1-k, U1=r-k.
v0 = 1-k
v1 = r-k
p0 = d*v0 + alpha*(sp.exp(-d)*v1-v0*sp.cosh(m))
p1 = d*v1 + alpha*(v1*sp.cosh(m)-sp.exp(d)*v0)
H = sp.expand(p0 + p1/r - 2*sp.log(r))

P = alpha*sp.exp(-d)
beta = d*k + alpha*(sp.exp(d)*(1-k)+k*sp.cosh(m))

assert esimp(sp.diff(H,r) - (P - 2/r + beta/r**2)) == 0
print("PASS H'(r)=P-2/r+beta/r^2")

H1_target = 2*(1-k)*(d-m*sp.sinh(d)/sp.sinh(m))
assert esimp(H.subs(r,1)-H1_target) == 0
print("PASS H(1)=2(1-k)[d-m sinh(d)/sinh(m)]")

L = d + alpha*(sp.cosh(m)-sp.exp(d))
pb_target = alpha**2 + k*alpha*sp.exp(-d)*L
assert esimp(P*beta-pb_target) == 0
print("PASS P*beta=alpha^2+k alpha e^{-d} L")

assert esimp(L.subs(d,m)) == 0
assert esimp(L.subs(d,-m)) == 0
assert esimp(sp.diff(L,d,2) + alpha*sp.exp(d)) == 0
print("PASS L(±m)=0 and L''=-alpha e^d")

Kappa = (1-alpha**2)/(alpha*sp.exp(-d)*L)
Kappa_balanced = ((sp.sinh(m)/m)**2-1)/(sp.cosh(m)-1)
assert esimp(Kappa.subs(d,0)-Kappa_balanced) == 0
print("PASS unequal threshold reduces to prior balanced kappa at d=0")

print("ALL_EXACT_SYMBOLIC_CHECKS_PASS")
