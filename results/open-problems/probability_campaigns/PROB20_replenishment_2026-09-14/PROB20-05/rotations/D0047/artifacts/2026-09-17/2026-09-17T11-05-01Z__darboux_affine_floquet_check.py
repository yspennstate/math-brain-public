#!/usr/bin/env python3
"""
D0047 exact symbolic self-check for the third Brownian-carousel/Painleve run.

Checks derived-before-code identities:
1) the general first-order time-dependent Darboux shift inside the
   hyperbolic quantum-PV Hamiltonian family;
2) the carousel source chain H0 -> H1 -> H2;
3) the exact no-go for extending H2 by the same three-term
   superpotential ansatz;
4) the source x=cot(alpha/2) generator form;
5) the first two coefficients in the +infinity connection-tail hierarchy.

This is a self-check only. It does NOT prove the missing global
monodromy/tau-function identification and does not close Virag Q9.
"""
import sympy as sp

z,t = sp.symbols("z t", real=True)
zet,eta,sigma = sp.symbols("zet eta sigma")
E = sp.exp(2*t)

def V(zet, eta, sigma):
    return (
        (2*zet**2-sp.Rational(1,8))/sp.cosh(z)**2
        + (sp.Rational(1,8)-2*eta**2)/sp.sinh(z)**2
        - E**2*sp.cosh(4*z)/16
        + (sigma-sp.Rational(1,2))*E*sp.cosh(2*z)
    )

def intertwiner_residual(V0, V1, a):
    # (d_t-H1)(d_z+a)=(d_z+a)(d_t-H0)
    r1 = sp.simplify(sp.trigsimp(V1 - (V0-sp.diff(a,z))))
    r0 = sp.simplify(sp.trigsimp(
        sp.diff(a,t) + sp.diff(V0,z) - sp.diff(a,z,2)/2
        + a*sp.diff(a,z)
    ))
    return r1, r0

# General signed Darboux law.
for eps in (1,-1):
    for sz in (1,-1):
        for se in (1,-1):
            Ac = -sp.Rational(1,2) + 2*sz*zet
            Bc = -sp.Rational(1,2) + 2*se*eta
            Cc = sp.Rational(eps,2)
            sig = sp.simplify((1-eps*(Ac+Bc))/2)
            zetp = zet-sp.Rational(sz,2)
            etap = eta-sp.Rational(se,2)
            sigp = sig-eps
            a = Ac*sp.tanh(z)+Bc*sp.coth(z)+Cc*E*sp.sinh(2*z)
            r1,r0 = intertwiner_residual(V(zet,eta,sig),V(zetp,etap,sigp),a)
            assert sp.simplify(sp.trigsimp(r1.rewrite(sp.exp))) == 0
            assert sp.simplify(sp.trigsimp(r0.rewrite(sp.exp))) == 0

# Carousel chain H0 -> H1 -> H2.
V0 = V(0,0,1)
V1 = V(sp.Rational(1,2),sp.Rational(1,2),0)
V2 = V(0,0,-1)

a0 = -sp.coth(2*z)+E*sp.sinh(2*z)/2
a1 =  sp.coth(2*z)+E*sp.sinh(2*z)/2

for left,right,a in ((V0,V1,a0),(V1,V2,a1)):
    r1,r0 = intertwiner_residual(left,right,a)
    assert sp.simplify(sp.trigsimp(r1.rewrite(sp.exp))) == 0
    assert sp.simplify(sp.trigsimp(r0.rewrite(sp.exp))) == 0

# H2=(zet,eta,sigma)=(0,0,-1): in the same ansatz,
# the singular-residue conditions force A=B=-1/2.
A2=B2=-sp.Rational(1,2)
# The exponential balance forces C=eps/2. The remaining hyperplane is
# eps*(A+B)+2*sigma-1=0, which fails for both eps signs.
for eps in (1,-1):
    hyper = sp.simplify(eps*(A2+B2) + 2*(-1)-1)
    assert hyper != 0
assert (-1*(A2+B2) + 2*(-1)-1) == -2
assert ( 1*(A2+B2) + 2*(-1)-1) == -4

# Source x=cot(alpha/2) generator.
alpha,s = sp.symbols("alpha s", positive=True)
x = sp.symbols("x", real=True)
dx_da = -(1+x**2)/2
d2x_da2 = x*(1+x**2)/2
# L = s*d_alpha + 2(1-cos alpha)*d_alphaalpha,
# with 1-cos alpha = 2/(1+x^2).
coef_uxx = sp.simplify(4/(1+x**2) * dx_da**2)
coef_ux = sp.simplify(s*dx_da + 4/(1+x**2)*d2x_da2)
assert coef_uxx == 1+x**2
assert coef_ux == 2*x - s*(1+x**2)/2

# +infinity connection-tail hierarchy.
# U=G+a1/x+a2/x^2+a3/x^3+... in
# s U_s=(1+x^2)U_xx+(2x-s(1+x^2)/2)U_x.
G = sp.Function("G")(s)
a_1 = sp.Function("a1")(s)
a_2 = sp.Function("a2")(s)
a_3 = sp.Function("a3")(s)
U = G+a_1/x+a_2/x**2+a_3/x**3
rhs = (1+x**2)*sp.diff(U,x,2)+(2*x-s*(1+x**2)/2)*sp.diff(U,x)
lhs = s*sp.diff(U,s)
# Expand after w=1/x about w=0.
w=sp.symbols("w")
res = sp.expand((lhs-rhs).subs(x,1/w))
series = sp.series(res,w,0,3).removeO().expand()
c0 = sp.simplify(series.coeff(w,0))
c1 = sp.simplify(series.coeff(w,1))
assert sp.simplify(c0 - s*(sp.diff(G,s)-a_1/2)) == 0
assert sp.simplify(c1 - s*(sp.diff(a_1,s)-a_2)) == 0

print("D0047 DARBOUX-AFFINE/FLOQUET-BRIDGE EXACT CHECK PASSED")
print("general Darboux shift: zet' = zet-sz/2, eta' = eta-se/2, sigma' = sigma-eps")
print("hyperplane: eps*(A+B)+2*sigma-1 = 0")
print("carousel chain: (0,0,1) -> (1/2,1/2,0) -> (0,0,-1)")
print("same-ansatz H2 continuation: IMPOSSIBLE for eps=+/-1")
print("x-generator: s U_s=(1+x^2)U_xx+(2x-s(1+x^2)/2)U_x")
print("tail: a1=2 G'(s), a2=a1'(s)=2 G''(s)")
