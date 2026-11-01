from fractions import Fraction as F
from itertools import combinations

n=7
edges=list(combinations(range(4),2))+[(0,4),(0,5),(0,6)]
adj={i:[] for i in range(n)}
for u,v in edges:
    adj[u].append(v); adj[v].append(u)

def solve(A,b):
    m=len(b)
    M=[list(A[i])+[b[i]] for i in range(m)]
    for c in range(m):
        p=next(r for r in range(c,m) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(m):
            if r!=c and M[r][c]:
                q=M[r][c]
                M[r]=[M[r][j]-q*M[c][j] for j in range(m+1)]
    return [M[i][-1] for i in range(m)]

def hit(target):
    S=[v for v in range(n) if v!=target]; ix={v:i for i,v in enumerate(S)}
    A=[[F(i==j) for j in range(len(S))] for i in range(len(S))]
    b=[F(1) for _ in S]
    for v in S:
        for w in adj[v]:
            if w!=target: A[ix[v]][ix[w]]-=F(1,len(adj[v]))
    x=solve(A,b); return {target:F(0),**{v:x[ix[v]] for v in S}}

H={(s,t):hit(t)[s] for t in range(n) for s in range(n)}
thit=max(H.values())
ALL=(1<<n)-1
E={(ALL,v):F(0) for v in range(n)}
E2={(ALL,v):F(0) for v in range(n)}
for k in range(n-1,0,-1):
    for mask in range(1<<n):
        if mask.bit_count()!=k: continue
        S=[v for v in range(n) if mask>>v&1]; ix={v:i for i,v in enumerate(S)}
        A=[[F(i==j) for j in range(len(S))] for i in range(len(S))]
        b=[F(1) for _ in S]
        for v in S:
            d=len(adj[v])
            for w in adj[v]:
                if mask>>w&1: A[ix[v]][ix[w]]-=F(1,d)
                else: b[ix[v]]+=F(1,d)*E[(mask|1<<w,w)]
        x=solve(A,b)
        for v in S: E[(mask,v)]=x[ix[v]]
        A=[[F(i==j) for j in range(len(S))] for i in range(len(S))]
        b=[F(1) for _ in S]
        for v in S:
            d=len(adj[v])
            for w in adj[v]:
                nm=mask|1<<w
                b[ix[v]]+=F(2,d)*E[(nm,w)]
                if mask>>w&1: A[ix[v]][ix[w]]-=F(1,d)
                else: b[ix[v]]+=F(1,d)*E2[(nm,w)]
        x=solve(A,b)
        for v in S: E2[(mask,v)]=x[ix[v]]

s=1
mu=E[(1<<s,s)]
var=E2[(1<<s,s)]-mu*mu
means=[E[(1<<v,v)] for v in range(n)]
print("C0117_EXACT_WORST_START_PASS")
print("edges=",edges)
print("start=",s)
print("t_hit=",thit)
print("E_tau=",mu)
print("Var_tau=",var)
print("Var_minus_t_hit_sq=",var-thit*thit)
print("start_means=",means)
print("t_cov=",max(means))
assert thit==20
assert var>thit*thit
assert max(means)==mu
