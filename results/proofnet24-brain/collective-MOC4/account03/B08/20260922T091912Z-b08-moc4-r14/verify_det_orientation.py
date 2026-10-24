#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(x) for x in zip(*A)]
def inv(A):
    n=len(A); M=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]); M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[x/q for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                q=M[i][c]; M[i]=[M[i][j]-q*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]
def det(A):
    n=len(A); ans=F(0)
    for p in permutations(range(n)):
        invs=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        q=F(1)
        for i in range(n): q*=A[i][p[i]]
        ans += -q if invs%2 else q
    return ans
S=[[F(x) for x in r] for r in [[0,1,2,3],[-1,0,4,5],[-2,-4,0,6],[-3,-5,-6,0]]]
t=F(1,10**10); I=[[F(i==j) for j in range(4)] for i in range(4)]
Q=mm([[I[i][j]-t*S[i][j] for j in range(4)] for i in range(4)],
     inv([[I[i][j]+t*S[i][j] for j in range(4)] for i in range(4)]))
p=(3,2,1,0)
P=[[F(j==p[i]) for j in range(4)] for i in range(4)]
U=mm(Q,P)
assert mm(U,mt(U))==I
assert det(Q)==1
assert det(P)==1
assert det(U)==1
print('orientation verification PASS: det(Q)=det(P)=det(U)=1 exactly')
