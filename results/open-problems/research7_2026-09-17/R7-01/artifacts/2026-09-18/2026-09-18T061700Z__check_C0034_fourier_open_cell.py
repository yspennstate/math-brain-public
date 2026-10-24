from fractions import Fraction
from itertools import permutations

V = tuple(range(6))

def edge(a,b):
    return tuple(sorted((a,b)))

def cyc_dist(e):
    a,b=e
    d=(b-a)%6
    return min(d,6-d)

def matchings(vertices):
    vertices=tuple(sorted(vertices))
    if not vertices:
        yield ()
        return
    a=vertices[0]
    for b in vertices[1:]:
        rest=tuple(v for v in vertices if v not in (a,b))
        for M in matchings(rest):
            yield tuple(sorted((edge(a,b),)+M))

MS=sorted(set(matchings(V)))
assert len(MS)==15

def typ(M):
    return tuple(sorted(cyc_dist(e) for e in M))

# Fourier row-pair DPP weights w_e.
w_by_d={1:Fraction(1,36),2:Fraction(1,12),3:Fraction(1,9)}
w={edge(i,j):w_by_d[cyc_dist(edge(i,j))] for i in V for j in V if i<j}
assert sum(w.values())==1

# Total probability mass assigned to each dihedral matching type.
type_mass={
    (1,1,1): Fraction(1,20),
    (1,2,2): Fraction(1,20),
    (1,1,3): Fraction(3,20),
    (2,2,3): Fraction(7,10),
    (3,3,3): Fraction(1,20),
}
counts={t:sum(1 for M in MS if typ(M)==t) for t in type_mass}
assert counts=={(1,1,1):2,(1,2,2):6,(1,1,3):3,(2,2,3):3,(3,3,3):1}
mu={M:type_mass[typ(M)]/counts[typ(M)] for M in MS}
assert sum(mu.values())==1
assert min(mu.values())==Fraction(1,120)

# Uncolored edge marginals must equal 3 w_e.
for e in w:
    inc=sum(mu[M] for M in MS if e in M)
    assert inc==3*w[e], (e,inc,3*w[e])

# Color each matching uniformly by a bijection of its three edges to colors 0,1,2.
atoms=[]
for M in MS:
    for perm in permutations(M):
        # X_r is perm[r].
        atoms.append((tuple(perm), mu[M]/6))
assert len(atoms)==90
assert sum(p for _,p in atoms)==1
assert min(p for _,p in atoms)==Fraction(1,720)

# Each color has the Fourier rank-two DPP law w.
for r in range(3):
    for e in w:
        pr=sum(p for X,p in atoms if X[r]==e)
        assert pr==w[e], (r,e,pr,w[e])

# For H=H1+H2, union law is complement of color 2, hence the complement DPP of H3.
for e in w:
    T=tuple(sorted(set(V)-set(e)))
    pr=sum(p for X,p in atoms if tuple(sorted(set(X[0])|set(X[1])))==T)
    assert pr==w[e], (T,pr,w[e])

# Exact incidence rank for the n=6 2+2 transport system.
import sympy as sp
pairs=sorted(w)
quads=sorted(tuple(sorted(set(V)-set(e))) for e in w)
# variables are ordered colored pair choices (A,B), disjoint; C is their complement.
vars_ab=[(A,B) for A in pairs for B in pairs if set(A).isdisjoint(B)]
rows=[]
for A0 in pairs:
    rows.append([1 if A==A0 else 0 for A,B in vars_ab])
for B0 in pairs:
    rows.append([1 if B==B0 else 0 for A,B in vars_ab])
for T0 in quads:
    ST=set(T0)
    rows.append([1 if set(A)|set(B)==ST else 0 for A,B in vars_ab])
rank=sp.Matrix(rows).rank()
assert len(vars_ab)==90
assert rank==38
print('INCIDENCE_RANK',rank)

print('MATCHINGS',len(MS))
print('COLORED_ATOMS',len(atoms))
print('MIN_MATCHING_WEIGHT',min(mu.values()))
print('MIN_COLORED_ATOM',min(p for _,p in atoms))
print('EDGE_WEIGHTS',w_by_d)
print('ALL_EXACT_CHECKS_PASS')
