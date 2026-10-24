from fractions import Fraction
from itertools import combinations
from collections import defaultdict

V = (0,1,2,3)
E = ((0,1),(0,2),(0,3),(1,2))
u,v = 1,3
e=(0,1); f=(0,2)

def canon(a):
    x,y=a
    return (x,y) if x<y else (y,x)

E=tuple(canon(x) for x in E)
e=canon(e); f=canon(f)

def is_forest(edges):
    parent={x:x for x in V}
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb: return False
        parent[rb]=ra
        return True
    for a,b in edges:
        if not union(a,b): return False
    return True

def connected(edges,a,b):
    adj={x:[] for x in V}
    for x,y in edges:
        adj[x].append(y); adj[y].append(x)
    seen={a}; stack=[a]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return b in seen

def u_component(edges):
    adj={x:[] for x in V}
    for x,y in edges:
        adj[x].append(y); adj[y].append(x)
    seen={u}; stack=[u]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return frozenset(seen)

forests=[]
for r in range(len(E)+1):
    for F in combinations(E,r):
        if is_forest(F):
            forests.append(frozenset(F))

cond=[F for F in forests if not connected(F,u,v)]
assert len(cond)==10
Ne=sum(e in F for F in cond)
Nf=sum(f in F for F in cond)
Nef=sum(e in F and f in F for F in cond)
gap=Ne*Nf-len(cond)*Nef
cov=Fraction(Nef,len(cond))-Fraction(Ne,len(cond))*Fraction(Nf,len(cond))
assert (Ne,Nf,Nef,gap,cov)==(3,4,1,2,Fraction(-1,50))

by=defaultdict(list)
for F in cond:
    by[u_component(F)].append(F)

stats=[]
within=Fraction(0)
Em_e=Fraction(0); Em_f=Fraction(0); Em_ef=Fraction(0)
for S, Fs in sorted(by.items(), key=lambda kv:(len(kv[0]),tuple(kv[0]))):
    w=len(Fs)
    me=Fraction(sum(e in F for F in Fs),w)
    mf=Fraction(sum(f in F for F in Fs),w)
    mef=Fraction(sum(e in F and f in F for F in Fs),w)
    c=mef-me*mf
    p=Fraction(w,len(cond))
    within += p*c
    Em_e += p*me
    Em_f += p*mf
    Em_ef += p*me*mf
    stats.append((tuple(sorted(S)),w,me,mf,c))

expected=[
    ((1,),4,Fraction(0),Fraction(1,2),Fraction(0)),
    ((0,1),1,Fraction(1),Fraction(0),Fraction(0)),
    ((1,2),2,Fraction(0),Fraction(0),Fraction(0)),
    ((0,1,2),3,Fraction(2,3),Fraction(2,3),Fraction(-1,9)),
]
assert stats==expected, (stats, expected)
mix=Em_ef-Em_e*Em_f
assert mix==Fraction(1,75)
assert within==Fraction(-1,30)
assert within+mix==cov==Fraction(-1,50)

# Direct verification of component-weight identity:
# weight(S) = tau(J[S]) * Z(J[V-S]).
def induced_edges(S):
    S=set(S)
    return tuple(h for h in E if h[0] in S and h[1] in S)

def forest_count(vertices, edges):
    vertices=tuple(vertices)
    total=0
    for r in range(len(edges)+1):
        for F in combinations(edges,r):
            parent={x:x for x in vertices}
            def find(x):
                while parent[x]!=x:
                    parent[x]=parent[parent[x]]
                    x=parent[x]
                return x
            ok=True
            for a,b in F:
                ra,rb=find(a),find(b)
                if ra==rb:
                    ok=False; break
                parent[rb]=ra
            if ok: total+=1
    return total

def spanning_tree_count(S):
    S=set(S)
    if len(S)==1: return 1
    es=induced_edges(S)
    cnt=0
    for F in combinations(es,len(S)-1):
        if not is_forest(F): continue
        adj={x:[] for x in S}
        for a,b in F:
            adj[a].append(b); adj[b].append(a)
        seen={next(iter(S))}; stack=list(seen)
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        if seen==S: cnt+=1
    return cnt

for S,Fs in by.items():
    comp=set(S)
    rest=set(V)-comp
    tau=spanning_tree_count(comp)
    z=forest_count(rest, tuple(h for h in E if h[0] in rest and h[1] in rest))
    assert tau*z==len(Fs), (S,tau,z,len(Fs))

# Generic marked-weight scaling checked by enumeration on the witness graph.
def weighted_counts(we,wf):
    Z=Ze=Zf=Zef=0
    for F in forests:
        w=(we if e in F else 1)*(wf if f in F else 1)
        Z+=w
        if e in F: Ze+=w
        if f in F: Zf+=w
        if e in F and f in F: Zef+=w
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef

base=weighted_counts(1,1)[-1]
for we in (1,2,3,5):
    for wf in (1,2,4):
        assert weighted_counts(we,wf)[-1] == we*wf*base

print("WITNESS_N_NE_NF_NEF_GAP", len(cond),Ne,Nf,Nef,gap)
print("WITNESS_COV", cov)
for row in stats:
    print("STRATUM", row)
print("MIXTURE_COV", mix)
print("WITHIN_STRATUM_COV", within)
print("TOTAL_COV", within+mix)
print("MARKED_WEIGHT_SCALING_BASE_GAP", base)
print("ALL_EXACT_ASSERTIONS_PASSED")
