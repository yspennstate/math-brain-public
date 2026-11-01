#!/usr/bin/env python3
import itertools
from collections import Counter
import sympy as sp

I=sp.I
omega=sp.Rational(1,2)+I*sp.sqrt(3)/2

def det_weight(S,T):
    M=sp.Matrix([[omega**(s*t)/sp.sqrt(6) for t in T] for s in S])
    d=sp.simplify(M.det())
    return sp.simplify(sp.expand_complex(d*sp.conjugate(d)))

def weights(S):
    k=len(S)
    return {T:sp.simplify(det_weight(S,T)) for T in itertools.combinations(range(6),k)}

W2=weights((0,1))
W3=weights((0,1,2))
W4=weights((0,1,3,4))
W5=weights((0,1,2,3,4))
assert set(W2.values()) == {sp.Rational(1,36),sp.Rational(1,12),sp.Rational(1,9)}
assert set(W3.values()) == {sp.Rational(1,72),sp.Rational(1,18),sp.Rational(1,8)}
assert set(W4.values()) == {sp.Rational(0),sp.Rational(1,9)}
assert set(W5.values()) == {sp.Rational(1,6)}

def f_T(T):
    k=len(T)
    if k<=1:
        return sp.Rational(1)
    if k>=4:
        return sp.Rational(0)
    if k==2:
        return sp.simplify(1-6*W2[tuple(T)])
    if k==3:
        return sp.simplify(2*det_weight((0,2,4),tuple(T)))

fvals={T:f_T(T) for k in range(7) for T in itertools.combinations(range(6),k)}
counts={k:Counter(fvals[T] for T in fvals if len(T)==k) for k in range(7)}
assert counts[0] == Counter({sp.Rational(1):1})
assert counts[1] == Counter({sp.Rational(1):6})
assert counts[2] == Counter({sp.Rational(5,6):6,sp.Rational(1,2):6,sp.Rational(1,3):3})
assert counts[3] == Counter({sp.Rational(0):12,sp.Rational(1,4):8})
assert all(fvals[T]==0 for T in fvals if len(T)>=4)
for A,vA in fvals.items():
    sA=set(A)
    for B,vB in fvals.items():
        if sA.issubset(B):
            assert vA >= vB

def quad_matrix(W):
    A=sp.zeros(6)
    for T,c in W.items():
        v=sp.zeros(6,1)
        for i in T:
            v[i]=1
        A += c*(v*v.T)
    return sp.simplify(A)

A2,A3,A4,A5=map(quad_matrix,(W2,W3,W4,W5))
p=sp.symbols('p')
M=sp.simplify(6*p**2*A2-6*p**3*A3-3*p**4*A4+6*p**5*A5)
r=[sp.factor(M[0,j]) for j in range(6)]
lam={}
for m in range(4):
    lam[m]=sp.factor(r[0]+2*r[1]*sp.cos(sp.pi*m/3)+2*r[2]*sp.cos(2*sp.pi*m/3)+r[3]*sp.cos(sp.pi*m))
assert lam[1] == p**2*(p-1)**2*(p+1)
assert lam[2] == p**2*(p-1)*(p**2-2)
assert lam[3] == p**2*(p-1)**2*(p+2)

print('C0036 Z6 SPECTRAL-MIXTURE / HESSIAN EXACT SELF-CHECK')
print('W2_VALUES=', sorted(map(str,set(W2.values()))))
print('W3_VALUES=', sorted(map(str,set(W3.values()))))
print('W4_VALUES=', sorted(map(str,set(W4.values()))))
print('W5_VALUES=', sorted(map(str,set(W5.values()))))
for k in range(7):
    print('F_COUNTS_SIZE_%d='%k, sorted((str(v),n) for v,n in counts[k].items()))
print('F_MONOTONE_DECREASING_UNDER_INCLUSION=PASS')
print('HESSIAN_MODE_1_5=', sp.factor(lam[1]))
print('HESSIAN_MODE_2_4=', sp.factor(lam[2]), '= p^2*(1-p)*(2-p^2) on 0<p<1')
print('HESSIAN_MODE_3=', sp.factor(lam[3]))
print('ALL_EXACT_CHECKS_PASS')
