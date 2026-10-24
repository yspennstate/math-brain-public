#!/usr/bin/env python3
# PROB10-07 exact checker: uniform-all-forests Rayleigh for K_{4,n} and K_{5,n}.
# Standard library only. Every arithmetic comparison is integer/Fraction exact.

from fractions import Fraction
from itertools import combinations

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b:b[0]))

def partitions(seq):
    if not seq:
        yield ()
        return
    x=seq[0]
    for p in partitions(seq[1:]):
        yield canon(((x,),)+p)
        for i in range(len(p)):
            q=[tuple(b) for b in p]
            q[i]=tuple(sorted(q[i]+(x,)))
            yield canon(tuple(q))

def build(m):
    P=sorted(set(partitions(tuple(range(m)))), key=lambda p:(-len(p),p))
    idx={p:i for i,p in enumerate(P)}
    d=len(P)
    def zmat(): return [[0]*d for _ in range(d)]
    M=zmat(); E0=zmat(); E1=zmat(); E01=zmat()
    def legal(p,S):
        S=set(S)
        return all(sum(x in S for x in b)<=1 for b in p)
    def nxt(p,S):
        S=set(S)
        if len(S)<=1: return p
        hit=[i for i,b in enumerate(p) if any(x in S for x in b)]
        merged=tuple(sorted(x for i in hit for x in p[i]))
        return canon([p[i] for i in range(len(p)) if i not in hit]+[merged])
    for i,p in enumerate(P):
        for r in range(m+1):
            for S in combinations(range(m),r):
                if not legal(p,S): continue
                j=idx[nxt(p,S)]
                M[i][j]+=1
                if 0 in S: E0[i][j]+=1
                if 1 in S: E1[i][j]+=1
                if 0 in S and 1 in S: E01[i][j]+=1
    return P,M,E0,E1,E01

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def eye(n):
    A=[[0]*n for _ in range(n)]
    for i in range(n): A[i][i]=1
    return A
def matsub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[c*x for x in row] for row in A]
def mpow(A,k):
    R=eye(len(A)); B=A
    while k:
        if k&1: R=matmul(R,B)
        B=matmul(B,B); k//=2
    return R
def rowmul(v,A):
    return [sum(v[k]*A[k][j] for k in range(len(v))) for j in range(len(A[0]))]
def chain(d,mats):
    v=[1]+[0]*(d-1)
    for A in mats: v=rowmul(v,A)
    return sum(v)

def formulas(m,n):
    if m==4:
        Z =Fraction(5**n*(16*n**3+87*n**2+172*n+125),125)
        E =Fraction(5**n*(16*n**3+159*n**2+436*n+389),625)
        R =Fraction(5**n*(n+3)*(8*n+17),125)
        L =Fraction(5**n*(16*n**3+231*n**2+766*n+791),3125)
        D =Fraction(5**n*(16*n**3+231*n**2+966*n+1141),3125)
        pR=[256,2144,7577,14698,16271,8054]
        pL=[688,5011,14059,17901,8741]
        pD=[464,3533,9752,11103,4348]
        def peval(cs): return sum(c*n**(len(cs)-1-i) for i,c in enumerate(cs))
        DR=Fraction(5**(2*n)*(n-1)*peval(pR),390625)
        DL=Fraction(6*5**(2*n)*peval(pL),390625)
        DD=Fraction(2*5**(2*n)*peval(pD),390625)
        return Z,E,R,L,D,DR,DL,DD,pR,pL,pD
    if m==5:
        Z =Fraction(6**n*(125*n**4+810*n**3+2095*n**2+2586*n+1296),1296)
        E =Fraction(6**n*(125*n**4+1510*n**3+5527*n**2+8558*n+5016),7776)
        R =Fraction(6**n*(25*n**3+174*n**2+383*n+282),648)
        L =Fraction(6**n*(125*n**4+2210*n**3+9739*n**2+17398*n+11544),46656)
        D =Fraction(6**n*(125*n**4+2210*n**3+12439*n**2+25930*n+18672),46656)
        pR=[15625,168125,805975,2271335,4142704,4942988,3544512,1153728]
        pL=[98125,953625,3957811,8974947,11722144,8363316,2549808]
        pD=[6875,70125,296603,658671,799058,495348,120168]
        def peval(cs): return sum(c*n**(len(cs)-1-i) for i,c in enumerate(cs))
        DR=Fraction(6**(2*n)*(n-1)*peval(pR),60466176)
        DL=Fraction(6**(2*n)*peval(pL),15116544)
        DD=Fraction(6**(2*n)*peval(pD),7558272)
        return Z,E,R,L,D,DR,DL,DD,pR,pL,pD
    raise ValueError

def verify_transfer(m):
    P,M,E0,E1,E01=build(m); d=len(P); c=m+1
    N=matsub(M,scale(eye(d),c))
    assert mpow(N,m)==[[0]*d for _ in range(d)]
    assert mpow(N,m-1)!=[[0]*d for _ in range(d)]
    for n in range(1,2*m+6):
        Z,E,R,L,D,DR,DL,DD,pR,pL,pD=formulas(m,n)
        assert chain(d,[mpow(M,n)])==Z
        assert chain(d,[E0,mpow(M,n-1)])==E
        assert chain(d,[E01,mpow(M,n-1)])==R
        assert E*E-Z*R==DR
        if n>=2:
            assert chain(d,[E0,E0,mpow(M,n-2)])==L
            assert chain(d,[E0,E1,mpow(M,n-2)])==D
            assert E*E-Z*L==DL
            assert E*E-Z*D==DD
        assert all(x>0 for x in pR+pL+pD)
        assert DR>=0
        if n>=2: assert DL>0 and DD>0
    return d

def is_forest(vcount,edges,mask):
    p=list(range(vcount)); r=[0]*vcount
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b:return False
        if r[a]<r[b]:a,b=b,a
        p[b]=a
        if r[a]==r[b]:r[a]+=1
        return True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1 and not union(u,v): return False
    return True

def brute(m,n):
    edges=[(i,m+j) for j in range(n) for i in range(m)]
    e=0; fr=1; fl=m if n>=2 else None; fd=m+1 if n>=2 else None
    z=ee=rr=ll=dd=0
    for mask in range(1<<len(edges)):
        if not is_forest(m+n,edges,mask): continue
        z+=1
        if mask&1: ee+=1
        if (mask&1) and ((mask>>fr)&1): rr+=1
        if n>=2:
            if (mask&1) and ((mask>>fl)&1): ll+=1
            if (mask&1) and ((mask>>fd)&1): dd+=1
    Z,E,R,L,D,*_=formulas(m,n)
    assert (z,ee,rr)==(Z,E,R)
    if n>=2: assert (ll,dd)==(L,D)
    return z,ee,rr,ll,dd

d4=verify_transfer(4)
d5=verify_transfer(5)
print('states_m4',d4)
print('states_m5',d5)
for m,upto in [(4,4),(5,3)]:
    for n in range(1,upto+1):
        print('brute',m,n,brute(m,n))
for m in (4,5):
    _,_,_,_,_,_,_,_,pR,pL,pD=formulas(m,2)
    print('positive_factor_coefficients_m',m,'R',pR)
    print('positive_factor_coefficients_m',m,'L',pL)
    print('positive_factor_coefficients_m',m,'D',pD)
print('K4_K5_TRANSFER_EXACT_PASS')