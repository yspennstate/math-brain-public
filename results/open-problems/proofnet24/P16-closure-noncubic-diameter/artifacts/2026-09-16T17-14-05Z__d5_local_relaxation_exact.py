#!/usr/bin/env python3
from fractions import Fraction as F
# Zhu Lemma 2.5 lower-envelope data for fixed d=5 and a small cut k=q_a=1.
d=5; k=1
p=[k]+[t*(d-t+1)-k for t in range(1,d)]
assert p==[1,4,7,8,7]
# Explicit nonnegative x with sum 1.
x=[F(124,175),F(31,175),F(0),F(8,175),F(12,175)]
assert sum(x)==1
Q=sum(F(p[i])*x[i]*x[i] for i in range(d))
Q += sum(F(p[i]+p[i+1]-d)*x[i]*x[i+1] for i in range(d-1))
print('d',d,'k',k,'p',p)
print('x',*[str(z) for z in x])
print('sum_x',sum(x))
print('Q',Q)
print('path_constant_alpha=d*Q',d*Q)
print('desired_odd_d_candidate_alpha=d-1',d-1)
assert Q==F(124,175)
assert d*Q==F(124,35)
assert d*Q < d-1
print('CLAIM: the tridiagonal/lower-envelope relaxation alone cannot certify alpha=d-1 at d=5 from this local block.')
print('SCOPE: obstruction to this relaxation only; not a counterexample graph and not a disproof of Conjecture 5.4.')
print('ALL_EXACT_CHECKS_PASSED')
