#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

def det(A):
    n=len(A)
    if n==0: return F(1)
    M=[row[:] for row in A]; out=F(1)
    for c in range(n):
        piv=next((r for r in range(c,n) if M[r][c]),None)
        if piv is None: return F(0)
        if piv!=c:
            M[c],M[piv]=M[piv],M[c]; out=-out
        p=M[c][c]; out*=p
        for j in range(c,n): M[c][j]/=p
        for r in range(c+1,n):
            q=M[r][c]
            if q:
                for j in range(c,n): M[r][j]-=q*M[c][j]
    return out

def inv(A):
    n=len(A)
    M=[A[i][:]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c])
        if piv!=c: M[c],M[piv]=M[piv],M[c]
        p=M[c][c]; M[c]=[x/p for x in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q: M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def stationary(P):
    n=len(P)
    A=[[P[j][i]-F(int(i==j)) for j in range(n)] for i in range(n-1)]
    A.append([F(1)]*n)
    b=[F(0)]*(n-1)+[F(1)]
    B=inv(A)
    return [sum(B[i][j]*b[j] for j in range(n)) for i in range(n)]

def group_Z(P,pi):
    n=len(P)
    B=inv([[F(int(i==j))-P[i][j]+pi[j] for j in range(n)] for i in range(n)])
    return [[B[i][j]-pi[j] for j in range(n)] for i in range(n)]

def boundary_matrix(A,Z,pi):
    A=list(A); m=len(A)
    return [[Z[a][b] for a in A]+[-pi[b]] for b in A] + [[F(1)]*m+[F(0)]]

def singleton_green(a,i,j,Z,pi):
    if i==a or j==a: return F(0)
    return Z[i][j]-Z[a][j]+pi[j]*(Z[a][a]-Z[i][a])/pi[a]

def killed_green(P,A):
    T=[i for i in range(len(P)) if i not in A]
    Q=[[P[i][j] for j in T] for i in T]
    N=inv([[F(int(i==j))-Q[i][j] for j in range(len(T))] for i in range(len(T))])
    return T,N

P1=[[F(1,2),F(1,2),0],[F(1,4),F(1,2),F(1,4)],[0,F(1,2),F(1,2)]]
C=[[F(2),F(1),0,F(1)],[F(1),F(3),F(2),0],[0,F(2),F(1),F(1)],[F(1),0,F(1),F(4)]]
P2=[[x/sum(row) for x in row] for row in C]
P3=[[0,F(1,2),0,F(1,2)],[F(1,2),0,F(1,2),0],[0,F(1,2),0,F(1,2)],[F(1,2),0,F(1,2),0]]
P4=[[0,1,0],[0,0,1],[1,0,0]]
chains=[("lazy_path3",P1),("weighted_reversible4",P2),("periodic_cycle4",P3),("directed_cycle3",P4)]

denom_cases=green_cases=numerator_cases=0
for name,P in chains:
    P=[[F(x) for x in row] for row in P]
    n=len(P); pi=stationary(P); Z=group_Z(P,pi)
    for k in range(1,n):
        for A in combinations(range(n),k):
            a=A[0]; S=[x for x in A if x!=a]
            M=boundary_matrix(A,Z,pi); Delta=det(M)
            FSS=[[singleton_green(a,s,t,Z,pi) for t in S] for s in S]
            assert Delta == pi[a]*det(FSS)
            denom_cases += 1
            T,GA=killed_green(P,set(A))
            FSSinv=inv(FSS) if S else None
            for i in T:
                for j in T:
                    Fa=singleton_green(a,i,j,Z,pi)
                    if S:
                        vi=[singleton_green(a,i,s,Z,pi) for s in S]
                        wj=[singleton_green(a,s,j,Z,pi) for s in S]
                        correction=sum(vi[r]*FSSinv[r][c]*wj[c]
                                       for r in range(len(S)) for c in range(len(S)))
                    else:
                        correction=F(0)
                    schur=Fa-correction
                    true=GA[T.index(i)][T.index(j)]
                    assert schur == true

                    bvec=[Z[i][x] for x in A]+[F(1)]
                    rvec=[Z[x][j] for x in A]+[-pi[j]]
                    K=[M[r]+[bvec[r]] for r in range(len(M))]
                    K.append(rvec+[Z[i][j]])
                    port=det(K)/Delta
                    assert port == true
                    green_cases += 1

                    if S:
                        B=[[singleton_green(a,s,t,Z,pi) for t in S]+
                           [singleton_green(a,s,j,Z,pi)] for s in S]
                        B.append([singleton_green(a,i,t,Z,pi) for t in S]+
                                 [singleton_green(a,i,j,Z,pi)])
                        schur_num=det(B)
                    else:
                        schur_num=singleton_green(a,i,j,Z,pi)
                    assert det(K) == pi[a]*schur_num
                    numerator_cases += 1

print("exact Fraction arithmetic only")
print("chains=4")
print(f"denominator_identity_cases={denom_cases}")
print(f"green_schur_port_cases={green_cases}")
print(f"numerator_identity_cases={numerator_cases}")
print("PASS")
