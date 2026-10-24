from fractions import Fraction as F
import sympy as sp

p1, p2, p3 = sp.symbols('p1 p2 p3')
q1, q2, q3 = 1-p1, 1-p2, 1-p3

delta = 2*(p1+p2+p3)-3
m0 = q1*p2 + 2*q1*q2*p3 + 4*q1*q2*q3
m1 = (
    p1*q2*p3 + q1*p2*p3
    + 3*(p1*q2*q3 + q1*p2*q3 + q1*q2*p3)
    + 5*q1*q2*q3
)

c0 = sp.expand(m0 + delta - 1)
c1 = sp.expand(m1 + delta - 2)
target_c0 = sp.expand(p1*(2*p2-1) + (2*p3-1)*(p1+p2-p1*p2))
target_c1 = sp.expand(p1*p2*(2*p3-1))

assert sp.simplify(c0-target_c0) == 0
assert sp.simplify(c1-target_c1) == 0

print('c0 identity: PASS')
print('c1 identity: PASS')
print('c0 =', sp.factor(c0))
print('c1 =', sp.factor(c1))
print('c0-c1 =', sp.factor(c0-c1))


def dlt(st):
    a,b,c = st
    return 2*(a+b+c)-3


def C0(st):
    a,b,c = st
    return a*(2*b-1) + (2*c-1)*(a+b-a*b)


def C1(st):
    a,b,c = st
    return a*b*(2*c-1)


def avg(vals):
    vals = list(vals)
    return sum(vals, F(0))/len(vals)


# Mixed-sign third-cookie cancellation example.
stacks = [
    (F(9,10), F(9,10), F(7,10)),
    (F(9,10), F(9,10), F(3,10)),
]
D = avg(dlt(s) for s in stacks)
cc0 = avg(C0(s) for s in stacks)
cc1 = avg(C1(s) for s in stacks)
mu1 = avg(s[0] for s in stacks)
pi0 = (D-1)/cc0
pesc = mu1*pi0
assert (D, cc0, cc1, mu1, pi0, pesc) == (
    F(8,5), F(18,25), F(0), F(9,10), F(5,6), F(3,4)
)
print('mixed example: PASS', D, cc0, cc1, mu1, pi0, pesc)

# Positive deterministic example and extremal interval.
s = (F(4,5), F(4,5), F(4,5))
D = dlt(s)
d = D-1
cc0 = C0(s)
cc1 = C1(s)
lb = (d-cc1)/(cc0-cc1)
ub = d/cc0
assert (D, cc0, cc1, lb, ub) == (
    F(9,5), F(132,125), F(48,125), F(13,21), F(25,33)
)
assert s[0]*lb == F(52,105)
assert s[0]*ub == F(20,33)
print('positive example: PASS', D, cc0, cc1, lb, ub, s[0]*lb, s[0]*ub)

print('ALL_EXACT_CHECKS_PASS')
