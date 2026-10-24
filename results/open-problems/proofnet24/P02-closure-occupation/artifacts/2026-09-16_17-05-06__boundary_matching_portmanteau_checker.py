#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations, permutations

def det(A):
    n=len(A)
    if n==0: return F(1)
    M=[list(map(F,row)) for row in A]; out=F(1)
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
    if n==0: return []
    M=[list(map(F,A[i]))+[F(int(i==j)) for j in range(n)] for i in range(n)]
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
    # row a, column b is Z_{b,a}
    return [[Z[b][a] for b in A]+[-pi[a]] for a in A] + [[F(1)]*m+[F(0)]]

def solve(A,b):
    B=inv(A)
    return [sum(B[i][j]*b[j] for j in range(len(b))) for i in range(len(A))]

def killed_data(P,A,i,strict=False):
    """Exact pre-stopping occupation x, terminal law tau, and E[T].
    standard: T_A=inf{t>=0:X_t in A}
    strict:   T_A^+=inf{t>=1:X_t in A} when i in A
    """
    n=len(P); A=set(A); Al=sorted(A); T=[s for s in range(n) if s not in A]
    if T:
        Q=[[P[r][c] for c in T] for r in T]
        N=inv([[F(int(r==c))-Q[r][c] for c in range(len(T))] for r in range(len(T))])
        R=[[P[r][a] for a in Al] for r in T]
        H=[[sum(N[rr][k]*R[k][aa] for k in range(len(T))) for aa in range(len(Al))]
           for rr in range(len(T))]
        times=[sum(N[rr]) for rr in range(len(T))]
    else:
        N=[]; H=[]; times=[]
    def standard(s):
        x=[F(0)]*n; tau=[F(0)]*n
        if s in A:
            tau[s]=F(1); return x,tau,F(0)
        rr=T.index(s)
        for cc,j in enumerate(T): x[j]=N[rr][cc]
        for aa,a in enumerate(Al): tau[a]=H[rr][aa]
        return x,tau,times[rr]
    if not strict or i not in A:
        return standard(i)
    x=[F(0)]*n; x[i]=F(1)
    tau=[F(0)]*n; t=F(1)
    for y,p in enumerate(P[i]):
        if not p: continue
        if y in A:
            tau[y]+=p
        else:
            xx,ttau,ty=standard(y)
            for j in range(n): x[j]+=p*xx[j]
            for a in range(n): tau[a]+=p*ttau[a]
            t+=p*ty
    return x,tau,t

def port_formula(A,i,j,c,Z,pi):
    A=list(A)
    M=boundary_matrix(A,Z,pi); D=det(M)
    b=[Z[i][a]-c.get(a,F(0)) for a in A]+[F(1)]
    r=[Z[a][j] for a in A]+[-pi[j]]
    K=[M[k]+[b[k]] for k in range(len(M))]
    K.append(r+[Z[i][j]])
    return det(K)/D,D,K

def perm_sign(p):
    invs=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if invs%2 else 1

def matching_sum(matrix):
    s=F(0)
    for p in permutations(range(len(matrix))):
        term=F(perm_sign(p))
        for i,j in enumerate(p):
            term*=matrix[i][j]
            if term==0: break
        s+=term
    return s

P1=[[F(1,2),F(1,2),0],[F(1,4),F(1,2),F(1,4)],[0,F(1,2),F(1,2)]]
C=[[F(2),F(1),0,F(1)],[F(1),F(3),F(2),0],
   [0,F(2),F(1),F(1)],[F(1),0,F(1),F(4)]]
P2=[[F(x)/sum(F(y) for y in row) for x in row] for row in C]
P3=[[0,F(1,2),0,F(1,2)],[F(1,2),0,F(1,2),0],
    [0,F(1,2),0,F(1,2)],[F(1,2),0,F(1,2),0]]
P4=[[0,1,0],[0,0,1],[1,0,0]]
chains=[("lazy_path3",P1),("weighted_reversible4",P2),
        ("periodic_cycle4",P3),("directed_cycle3",P4)]

boundary_cases=standard_cases=strict_cases=0
matching_den_cases=matching_num_cases=identity_checks=0

