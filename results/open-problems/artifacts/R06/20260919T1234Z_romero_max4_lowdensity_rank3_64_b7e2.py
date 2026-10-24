#!/usr/bin/env python3
"""
Exact symbolic certificate for R06 / Romero split reliability / max-minus-four
low-density leading coefficient, uniform in n >= 8.

Terminals are 0,1. After the terminal-edge swap reduction, every relevant
host has missing set {(0,1)} union D with |D|=3 and D not using (0,1).
All terminal-isomorphism types stabilize on vertices 0,...,7.

For H = K_n - {(0,1)} - D, the first nonzero split coefficient is N_{n-2},
the number of spanning two-forests separating the terminals. By the all-minors
Matrix-Tree theorem it is the determinant of the Laplacian minor deleting
the terminal rows/columns.

For K_n that minor is A = n I - J on r=n-2 nonterminal vertices, with
det(A)=2*n^(n-3) and A^{-1}=(1/n)I+(1/(2n))J.
Every additional missing edge contributes a rank-one subtraction vv^T:
terminal--nonterminal: v=e_u; nonterminal--nonterminal: v=e_u-e_v.
Hence N_{n-2}(H)=det(A)*det(I_3-V^T A^{-1} V).

We enumerate exactly the 21 stable terminal types, compute that 3x3 factor
symbolically, and certify that the terminal-centered three-star D* maximizes
it for every n>=8. Positivity is certified by multiplying each gap by 2n^3,
substituting n=q+8, and checking that every coefficient in q is nonnegative.
"""
from itertools import combinations, permutations
from collections import Counter
import sympy as sp

CORE_N=8
S,T=0,1
NONTERMS=list(range(2,8))

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def norm_edge(a,b):
    return (a,b) if a<b else (b,a)

CORE_ALLOWED=[e for e in all_edges(CORE_N) if e!=(0,1)]

ACTIONS=[]
for perm in permutations(NONTERMS):
    base={0:0,1:1}
    base.update({NONTERMS[i]:perm[i] for i in range(6)})
    ACTIONS.append(base)
    sw=dict(base); sw[0],sw[1]=1,0
    ACTIONS.append(sw)

def act_D(D,mp):
    return tuple(sorted(norm_edge(mp[a],mp[b]) for a,b in D))

def canon_D(D):
    D=tuple(sorted(D))
    return min(act_D(D,mp) for mp in ACTIONS)

classes={}
for D in combinations(CORE_ALLOWED,3):
    c=canon_D(D)
    classes[c]=classes.get(c,0)+1

assert sum(classes.values())==2925
assert len(classes)==21

def shape(D):
    deg=Counter()
    for a,b in D:
        deg[a]+=1; deg[b]+=1
    vals=sorted(deg.values(), reverse=True)
    if vals==[3,1,1,1]: return "S3"
    if vals==[2,2,1,1]: return "P4"
    if vals==[2,1,1,1,1]: return "P3+K2"
    if vals==[2,2,2]: return "K3"
    if vals==[1,1,1,1,1,1]: return "3K2"
    raise AssertionError((D,vals))

shape_counts=Counter(shape(D) for D in classes)
assert shape_counts==Counter({"P3+K2":7,"P4":5,"S3":4,"3K2":3,"K3":2})

n,q=sp.symbols("n q", integer=True, positive=True)

# Coordinates are the six possible defect nonterminals 2,...,7.
# Extra vertices for n>8 have zero coordinates in all defect vectors.
def defect_vec(e):
    a,b=e
    v=sp.zeros(6,1)
    if a in (S,T):
        assert b not in (S,T)
        v[b-2]=1
    elif b in (S,T):
        assert a not in (S,T)
        v[a-2]=1
    else:
        v[a-2]=1
        v[b-2]=-1
    return v

def low_density_factor(D):
    V=sp.Matrix.hstack(*(defect_vec(e) for e in D))
    # restriction of A^{-1}=(1/n)I+(1/(2n))J to defect support
    Ainv=(sp.eye(6)+sp.ones(6,6)/2)/n
    G=sp.simplify(V.T*Ainv*V)
    return sp.factor((sp.eye(3)-G).det())

Dstar=canon_D(((0,2),(0,3),(0,4)))
Dtie=canon_D(((0,2),(0,3),(1,4)))
fstar=sp.factor(low_density_factor(Dstar))
assert sp.factor(fstar - (n-1)**2*(2*n-5)/(2*n**3))==0

ties=[]
rows=[]
for D in sorted(classes):
    f=sp.factor(low_density_factor(D))
    delta=sp.factor(fstar-f)
    scaled=sp.Poly(sp.expand(2*n**3*delta), n)
    # verify the denominator-cleared identity is a polynomial
    assert scaled.as_expr()==sp.expand(2*n**3*delta)
    shifted=sp.Poly(sp.expand(scaled.as_expr().subs(n,q+8)),q)
    coeffs=shifted.all_coeffs()
    assert all(c.is_Integer and c>=0 for c in coeffs), (D,delta,shifted)
    if sp.simplify(delta)==0:
        ties.append(D)
    rows.append((D,shape(D),f,delta,shifted.as_expr()))

assert set(ties)=={Dstar,Dtie}
assert len(ties)==2

print("ROMERO max-minus-four uniform low-density certificate")
print("stable_core_labeled_D=2925")
print("terminal_isomorphism_types=21")
print("shape_type_counts=S3:4,P4:5,P3+K2:7,K3:2,3K2:3")
print(f"Dstar={Dstar}")
print(f"Dtie={Dtie}")
print(f"candidate_factor={fstar}")
print("certificate_rule: for every type, 2*n^3*(F_star-F_D) at n=q+8 has nonnegative integer coefficients")
print(f"exact_leading_ties={len(ties)}")
for D,sh,f,delta,shifted in rows:
    print(f"type={D} shape={sh} factor={f} gap={delta} shifted_scaled_gap={shifted}")
print("PASS: for every n>=8 and every stable three-edge defect type D,")
print("F_star(n)>=F_D(n), hence the terminal-centered four-star host maximizes N_{n-2}.")
print("Exactly one nonisomorphic type ties at leading order: two terminal-incident missing")
print("edges at one terminal and one terminal-incident missing edge at the other, on distinct nonterminals.")
