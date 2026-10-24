#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

# Exact toy semidirect Cayley graph:
# Gamma=C2 acts on Lambda=C3xC3 by swapping coordinates.
Gamma = [0, 1]
Lam = [(i,j) for i in range(3) for j in range(3)]
idxL = {x:i for i,x in enumerate(Lam)}

def add3(x,y):
    return ((x[0]+y[0])%3, (x[1]+y[1])%3)

def neg3(x):
    return ((-x[0])%3, (-x[1])%3)

def theta(g,x):
    return x if g == 0 else (x[1],x[0])

def mul(z,w):
    g,x = z
    h,y = w
    return ((g+h)%2, add3(x, theta(g,y)))

def inv(z):
    g,x = z
    return (g, theta(g,neg3(x)))

S = [1]
T = [(1,0),(2,0),(0,1),(0,2)]
eL = (0,0)
Sigma = [(1,eL)] + [(0,t) for t in T] + [(1,t) for t in T]

assert all(inv(s) in Sigma for s in Sigma)
states = [(g,x) for g in Gamma for x in Lam]
idx = {z:i for i,z in enumerate(states)}
A = np.zeros((18,18), dtype=int)
for z in states:
    for sig in Sigma:
        A[idx[z], idx[mul(sig,z)]] += 1

assert set(A.sum(axis=1)) == {9}
assert np.array_equal(A,A.T)
assert int(np.trace(A)) == 0
for z in states:
    c = Counter(mul(sig,z)[0] for sig in Sigma)
    assert c[z[0]] == 4 and c[1-z[0]] == 5

# Fiber walk and swap commute exactly.
AB = np.zeros((9,9),dtype=int)
for x in Lam:
    for t in T:
        AB[idxL[x],idxL[add3(t,x)]] += 1
QB = sp.Matrix(AB) / 4
J = np.zeros((9,9),dtype=int)
for x in Lam:
    J[idxL[x],idxL[(x[1],x[0])]] = 1
assert sp.Matrix(J)*QB == QB*sp.Matrix(J)

spec_B = QB.eigenvals()
spec_H = (sp.Matrix(A)/9).eigenvals()
assert spec_B == {sp.Integer(1):1, sp.Rational(-1,2):4, sp.Rational(1,4):4}
assert spec_H == {sp.Integer(1):1, sp.Rational(1,3):4,
                  sp.Rational(-1,3):4, sp.Rational(-1,9):9}

# Numerical continuous-time sandwich on the toy graph.
QA = np.array([[0.,1.],[1.,0.]])
QH = A/9.0
rA_toy = Fraction(5,9)
beta_toy = Fraction(4,9)
gammaB_toy = Fraction(3,4)
spot = []
for t in [0.5,1.0,2.0,4.0,8.0]:
    h = expm(t*(QH-np.eye(18)))[0]
    a = expm(float(rA_toy)*t*(QA-np.eye(2)))[0]
    dH = 0.5*np.abs(h-1/18).sum()
    dA = 0.5*np.abs(a-1/2).sum()
    err = 0.5*math.sqrt(8)*math.exp(-float(beta_toy*gammaB_toy)*t)
    assert dA <= dH + 1e-12
    assert dH <= dA + err + 1e-12
    spot.append((t,dA,dH,dA+err))

# Planned 103-regular class:
# A=(6-regular Ramanujan Cayley base) box K2, so a=7.
# B=(6-regular Cayley Ramanujan) box itself, so b=12.
a,b = 7,12
D = a+b+a*b
rA = Fraction(a*(1+b),D)
beta = Fraction(b,D)
A_center = Fraction(7,4)   # times log_5 n
H_center = A_center/rA
window_scale_from_base = Fraction(7,6)/rA
assert D == 103
assert rA == Fraction(91,103)
assert beta == Fraction(12,103)
assert H_center == Fraction(103,52)
assert window_scale_from_base == Fraction(103,78)
assert 25 < D-1  # output ball exponential bound versus LRE tree base

# Pair-phase lemma algebra:
# If Var(I)>=c0 L^2 and osc(I)<=M L, then E[(I-I')^2]>=2c0 L^2.
# With threshold sqrt(c0)L, P(|I-I'|>=threshold)>=c0/M^2.
c0 = Fraction(1,25)
M = Fraction(4,1)
lower_pair_prob = c0/(M*M)
assert lower_pair_prob == Fraction(1,400)

print("SEMIDIRECT_TOY_DEGREE=9")
print("SEMIDIRECT_TOY_INVERSE_CLOSED=True")
print("SEMIDIRECT_TOY_PROJECTION=A_move_5_hold_4")
print("FIBER_SPECTRUM=", {str(k):v for k,v in spec_B.items()})
print("OUTPUT_SPECTRUM=", {str(k):v for k,v in spec_H.items()})
for t,dA,dH,up in spot:
    print(f"TV_SANDWICH t={t:g} lower={dA:.12f} actual={dH:.12f} upper={up:.12f}")
print("PLANNED_DEGREE=",D)
print("PLANNED_A_SPEED=",rA)
print("PLANNED_FIBER_ONLY_RATE=",beta)
print("PLANNED_CENTER_COEFF_LOG5_N=",H_center)
print("PLANNED_WINDOW_SCALE_FROM_RAMANUJAN_BASE=",window_scale_from_base)
print("BALL_EXP_BASE_BOUND=25 < LRE_TREE_BASE=102")
print("PAIR_PHASE_TEST_CONSTANT c0=1/25 M=4 gives prob>=",lower_pair_prob)
print("ALL_CHECKS_PASS")
