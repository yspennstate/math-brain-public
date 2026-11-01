from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict

# exact determinant over Fractions
def det(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0:return F(1)
    out=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None:return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; out=-out
        piv=A[c][c]; out*=piv
        for j in range(c,n):A[c][j]/=piv
        for r in range(c+1,n):
            t=A[r][c]
            if t:
                for j in range(c,n):A[r][j]-=t*A[c][j]
    return out

def principal_det(K,S):
    S=sorted(S)
    return det([[K[i][j] for j in S] for i in S])

def dpp_masses(K):
    n=len(K); rho={}
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        rho[mask]=principal_det(K,S)
    p={}
    for mask in range((1<<n)-1,-1,-1):
        s=F(0)
        rest=((1<<n)-1)^mask
        sub=rest
        while sub:
            s+=p[mask|sub]
            sub=(sub-1)&rest
        p[mask]=rho[mask]-s
    assert all(v>=0 for v in p.values())
    assert sum(p.values())==1
    return p

# quotient positive contraction, deliberately not a projection
Q0=[
 [F(1,2),F(1,6),F(0)],
 [F(1,6),F(1,2),F(1,6)],
 [F(0),F(1,6),F(1,2)],
]
I3=[[F(int(i==j)) for j in range(3)] for i in range(3)]
Q1=[[I3[i][j]-Q0[i][j] for j in range(3)] for i in range(3)]

def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
assert matmul(Q0,Q0)!=Q0
for Q in [Q0,Q1]:
 for mask in range(1,1<<3):
  S=[i for i in range(3) if mask>>i&1]
  assert principal_det(Q,S)>=0

# physical blocks and rational unit weights
blocks=[[0,1],[2,3,4],[5,6]]
weights=[[F(3,5),F(4,5)],[F(1,3),F(2,3),F(2,3)],[F(5,13),F(12,13)]]
for w in weights: assert sum(x*x for x in w)==1
E=7
owners=[0,1,0] # S0={0,2}, S1={1}

J=[[F(0) for b in range(3)] for x in range(E)]
for b,B in enumerate(blocks):
 for loc,x in enumerate(B):J[x][b]=weights[b][loc]

def transpose(A):return list(map(list,zip(*A)))
def add(A,B):return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def inflate(Q,color):
 Sdiag=[[F(int(i==j and owners[i]==color)) for j in range(3)] for i in range(3)]
 D=[[F(0) for y in range(E)] for x in range(E)]
 for b,B in enumerate(blocks):
  if owners[b]==color:
   for x in B:D[x][x]=1
 return add(D,matmul(matmul(J,sub(Q,Sdiag)),transpose(J)))

K0=inflate(Q0,0); K1=inflate(Q1,1)
I7=[[F(int(i==j)) for j in range(E)] for i in range(E)]
assert add(K0,K1)==I7
assert matmul(K0,K0)!=K0 and matmul(K1,K1)!=K1

# exact quotient complement coupling
py0=dpp_masses(Q0); py1=dpp_masses(Q1)
for m,p in py0.items():
 comp=((1<<3)-1)^m
 assert py1[comp]==p

# enumerate shared Z choices and lift
joint=defaultdict(F)
for ymass,p in py0.items():
 y0={b for b in range(3) if ymass>>b&1}
 zchoices=[[(x,weights[b][loc]**2) for loc,x in enumerate(B)] for b,B in enumerate(blocks)]
 for z0,p0 in zchoices[0]:
  for z1,p1 in zchoices[1]:
   for z2,p2 in zchoices[2]:
    zs=[z0,z1,z2]; mass=p*p0*p1*p2
    X=[set(),set()]
    for b,B in enumerate(blocks):
     o=owners[b]; q=0 if b in y0 else 1; z=zs[b]
     if o==q:X[o].update(B)
     else:
      X[o].update(set(B)-{z}); X[q].add(z)
    assert X[0].isdisjoint(X[1]) and X[0]|X[1]==set(range(E))
    masks=[sum(1<<x for x in X[c]) for c in [0,1]]
    joint[tuple(masks)]+=mass
assert sum(joint.values())==1

# exact physical DPP marginals
pk=[dpp_masses(K0),dpp_masses(K1)]
for c in [0,1]:
 got=defaultdict(F)
 for ms,p in joint.items():got[ms[c]]+=p
 assert dict(got)=={m:p for m,p in pk[c].items() if p}

# independent exact generating-determinant checks
f=[F(1,7),F(-1,5),F(2,9),F(1,4),F(-1,6),F(3,10),F(-2,11)]
for c,K in enumerate([K0,K1]):
 lhs=F(0)
 for m,p in pk[c].items():
  prod=F(1)
  for x in range(E):
   if m>>x&1:prod*=1+f[x]
  lhs+=p*prod
 KF=[[K[i][j]*f[j] for j in range(E)] for i in range(E)]
 M=[[F(int(i==j))+KF[i][j] for j in range(E)] for i in range(E)]
 assert lhs==det(M)

print('quotient_nonprojection',matmul(Q0,Q0)!=Q0)
print('physical_nonprojection',matmul(K0,K0)!=K0 and matmul(K1,K1)!=K1)
print('joint_atoms',len(joint))
print('physical_support_sizes',[sum(1 for v in pk[c].values() if v) for c in [0,1]])
print('exact_generating_checks',2)
print('ALL EXACT CHECKS PASSED')
