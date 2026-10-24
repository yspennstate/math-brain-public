#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

print("P26-R05-I0030-C14-INDEPENDENT-EXACT-AUDIT: PASS_START")

h = sp.symbols("h", positive=True, real=True)
a1 = h
b1 = 1-h
a2 = h**2 + (1-h)**2
b2 = 2*h*(1-h)
r1 = sp.cancel(b1/a1)
r2 = sp.cancel(b2/a2)
gap = sp.factor(r1-r2)
target = sp.factor((1-h)*(1-2*h)/(h*(h**2+(1-h)**2)))
assert sp.simplify(gap-target) == 0
print("K2 symbolic sharpness factor:", gap)

# Exact interior witness h=1/4.
hh = F(1,4)
aa1 = hh
bb1 = 1-hh
aa2 = hh*hh + (1-hh)*(1-hh)
bb2 = 2*hh*(1-hh)
rr1 = bb1/aa1
rr2 = bb2/aa2
assert rr1 == F(3,1)
assert rr2 == F(3,5)
assert rr1 > rr2
print("h=1/4 exact ratios:", rr1, rr2, "DECREASE_PASS")

# Boundary h=1/2 on K2: Q is rank-one averaging, hence Q^m=Q for m>=1.
Q = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert mm(Q,Q) == Q
print("h=1/2 K2 idempotence: PASS; ratios are 0,1,1,...")

# Equivalent spectral parameter c=2h-1 formula.
c = sp.symbols("c", real=True)
r1c = (1-c)/(1+c)
r2c = (1-c**2)/(1+c**2)
cgap = sp.factor(r1c-r2c)
assert sp.simplify(cgap - 2*c*(c-1)/((c+1)*(c**2+1))) == 0
print("spectral c-form sharpness factor:", cgap)

# Two-point exact Hankel determinant identity, the finite algebra behind the
# general double-integral proof. The written report supplies the all-m proof.
p,q,w = sp.symbols("p q w", real=True)
for M in range(0,8):
    aM   = w*p**M + (1-w)*q**M
    aM1  = w*p**(M+1) + (1-w)*q**(M+1)
    aM2  = w*p**(M+2) + (1-w)*q**(M+2)
    D = sp.factor(aM*aM2-aM1**2)
    expected = sp.factor(w*(1-w)*(p*q)**M*(p-q)**2)
    assert sp.simplify(D-expected) == 0
print("two-point Hankel factorization m=0..7: PASS")

print("P26-R05-I0030-C14-INDEPENDENT-EXACT-AUDIT: PASS_END")
