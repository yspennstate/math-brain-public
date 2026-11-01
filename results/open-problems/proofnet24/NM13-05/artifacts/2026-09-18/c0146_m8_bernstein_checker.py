#!/usr/bin/env python3
from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque
from fractions import Fraction
from math import comb, gcd

N_BERN = 7

REPS = {
    3: [
        (3, [(0,1),(0,2),(1,2)]),
    ],
    4: [
        (4, [(0,1),(0,3),(1,2),(2,3)]),
    ],
    5: [
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3)]),
        (5, [(0,1),(0,4),(1,2),(2,3),(3,4)]),
    ],
    6: [
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
        (5, [(0,1),(0,2),(0,3),(1,2),(1,4),(3,4)]),
        (5, [(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)]),
        (6, [(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]),
    ],
    7: [
        (5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]),
        (5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,4)]),
        (5, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,4)]),
        (6, [(0,1),(0,2),(0,3),(1,2),(1,4),(3,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(3,5)]),
        (6, [(0,1),(0,2),(0,3),(1,4),(2,4),(3,5),(4,5)]),
        (7, [(0,1),(0,2),(1,3),(2,4),(3,5),(4,6),(5,6)]),
    ],
    8: [
        (5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3)]),
        (5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,4),(3,4)]),
        (6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(3,4),(3,5)]),
        (6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(3,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(0,4),(1,5),(2,5),(3,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,5)]),
        (6, [(0,1),(0,2),(0,3),(1,2),(1,4),(3,4),(3,5),(4,5)]),
        (6, [(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,5),(3,4)]),
        (7, [(0,1),(0,2),(0,3),(1,2),(1,4),(3,5),(4,6),(5,6)]),
        (7, [(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(3,6),(5,6)]),
        (7, [(0,1),(0,2),(0,3),(1,4),(2,4),(3,5),(4,6),(5,6)]),
        (7, [(0,1),(0,2),(0,3),(1,4),(2,5),(3,6),(4,5),(4,6)]),
        (8, [(0,1),(0,2),(1,3),(2,4),(3,5),(4,6),(5,7),(6,7)]),
    ],
}

def norm_edges(edges):
    return tuple(sorted((min(u,v), max(u,v)) for u,v in edges))

def connected(n, edges, skip=None):
    verts=[v for v in range(n) if v != skip]
    if len(verts) <= 1:
        return True
    adj=[[] for _ in range(n)]
    for u,v in edges:
        if u==skip or v==skip:
            continue
        adj[u].append(v); adj[v].append(u)
    seen={verts[0]}; dq=[verts[0]]
    while dq:
        u=dq.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); dq.append(v)
    return len(seen)==len(verts)

def biconnected(n, edges):
    if n < 3 or len(edges) < n:
        return False
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1; deg[v]+=1
    if min(deg) < 2 or not connected(n,edges):
        return False
    return all(connected(n,edges,skip=z) for z in range(n))

def edge_bit_order(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def canonical_code(n, edges):
    edges=set(norm_edges(edges))
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1; deg[v]+=1
    groups=[]
    for d in sorted(set(deg)):
        groups.append([v for v in range(n) if deg[v]==d])
    all_e=edge_bit_order(n)
    idx={e:i for i,e in enumerate(all_e)}
    best=None
    perm_lists=[list(permutations(g)) for g in groups]
    for blocks in product(*perm_lists):
        order=[]
        for b in blocks:
            order.extend(b)
        rel={old:new for new,old in enumerate(order)}
        code=0
        for u,v in edges:
            a,b=sorted((rel[u],rel[v]))
            code |= 1<<idx[(a,b)]
        if best is None or code<best:
            best=code
    return (tuple(sorted(deg)), best)

def component_count(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a!=b:
                p[b]=a
    return len({find(i) for i in range(n)})

def lcm(a,b):
    if a==0 or b==0: return 0
    return a//gcd(a,b)*b

def bernstein_coeff(poly, N, j):
    # poly is dict power -> integer coefficient, degree <= N.
    # q^k = sum_{j=k}^N C(j,k)/C(N,k) B_{j,N}(q).
    ans=Fraction(0)
    for k,a in poly.items():
        if a and k<=j:
            ans += Fraction(a*comb(j,k), comb(N,k))
    return ans

class Dinic:
    def __init__(self,n):
        self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None]; b=[u,0,a]; a[2]=b
        self.g[u].append(a); self.g[v].append(b)
    def maxflow(self,s,t):
        flow=0
        INF=10**100
        while True:
            level=[-1]*len(self.g); level[s]=0; dq=deque([s])
            while dq:
                u=dq.popleft()
                for e in self.g[u]:
                    if e[1]>0 and level[e[0]]<0:
                        level[e[0]]=level[u]+1; dq.append(e[0])
            if level[t]<0: break
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1]>0 and level[e[0]]==level[u]+1:
                        z=dfs(e[0], min(f,e[1]))
                        if z:
                            e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,INF)
                if not z: break
                flow+=z
        return flow

