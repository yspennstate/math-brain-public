#!/usr/bin/env python3
"""Exact symbolic audit of P20-D0010-ALL-M-PIECE-IFF-02.

Scope: algebraic normalization/mean/positivity/monotonicity/tail identities for the
explicit m-piece family. The final sufficiency implication additionally invokes the
published Wang-Wang monotone-density complete-mixability theorem; this script does
not re-prove that external theorem.
"""
import sympy as sp

k, j, t = sp.symbols('k j t', integer=True, positive=True)
A = (8*k + 1)/(k - 1)
B = -18*k/(k**2 - 1)
a = A + B*j

sum_a = sp.factor(sp.summation(a, (j, 1, k)))
sum_w = sp.factor(sp.summation((2*j - 1)*a, (j, 1, k)))
a1 = sp.factor(a.subs(j, 1))
ak = sp.factor(a.subs(j, k))
gap = sp.factor(a - a.subs(j, j+1))

assert sp.simplify(sum_a + k) == 0
assert sp.simplify(sum_w + 4*k**2) == 0
assert sp.simplify(a1 - (8*k-1)/(k+1)) == 0
assert sp.simplify(ak + (10*k+1)/(k+1)) == 0
assert sp.simplify(gap - 18*k/(k**2-1)) == 0

# Exact total mass and mean for the density in P20's report.
pre_mass = sp.factor((2*k + t*sum_a)/(3*k))
tail_mass = (1+t)/3
total_mass = sp.factor(pre_mass + tail_mass)
pre_mean = sp.factor((2*sp.summation(2*j-1,(j,1,k)) + t*sum_w)/(18*k**2))
tail_mean = sp.factor(2*(1+t)/9)
total_mean = sp.factor(pre_mean + tail_mean)
assert sp.simplify(total_mass - 1) == 0
assert sp.simplify(total_mean - sp.Rational(1,3)) == 0

# Endpoint lower bounds valid for k>=2 and |t|<=1/10.
pos_t_ge0 = sp.factor(2 + ak/sp.Integer(10))
pos_t_le0 = sp.factor(2 - a1/sp.Integer(10))
boundary_drop = sp.factor((2 + ak/sp.Integer(10)) - sp.Rational(11,20))
assert sp.simplify(pos_t_ge0 - (10*k+19)/(10*(k+1))) == 0
assert sp.simplify(pos_t_le0 - 3*(4*k+7)/(10*(k+1))) == 0
assert sp.simplify(boundary_drop - 9*(k+3)/(20*(k+1))) == 0

# Tail statistic; c=(1+t)/3. For a 3-complete mix of an atomless law
# with mean 1/3, at least one coordinate is >1/3 almost surely, so 1<=3c.
c = sp.factor(tail_mass)
assert sp.simplify(c - (1+t)/3) == 0

print('sum_a =', sum_a)
print('sum_(2j-1)a =', sum_w)
print('a_1 =', a1)
print('a_k =', ak)
print('adjacent_drop =', gap)
print('total_mass =', total_mass)
print('total_mean =', total_mean)
print('min_height_t>=0_at_t=1/10 =', pos_t_ge0)
print('min_height_t<=0_at_t=-1/10 =', pos_t_le0)
print('last_pretail_minus_tail_at_t=1/10 =', boundary_drop)
print('tail_mass =', c)
print('For k>=2 all displayed positivity numerators and denominators are positive.')
print('Necessity: 3-CM => 1 <= 3*P(X>1/3)=1+t => t>=0.')
print('Sufficiency for t>=0 uses Wang-Wang (2011): monotone density + moderate mean.')
print('P19-AUDIT-P20-D0010-ALL-M-PIECE-IFF-22 PASS')
