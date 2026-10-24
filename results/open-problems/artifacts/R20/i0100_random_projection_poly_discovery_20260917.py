#!/usr/bin/env python3
"""R20 / I0100 discovery-only computations.

NO CLAIM IN THIS FILE IS AN EXACT CERTIFICATE.
The script uses floating FFT/LP/QR only to compare:
  (i) low-degree balanced scalar-profile hierarchy for the Paley half-Fourier spaces;
  (ii) previously recorded full numerical radial-LP values;
  (iii) Haar-random half-dimensional simplex projections.

It is an idea-discovery artifact, not admissible evidence for the fixed exact-prime metric.
"""
import math
import numpy as np
from scipy.optimize import linprog

np.set_printoptions(precision=10, suppress=True)


def prime_factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out


def primitive_root(p):
    fac=prime_factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac):
            return g
    raise RuntimeError


def paley_halves(p):
    assert p%4==1
    n=(p-1)//2
    g=primitive_root(p); alpha=pow(g,2,p)
    Q={pow(x,2,p) for x in range(1,p)}
    S=[]
    x=1
    for d in range(1,n):
        x=(x*alpha)%p
        if (x-1)%p in Q:S.append(d)
    S=set(S)
    N=set(range(1,n))-S
    return n, sorted(S), sorted(N)


def c_vector(n,Z):
    d=len(Z); A=n/d
    spec=np.zeros(n,dtype=complex)
    spec[Z]=A
    return np.fft.ifft(spec).real


def balance_profile(n,Z,f,c):
    d=len(Z); q=d/n
    fh=np.fft.fft(f)
    proj_spec=np.zeros(n,dtype=complex); proj_spec[Z]=fh[Z]
    P=np.fft.ifft(proj_spec).real
    radial=float(np.dot(c,f))
    return f-P+q*radial*c


def polynomial_hierarchy(n,Z,degrees):
    c=c_vector(n,Z)
    maxdeg=max(degrees)
    cols=[]
    for r in range(maxdeg+1):
        f=np.zeros(n)
        # scaled monomial basis improves numerical conditioning but spans the same profiles
        f[1:]=(math.sqrt(n)*c[1:])**r
        cols.append(balance_profile(n,Z,f,c)[1:])
    B=np.column_stack(cols)
    mass=B.sum(axis=0)
    obj=-(c[1:,None]*B).sum(axis=0)
    rows=[]
    for m in degrees:
        BM=B[:,:m+1]; mm=mass[:m+1]; oo=obj[:m+1]
        res=linprog(-oo,A_ub=-BM,b_ub=np.zeros(n-1),A_eq=mm[None,:],b_eq=np.array([1.0]),
                    bounds=[(None,None)]*(m+1),method='highs')
        rows.append((m,float(oo@res.x)*math.sqrt(n) if res.success else float('nan')))
    return rows


def haar_subspace(n,d,rng):
    G=rng.normal(size=(n,d))
    G-=G.mean(axis=0,keepdims=True)
    Q,_=np.linalg.qr(G)
    return Q[:,:d]


def random_radial(Q):
    n,d=Q.shape
    # Rows of Q are a coordinate realization of the projected regular-simplex vertices.
    # Maximize a with sum_{i>0} y_i Q_i + a Q_0 = 0, sum y_i=1, y_i>=0, a>=0.
    c=np.r_[np.zeros(n-1),-1.]
    Aeq=np.zeros((d+1,n))
    Aeq[:d,:n-1]=Q[1:].T
    Aeq[:d,-1]=Q[0]
    Aeq[d,:n-1]=1
    beq=np.r_[np.zeros(d),1.]
    res=linprog(c,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*n,method='highs')
    return -float(res.fun)


def wendel_exceedance_at_critical(n,d):
    not_in=sum(math.comb(n-2,j) for j in range(d))/(2**(n-2))
    return 1.0-not_in


print('DISCOVERY_ONLY_NO_CERTIFICATE')
print('Paley p=1213 balanced polynomial hierarchy, values = sqrt(n)*a_profile')
n,S,N=paley_halves(1213)
degs=[1,2,3,4,5,8,10,12,15]
print('n',n,'|S|',len(S),'|N|',len(N))
print('N',polynomial_hierarchy(n,N,degs))
print('S',polynomial_hierarchy(n,S,degs))
print()
print('Full numerical radial LP values recovered from the preceding R20 discovery record; not recomputed here.')
print('p=181 N=1.0964371 S=1.1396844')
print('p=421 N=1.0370994 S=1.1125598')
print('p=1009 N=1.0366990 S=1.0566405')
print('p=1201 N=1.0493688 S=1.0358020')
print('p=1213 N=1.0583357 S=1.0266002')
print()
print('Haar-random half-dimensional projected simplex radial statistic')
rng=np.random.default_rng(20260917)
for n,reps in [(100,30),(200,15),(400,6),(800,2)]:
    d=n//2
    vals=np.array([math.sqrt(n)*random_radial(haar_subspace(n,d,rng)) for _ in range(reps)])
    critical=math.sqrt(n)/(math.sqrt(n)-1)
    empirical=float(np.mean(vals>=critical))
    exact=wendel_exceedance_at_critical(n,d)
    print('n',n,'reps',reps,'mean',float(vals.mean()),'median',float(np.median(vals)),
          'sd',float(vals.std()),'critical_scaled',critical,
          'empirical_P_ge_critical',empirical,'Wendel_exact',exact)
print('END_DISCOVERY_ONLY')
