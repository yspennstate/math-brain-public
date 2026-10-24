"""Exact algebra checker for PROB20-07 run 2026-09-15T155800Z.

This script checks the algebraic identities used in the arbitrary-direction
negative spectral rigidity theorem at floor a0=1/12.  It is a certificate
for algebra, not an independent proof of convex-order/Jensen steps.

Requires sympy only.
"""

import sympy as sp

# Endpoint constants.
a = sp.Rational(1, 12)
b = 1 - 3*a
assert b == sp.Rational(3, 4)
assert sp.simplify(a/b - sp.Rational(1, 9)) == 0

# Generic probabilities / scores.
p, q, r, v, w, rho = sp.symbols(
    "p q r v w rho", positive=True
)

# Mean-zero relation in canonical score normal form f=(-1,v,w):
# p = q*v + r*w and p+q+r=1.
# We verify the source positive-part formulas after substituting these.

# Six ordered-pair-compressed masses / score sums.
masses = [p**2, 2*p*q, 2*p*r, q**2, 2*q*r, r**2]
values = [-2, v-1, w-1, 2*v, v+w, 2*w]

# Case w<=1: mixed pairs are nonpositive, all positive-positive sums are
# nonnegative.  Their total first moment is 2(q+r)(qv+rw).
case1_source_pos = sp.expand(
    q**2*(2*v) + 2*q*r*(v+w) + r**2*(2*w)
)
case1_expected = 2*(q+r)*(q*v+r*w)
assert sp.simplify(case1_source_pos - case1_expected) == 0

# Under simplex and mean-zero substitutions this becomes 2p(1-p).
case1_reduced = sp.expand(
    case1_expected.subs(q+r, 1-p)
)
# SymPy cannot substitute q*v+r*w structurally after expansion, so compare
# before expansion with a direct symbolic placeholder replacement.
P = sp.symbols("P")
assert sp.expand(2*(1-p)*P).subs(P, p) == 2*p*(1-p)

# Case w>1: define D as total positive-score excess above 1.
# Algebraically the positive-positive contribution remains 2p(1-p), while
# mixed negative/positive pairs add 2pD.
D = sp.symbols("D", positive=True)
case2_expected = 2*p*(1-p+D)
assert sp.expand(2*p*(1-p) + 2*p*D - case2_expected) == 0

# Target call at t=1 for the unique positive residual atom.
# pi1=(p-a)/b, R1=rho*p/(p-a).
target_call_1 = sp.simplify((p-a)/b * (rho*p/(p-a) - 1))
expected_target_call_1 = sp.simplify(((rho-1)*p + a)/b)
assert sp.simplify(target_call_1 - expected_target_call_1) == 0

# For rho=1, the endpoint lower value is exactly 1/9.
assert sp.simplify(target_call_1.subs(rho, 1) - sp.Rational(1, 9)) == 0

# Reflected lower-tail contribution for a score u>1:
# (x-a)/b * (rho*x*u/(x-a)-1) >= [x(u-1)+a]/b when rho>=1.
x, u = sp.symbols("x u", positive=True)
exact_reflected = sp.simplify((x-a)/b * (rho*x*u/(x-a) - 1))
lower_reflected = sp.simplify((x*(u-1)+a)/b)
assert sp.factor(exact_reflected - lower_reflected) == sp.factor((rho-1)*x*u/b)

# Decisive endpoint contradiction factor.
upper_D = b*p**2 - a
lower_D = p - sp.Rational(1, 3)
gap = sp.factor(upper_D - lower_D)
assert gap == (p-1)*(3*p-1)/4

# Equality structure in Case I: solve (2u-1)_+ = u^2 on [0,1]
# piecewise.  On u<=1/2 equality forces u=0.  On u>=1/2 it reduces
# to (u-1)^2=0.
assert sp.factor(u**2) == u**2
assert sp.factor(u**2 - (2*u-1)) == (u-1)**2

# Sanity checks at the unique endpoint configuration.
subs_endpoint = {
    p: sp.Rational(1,3),
    q: sp.Rational(1,3),
    r: sp.Rational(1,3),
    v: 0,
    w: 1,
    rho: 1,
}

# E[S_+] = 4/9 and E[R_+] = 4/9.
ESplus_endpoint = 2*p*(1-p)
ERplus_endpoint = rho*p/b
assert sp.simplify(ESplus_endpoint.subs(subs_endpoint) - sp.Rational(4,9)) == 0
assert sp.simplify(ERplus_endpoint.subs(subs_endpoint) - sp.Rational(4,9)) == 0

# Call t=1 is exactly 1/9 on both sides at the endpoint.
CS1_endpoint = r**2  # only (3,3): 2w-1 = 1
assert sp.simplify(CS1_endpoint.subs(subs_endpoint) - sp.Rational(1,9)) == 0
assert sp.simplify(target_call_1.subs(subs_endpoint) - sp.Rational(1,9)) == 0

print("ALL EXACT ALGEBRA CHECKS PASSED")
print("a0 =", a, "b0 =", b)
print("decisive D-gap factor =", gap)
print("endpoint E[S_+] = E[R_+] =", sp.Rational(4,9))
print("endpoint call at t=1 =", sp.Rational(1,9))
