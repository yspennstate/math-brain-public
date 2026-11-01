#!/usr/bin/env python3
"""
Exact symbolic checker for HARD7-02 axis-family dilation calculation.

This checks only the algebraic identities used after the probabilistic/cavity
reduction. It is a self-check, not an independent proof of the PWIT limit or
Hermitization passage.
"""
import sympy as sp

p = sp.symbols("p", positive=True)
u, v = sp.symbols("u v", real=True)
alpha = sp.symbols("alpha", positive=True)
q = 1 - p
a = 2*p - 1
L = sp.log(p/q)
lam = a/L

# Balanced limit.
assert sp.simplify(sp.limit(lam, p, sp.Rational(1,2)) - sp.Rational(1,2)) == 0

# General Perron-profile identity is checked by its two algebraic pieces:
# f(u) = R^(u-1/2), K_p f = q int_u^1 f + p int_0^u f.
R = p/q
# Constant term in K_p f cancels:
const_cancel = sp.simplify(q*sp.sqrt(R) - p/sp.sqrt(R))
assert const_cancel == 0
# Remaining coefficient equals lambda_p:
assert sp.simplify((p-q)/L - lam) == 0

# Exact direct integral checks at representative rational p on both sides of 1/2.
for pv in [sp.Rational(1,4), sp.Rational(1,3), sp.Rational(2,3), sp.Rational(3,4)]:
    qv = 1-pv
    Lv = sp.log(pv/qv)
    lamv = (2*pv-1)/Lv
    fv = sp.exp(Lv*(v-sp.Rational(1,2)))
    fu = sp.exp(Lv*(u-sp.Rational(1,2)))
    Kv = qv*sp.integrate(fv, (v,u,1)) + pv*sp.integrate(fv, (v,0,u))
    assert sp.simplify(Kv - lamv*fu) == 0

# p <-> 1-p symmetry checked exactly on the formula by log(-) identity at p=1/4.
lam14 = sp.simplify(lam.subs(p, sp.Rational(1,4)))
lam34 = sp.simplify(lam.subs(p, sp.Rational(3,4)))
assert sp.simplify(lam14 - 1/(2*sp.log(3))) == 0
assert sp.simplify(lam34 - lam14) == 0

# Spatial dilation factor k_p=(2 lambda_p)^(1/alpha).
k14 = sp.log(3)**(-1/alpha)
assert sp.simplify((2*lam14)**(1/alpha) - k14) == 0

# For alpha=1, p=1/4:
k14_a1 = sp.simplify(k14.subs(alpha,1))
origin_density_ratio = sp.simplify(k14_a1**(-2))
assert sp.simplify(k14_a1 - 1/sp.log(3)) == 0
assert sp.simplify(origin_density_ratio - sp.log(3)**2) == 0

# Scaling-consistency identity for the scalar fixed-point equation:
# if lambda=lambda0*k^(2 beta), r=k^2 r0, y=k^2 y0, then
# lambda*(S'/(r+ySS'))^beta = lambda0*(S'/(r0+y0SS'))^beta.
beta, lam0, k, r0, y0, S, Sp = sp.symbols(
    "beta lam0 k r0 y0 S Sp", positive=True
)
lhs = lam0*k**(2*beta) * (Sp/(k**2*r0+k**2*y0*S*Sp))**beta
rhs = lam0 * (Sp/(r0+y0*S*Sp))**beta
assert sp.simplify(lhs-rhs) == 0

print("lambda_half_limit =", sp.limit(lam, p, sp.Rational(1,2)))
print("lambda_1_4 =", lam14)
print("k_1_4(alpha=1) =", k14_a1)
print("origin_density_ratio_1_4_vs_half(alpha=1) =", origin_density_ratio)
print("k_1_4(alpha=1) numeric =", sp.N(k14_a1, 18))
print("origin_density_ratio numeric =", sp.N(origin_density_ratio, 18))
print("ALL_EXACT_CHECKS_PASS = True")
