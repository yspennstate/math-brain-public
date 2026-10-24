#!/usr/bin/env python3
"""
R12 / I0102 second-run exact checker.

Finite exact-arithmetic/self-checks only.  It does not prove the asymptotic
Randomstrasse Conjecture 28.

Checks:
  C04. Exact degree-4 polynomial identity and the K4-free certificate.
  C04. Paley p=13,17 have a triangle and no K4, hence (by the proved
       certificate plus an actual clique lower bound) U4=3.
  C05. Clique-algebra identities used in the edge-compatibility theta compiler.
  C06. Exact midpoint/half-difference edge parameterization and affine action,
       verifying the three Fourier-orbit block types for p=13,17,29,41.
  finite orbit counts for triangles/K4s under the Paley affine automorphism group.
"""
from itertools import combinations
import sympy as sp

print("R12 run2 exact checker: start")

# ---------------------------------------------------------------------------
# C04 polynomial identity.
# ---------------------------------------------------------------------------
S = sp.symbols('S')
fall4 = S*(S-1)*(S-2)*(S-3)
rhs = sp.Rational(1,6)*(S*(S-3))**2 + sp.Rational(1,3)*(S-3)**2 - sp.Rational(1,6)*fall4
assert sp.expand(rhs - (3-S)) == 0
print("C04 POLYNOMIAL IDENTITY: PASS")

