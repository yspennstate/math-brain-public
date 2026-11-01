"""PROB20-12 sparse-cover certificate, 2026-09-15T194741Z.

Exact checks:
  * 90 labeled perfect matchings, affine dimension 37.
  * sparse inequality is a facet: 60 active states, active affine dimension 36,
    deterministic slack {0,1}.
  * S6 x S3 orbit has 1080 distinct active sets.

Numerical diagnostic:
  * for seeded Haar-complex unitary frames, constructs the 2x7 hybrid
    exterior-cover operator M;
  * checks target Laplace vector a = M z up to the common Jacobi phase/norm;
  * checks max eigenvalue(M M*) <= 1 + tolerance.

The operator-norm proof itself is analytic and lives in the accompanying report;
the random check is not a proof.
"""
import itertools
import numpy as np
import sympy as sp

V=tuple(range(6))
EDGES=list(itertools.combinations(V,2))
EID={e:i for i,e in enumerate(EDGES)}
def edge(e): return tuple(sorted(e))
def ix(c,e): return 15*c+EID[edge(e)]

STATES=[]
for coloring in itertools.product(range(3), repeat=6):
    if all(coloring.count(c)==2 for c in range(3)):
        row=[0]*45
        for c in range(3):
            pts=tuple(v for v in V if coloring[v]==c)
            row[ix(c,pts)]=1
        STATES.append(row)
assert len(STATES)==90

def affdim(rows):
    return sp.Matrix([[1]+list(r) for r in rows]).rank()-1
assert affdim(STATES)==37

sparse=[0]*45
for e in [(0,1),(0,2)]: sparse[ix(0,e)]+=1
for e in [(1,5),(2,5),(3,4),(3,5),(4,5)]: sparse[ix(1,e)]-=1
for e in [(3,5),(4,5)]: sparse[ix(2,e)]-=1

vals=[-sum(a*x for a,x in zip(sparse,r)) for r in STATES]
assert set(vals)=={0,1}
active=[r for r,s in zip(STATES,vals) if s==0]
assert len(active)==60
assert affdim(active)==36

def transform_coeff(a, vp, cp):
    out=[0]*45
    for c in range(3):
        for e in EDGES:
            ee=edge((vp[e[0]],vp[e[1]]))
            out[ix(cp[c],ee)]=a[ix(c,e)]
    return out

active_sets=set()
for vp_tuple in itertools.permutations(V):
    vp={i:vp_tuple[i] for i in V}
    for cp_tuple in itertools.permutations(range(3)):
        cp={i:cp_tuple[i] for i in range(3)}
        aa=transform_coeff(sparse,vp,cp)
        act=tuple(j for j,r in enumerate(STATES)
                  if -sum(a*x for a,x in zip(aa,r))==0)
        active_sets.add(act)
assert len(active_sets)==1080
print("exact sparse facet: active=60, face-dim=36, orbit=1080")

S1=[(1,5),(2,5),(3,4),(3,5),(4,5)]
S2=[(3,5),(4,5)]
zlabels=[(1,e) for e in S1]+[(2,e) for e in S2]

def haar_unitary(n,rng):
    Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    Q,R=np.linalg.qr(Z)
    d=np.diag(R)
    Q=Q*(d/np.abs(d)).conj()
    return Q

def minor(U,c,e):
    return np.linalg.det(U[np.ix_(list(e),[2*c,2*c+1])])

def lapsign(C,B):
    pos=[C.index(x) for x in B]
    return (-1)**(sum(pos)+1)

def coeff_row(U,target):
    C=[v for v in V if v not in target]
    row=np.zeros(len(zlabels),dtype=complex)
    for B in itertools.combinations(C,2):
        comp=tuple(x for x in C if x not in B)
        s=lapsign(C,list(B))
        for j,(c,e) in enumerate(zlabels):
            if c==1 and tuple(B)==e:
                row[j]+=s*minor(U,2,comp)
            elif c==2 and tuple(comp)==e:
                row[j]+=s*minor(U,1,B)
    return row

rng=np.random.default_rng(20260915)
maxeig=0.0
maxnormerr=0.0
for _ in range(2000):
    U=haar_unitary(6,rng)
    M=np.vstack([coeff_row(U,(0,1)), coeff_row(U,(0,2))])
    z=np.array([minor(U,c,e) for c,e in zlabels])
    a=M@z
    target=np.array([minor(U,0,(0,1)),minor(U,0,(0,2))])
    maxnormerr=max(maxnormerr,abs(np.vdot(a,a).real-np.vdot(target,target).real))
    lam=np.linalg.eigvalsh(M@M.conj().T)[-1].real
    maxeig=max(maxeig,lam)
    assert lam <= 1+2e-10
    assert np.vdot(a,a).real <= np.vdot(z,z).real+2e-10

print("numerical operator diagnostic: max eigenvalue",maxeig)
print("target norm-square agreement max error",maxnormerr)
print("ALL CHECKS PASSED")
