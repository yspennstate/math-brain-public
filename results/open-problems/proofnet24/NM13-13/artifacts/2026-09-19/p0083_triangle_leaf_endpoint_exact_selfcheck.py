#!/usr/bin/env python3
"""Exact self-check for NM13-13 P0083 triangle+pendant endpoint theorem.

Checks only symbolic/rational algebra used in the 2026-09-19 report.
This is a self-check, not an independent audit.
"""
import sympy as sp

u,v,X,Y,q,s = sp.symbols("u v X Y q s")

# 1. Difference of the two triangle-vertex equilibrium equations at p=3.
F = u/(1+u)**4 - v/(1+v)**4 + (u-v)/(u+v)**4
num, den = sp.together(F).as_numer_denom()
B = sp.cancel(-num/(u-v))
assert sp.expand(num + (u-v)*B) == 0
Bxy = sp.Poly(sp.expand(B.subs({u:1+X, v:1+Y})), X, Y)
coeffs_B = [c for _, c in Bxy.terms()]
assert coeffs_B and all(c > 0 for c in coeffs_B)

# 2. q <= 1/3 would force the central triangle incidence nonpositive.
P = q**6 - 3*q**5 + 15*q**4 - 33*q**3 + 18*q**2 + 8*q + 2
E = 2*(1+q)**4*(1-q)**3 - q**3*(3-q)**4
assert sp.expand(E + (3*q-1)*P) == 0

# 3. Root-vs-leaf Rayleigh witness.
D = -2*q**2 + 5*q - 1
Q = (8*q**7 - 64*q**6 + 216*q**5 - 368*q**4
     + 307*q**3 - 107*q**2 + 17*q - 1)
E2 = D**4 - 8*q**3*(1-q)**5
assert sp.expand(E2 - (3*q-1)*Q) == 0

# 4. Exact Bernstein positivity of Q on [1/3,3/5].
n = 7
affine = sp.Rational(1,3) + sp.Rational(4,15)*s
Qs = sp.Poly(sp.expand(Q.subs(q, affine)), s)
a = [Qs.nth(j) for j in range(n+1)]
bern = [
    sp.simplify(sum(a[j]*sp.binomial(k,j)/sp.binomial(n,j)
                    for j in range(k+1)))
    for k in range(n+1)
]
expected = [
    sp.Rational(896,2187),
    sp.Rational(15616,25515),
    sp.Rational(1408,1575),
    sp.Rational(447296,354375),
    sp.Rational(1009024,590625),
    sp.Rational(52352,23625),
    sp.Rational(907136,328125),
    sp.Rational(260416,78125),
]
assert bern == expected
assert all(c > 0 for c in bern)

print("P0083_TRIANGLE_LEAF_ENDPOINT_EXACT_SELF_CHECK")
print("difference_factor_identity=PASS")
print("shifted_factor_term_count=", len(Bxy.terms()))
print("shifted_factor_min_coefficient=", min(coeffs_B))
print("q_one_third_factor_identity=PASS")
print("rayleigh_factor_identity=PASS")
print("bernstein_coefficients_Q_[1/3,3/5]=")
for c in bern:
    print(c)
print("bernstein_positivity=PASS")
print("EXACT_SELF_CHECK_PASS")
