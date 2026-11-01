import itertools, json, hashlib, collections

ADJ={
0:[1,8,9,15,16,17,20],1:[2,5,7,9,10,15,18],2:[3,6,9,10,11,12,15],3:[0,4,6,9,11,12,13],
4:[2,5,11,12,13,14,21],5:[2,3,6,9,11,13,14],6:[0,1,7,10,11,12,13],7:[2,3,4,10,11,12,14],
8:[3,5,6,7,9,13,14],9:[4,6,7,10,14,19,20],10:[0,3,4,5,11,15,18],11:[0,12,13,16,17,18,19],
12:[1,5,8,13,14,18,20],13:[1,9,10,14,17,20,21],14:[1,3,6,11,17,19,20],15:[3,6,7,8,11,12,16],
16:[6,7,8,9,12,18,20],17:[6,8,10,12,19,20,21],18:[0,4,6,8,9,19,20],19:[0,1,4,6,7,20,21],
20:[1,3,6,7,10,11,21],21:[0,1,2,5,6,10,11]}
V=set(ADJ)
E={(u,v) for u,vs in ADJ.items() for v in vs}
H=[0,1,2,3]; B=[4,5,6,7]; A=[8,9,10,11,12]; R=list(range(13,22)); Rp=[5]+list(range(13,21))
Bstar=[4,21,6,7]

def cyc_edges(c):
    return {(c[i],c[(i+1)%len(c)]) for i in range(len(c))}

def is_acyclic(nodes):
    nodes=set(nodes); state={v:0 for v in nodes}
    def dfs(u):
        state[u]=1
        for v in ADJ[u]:
            if v not in nodes: continue
            if state[v]==1: return False
            if state[v]==0 and not dfs(v): return False
        state[u]=2; return True
    return all(state[u] or dfs(u) for u in list(nodes))

def reachable_after_remove(src,rem):
    if src in rem:return set()
    seen={src}; q=collections.deque([src])
    while q:
        u=q.popleft()
        for v in ADJ[u]:
            if v in rem or v in seen: continue
            seen.add(v);q.append(v)
    return seen

def strong_after_remove(rem):
    left=V-set(rem)
    return all(reachable_after_remove(s,set(rem))>=left for s in left)

def shortest_bypass(pred,succ,Rset):
    allowed=set(Rset)|{pred,succ}; q=collections.deque([(pred,0)]); seen={pred}
    while q:
        u,d=q.popleft()
        for v in ADJ[u]:
            if v not in allowed: continue
            if v==succ:return d+1
            if v not in seen:
                seen.add(v);q.append((v,d+1))
    return None

def fwd_interval(n,p,q):
    out=[];x=(p+1)%n
    while True:
        out.append(x)
        if x==q:return out
        x=(x+1)%n

def allcross(n,p1,F1,p2,F2):
    return set(F1)<=set(fwd_interval(n,p1,p2)) or set(F2)<=set(fwd_interval(n,p2,p1))

def bridge_or_slack(n,p1,F1,p2,F2):
    m1,m2=len(F1),len(F2)
    I12=fwd_interval(n,p1,p2); I21=fwd_interval(n,p2,p1)
    d12,d21=len(I12),len(I21)
    if not allcross(n,p1,F1,p2,F2): return True
    return (p2 in F1) or (d12>=m1+1) or (p1 in F2) or (d21>=m2+1)

# Full-certificate checks.
assert V==set(range(22))
assert all(len(ADJ[u])==7 and u not in ADJ[u] for u in V)
assert all(not ((v,u) in E) for (u,v) in E)
for C in (H,B,A,Bstar): assert cyc_edges(C)<=E
for C in (H,B,A):
    ce=cyc_edges(C)
    assert all((u,v) in ce or (u,v) not in E for u in C for v in C if u!=v)
assert is_acyclic(R) and is_acyclic(Rp)
# 3-vertex-strong (indeed survives every deletion of <=2 vertices).
assert strong_after_remove(())
for k in (1,2):
    for rem in itertools.combinations(sorted(V),k): assert strong_after_remove(rem)
# Every arc is dominated by a common predecessor.
assert all(any(q not in (u,v) and (q,u) in E and (q,v) in E for q in V) for u,v in E)
# G1 sink / unique return port and fan.
assert not any((21,r) in E for r in R if r!=21)
assert (4,21) in E and all((b,21) not in E for b in [5,6,7])
assert all((u,21) not in E for u in H+A)
assert set(ADJ[21])=={0,1,2,5,6,10,11}
# G1-S residual degree-two set after deleting H U A.
res=V-set(H)-set(A)
W={u for u in res if sum(v in res for v in ADJ[u])==2}
assert W=={6,7,21}
# Same-heavy witnesses on A: distinct inports, common 3-fan, no port bridge.
F6=set(ADJ[6])&set(A);F7=set(ADJ[7])&set(A)
assert (8,6) in E and (9,7) in E and F6==F7=={10,11,12}
assert 9 not in F6 and 8 not in F7
# On A=(8,9,10,11,12), corridor is carried by z7 from p7=9 to p6=8: distance4=3+1.
assert allcross(5,0,{2,3,4},1,{2,3,4})
assert len(fwd_interval(5,1,0))==4
# No short/equality TCEX bypass; both shortest lengths are 4 while m=3.
b6=shortest_bypass(21,7,Rp); b7=shortest_bypass(6,4,Rp)
assert b6==4 and b7==4
# Explicit strict smaller 3-pack, proving this is not globally minimum and not a BT4 counterexample.
pack=[[2,3,4],[1,5,6],[0,9,10]]
assert all(cyc_edges(c)<=E for c in pack)
assert len(set().union(*map(set,pack)))==sum(map(len,pack))
assert sum(map(len,pack))==9 < len(H)+len(B)+len(A)

# Exhaustive symbolic check of the universal bridge-or-slack lemma for n<=10 and m in {3,4,5}.
checked=0
for n in range(4,11):
    verts=range(n)
    for p1,p2 in itertools.permutations(verts,2):
        for m1 in range(3,min(5,n-1)+1):
            for F1 in map(set,itertools.combinations([v for v in verts if v!=p1],m1)):
                for m2 in range(3,min(5,n-1)+1):
                    for F2 in map(set,itertools.combinations([v for v in verts if v!=p2],m2)):
                        if allcross(n,p1,F1,p2,F2):
                            checked+=1
                            assert bridge_or_slack(n,p1,F1,p2,F2)
# Sharp defect-one family for m=3,4,5: n=m+2, ports0,1, common fan{2,...,m+1}; no bridge, gap=m+1.
sharp=[]
for m in (3,4,5):
    n=m+2; F=set(range(2,m+2))
    assert allcross(n,0,F,1,F) and 1 not in F and 0 not in F
    d=len(fwd_interval(n,1,0));assert d==m+1
    sharp.append({"m":m,"n":n,"gap":d,"defect":d-m})

payload={
 "certificate":{"n":22,"arcs":len(E),"W_HA":sorted(W),"bypass_lengths":{"z6":b6,"z7":b7},"strict_three_pack":pack},
 "symbolic":{"checked_allcross_configs":checked,"n_max":10,"fan_sizes":[3,4,5],"sharp_family":sharp},
 "result":"PASS"}
canon=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
payload["payload_sha256"]=hashlib.sha256(canon).hexdigest()
print(json.dumps(payload,sort_keys=True,indent=2))