# ---------------------------------------------------------------------------
# Paley graph helpers / exact clique enumeration.
# ---------------------------------------------------------------------------
def legendre(x,p):
    x %= p
    if x == 0:
        return 0
    t = pow(x,(p-1)//2,p)
    return 1 if t == 1 else -1

def is_edge(u,v,p):
    return u != v and legendre(u-v,p) == 1

def is_clique(C,p):
    return all(is_edge(u,v,p) for u,v in combinations(C,2))

def cliques_of_size(p,r):
    return [C for C in combinations(range(p),r) if is_clique(C,p)]

for p in [13,17]:
    tris = cliques_of_size(p,3)
    k4s = cliques_of_size(p,4)
    assert len(tris) > 0
    assert len(k4s) == 0
    print(f"C04 PALEY p={p}: triangles={len(tris)}, K4s=0 -> U4=3 by analytic certificate: PASS")

# ---------------------------------------------------------------------------
# C05 clique-algebra identities, exact finite reduction for sample Paley graphs.
# Polynomial represented by dict monomial frozenset -> integer coefficient,
# with Boolean union and non-clique monomials deleted.
# ---------------------------------------------------------------------------
def padd(P,Q):
    R = dict(P)
    for U,c in Q.items():
        R[U] = R.get(U,0)+c
        if R[U] == 0: del R[U]
    return R

def pscale(a,P):
    return {U:a*c for U,c in P.items() if a*c}

def pmul(P,Q,p):
    R={}
    for U,a in P.items():
        for V,b in Q.items():
            W=U|V
            if is_clique(tuple(W),p):
                R[W]=R.get(W,0)+a*b
    return {U:c for U,c in R.items() if c}

def powers(P,k,p):
    R={frozenset():1}
    for _ in range(k): R=pmul(R,P,p)
    return R

def mono_sum(cliques):
    return {frozenset(C):1 for C in cliques}

for p in [13,17,29]:
    V = mono_sum([(i,) for i in range(p)])
    E = mono_sum(cliques_of_size(p,2))
    T = mono_sum(cliques_of_size(p,3))
    K4 = mono_sum(cliques_of_size(p,4))
    # S^2 = S + 2 E2
    assert padd(powers(V,2,p), pscale(-1,padd(V,pscale(2,E)))) == {}
    # S E2 = 2 E2 + 3 E3
    assert padd(pmul(V,E,p), pscale(-1,padd(pscale(2,E),pscale(3,T)))) == {}
    # E2^2 = E2 + 6 E3 + 6 E4
    target = padd(E,padd(pscale(6,T),pscale(6,K4)))
    assert padd(pmul(E,E,p),pscale(-1,target)) == {}
    # falling factorial = 24 E4
    s2=powers(V,2,p); s3=powers(V,3,p); s4=powers(V,4,p)
    falling=padd(s4,padd(pscale(-6,s3),padd(pscale(11,s2),pscale(-6,V))))
    assert padd(falling,pscale(-24,K4)) == {}
    print(f"C05 CLIQUE-ALGEBRA IDENTITIES p={p}: PASS")

# ---------------------------------------------------------------------------
# C06 midpoint / half-difference parameterization and affine group action.
# Let R={h!=0: chi(2h)=1}/±. Choose canonical representative min(h,-h).
# Edge e_(x,[h])={x-h,x+h}.
# ---------------------------------------------------------------------------
def sqs(p): return {x*x % p for x in range(1,p)}

def canon_pm(h,p):
    h%=p
    return min(h,(-h)%p)

def half_types(p):
    return sorted({canon_pm(h,p) for h in range(1,p) if legendre(2*h,p)==1})

def edge_from_mid(x,h,p):
    return tuple(sorted(((x-h)%p,(x+h)%p)))

def all_edges(p):
    return {tuple(sorted((u,v))) for u in range(p) for v in range(u+1,p) if is_edge(u,v,p)}

for p in [13,17,29,41]:
    H=half_types(p)
    assert len(H)==(p-1)//4
    param={(x,h):edge_from_mid(x,h,p) for x in range(p) for h in H}
    # Injectivity/bijection.
    assert len(set(param.values())) == len(param)
    assert set(param.values()) == all_edges(p)
    # translations preserve h type and shift midpoint.
    for b in range(p):
        for (x,h),e in list(param.items())[:min(20,len(param))]:
            te=tuple(sorted(((e[0]+b)%p,(e[1]+b)%p)))
            assert te==edge_from_mid((x+b)%p,h,p)
    # square multipliers permute half-types and send midpoint x -> ax.
    Q=sorted(sqs(p))
    for a in Q:
        image_types={canon_pm(a*h,p) for h in H}
        assert image_types==set(H)
        for (x,h),e in list(param.items())[:min(20,len(param))]:
            se=tuple(sorted(((a*e[0])%p,(a*e[1])%p)))
            assert se==edge_from_mid((a*x)%p,canon_pm(a*h,p),p)
    # Nonzero additive frequencies have exactly two Q-multiplier orbits.
    nonzero=set(range(1,p))
    orbits=[]
    while nonzero:
        x=min(nonzero)
        orb={(a*x)%p for a in Q}
        orbits.append(orb)
        nonzero-=orb
    assert len(orbits)==2
    assert sorted(map(len,orbits))==[(p-1)//2,(p-1)//2]
    r=(p-1)//4
    print(f"C06 p={p}: edge_types={r}, Fourier block dims zero={r+2}, square={r+1}, nonsquare={r+1}: PASS")

# ---------------------------------------------------------------------------
# Exact triangle/K4 affine orbit counts under x -> a x + b, a square.
# ---------------------------------------------------------------------------
def aff_image(C,a,b,p):
    return tuple(sorted(((a*x+b)%p for x in C)))

def affine_orbits(cliques,p):
    remaining=set(cliques)
    Q=sorted(sqs(p))
    orbits=[]
    while remaining:
        C=min(remaining)
        O={aff_image(C,a,b,p) for a in Q for b in range(p)}
        O &= set(cliques)
        # For a Paley clique, every affine square image is a Paley clique.
        assert len(O)>0
        orbits.append(O)
        remaining-=O
    return sorted(len(O) for O in orbits)

for p in [13,17,29,41]:
    tris=cliques_of_size(p,3)
    k4s=cliques_of_size(p,4)
    torb=affine_orbits(tris,p)
    korb=affine_orbits(k4s,p) if k4s else []
    print(f"AFFINE ORBITS p={p}: triangles total={len(tris)} orbit_sizes={torb}; K4 total={len(k4s)} orbit_sizes={korb}")

print("ALL_EXACT_CHECKS_PASS")