def flow_feasible(src_masks, dst_masks, rows, cols):
    # rows/cols Fractions, same total. Scale to integer exactly, solve the
    # inclusion max-flow, then independently re-sum the realized edge flow.
    den=1
    for x in list(rows.values())+list(cols.values()):
        den=lcm(den,x.denominator)
    ri={a:int(rows[a]*den) for a in src_masks}
    ci={b:int(cols[b]*den) for b in dst_masks}
    total=sum(ri.values())
    assert total==sum(ci.values())
    if total==0:
        return True
    ns=len(src_masks); nd=len(dst_masks)
    S=0; so=1; do=so+ns; T=do+nd
    D=Dinic(T+1)
    sidx={a:i for i,a in enumerate(src_masks)}
    didx={b:i for i,b in enumerate(dst_masks)}
    for a in src_masks: D.add(S,so+sidx[a],ri[a])
    for b in dst_masks: D.add(do+didx[b],T,ci[b])
    arc={}
    for a in src_masks:
        for b in dst_masks:
            if (a & b)==a:
                u=so+sidx[a]; v=do+didx[b]
                D.add(u,v,total)
                arc[(a,b)]=D.g[u][-1]
    if D.maxflow(S,T)!=total:
        return False
    out=defaultdict(int); inc=defaultdict(int)
    for (a,b),e in arc.items():
        used=total-e[1]
        assert used>=0
        if used:
            out[a]+=used; inc[b]+=used
    assert all(out[a]==ri[a] for a in src_masks)
    assert all(inc[b]==ci[b] for b in dst_masks)
    return True

def shifted(poly, shift):
    return {k+shift:v for k,v in poly.items() if v}

def automorphism_count(n, edges):
    E=set(norm_edges(edges))
    ans=0
    for p in permutations(range(n)):
        image={tuple(sorted((p[u],p[v]))) for u,v in E}
        if image==E:
            ans+=1
    return ans

# Method-14 symmetry diagnostic for the four six-edge blocks.
aut_m6=[automorphism_count(n,es) for n,es in REPS[6]]
assert aut_m6==[24,2,12,12]

# 1. Verify hard-coded representatives and exact completeness through 8 edges.
rep_codes={}
for m,reps in REPS.items():
    rep_codes[m]={}
    for n,es in reps:
        es=norm_edges(es)
        assert len(es)==m and len(set(es))==m
        assert all(0<=u<v<n for u,v in es)
        assert biconnected(n,es)
        code=canonical_code(n,es)
        assert code not in rep_codes[m].setdefault(n,set())
        rep_codes[m][n].add(code)

labeled_biconnected_counts={}
unlabeled_counts={}
for m in range(3,9):
    seen=set()
    labeled=0
    for n in range(3,m+1):
        if comb(n,2)<m: continue
        if n==m:
            # 2-connected + m edges on m vertices implies min degree>=2 and
            # degree sum=2m=2n, hence every degree is 2; connected => C_m.
            cyc=[x for x in REPS[m] if x[0]==n]
            assert len(cyc)==1
            seen.add((n,canonical_code(n,cyc[0][1])))
            continue
        allE=edge_bit_order(n)
        for es in combinations(allE,m):
            deg=[0]*n
            for u,v in es:
                deg[u]+=1; deg[v]+=1
            if min(deg)<2:
                continue
            if biconnected(n,es):
                labeled += 1
                code=canonical_code(n,es)
                assert code in rep_codes[m].get(n,set()), (m,n,es,code)
                seen.add((n,code))
    expected={(n,c) for n,d in rep_codes[m].items() for c in d}
    assert seen==expected, (m,len(seen),len(expected),expected-seen,seen-expected)
    labeled_biconnected_counts[m]=labeled
    unlabeled_counts[m]=len(seen)

assert [unlabeled_counts[m] for m in range(3,9)] == [1,1,2,4,7,16]

# 2. Exact coefficientwise Bernstein transport for every adjacent layer.
flow_instances=0
transport_pairs=0
for m in range(3,9):
    for n,es0 in REPS[m]:
        es=list(norm_edges(es0))
        layers={r:[a for a in range(1<<m) if a.bit_count()==r] for r in range(m+1)}
        nullity={}
        W={}
        for r in range(m+1):
            cc=Counter()
            for a in layers[r]:
                k=component_count(n,es,a)
                c=r-n+k
                assert c>=0
                nullity[a]=c
                cc[c]+=1
            W[r]=dict(cc)
        for r in range(m):
            transport_pairs += 1
            src=layers[r]; dst=layers[r+1]
            row_poly={a:shifted(W[r+1],nullity[a]) for a in src}
            col_poly={b:shifted(W[r],nullity[b]) for b in dst}
            maxdeg=max([0]+[max(p) for p in list(row_poly.values())+list(col_poly.values()) if p])
            assert maxdeg<=N_BERN, (m,n,r,maxdeg)
            for j in range(N_BERN+1):
                rows={a:bernstein_coeff(row_poly[a],N_BERN,j) for a in src}
                cols={b:bernstein_coeff(col_poly[b],N_BERN,j) for b in dst}
                assert all(x>=0 for x in rows.values())
                assert all(x>=0 for x in cols.values())
                assert sum(rows.values())==sum(cols.values())
                assert flow_feasible(src,dst,rows,cols), (m,n,r,j)
                flow_instances += 1

print('m6_automorphism_group_orders', aut_m6)
print('unlabeled_2connected_type_counts_m3_to_m8', [unlabeled_counts[m] for m in range(3,9)])
print('labeled_2connected_enumerated_n_lt_m', [labeled_biconnected_counts[m] for m in range(3,9)])
print('representatives_total', sum(unlabeled_counts.values()))
print('adjacent_layer_transport_pairs', transport_pairs)
print('bernstein_degree', N_BERN)
print('bernstein_coefficient_flow_instances', flow_instances)
print('ALL_EXACT_CHECKS_PASS')
