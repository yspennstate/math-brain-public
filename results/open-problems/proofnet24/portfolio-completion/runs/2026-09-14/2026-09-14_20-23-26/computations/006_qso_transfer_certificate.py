"""Exact finite validation supporting (not replacing) the proof in agents/006.md.
Uses only the Python standard library. No fixed-point search is used.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random
from math import sqrt
import json

N=4
pairs=list(combinations(range(N),2))
unordered=[(i,j) for i in range(N) for j in range(i,N)]
allowed=[[k for k in range(N) if k not in (i,j)] for i,j in unordered]

def tensor_from_targets(targets):
    P=[[[0]*N for _ in range(N)] for _ in range(N)]
    for (i,j),k in zip(unordered,targets):
        P[i][j][k]=P[j][i][k]=1
    return P

vertices=0
transfer_certificates=0
for targets in product(*allowed):
    P=tensor_from_targets(targets)
    vertices+=1
    for G in pairs:
        H=tuple(i for i in range(N) if i not in G)
        p=[[sum(P[a][b][r] for r in G) for b in range(N)] for a in range(N)]
        for i in G:
            k=next(a for a in G if a!=i)
            for j in H:
                ell=next(a for a in H if a!=j)
                assert p[k][i]==0 and p[ell][j]==1
                # L = sum_a m_a (p_ai - p_aj).
                # U = m_i(1-p_ij)+m_j*p_ij.
                # U-L has coefficient vector (1-p_ii, p_jj, p_kj, 1-p_li)
                # in the ordering (i,j,k,ell), so is nonnegative for all m >= 0.
                coeff_L=[p[a][i]-p[a][j] for a in range(N)]
                coeff_U=[0]*N
                coeff_U[i]=1-p[i][j]
                coeff_U[j]=p[i][j]
                residual=[coeff_U[a]-coeff_L[a] for a in range(N)]
                expected=[0]*N
                expected[i]=1-p[i][i]
                expected[j]=p[j][j]
                expected[k]=p[k][j]
                expected[ell]=1-p[ell][i]
                assert residual==expected and min(residual)>=0
                transfer_certificates+=1

# Check polarization, transfer decomposition, and bound using exact rational nonvertex P.
rng=Random(6006)
def random_point():
    weights=[rng.randint(0,20) for _ in range(N)]
    if sum(weights)==0: weights[0]=1
    return [F(w,sum(weights)) for w in weights]
def random_tensor():
    P=[[[F(0)]*N for _ in range(N)] for _ in range(N)]
    for (i,j),opts in zip(unordered,allowed):
        ww=[rng.randint(0,20) for _ in opts]
        if sum(ww)==0: ww[0]=1
        for k,w in zip(opts,ww): P[i][j][k]=P[j][i][k]=F(w,sum(ww))
    return P
def V(P,x):
    return [sum(P[i][j][k]*x[i]*x[j] for i in range(N) for j in range(N)) for k in range(N)]
polarization_checks=0
rational_transfer_checks=0
for trial in range(200):
    P=random_tensor();x=random_point();y=random_point()
    m=[(a+b)/2 for a,b in zip(x,y)];z=[a-b for a,b in zip(x,y)]
    A=[[sum(P[a][j][k]*m[a] for a in range(N)) for j in range(N)] for k in range(N)]
    vx=V(P,x);vy=V(P,y)
    assert [a-b for a,b in zip(vx,vy)]==[2*sum(A[k][j]*z[j] for j in range(N)) for k in range(N)]
    polarization_checks+=1
    for G in pairs:
        H=tuple(i for i in range(N) if i not in G)
        for i in G:
            for j in H:
                T=sum(A[k][i]-A[k][j] for k in G)
                assert T<=max(m[i],m[j])
                rational_transfer_checks+=1
    G=[i for i in range(N) if z[i]>0];H=[i for i in range(N) if z[i]<0]
    if len(G)==len(H)==2:
        h=sum(z[i] for i in G)
        zz=[F(0)]*N
        for i in G:
            for j in H:
                t=z[i]*(-z[j])/h
                zz[i]+=t;zz[j]-=t
        assert zz==z
        assert sum(vx[i]-vy[i] for i in G)<=2*max(m)*h

results={
    'vertex_operators_checked':vertices,
    'exact_coefficient_certificates_checked':transfer_certificates,
    'exact_rational_polarization_checks':polarization_checks,
    'exact_rational_transfer_checks':rational_transfer_checks,
    'contraction_factor_3_minus_sqrt5':3-sqrt(5),
    'status':'all assertions passed',
    'limitations':'Finite checks validate identities and guard indexing. The general uniqueness theorem is proved in agents/006.md, not inferred from sampling.'
}
print(json.dumps(results,indent=2))
