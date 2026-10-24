#!/usr/bin/env python3
import sympy as sp

x,y,eps = sp.symbols("x y eps", real=True)
z = 1-x-y
e2 = sp.expand(x*y + y*z + z*x)
h = sp.expand(e2 - sp.Rational(1,4))
w = sp.expand(2 + eps*h)

# Exact simplex integrals.
I_e2 = sp.integrate(sp.integrate(e2, (y,0,1-x)), (x,0,1))
I_h = sp.integrate(sp.integrate(h, (y,0,1-x)), (x,0,1))
I_w = sp.simplify(sp.integrate(sp.integrate(w, (y,0,1-x)), (x,0,1)))
assert I_e2 == sp.Rational(1,8)
assert I_h == 0
assert I_w == 1

# Exact marginal and moments.
f = sp.factor(sp.integrate(w, (y,0,1-x)))
f_expected = sp.factor((1-x)*(2 - eps*(10*x**2-8*x+1)/12))
assert sp.simplify(f-f_expected) == 0
mass = sp.simplify(sp.integrate(f,(x,0,1)))
mean = sp.simplify(sp.integrate(x*f,(x,0,1)))
assert mass == 1
assert mean == sp.Rational(1,3)

fp = sp.factor(sp.diff(f,x))
fp_expected = (eps*(10*x**2-12*x+3)-8)/4
assert sp.simplify(fp-fp_expected) == 0

p = 10*x**2-12*x+3
assert p.subs(x,0) == 3
assert p.subs(x,1) == 1
assert sp.diff(p,x).subs(x,sp.Rational(3,5)) == 0
assert p.subs(x,sp.Rational(3,5)) == -sp.Rational(3,5)

# Endpoint cases certify the full monotonicity interval by the convex/concave argument:
# eps >= 0: max p=3 -> eps <= 8/3.
# eps <= 0: max eps*p occurs at min p=-3/5 -> eps >= -40/3.
eps_lo = -sp.Rational(40,3)
eps_hi = sp.Rational(8,3)
assert sp.simplify(eps_hi*3-8) == 0
assert sp.simplify(eps_lo*(-sp.Rational(3,5))-8) == 0

# e2 ranges from 0 to 1/3 on the simplex.
# Check target-density worst cases over the proved epsilon interval.
w_min_pos = sp.simplify(2 - eps_hi/sp.Integer(4))  # eps>=0, e2=0
w_max_pos = sp.simplify(2 + eps_hi/sp.Integer(12)) # eps>=0, e2=1/3
w_min_neg = sp.simplify(2 + eps_lo/sp.Integer(12)) # eps<=0, e2=1/3
w_max_neg = sp.simplify(2 - eps_lo/sp.Integer(4))  # eps<=0, e2=0
assert w_min_pos == sp.Rational(4,3)
assert w_max_pos == sp.Rational(20,9)
assert w_min_neg == sp.Rational(8,9)
assert w_max_neg == sp.Rational(16,3)

# Uniform-simplex proposal density is 2. Universal rejection constant C=8/3,
# so acceptance probability is 3*w/16 and average acceptance is 3/8.
C = sp.Rational(8,3)
assert w_max_neg/2 == C
assert sp.simplify(1/C) == sp.Rational(3,8)

print("I_e2 =", I_e2)
print("marginal =", f)
print("mass =", mass, "mean =", mean)
print("derivative =", fp)
print("epsilon_interval =", eps_lo, eps_hi)
print("joint_density_range_endpoints =", w_min_neg, w_max_neg, w_min_pos, w_max_pos)
print("universal_rejection_C =", C, "mean_acceptance =", sp.Rational(3,8))
print("ALL EXACT CHECKS PASSED")
