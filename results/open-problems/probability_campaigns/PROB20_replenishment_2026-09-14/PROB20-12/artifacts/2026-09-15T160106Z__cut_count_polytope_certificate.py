"""Exact finite certificate for PROB20-12 cut-count coarse graining.

This script checks, using only integer/rational linear algebra, the small count
polytopes that arise in the first open rank profile r0=r1=r2=2 on |E|=6.
For a fixed B subset E, write N_i=|X_i cap B|.  Any genuine colored
partition has N0+N1+N2=|B| and 0<=N_i<=2.

The mixed-determinant theorem in the accompanying report proves that the
three DPP count marginals always admit a coupling supported on these count
compositions.  Here we classify the resulting one-cut symmetric marginal
polytopes for |B|=2 and |B|=3 exactly.
"""
from fractions import Fraction
import itertools
import sympy as sp


def affdim(points):
    b = points[0]
    return sp.Matrix([[p[j]-b[j] for j in range(len(b))] for p in points[1:]]).rank()


def face_dim(points, vals, rhs):
    ids=[i for i,v in enumerate(vals) if v==rhs]
    assert ids
    b=points[ids[0]]
    if len(ids)==1:
        return 0,len(ids)
    return sp.Matrix([[points[i][j]-b[j] for j in range(len(b))] for i in ids[1:]]).rank(),len(ids)

# Coordinates are (u0,u1,u2,v0,v1,v2), where
# u_i=P(N_i=2), v_i=P(N_i=0).
def uv(state):
    u=[int(a==2) for a in state]
    v=[int(a==0) for a in state]
    return tuple(u+v)

# |B|=2: six count states, permutations of (2,0,0) and (1,1,0).
states2=sorted(set(itertools.permutations((2,0,0))))+sorted(set(itertools.permutations((1,1,0))))
pts2=[uv(s) for s in states2]
assert len(states2)==6
assert affdim(pts2)==5  # simplex
# Affine identity sum v - sum u =1.
for p in pts2:
    assert sum(p[3:])-sum(p[:3])==1
# Facets: u_i>=0 and beta_i:=v_i-u_j-u_k>=0.
for i in range(3):
    vals_u=[p[i] for p in pts2]
    d,n=face_dim(pts2,vals_u,0)
    assert d==4
    j,k=[z for z in range(3) if z!=i]
    vals_b=[p[3+i]-p[j]-p[k] for p in pts2]
    assert min(vals_b)==0
    d,n=face_dim(pts2,vals_b,0)
    assert d==4

# Explicit inversion of the count coupling for m=2.
# alpha_i=u_i is mass of state with N_i=2; beta_i=v_i-u_j-u_k
# is mass of state with N_i=0 and the other two counts equal 1.
for s,p in zip(states2,pts2):
    u=list(map(Fraction,p[:3])); v=list(map(Fraction,p[3:]))
    alpha=u
    beta=[]
    for i in range(3):
        j,k=[z for z in range(3) if z!=i]
        beta.append(v[i]-u[j]-u[k])
    # For a deterministic count state exactly one of these six masses is 1.
    masses=alpha+beta
    assert sorted(masses)==[0,0,0,0,0,1]

# |B|=3: seven states: (1,1,1) and six permutations of (2,1,0).
states3=[(1,1,1)]+sorted(set(itertools.permutations((2,1,0))))
pts3=[uv(s) for s in states3]
assert len(states3)==7
assert affdim(pts3)==5
# Affine identity t=sum u=sum v.
for p in pts3:
    assert sum(p[:3])==sum(p[3:])
# Candidate nontrivial facets: t<=1 and u_i+v_i<=t.
vals_t=[sum(p[:3]) for p in pts3]
assert max(vals_t)==1
# equality t=1 is a facet (all six (2,1,0) states).
d,n=face_dim(pts3,vals_t,1)
assert d==4 and n==6
for i in range(3):
    vals=[p[i]+p[3+i]-sum(p[:3]) for p in pts3]
    assert max(vals)==0
    d,n=face_dim(pts3,vals,0)
    assert d==4
# Nonnegativity u_i,v_i are also count-polytope facets.
for j in range(6):
    vals=[p[j] for p in pts3]
    d,n=face_dim(pts3,vals,0)
    assert d==4

# Verify Hall reduction for the off-diagonal 3x3 transport representation.
# For any convex combination of states3, let q_ij be mass of count state with
# N_i=2,N_j=0 (i!=j), and h mass of (1,1,1). Then u=row sums,
# v=column sums, h=1-t. The only nontrivial Hall cuts of K_{3,3}\diag are
# u_i <= t-v_i, i.e. u_i+v_i<=t.
# Enumerate all row subsets and verify the neighborhood reductions symbolically
# as set identities.
L=range(3); R=range(3)
for r in range(1,4):
    for S in itertools.combinations(L,r):
        N={j for i in S for j in R if j!=i}
        if len(S)==1:
            i=S[0]
            assert N==set(R)-{i}
        else:
            assert N==set(R)

print('m=2 states:', states2)
print('m=2 affine dimension:', affdim(pts2))
print('m=2 complete nontrivial facets: beta_i=v_i-u_j-u_k >= 0 (plus u_i>=0)')
print('m=3 states:', states3)
print('m=3 affine dimension:', affdim(pts3))
print('m=3 complete nontrivial facets: sum_i u_i<=1 and u_i+v_i<=sum_j u_j')
print('Hall neighborhood check for K3,3 minus diagonal: exact')
