#!/usr/bin/env python3
# Exact symbolic certificate for C28 / I0032 three-state matched-hitting obstruction.
# All asserted algebraic identities are checked with SymPy exact arithmetic.

import sympy as sp

p = sp.symbols('p', positive=True)
nu = 4*p - 1
c = nu**2
R = 1 + 2*c/p

pi = [p/2, p/2, 1-p]
P = sp.Matrix([
    [0, 1/R, (2*c/p)/R],
    [1/R, 0, (2*c/p)/R],
    [(c/(1-p))/R, (c/(1-p))/R, 1 - (2*c/(1-p))/R],
])
L = sp.eye(3) - P

def z(x):
    return sp.factor(sp.simplify(x))

assert all(z(sum(P[i,j] for j in range(3)) - 1) == 0 for i in range(3))
for i in range(3):
    for j in range(i+1,3):
        assert z(pi[i]*P[i,j] - pi[j]*P[j,i]) == 0

vf = sp.Matrix([1,-1,0])
vs = sp.Matrix([1,1,-p/(1-p)])
lam_f = z((2 + 2*c/p)/R)
lam_s = z((2*c/(p*(1-p)))/R)
assert all(z(x)==0 for x in (L*vf - lam_f*vf))
assert all(z(x)==0 for x in (L*vs - lam_s*vs))

norm_f2 = z(sum(pi[i]*vf[i]**2 for i in range(3)))
norm_s2 = z(sum(pi[i]*vs[i]**2 for i in range(3)))
A = z(vs[0]**2 / norm_s2)
B = z(vf[0]**2 / norm_f2)
C = z(vs[2]**2 / norm_s2)
assert z(norm_f2-p) == 0
assert z(norm_s2-p/(1-p)) == 0
assert z(A-(1-p)/p) == 0
assert z(B-1/p) == 0
assert z(C-p/(1-p)) == 0

# Threshold gap identity.
assert z(3-A-nu/p) == 0

# Source normalization: rare-state total jump rate is exactly one.
rare_exit = z(P[0,1]+P[0,2])
assert z(rare_exit-1) == 0

# The common state's holding probability is nonnegative on 1/4<p<1/2:
# P22=[p(1-p)+2c(1-2p)]/[p(1-p)R], whose numerator is positive there.
common_hold_num = z(p*(1-p) + 2*c*(1-2*p))
assert z(P[2,2] - common_hold_num/(p*(1-p)*R)) == 0

# Matched threshold g(u)=u+sqrt(3u(1-u)); solve g(u)=1.
u = sp.symbols('u', real=True)
poly = sp.factor((1-u)**2 - 3*u*(1-u))
assert poly == (u-1)*(4*u-1)
assert z(poly.subs(u, sp.Rational(1,4))) == 0

g18 = sp.Rational(1,8) + sp.sqrt(3)*sp.sqrt(sp.Rational(1,8)*sp.Rational(7,8))
assert z(g18 - (1+sp.sqrt(21))/8) == 0

# Limits at p -> 1/4+.
p0 = sp.Rational(1,4)
assert sp.limit(lam_f, p, p0, dir='+') == 2
assert sp.limit(lam_s, p, p0, dir='+') == 0
assert sp.limit(A, p, p0, dir='+') == 3
assert sp.limit(B, p, p0, dir='+') == 4

# For any fixed T>0, the rare-state squared L2 distance tends to 3+4e^{-4T}>3.
T = sp.symbols('T', positive=True)
F = A*sp.exp(-2*lam_s*T) + B*sp.exp(-2*lam_f*T)
Flim = sp.simplify(sp.limit(F, p, p0, dir='+'))
assert Flim == 3 + 4*sp.exp(-4*T)

print('C28_I0032_THREE_STATE_HITTING_OBSTRUCTION_EXACT')
print('row_sums=1')
print('detailed_balance=PASS')
print('lambda_fast=', lam_f)
print('lambda_slow=', lam_s)
print('rare_L2_coeff_slow=', A)
print('rare_L2_coeff_fast=', B)
print('common_L2_coeff_slow=', C)
print('threshold_gap=nu/p')
print('rare_exit_rate_source_normalized=1')
print('g(1/8)=(1+sqrt(21))/8')
print('fixed_T_limit_d2rare_sq=', Flim)
print('ALL_EXACT_SYMBOLIC_CHECKS_PASS')