for name,P in chains:
    P=[[F(x) for x in row] for row in P]
    n=len(P); pi=stationary(P); Z=group_Z(P,pi)

    # New boundary-data portmanteau + explicit signed matching expansion.
    for k in range(1,n+1):
        for A in combinations(range(n),k):
            M=boundary_matrix(A,Z,pi); D=det(M)
            assert D != 0
            assert matching_sum(M)==D
            boundary_cases += 1; matching_den_cases += 1
            for i in range(n):
                for strict in (False,True):
                    x,tau,t=killed_data(P,A,i,strict)
                    c={a:x[a] for a in A}
                    if not strict or i not in A:
                        assert all(c[a]==0 for a in A)
                    else:
                        assert all(c[a]==F(int(a==i)) for a in A)
                    y=solve(M,[Z[i][a]-c[a] for a in A]+[F(1)])
                    assert y[:-1]==[tau[a] for a in A]
                    assert y[-1]==t
                    for j in range(n):
                        port,D,K=port_formula(A,i,j,c,Z,pi)
                        assert port==x[j]
                        assert matching_sum(K)==det(K)
                        if strict: strict_cases += 1
                        else: standard_cases += 1
                        matching_num_cases += 1

    # Direct exact checks of the frozen eleven Section 2.2.2 identities.
    HT=[[killed_data(P,{j},i,False)[2] for j in range(n)] for i in range(n)]
    # Lemma 2.5
    for i in range(n):
        x,tau,t=killed_data(P,{i},i,True)
        assert t==1/pi[i]; identity_checks+=1
    # Lemma 2.6
    for i in range(n):
        x,tau,t=killed_data(P,{i},i,True)
        for j in range(n):
            assert x[j]==pi[j]/pi[i]; identity_checks+=1
    # Lemma 2.7
    for i in range(n):
        for j in range(n):
            if j==i: continue
            x,_,_=killed_data(P,{i},j,False)
            assert x[j]==pi[j]*(HT[j][i]+HT[i][j]); identity_checks+=1
    # Corollary 2.8
    for i in range(n):
        for j in range(n):
            if j==i: continue
            _,tau,_=killed_data(P,{i,j},i,True)
            assert tau[j]==1/(pi[i]*(HT[i][j]+HT[j][i])); identity_checks+=1
    # Lemma 2.9
    for i in range(n):
        for l in range(n):
            if i==l: continue
            x,_,_=killed_data(P,{l},i,False)
            for j in range(n):
                assert x[j]==pi[j]*(HT[i][l]+HT[l][j]-HT[i][j]); identity_checks+=1
    # Corollary 2.10
    for i in range(n):
        for l in range(n):
            if i==l: continue
            for j in range(n):
                if j==l: continue
                _,tau,_=killed_data(P,{j,l},i,False)
                rhs=(HT[i][l]+HT[l][j]-HT[i][j])/(HT[j][l]+HT[l][j])
                assert tau[j]==rhs; identity_checks+=1
    # Lemma 2.11
    for i in range(n):
        epi=sum(pi[s]*HT[s][i] for s in range(n))
        assert pi[i]*epi==Z[i][i]; identity_checks+=1
    # Lemma 2.12
    for i in range(n):
        for j in range(n):
            assert pi[j]*HT[i][j]==Z[j][j]-Z[i][j]; identity_checks+=1
    # Corollaries 2.13 and 2.14
    trace=sum(Z[j][j] for j in range(n))
    vals=[]
    for i in range(n):
        val=sum(pi[j]*HT[i][j] for j in range(n))
        assert val==trace; identity_checks+=1
        vals.append(val)
    assert all(v==vals[0] for v in vals); identity_checks+=n
    # Lemma 2.15
    for i in range(n):
        xs=[killed_data(P,{i},s,False)[0] for s in range(n)]
        for j in range(n):
            lhs=sum(pi[s]*xs[s][j] for s in range(n))
            rhs=pi[j]*Z[i][i]/pi[i]-Z[i][j]
            assert lhs==rhs; identity_checks+=1

print("exact Fraction arithmetic only")
print(f"chains={len(chains)}")
print(f"boundary_invertibility_cases={boundary_cases}")
print(f"standard_hit_occupation_cases={standard_cases}")
print(f"strict_hit_occupation_cases={strict_cases}")
print(f"matching_denominator_expansions={matching_den_cases}")
print(f"matching_numerator_expansions={matching_num_cases}")
print(f"frozen_source_identity_checks={identity_checks}")
print("PASS")
