#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque
from fractions import Fraction
from math import comb, gcd

M=9
N_BERN=9

def norm_edges(es):
    return tuple(sorted((min(u,v),max(u,v)) for u,v in es))

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def connected(n, es, skip=None):
    vs=[v for v in range(n) if v!=skip]
    if len(vs)<=1: return True
    adj=[[] for _ in range(n)]
    for u,v in es:
        if u==skip or v==skip: continue
        adj[u].append(v); adj[v].append(u)
    seen={vs[0]}; stack=[vs[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==len(vs)

def biconnected(n, es):
    if n<3 or len(es)<n: return False
    deg=[0]*n
    for u,v in es:
        deg[u]+=1; deg[v]+=1
    return min(deg)>=2 and connected(n,es) and all(connected(n,es,z) for z in range(n))

def canonical_code(n, es):
    E=set(norm_edges(es))
    deg=[0]*n
    for u,v in E:
        deg[u]+=1; deg[v]+=1
    groups=[[v for v in range(n) if deg[v]==d] for d in sorted(set(deg))]
    idx={e:i for i,e in enumerate(all_edges(n))}
    best=None
    for blocks in product(*(list(permutations(g)) for g in groups)):
        order=[v for block in blocks for v in block]
        rel={old:new for new,old in enumerate(order)}
        code=0
        for u,v in E:
            a,b=sorted((rel[u],rel[v]))
            code |= 1<<idx[(a,b)]
        best=code if best is None or code<best else best
    return (tuple(sorted(deg)),best)

def component_count(n, es, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(u,v) in enumerate(es):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a!=b: p[b]=a
    return len({find(i) for i in range(n)})

def lcm(a,b):
    return a//gcd(a,b)*b if a and b else 0

def bern_coeff(poly,N,j):
    return sum((Fraction(a*comb(j,k),comb(N,k)) for k,a in poly.items() if a and k<=j),Fraction(0))

class Dinic:
    def __init__(self,n): self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None]; b=[u,0,a]; a[2]=b
        self.g[u].append(a); self.g[v].append(b)
    def maxflow(self,s,t):
        ans=0; INF=10**100
        while True:
            lev=[-1]*len(self.g); lev[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for e in self.g[u]:
                    if e[1]>0 and lev[e[0]]<0:
                        lev[e[0]]=lev[u]+1; q.append(e[0])
            if lev[t]<0: return ans
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1]>0 and lev[e[0]]==lev[u]+1:
                        z=dfs(e[0],min(f,e[1]))
                        if z:
                            e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,INF)
                if not z: break
                ans+=z

def flow_ok(src,dst,rows,cols):
    den=1
    for x in list(rows.values())+list(cols.values()): den=lcm(den,x.denominator)
    ri={a:int(rows[a]*den) for a in src}; ci={b:int(cols[b]*den) for b in dst}
    total=sum(ri.values()); assert total==sum(ci.values())
    if total==0: return True
    ns=len(src); nd=len(dst); S=0; so=1; do=so+ns; T=do+nd
    D=Dinic(T+1); si={a:i for i,a in enumerate(src)}; di={b:i for i,b in enumerate(dst)}
    for a in src: D.add(S,so+si[a],ri[a])
    for b in dst: D.add(do+di[b],T,ci[b])
    arcs={}
    for a in src:
        for b in dst:
            if (a&b)==a:
                u=so+si[a]; v=do+di[b]; D.add(u,v,total); arcs[(a,b)]=D.g[u][-1]
    if D.maxflow(S,T)!=total: return False
    out=defaultdict(int); inc=defaultdict(int)
    for (a,b),e in arcs.items():
        used=total-e[1]
        if used: out[a]+=used; inc[b]+=used
    assert all(out[a]==ri[a] for a in src)
    assert all(inc[b]==ci[b] for b in dst)
    return True

# Exact exhaustive isomorphism census for n<=7.
reps=[]
labeled={}
unlabeled={}
for n in (5,6,7):
    seen={}
    count=0
    for es in combinations(all_edges(n),M):
        deg=[0]*n
        for u,v in es: deg[u]+=1; deg[v]+=1
        if min(deg)<2 or not biconnected(n,es): continue
        count+=1
        code=canonical_code(n,es)
        if code not in seen: seen[code]=norm_edges(es)
    labeled[n]=count; unlabeled[n]=len(seen)
    reps.extend((n,es) for es in seen.values())
assert [labeled[n] for n in (5,6,7)]==[10,3535,46830]
assert [unlabeled[n] for n in (5,6,7)]==[1,14,20]

# For n=8,m=9, 2-connectivity forces the degree surplus 2 to be two
# degree-3 vertices; suppressing degree-2 vertices gives a theta graph.
# The sorted path lengths sum to 9, and simplicity permits at most one 1.
parts=[]
for a in range(1,10):
    for b in range(a,10):
        c=9-a-b
        if c>=b and sum(x==1 for x in (a,b,c))<=1: parts.append((a,b,c))
assert parts==[(1,2,6),(1,3,5),(1,4,4),(2,2,5),(2,3,4),(3,3,3)]

def theta(lengths):
    es=[]; nxt=2
    for L in lengths:
        if L==1:
            es.append((0,1)); continue
        prev=0
        for _ in range(L-1):
            v=nxt; nxt+=1; es.append((prev,v)); prev=v
        es.append((prev,1))
    assert nxt==8
    return norm_edges(es)

theta_reps=[theta(p) for p in parts]
theta_codes={canonical_code(8,es) for es in theta_reps}
assert len(theta_codes)==6 and all(biconnected(8,es) for es in theta_reps)
reps.extend((8,es) for es in theta_reps)

# For n=9,m=9, min degree 2 and average degree 2 force the unique cycle.
c9=norm_edges([(i,i+1) for i in range(8)]+[(0,8)])
assert biconnected(9,c9)
reps.append((9,c9))
assert len(reps)==42

# Exact Bernstein coefficient transports for every adjacent fixed-size layer.
pairs=0; instances=0
for n,es in reps:
    layers={r:[x for x in range(1<<M) if x.bit_count()==r] for r in range(M+1)}
    nullity={}; W={}
    for r in range(M+1):
        cc=Counter()
        for x in layers[r]:
            c=r-n+component_count(n,es,x)
            assert c>=0; nullity[x]=c; cc[c]+=1
        W[r]=dict(cc)
    for r in range(M):
        pairs+=1; src=layers[r]; dst=layers[r+1]
        rows_poly={a:{k+nullity[a]:v for k,v in W[r+1].items()} for a in src}
        cols_poly={b:{k+nullity[b]:v for k,v in W[r].items()} for b in dst}
        assert max(max(p) for p in list(rows_poly.values())+list(cols_poly.values()))<=N_BERN
        for j in range(N_BERN+1):
            rows={a:bern_coeff(rows_poly[a],N_BERN,j) for a in src}
            cols={b:bern_coeff(cols_poly[b],N_BERN,j) for b in dst}
            assert min(rows.values())>=0 and min(cols.values())>=0
            assert sum(rows.values())==sum(cols.values())
            assert flow_ok(src,dst,rows,cols),(n,r,j)
            instances+=1
assert pairs==378 and instances==3780

print("labeled_biconnected_n5_n6_n7", [labeled[n] for n in (5,6,7)])
print("unlabeled_counts_by_n", {5:1,6:14,7:20,8:6,9:1})
print("theta_path_partitions_n8", parts)
print("m9_representatives_total",len(reps))
print("adjacent_layer_transport_pairs",pairs)
print("bernstein_degree",N_BERN)
print("coefficient_flow_instances",instances)
print("ALL_EXACT_CHECKS_PASS")
