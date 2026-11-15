"""Audit intermediate comb estimates, nonreversible lemma, and source data."""
import json
import random
from fractions import Fraction as F
from collections import deque
from referee_core import exact_chain,comb,lump,exact_hit,display

rng=random.Random(424211)
out={'seed':424211,'comb_cases':0,'median_estimates':0,
     'per_level_estimates':0,'bridge_identities':0,'cited_data_rows_compared':0}

def path(adj,a,b):
    q=deque([a]); parent={a:None}
    while q:
        x=q.popleft()
        if x==b:
            ans=[]
            while x is not None:
                ans.append(x);x=parent[x]
            return ans[::-1]
        for y in adj[x]:
            if y not in parent:
                parent[y]=x;q.append(y)

for _ in range(60):
    n=rng.randint(1,5)
    h=F(rng.randint(2,40),2)
    alpha=F(rng.randint(1,50),rng.randint(1,5))
    r=F(rng.randint(4,30),2)
    ell=F(rng.randint(0,100000))
    w,lab=comb(n,h,alpha,r,ell=ell)
    a=exact_chain(w);b=exact_chain(lump(w,lab))
    H=a['H']; pi=a['pi']; c=2*n+1; tot=sum(map(sum,w))
    delta=(2+alpha+alpha*h)/(r-1)
    M=h+(n+1)*(1+delta); B=M+1+delta; rho=sum(w[c])/r**n
    adj=[[j for j in range(len(w)) if j!=i and w[i][j]] for i in range(len(w))]
    level=list(range(n+1))+list(range(1,n+1))+[n+1]
    paths={(i,j):set(path(adj,i,j)) for i in range(len(w)) for j in range(len(w))}
    assert max(row[c] for row in H)<=M
    assert a['tmix']<=max(B,M+B-rho)
    assert b['H'][0][-1]>=n*h*alpha/(1+alpha)
    assert b['tmix']>=pi[c]*n*h*alpha/(1+alpha)
    for k in range(n+1):
        S=sum(sum(w[z]) for z in range(k+1))+sum(sum(w[n+1+y]) for y in range(k))
        nxt=k+1 if k<n else c
        assert S==1+(1+delta)*(r**k-1) <= (1+delta)*r**k
        assert H[k][nxt]==S/r**k <= 1+delta
        assert H[nxt][k]==(tot-S)/r**k
        out['bridge_identities']+=2
        if k<n:
            tooth=n+1+k
            assert H[tooth][k+1]==h
            assert H[k+1][tooth]==(tot-sum(w[tooth]))/(alpha*r**k)
            out['bridge_identities']+=2
    for j in range(c):
        q=level[j]
        assert a['D'][c][j] <= h+(n-q+2)*(1+delta) <= B
        for p in range(q+1,n+1):
            weight=sum(sum(w[k]) for k in range(c) if level[k]==p)
            assert weight*H[c][p]/tot <= 1+delta
            out['per_level_estimates']+=1
        for x in range(c):
            med=next(iter(paths[x,c]&paths[c,j]&paths[x,j]))
            assert med!=c
            assert H[x][j]-H[c][j] == H[x][med]-H[c][med]
            assert H[x][j]-H[c][j] <= H[x][c]-H[c][n] <= M-rho
            out['median_estimates']+=1
    out['comb_cases']+=1

# A nonreversible, diagonalizable rational example with negative eigenvalues.
# Doubly stochastic P = Pi + lambda*g*g^T/||g||^2 + a nilpotent term
# would complicate exact eigenvectors; instead use a circulant 4-state chain
# with clockwise probability 3/4 and anticlockwise probability 1/4.
# Eigenvalues are 1,-1,+i/2,-i/2. The real eigenfunction alternates signs.
p=[[F(0)]*4 for _ in range(4)]
for i in range(4):
    p[i][(i+1)%4]=F(3,4);p[i][(i-1)%4]=F(1,4)
# Solve the occupation LP by a rational linear system with each potential
# halting state in turn; nonsymmetric hitting calculations avoid reversibility.
from referee_core import inverse
hh=[[F(0)]*4 for _ in range(4)]
for j in range(4):
    oth=[i for i in range(4) if i!=j]
    ki=inverse([[F(i==k)-p[i][k] for k in oth] for i in oth])
    for row,i in zip(ki,oth):hh[i][j]=sum(row)
ts=[max(hh[i][j]-sum(hh[k][j] for k in range(4))/4 for j in range(4)) for i in range(4)]
assert min(ts)>=F(1,2)
out['nonreversible_real_negative_eigenvalue_case']={'lambda':-1,'optimal_times':list(map(str,ts))}

# Compare existing author output to independent exact results without running
# the author's code or using it in the independent implementations.
with open('data/lumping_checks.json') as f:published=json.load(f)
for row in published['comb']:
    n,t,heavy=row['N'],row['t'],row['heavy_end']
    w,labels=comb(n,t,t,1+t**3,heavy=heavy,ell=None if heavy else 1)
    a,b=exact_chain(w),exact_chain(lump(w,labels))
    assert abs(float(a['tmix'])-row['tau12_original'])<1e-8
    assert abs(float(b['tmix'])-row['tau12_induced'])<1e-8
    out['cited_data_rows_compared']+=1
out['all_passed']=True
with open('referee_details.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
