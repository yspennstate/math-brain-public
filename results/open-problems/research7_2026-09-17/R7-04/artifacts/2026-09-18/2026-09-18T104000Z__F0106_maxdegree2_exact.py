#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb

# Polynomials are coefficient lists in p, low degree first.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b):
    n = max(len(a), len(b))
    out = [F(0) for _ in range(n)]
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)

def scale(a, c):
    return trim([c*x for x in a])

def mul(a, b):
    out = [F(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def power(a, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, a)
    return out

one = [F(1)]
p = [F(0), F(1)]
q = [F(1), F(-1)]
p2 = mul(p,p)

# 1. Path supersolution identity:
# t^2-(1-p)t-p(1-p) = p^2((1-p)^2+1)/4.
t = [F(1), F(0), F(-1,2)]
lhs = add(add(power(t,2), scale(mul(q,t), F(-1))), scale(mul(p,q),F(-1)))
rhs = scale(mul(p2, add(power(q,2), one)), F(1,4))
assert lhs == rhs
assert lhs == [F(0), F(0), F(1,2), F(-1,2), F(1,4)]
print('PATH_IDENTITY_OK', lhs)

# 2. C4 certificate. Z4 = 1-4p^2+4p^3-p^4.
Z4 = [F(1), F(0), F(-4), F(4), F(-1)]
diff = add(power(t,4), scale(Z4,F(-1)))
assert diff[:2] == [F(0),F(0)]
Fpoly = trim(diff[2:]) # (t^4-Z4)/p^2, degree 6
bern = [F(2), F(4,3), F(5,6), F(1,2), F(3,10), F(1,6), F(1,16)]
bern_expanded = [F(0)]
for k,bk in enumerate(bern):
    term = scale(mul(power(p,k), power(q,6-k)), F(comb(6,k))*bk)
    bern_expanded = add(bern_expanded, term)
assert Fpoly == bern_expanded
print('C4_BERNSTEIN_COEFFS', *bern)

# 3. Paw graph has exactly empty set + 4 singleton independent sets + 2 independent pairs.
paw = add(add(power(q,4), scale(mul(p,power(q,3)),F(4))), scale(mul(p2,power(q,2)),F(2)))
assert paw == Z4
print('PAW_EQUALS_C4_OK', paw)

# 4. Endpoint rational certificate:
# exp(8/9) > sum_{k=0}^3 (8/9)^k/k! = 5251/2187 > 16/7.
x = F(8,9)
partial = F(1) + x + x*x/F(2) + x*x*x/F(6)
gap = partial - F(16,7)
assert partial == F(5251,2187)
assert gap == F(1765,15309) and gap > 0
print('EXP_LOWER_CERT', partial, 'minus_16_over_7', gap)

print('ALL_EXACT_CHECKS_PASS')
