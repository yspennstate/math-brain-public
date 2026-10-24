#!/usr/bin/env python3
"""Exact finite regression for the nested-endpoint reverse-channel compression.

Self-check only: the arbitrary-size result is proved symbolically in REPORT.md.
Enumerates all distinct transitively closed naturally labelled posets through n=6,
then checks every width<=3 incomparable pair (a,b) with Pred(b) subseteq Pred(a).
"""
from itertools import combinations

def closure(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    reach=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1: reach[i][j]=True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]: reach[i][j]=True
    cm=0
    for k,(i,j) in enumerate(pairs):
        if reach[i][j]: cm |= 1<<k
    return cm, reach

def all_closures(n):
    pairs=n*(n-1)//2
    seen={}
    for mask in range(1<<pairs):
        cm,r=closure(n,mask)
        seen.setdefault(cm,r)
    return list(seen.values())

def incomparable(i,j,r):
    return i != j and not r[i][j] and not r[j][i]

def width(n,r):
    best=0
    for mask in range(1,1<<n):
        vs=[i for i in range(n) if (mask>>i)&1]
        if all(incomparable(i,j,r) for i,j in combinations(vs,2)):
            best=max(best,len(vs))
    return best

def linexts(n,r):
    pred=[0]*n
    for j in range(n):
        for i in range(n):
            if r[i][j]: pred[j] |= 1<<i
    out=[]
    def rec(done, seq):
        if len(seq)==n:
            out.append(tuple(seq)); return
        for v in range(n):
            if not ((done>>v)&1) and pred[v]&~done==0:
                rec(done|(1<<v), seq+(v,))
    rec(0,tuple())
    return out

def preds(v,r):
    return {u for u in range(len(r)) if r[u][v]}

def maxes(S,r):
    return {x for x in S if not any(x!=y and r[x][y] for y in S)}

def mins(S,r):
    return {x for x in S if not any(x!=y and r[y][x] for y in S)}

def cover(x,y,r):
    return r[x][y] and not any(k not in (x,y) and r[x][k] and r[k][y] for k in range(len(r)))

def connected(n,r,kind):
    adj=[set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        c=r[i][j] or r[j][i]
        edge=c if kind=="comp" else not c
        if edge: adj[i].add(j); adj[j].add(i)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]-seen:
            seen.add(w); stack.append(w)
    return len(seen)==n

closures=0
width3=0
nested_pairs=0
strict_pairs=0
double_pred_pairs=0
for n in range(2,7):
    for r in all_closures(n):
        closures += 1
        if width(n,r)>3: continue
        width3 += 1
        exts=linexts(n,r)
        for a in range(n):
            for b in range(n):
                if not incomparable(a,b,r): continue
                PA,PB=preds(a,r),preds(b,r)
                if not PB.issubset(PA): continue
                nested_pairs += 1
                if PB != PA: strict_pairs += 1
                D=PA-PB
                T=maxes(D,r)
                S={z for z in range(n) if r[b][z] and incomparable(z,a,r)}
                U=mins(S,r)
                assert len(T)<=2
                assert len(U)<=2
                assert all(cover(t,a,r) for t in T)
                assert all(cover(b,u,r) for u in U)
                if len(T)==2 and not U:
                    double_pred_pairs += 1

                R=0
                union=0
                for L in exts:
                    pos={v:i for i,v in enumerate(L)}
                    if pos[b] < pos[a]:
                        between=L[pos[b]+1:pos[a]]
                        nonneutral=any(
                            (r[z][a] or r[a][z] or r[z][b] or r[b][z])
                            for z in between
                        )
                        if nonneutral: R += 1
                    atom=any(pos[b]<pos[t] for t in T) or any(pos[u]<pos[a] for u in U)
                    if atom: union += 1
                assert R==union

# Exact bi-connected width-three witness for the T=2,U=0 branch.
n=6
covers0=[(0,1),(0,5),(1,3),(1,4),(2,3)]
r=[[False]*n for _ in range(n)]
for i,j in covers0: r[i][j]=True
for k in range(n):
    for i in range(n):
        if r[i][k]:
            for j in range(n):
                if r[k][j]: r[i][j]=True
assert width(n,r)==3
assert connected(n,r,"comp") and connected(n,r,"inc")
exts=linexts(n,r); E=len(exts)
a,b=3,5
PA,PB=preds(a,r),preds(b,r)
D=PA-PB; T=maxes(D,r)
U=mins({z for z in range(n) if r[b][z] and incomparable(z,a,r)},r)
M=mins({z for z in range(n) if r[a][z] and incomparable(z,b,r)},r)
assert PA=={0,1,2} and PB=={0}
assert T=={1,2} and not U and not M
pos=[{v:i for i,v in enumerate(L)} for L in exts]
pab=sum(p[a]<p[b] for p in pos)
atoms={t:sum(p[b]<p[t] for p in pos) for t in sorted(T)}
inter=sum(all(p[b]<p[t] for t in T) for p in pos)
union=sum(any(p[b]<p[t] for t in T) for p in pos)
assert (E,pab,atoms,inter,union)==(33,10,{1:9,2:9},5,13)
assert 3*pab<E and all(3*c<E for c in atoms.values()) and 3*union>E
assert E - union == 20
assert 2*pab == E-union

balanced=[]
for i,j in combinations(range(n),2):
    if incomparable(i,j,r):
        c=sum(p[i]<p[j] for p in pos)
        if 3*c>=E and 3*c<=2*E:
            balanced.append((i,j,c,E-c))
assert balanced

print("POS3_NESTED_REVERSE_CHANNEL_COMPRESSION_V1_PASS")
print("natural_transitive_closures_n2_to_n6", closures)
print("width_le_3_closures", width3)
print("nested_endpoint_orientations_checked", nested_pairs)
print("strict_nested_endpoint_orientations", strict_pairs)
print("double_predecessor_no_successor_local_states", double_pred_pairs)
print("witness_covers", covers0)
print("witness_width", width(n,r))
print("witness_comparability_connected", connected(n,r,"comp"))
print("witness_incomparability_connected", connected(n,r,"inc"))
print("witness_E", E)
print("witness_pair_a_b", (a,b))
print("witness_Pred_a", sorted(PA))
print("witness_Pred_b", sorted(PB))
print("witness_T", sorted(T))
print("witness_U", sorted(U))
print("witness_M", sorted(M))
print("witness_count_a_before_b", pab)
print("witness_predecessor_atom_counts", atoms)
print("witness_atom_intersection", inter)
print("witness_atom_union_R", union)
print("witness_balanced_pairs", balanced)
