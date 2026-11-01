"""Reproduce agent 002's exact algebra and diagnostic numerical tables.

No numerical search establishes an asymptotic theorem. The proofs are in
agents/002.md. Uses only the Python standard library.
"""
from fractions import Fraction
from math import factorial, log, sqrt, lgamma

print('F0060 factorial class ratio; m=n-1:')
for n in (4, 10, 100, 1000):
    m = n - 1
    ratio = Fraction(n - 1, m)
    upper = 1 / (1 + ratio)
    print(n, m, 'split/all=', ratio, 'P(all) <=', upper)

print('\nF0060 omitted assignment entropy; n=m, counts of 0,1,2 all n/3:')
for n in (30, 300, 3000, 30000):
    log_type = lgamma(n + 1) - 3 * lgamma(n // 3 + 1)
    print(n, 'log(type)/n=', log_type/n,
          '(log(type)-n)/sqrt(n)=', (log_type-n)/sqrt(n))

print('\nF0059 exact pi_a=1/[4a^3] (a>=1), epsilon=1/2:')
def rate(a):
    return (-log(4) - 2*log(a))/a
for a in (10**2, 10**4, 10**6, 10**8, 10**10):
    gap = rate(a) - rate(a//2)
    print(a, 'gap=', gap, 'sqrt(a)*gap=', sqrt(a)*gap)

print('\nC0033 rational four-atom and second-derivative identities:')
a, b, c = Fraction(2,5), Fraction(3,5), Fraction(1,10)
u, s, v = Fraction(2,3), Fraction(3,4), Fraction(1,5)
p = [(1-a)*(1-b)-c*c, a*(1-b)+c*c,
     (1-a)*b+c*c, a*b-c*c]
dp = [-(1-b)*u-(1-a)*s-2*c*v,
      (1-b)*u-a*s+2*c*v,
      -b*u+(1-a)*s+2*c*v,
      b*u+a*s-2*c*v]
detd = u*s-v*v
ddp = [2*detd, -2*detd, -2*detd, 2*detd]
assert sum(p) == 1 and min(p) > 0
assert sum(dp) == sum(ddp) == 0
assert p[1]*p[2]-p[0]*p[3] == c*c
L = log(float(p[1]*p[2]/(p[0]*p[3])))
hpp_direct = -sum(float(x*x/q) + float(y)*log(float(q))
                  for q,x,y in zip(p,dp,ddp))
hpp_reduced = -sum(float(x*x/q) for q,x in zip(p,dp)) + 2*L*float(detd)
assert abs(hpp_direct-hpp_reduced) < 1e-12
print('atom normalization, odds identity, derivative normalization: exact PASS')
print('Hessian direct/reduced=', hpp_direct, hpp_reduced)
