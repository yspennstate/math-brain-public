#!/usr/bin/env python3
# R03 run37 exact finite self-check.
# Verifies the binary-pivot bijection C296 for d<=4 and an explicit d=5
# collision-free singular B for which J-2B is still singular (the pivot obstruction).
from itertools import product
from fractions import Fraction

def det_bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    if n==0: return 1
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            q=None
            for i in range(k+1,n):
                if A[i][k]!=0:
                    q=i; break
            if q is None:
                return 0
            A[k],A[q]=A[q],A[k]
            sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n):
            A[i][k]=0
    return sign*A[n-1][n-1]

def rank_exact(M):
    A=[[Fraction(x) for x in row] for row in M]
    n=len(A); m=len(A[0]) if n else 0
    r=0
    for c in range(m):
        p=None
        for i in range(r,n):
            if A[i][c]:
                p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(n):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(m)]
        r+=1
        if r==n: break
    return r

def nullvec(M):
    n=len(M)
    A=[[Fraction(x) for x in row] for row in M]
    pivcols=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,n) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(n):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        pivcols.append(c); r+=1
    free=[c for c in range(n) if c not in pivcols]
    assert len(free)==1
    f=free[0]
    v=[Fraction(0) for _ in range(n)]
    v[f]=1
    for i,c in reversed(list(enumerate(pivcols))):
        v[c]=-sum(A[i][j]*v[j] for j in range(c+1,n))
    from math import gcd
    from functools import reduce
    def lcm(a,b): return a//gcd(a,b)*b
    L=1
    for x in v: L=lcm(L,x.denominator)
    z=[int(x*L) for x in v]
    g=reduce(gcd,(abs(x) for x in z if x),0)
    z=[x//g for x in z]
    if next(x for x in z if x)<0: z=[-x for x in z]
    return z

def sign_matrix(bits,d):
    return [[1 if bits[i*d+j] else -1 for j in range(d)] for i in range(d)]

def binary_from_S(S):
    d=len(S)
    return [[(1-S[i][j])//2 for j in range(d)] for i in range(d)]

def S_from_B(B):
    d=len(B)
    return [[1-2*B[i][j] for j in range(d)] for i in range(d)]

def zero_row_col(B):
    d=len(B)
    zr=any(all(B[i][j]==0 for j in range(d)) for i in range(d))
    zc=any(all(B[i][j]==0 for i in range(d)) for j in range(d))
    return zr,zc

def no_equal_or_complement_rows_cols(B):
    d=len(B)
    rows=[tuple(B[i]) for i in range(d)]
    cols=[tuple(B[i][j] for i in range(d)) for j in range(d)]
    def good(V):
        if len(set(V))<len(V): return False
        S=set(V)
        for v in V:
            cv=tuple(1-x for x in v)
            if cv in S and cv!=v: return False
        return True
    return good(rows) and good(cols)

def key(B):
    return tuple(x for row in B for x in row)

def all_binary(d):
    for bits in product((0,1), repeat=d*d):
        yield [list(bits[i*d:(i+1)*d]) for i in range(d)]

for d in (2,3,4):
    direct={}
    for B in all_binary(d):
        if det_bareiss(B)!=0: continue
        S=S_from_B(B)
        if det_bareiss(S)==0: continue
        zr,zc=zero_row_col(B)
        if zr or zc: continue
        assert rank_exact(B)==d-1
        assert no_equal_or_complement_rows_cols(B)
        vr=nullvec(B)
        vl=nullvec([list(col) for col in zip(*B)])
        assert sum(vr)!=0 and sum(vl)!=0
        direct[key(B)]=B

    pre={}
    I=0
    section_excess_nontriv=0
    for sbits in product((0,1), repeat=d*d):
        R=sign_matrix(sbits,d)
        if det_bareiss(R)==0: continue
        I+=1
        good_x=0
        for xbits in product((-1,1), repeat=d):
            S=[[R[i][j]*xbits[j] for j in range(d)] for i in range(d)]
            B=binary_from_S(S)
            if det_bareiss(B)!=0: continue
            zr,zc=zero_row_col(B)
            if zr or zc: continue
            pre[key(B)]=pre.get(key(B),0)+1
            good_x+=1
        section_excess_nontriv += good_x
    assert set(pre)==set(direct)
    assert all(v==(1<<d) for v in pre.values())
    assert section_excess_nontriv==(1<<d)*len(direct)
    print("d",d,"I_d",I,"N_pivot",len(direct),
          "sum_nontriv_excess",section_excess_nontriv,"fiber",(1<<d))

B5=[
[0,1,1,1,1],
[1,1,1,1,1],
[1,0,0,1,1],
[1,1,0,0,1],
[1,0,1,1,0],
]
S5=S_from_B(B5)
assert det_bareiss(B5)==0
assert rank_exact(B5)==4
assert det_bareiss(S5)==0
assert rank_exact(S5)==4
zr,zc=zero_row_col(B5)
assert not zr and not zc
assert no_equal_or_complement_rows_cols(B5)
vr=nullvec(B5)
vl=nullvec([list(col) for col in zip(*B5)])
assert sum(vr)==0
assert sum(vl)!=0
print("d5_obstruction_B",B5)
print("d5_right_null",vr,"sum",sum(vr))
print("d5_left_null",vl,"sum",sum(vl))
print("d5_detB",det_bareiss(B5),"rankB",rank_exact(B5),
      "detS",det_bareiss(S5),"rankS",rank_exact(S5))
print("SELF-CHECK PASS")
