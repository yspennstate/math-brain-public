#!/usr/bin/env python3
"""
PROB10-10 exact/self-check artifact, 2026-09-20T0218Z.

Two finite cores:
(1) exact CTMC values for the synchronized contiguous-frontier slab compiler;
(2) an exact-rational verification of a longer-memory simple-path transfer
    certificate for the Exp(1) axis time constant.

The Perron/Collatz witness in (2) is *found* with floating-point sparse linear
algebra, but every inequality used in the mathematical certificate is then
verified exactly with fractions.Fraction. A pass therefore does not rely on
the floating approximation being accurate.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial
import numpy as np
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import eigs, spsolve

DIRS=((1,0),(-1,0),(0,1),(0,-1))

def q_sync(k,r):
    """Expected first time some k consecutive terminal vertices are infected.

    Oriented Exp(1) edges, k synchronized consecutive seeds at level 0,
    terminal antidiagonal at level r. Exact CTMC recurrence.
    """
    vertices=[]
    idx={}
    for s in range(r+1):
        for j in range(k+s):
            idx[(s,j)] = len(vertices)
            vertices.append((s,j))
    init=0
    for j in range(k):
        init |= 1 << idx[(0,j)]

    targets=[]
    for a in range(r+1):
        mask=0
        for j in range(a,a+k):
            mask |= 1 << idx[(r,j)]
        targets.append(mask)

    out={}
    for s in range(r):
        for j in range(k+s):
            u=idx[(s,j)]
            out[u]=(idx[(s+1,j)],idx[(s+1,j+1)])

    def done(mask):
        return any((mask&t)==t for t in targets)

    @lru_cache(None)
    def E(mask):
        if done(mask):
            return Fraction(0)
        rates={}
        for u,vs in out.items():
            if (mask>>u)&1:
                for v in vs:
                    if not ((mask>>v)&1):
                        rates[v]=rates.get(v,0)+1
        total=sum(rates.values())
        assert total>0
        ans=Fraction(1,total)
        for v,mult in rates.items():
            ans += Fraction(mult,total)*E(mask | (1<<v))
        return ans
    return E(init),E.cache_info().currsize

def gen_states(L):
    """Locally self-avoiding path states consisting of L remembered vertices."""
    paths=[((0,0),)]
    for _ in range(L-1):
        nxt=[]
        for p in paths:
            x,y=p[-1]
            used=set(p)
            for dx,dy in DIRS:
                q=(x+dx,y+dy)
                if q not in used:
                    nxt.append(p+(q,))
        paths=nxt
    states=[]
    for p in paths:
        x0,y0=p[-1]
        states.append(tuple((x-x0,y-y0) for x,y in p))
    return states

def build_transfer(L,z_float):
    states=gen_states(L)
    index={s:i for i,s in enumerate(states)}
    rows=[]; cols=[]; data=[]; trans=[]
    for i,s in enumerate(states):
        used=set(s)
        for dx,dy in DIRS:
            if (dx,dy) in used:
                continue
            ns=tuple((x-dx,y-dy) for x,y in s[1:])+((0,0),)
            j=index[ns]
            rows.append(i); cols.append(j); data.append(z_float**dx)
            trans.append((i,j,dx))
    A=csr_matrix((data,(rows,cols)),shape=(len(states),len(states)))
    return states,trans,A

def exp_upper(x,N=14):
    """Exact Taylor/geometric-tail upper bound for exp(x), x>=0."""
    s=sum((x**j)/factorial(j) for j in range(N+1))
    first=x**(N+1)/factorial(N+1)
    assert x < N+2
    return s + first/(1-x/Fraction(N+2,1))

print("PROB10-10 exact/self-check artifact")
print("candidate_generation_uses_float = True")
print("all_certificate_inequalities_verified_with_Fraction = True")
print()

# Synchronized frontier CTMC checks.
expected = {
    (2,1): Fraction(3,4),
    (2,2): Fraction(240439,216000),
    (2,3): Fraction(5687268454443679,3920736960000000),
    (3,1): Fraction(11,12),
    (3,2): Fraction(2617979177,1944810000),
}
print("[synchronized-frontier exact CTMC]")
for key,want in expected.items():
    q,states=q_sync(*key)
    assert q==want
    k,r=key
    diag=Fraction(2)*q/r
    print(f"k={k} r={r} states={states} q={q} diag_upper={diag} diag_upper_float={float(diag):.15f}")
assert expected[(2,1)] == Fraction(1,2)*(Fraction(1,1)+Fraction(1,2))
assert expected[(3,1)] == Fraction(1,2)*(Fraction(1,1)+Fraction(1,2)+Fraction(1,3))
print("one_level_harmonic_identity_k2_k3 = PASS")
print()

# Longer-memory axis transfer certificate.
L=10
z=Fraction(1583,500)
c=Fraction(3002823,10_000_000)
states,trans,A=build_transfer(L,float(z))
assert len(states)==16268
assert len(trans)==44100

# Find a positive Collatz witness numerically.
rho=float(abs(eigs(A,k=1,which="LM",return_eigenvectors=False,
                   tol=1e-9,maxiter=300000)[0]))
R0=rho+1e-6
v=spsolve(R0*eye(A.shape[0],format="csr")-A,np.ones(A.shape[0]))
assert np.all(np.isfinite(v)) and float(v.min())>0
scale=1e9/float(v.min())
V=np.ceil(v*scale).astype(np.int64)
assert int(V.min())>0

# Exact Collatz verification M(z)V <= R V.
row=[Fraction(0) for _ in states]
for i,j,dx in trans:
    if dx==1:
        w=z
    elif dx==-1:
        w=1/z
    else:
        w=Fraction(1)
    row[i] += w*int(V[j])
ratios=[row[i]/int(V[i]) for i in range(len(states))]
R=max(ratios)
imax=ratios.index(R)

# A decimal rational y strictly above R; y=1+s is the Chernoff parameter.
DEN=10**12
ynum=(R.numerator*DEN + R.denominator-1)//R.denominator
y=Fraction(ynum,DEN)
assert R<y
assert R/y<1

x=(y-1)*c
eu=exp_upper(x,14)
base=R*eu/(y*z)
assert base<1

print("[axis longer-memory exact certificate]")
print(f"remembered_vertices_L={L}")
print(f"states={len(states)} transitions={len(trans)}")
print(f"z={z} z_float={float(z):.15f}")
print(f"candidate_numeric_rho={rho:.15f}")
print(f"witness_min={int(V.min())} witness_max={int(V.max())}")
print(f"max_collatz_index={imax}")
print(f"R_exact={R}")
print(f"R_float={float(R):.15f}")
print(f"y_exact={y}")
print(f"c_axis_exact={c}")
print(f"c_axis_float={float(c):.15f}")
print(f"x_exact={x}")
print(f"exp_upper_N14={eu}")
print(f"geometric_base_exact={base}")
print(f"geometric_base_float={float(base):.15f}")
print(f"one_minus_base_float={float(1-base):.15e}")
print(f"sufficient_diagonal_target_exact={2*c}")
print(f"sufficient_diagonal_target_float={float(2*c):.15f}")
print()
print("ALL_EXACT_CHECKS_PASS = True")
