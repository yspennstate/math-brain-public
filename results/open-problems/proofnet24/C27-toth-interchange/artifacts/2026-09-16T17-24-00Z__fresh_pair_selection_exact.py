#!/usr/bin/env python3
# Exact self-check for C27 fresh-pair route:
# (i) P3 anticipative-selection counterexample at T=log 2, beta=2 log 2;
# (ii) exact scale-exponent arithmetic for the localized pair-escape block;
# (iii) small independent arithmetic checks for the directed C28 radius-two audit.

from fractions import Fraction
from itertools import permutations
from math import comb
import sympy as sp

# ---------- P3 interchange semigroup at T=log 2 ----------
perms = list(permutations(range(3)))
idx = {p:i for i,p in enumerate(perms)}
edges = [(0,1),(1,2)]

def left_transpose(p, e):
    a,b=e
    q=list(p)
    for i,x in enumerate(q):
        if x==a: q[i]=b
        elif x==b: q[i]=a
    return tuple(q)

def compose(q,w):
    # q o w
    return tuple(q[w[i]] for i in range(3))

Q = sp.zeros(6)
for p in perms:
    i=idx[p]
    for e in edges:
        q=left_transpose(p,e)
        Q[i,idx[q]] += 1
        Q[i,i] -= 1

# Spectrum is {0,-1,-3,-4}. At T=log 2, exp(lambda*T)=2^lambda.
evals = [sp.Integer(0), sp.Integer(-1), sp.Integer(-3), sp.Integer(-4)]
weights = {
    sp.Integer(0): sp.Rational(1),
    sp.Integer(-1): sp.Rational(1,2),
    sp.Integer(-3): sp.Rational(1,8),
    sp.Integer(-4): sp.Rational(1,16),
}
I = sp.eye(6)
P = sp.zeros(6)
for lam in evals:
    proj = I
    for mu in evals:
        if mu != lam:
            proj = proj * (Q - mu*I) / (lam-mu)
    P += weights[lam] * proj
P = sp.simplify(P)
assert P*sp.ones(6,1) == sp.ones(6,1)
assert (P.T-P) == sp.zeros(6)

idp=(0,1,2)
row=[sp.Rational(P[idx[idp],j]) for j in range(6)]
assert row == [
    sp.Rational(37,96), sp.Rational(7,32), sp.Rational(7,32),
    sp.Rational(7,96), sp.Rational(7,96), sp.Rational(1,32)
]

# W,Q independent with law P from identity; pi = Q o W.
den=sp.Rational(0)
num={0:sp.Rational(0),1:sp.Rational(0),2:sp.Rational(0)}
for w in perms:
    pw=row[idx[w]]
    for q in perms:
        pq=row[idx[q]]
        final=compose(q,w)
        A=final[0]
        if A==1:
            den += pw*pq
            num[w[A]] += pw*pq
cond={z:sp.factor(num[z]/den) for z in range(3)}
uncond={}
for z in range(3):
    uncond[z]=sp.factor(sum(row[idx[w]] for w in perms if w[1]==z))

assert den == sp.Rational(21,64)
assert cond == {0:sp.Rational(37,108),1:sp.Rational(10,27),2:sp.Rational(31,108)}
assert uncond == {0:sp.Rational(7,24),1:sp.Rational(5,12),2:sp.Rational(7,24)}
assert cond[0]-uncond[0] == sp.Rational(11,216)

# ---------- Exact localized scale balances ----------
a=Fraction(1,8)       # number of candidate strands beta^a
rho=Fraction(7,16)    # initial separation beta^rho
gamma=Fraction(1,8)   # close-approach radius beta^gamma
tau=Fraction(3,16)    # fresh phase duration beta^tau
balances = {
    "driver_coupling": a-Fraction(1,2),
    "driver_packing": a+3*rho-Fraction(3,2),
    "fresh_tube_rate": 2*gamma-tau,
    "listed_target_union": 2*a-Fraction(3,2)*tau,
    "fresh_pair_union": 2*a+gamma-rho,
}
assert balances == {
    "driver_coupling": Fraction(-3,8),
    "driver_packing": Fraction(-1,16),
    "fresh_tube_rate": Fraction(1,16),
    "listed_target_union": Fraction(-1,32),
    "fresh_pair_union": Fraction(-1,16),
}

# ---------- Directed C28 radius-two audit arithmetic ----------
assert comb(14,2)*comb(60,2) == 161070
r=sp.sqrt(73); s=sp.sqrt(13)
k2=(r-1+2*s)/(r-1-2*s)
ub=sp.Rational(71060,3279)+sp.Rational(8420,3279)*r
assert sp.simplify(r-1-2*s > 0) is sp.true
assert sp.simplify(k2-ub > 0) is sp.true

print("C27_FRESH_PAIR_AND_AUDIT_EXACT")
print("P3_half_semigroup_row=" + repr(row))
print("P_A_eq_1=" + str(den))
print("conditional_W_of_selected_label=" + repr(cond))
print("unconditional_W_of_label1=" + repr(uncond))
print("selection_bias_at_0=" + str(cond[0]-uncond[0]))
for k,v in balances.items():
    print(k+"_exponent="+str(v))
print("C28_radius2_neighbor_count=161070")
print("C28_radical_gap_positive=PASS")
print("ALL_EXACT_CHECKS_PASS")
