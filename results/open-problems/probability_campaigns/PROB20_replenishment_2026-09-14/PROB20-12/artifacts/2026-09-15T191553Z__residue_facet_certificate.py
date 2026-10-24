"""
PROB20-12 exact/reproducible certificate for the 2026-09-15 residue-facet proof.

Checks:
  1. The K6 rank-(2,2,2) colored marginal polytope has affine dimension 37.
  2. The residue representative is a genuine facet: 60 active states,
     face affine dimension 36, S6 x S3 orbit size 360.
  3. CORRECTION: with the integer normalization L<=1, deterministic slack is
     {0,3}, not {0,1}.
  4. The q-coefficient expansion of D=(1-L)/3 has the exact coefficient
     pattern used in the proof.
  5. Random Haar-complex tests verify direct Pluecker L, adapted-basis D,
     and grouped D=G+B1+B2 to floating tolerance. Numerics are diagnostic only.
"""
import itertools
import math
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

T={0,1,3}; d=2; R={4,5}
def inside(S): return [e for e in EDGES if set(e)<=set(S)]
A=set(inside(T)) | {edge((d,r)) for r in R}
B={edge((d,t)) for t in T} | set(inside(R))
C={edge((t,r)) for t in T for r in R}
assert len(A)==5 and len(B)==4 and len(C)==6
assert A|B|C==set(EDGES) and not(A&B or A&C or B&C)

coef=[0]*45
for e in A:
    coef[ix(0,e)]+=1; coef[ix(1,e)]-=1
for e in B:
    coef[ix(1,e)]+=1; coef[ix(2,e)]-=1
for e in C:
    coef[ix(2,e)]+=1; coef[ix(0,e)]-=1

vals=[sum(a*x for a,x in zip(coef,row)) for row in STATES]
slacks=[1-v for v in vals]
assert set(vals)=={1,-2}
assert set(slacks)=={0,3}
active=[row for row,s in zip(STATES,slacks) if s==0]
assert len(active)==60
assert affdim(active)==36
print("residue facet exact: active=60, face_dim=36, integer slack={0,3}")

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
        aa=transform_coeff(coef,vp,cp)
        act=tuple(j for j,row in enumerate(STATES)
                  if 1-sum(a*x for a,x in zip(aa,row))==0)
        active_sets.add(act)
assert len(active_sets)==360
print("residue orbit exact: 360 facets, stabilizer",4320//360)

p0,p1,p2=sp.symbols("p0 p1 p2", nonnegative=True)
w0=1-p0
labels=("u0","u1","u2","v0","v1","v2")
qsyms={pair:sp.symbols("q_"+pair[0]+pair[1])
       for pair in itertools.combinations(labels,2)}
expr=0
for pair,q in qsyms.items():
    c=0
    if "u0" in pair: c+=w0
    if "v0" in pair: c+=1
    if set(pair)=={"u0","v0"}: c-=1
    if "u1" in pair: c+=p1
    if set(pair)=={"u2","v2"}: c+=1
    c-=p1
    expr += sp.expand(c)*q
expr=sp.expand(expr.subs(p0,1-p1-p2))

expected={
("u0","u1"):p1+p2,
("u0","u2"):p2,
("u0","v0"):p2,
("u0","v1"):p2,
("u0","v2"):p2,
("u1","u2"):0,
("u1","v0"):1,
("u1","v1"):0,
("u1","v2"):0,
("u2","v0"):1-p1,
("u2","v1"):-p1,
("u2","v2"):1-p1,
("v0","v1"):1-p1,
("v0","v2"):1-p1,
("v1","v2"):-p1,
}
for pair,q in qsyms.items():
    got=sp.expand(expr).coeff(q)
    assert sp.simplify(got-expected[pair])==0
print("exact q coefficient table verified")

def haar_unitary(n,rng):
    z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    q,r=np.linalg.qr(z)
    diag=np.diag(r)
    return q*(diag/np.abs(diag))

def direct_L(U):
    mus=[]
    for i in range(3):
        cols=[2*i,2*i+1]
        md={}
        for e in EDGES:
            md[e]=abs(np.linalg.det(U[np.ix_(e,cols)]))**2
        mus.append(md)
    L=sum(mus[0][e] for e in A)-sum(mus[1][e] for e in A)
    L+=sum(mus[1][e] for e in B)-sum(mus[2][e] for e in B)
    L+=sum(mus[2][e] for e in C)-sum(mus[0][e] for e in C)
    return float(L)

def adapted(U):
    e=np.zeros(6,dtype=complex); e[d]=1
    ps=[]; fs=[]; bs=[]
    for i in range(3):
        H=U[:,2*i:2*i+2]
        h=H@(H.conj().T@e)
        p=float(np.vdot(h,h).real)
        if p<1e-12:
            return None
        g=h/np.sqrt(p)
        g*=np.exp(-1j*np.angle(g[d]))
        row=H[d,:]
        c=np.array([-row[1],row[0]],dtype=complex)
        c/=np.linalg.norm(c)
        f=H@c
        b=g-np.sqrt(p)*e
        ps.append(p);fs.append(f);bs.append(b)
    rix=sorted(R)
    us=[f[rix] for f in fs]
    vs=[b[rix] for b in bs]
    return ps,us,vs

def qdet(a,b):
    return abs(np.linalg.det(np.stack([a,b],axis=1)))**2

rng=np.random.default_rng(20260915)
max_e1=max_e2=max_rel=0.0
minD=minB1=minB2=1e9
for _ in range(500):
    U=haar_unitary(6,rng)
    z=adapted(U)
    if z is None: continue
    ps,us,vs=z
    p0n,p1n,p2n=ps
    w0n=1-p0n; w1n=1-p1n
    D=w0n*np.vdot(us[0],us[0]).real + np.vdot(vs[0],vs[0]).real
    D-=qdet(us[0],vs[0])
    D+=p1n*np.vdot(us[1],us[1]).real + qdet(us[2],vs[2]) - p1n
    G=w0n*qdet(us[0],us[1])
    G+=p2n*(qdet(us[0],us[2])+qdet(us[0],vs[0])
            +qdet(us[0],vs[1])+qdet(us[0],vs[2]))
    G+=qdet(us[1],vs[0])
    B1=w1n*(qdet(us[2],vs[0])+qdet(us[2],vs[2]))-p1n*qdet(us[2],vs[1])
    B2=w1n*(qdet(vs[0],vs[1])+qdet(vs[0],vs[2]))-p1n*qdet(vs[1],vs[2])
    L=direct_L(U)
    rel=np.linalg.norm(np.sqrt(p0n)*vs[0]+np.sqrt(p1n)*vs[1]+np.sqrt(p2n)*vs[2])
    max_e1=max(max_e1,abs((1-L)/3-D))
    max_e2=max(max_e2,abs(D-(G+B1+B2)))
    max_rel=max(max_rel,rel)
    minD=min(minD,D); minB1=min(minB1,B1); minB2=min(minB2,B2)

assert max_e1<1e-10 and max_e2<1e-10 and max_rel<1e-10
assert minD>-1e-10 and minB1>-1e-10 and minB2>-1e-10
print("diagnostic Haar checks passed")
print("max |(1-L)/3-D| =",max_e1)
print("max |D-(G+B1+B2)| =",max_e2)
print("max frame relation residual =",max_rel)
print("min sampled D,B1,B2 =",minD,minB1,minB2)
print("ALL CHECKS PASSED")
