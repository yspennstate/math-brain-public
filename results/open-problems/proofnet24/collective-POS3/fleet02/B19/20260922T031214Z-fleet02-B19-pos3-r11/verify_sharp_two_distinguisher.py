#!/usr/bin/env python3
"""Exact verifier for a sharp POS3 two-distinguisher adversary.

Uniform law only: every linear extension is enumerated once, weight one.
The distinguished pair (3,13) has exactly two relation distinguishers,
one lower and one upper, yet Pr(3<13)=1207/1810>2/3 with the minimum
possible positive integer slack 3*N(3<13)-2E=1.
"""
from fractions import Fraction
from itertools import combinations

N=15
ALL=(1<<N)-1
COVERS=(
 (0,1),(0,10),(1,2),(2,3),(2,12),(3,4),(3,9),
 (5,6),(6,2),(6,11),(7,3),(7,8),(7,13),(8,4),(8,9),
 (9,14),(10,6),(11,7),(11,12),(12,8),(12,13),(13,4),(13,14)
)
LMAJ=(0,5,10,1,6,11,2,7,12,3,8,13,9,4,14)
POS={x:i for i,x in enumerate(LMAJ)}

reach=[0]*N
for u,v in COVERS: reach[u]|=1<<v
for k in range(N):
    bk=1<<k
    for i in range(N):
        if reach[i]&bk: reach[i]|=reach[k]
assert all(not ((reach[i]>>i)&1) for i in range(N))
pred=[0]*N
for u in range(N):
    for v in range(N):
        if (reach[u]>>v)&1: pred[v]|=1<<u

def comp(a,b):
    return bool(((reach[a]>>b)&1) or ((reach[b]>>a)&1))

exts=[]
def rec(mask,seq):
    if mask==ALL:
        exts.append(tuple(seq)); return
    for x in range(N):
        if mask>>x&1: continue
        if pred[x]&~mask: continue
        seq.append(x); rec(mask|1<<x,seq); seq.pop()
rec(0,[])
E=len(exts)
positions=[]
for e in exts:
    p=[0]*N
    for i,x in enumerate(e): p[x]=i
    positions.append(p)

inc=[(a,b) for a in range(N) for b in range(a+1,N) if not comp(a,b)]
pc={}
balanced=[]
for a,b in inc:
    n=sum(p[a]<p[b] for p in positions)
    pc[(a,b)]=n
    if E<=3*n<=2*E: balanced.append((a,b,n))

def prob(u,v):
    a,b=sorted((u,v))
    q=Fraction(pc[(a,b)],E)
    return q if (u,v)==(a,b) else 1-q

def anti(S): return all(not comp(a,b) for a,b in combinations(S,2))
anti3=next(S for S in combinations(range(N),3) if anti(S))
anti4=next((S for S in combinations(range(N),4) if anti(S)),None)
assert anti4 is None
adj={x:set() for x in range(N)}
for a,b in inc: adj[a].add(b);adj[b].add(a)
seen=set(); stack=[0]
while stack:
    x=stack.pop()
    if x in seen: continue
    seen.add(x);stack.extend(adj[x]-seen)
assert len(seen)==N

def autonomous(mask):
    for z in range(N):
        if mask>>z&1: continue
        rr=None
        for a in range(N):
            if not (mask>>a)&1: continue
            r=-1 if (reach[z]>>a)&1 else (1 if (reach[a]>>z)&1 else 0)
            if rr is None: rr=r
            elif rr!=r: return False
    return True
mods=[]
for m in range(1,ALL):
    k=m.bit_count()
    if 2<=k<N and autonomous(m):
        mods.append(tuple(i for i in range(N) if m>>i&1))
assert not mods

assert all(POS[u]<POS[v] for u in range(N) for v in range(N) if (reach[u]>>v)&1)
maj_ok=True
for a,b in inc:
    n=pc[(a,b)]
    u,v=(a,b) if 2*n>E else (b,a)
    if POS[u]>=POS[v]: maj_ok=False
assert maj_ok

u,v=3,13
n=pc[(3,13)]
assert n==1207 and E==1810
assert 3*n-2*E==1
assert Fraction(n,E)==Fraction(1207,1810)

def relation(z,a):
    if (reach[z]>>a)&1:return -1
    if (reach[a]>>z)&1:return 1
    return 0
dist=[z for z in range(N) if z not in (u,v) and relation(z,u)!=relation(z,v)]
assert dist==[9,12]
Pred=lambda a:{z for z in range(N) if (reach[z]>>a)&1}
Succ=lambda a:{z for z in range(N) if (reach[a]>>z)&1}
assert Pred(13)==Pred(3)|{12}
assert Succ(3)==Succ(13)|{9}
assert relation(12,13)==-1 and relation(12,3)==0
assert relation(9,3)==1 and relation(9,13)==0
assert (reach[12]>>9)&1

order=sorted(range(N), key=lambda x:-len(adj[x]))
color=[-1]*N
cover_set=set()
def color_rec(i,max_used):
    if i==len(order):
        if set(color)=={0,1,2}:
            groups=[]
            for c in range(3):
                g=tuple(sorted((x for x in range(N) if color[x]==c),key=lambda x:POS[x]))
                assert all((reach[g[i]]>>g[j])&1 for i in range(len(g)) for j in range(i+1,len(g)))
                groups.append(g)
            cover_set.add(tuple(sorted(groups)))
        return
    x=order[i]
    for c in range(min(2,max_used+1)+1):
        if all(color[y]!=c for y in adj[x] if color[y]!=-1):
            color[x]=c;color_rec(i+1,max(max_used,c));color[x]=-1
color[order[0]]=0
color_rec(1,0)
chain_covers=sorted(cover_set)
assert len(chain_covers)==1536
extreme=[c for c in chain_covers if tuple(sorted(map(len,c)))==(2,5,8)]
assert len(extreme)==8
chains=extreme[0]

def cover_stats(chains):
    cof={x:i for i,c in enumerate(chains) for x in c}
    rows=[];cells=[]
    for x in range(N):
        cx=cof[x]
        for ci,c in enumerate(chains):
            if ci==cx: continue
            if not any(not comp(x,y) for y in c): continue
            arr=[0]*(len(c)+1)
            for p in positions:
                arr[sum(p[y]<p[x] for y in c)]+=1
            g=sum(POS[y]<POS[x] for y in c)
            before=sum(arr[:g]);through=before+arr[g]
            rows.append((x,ci,g,tuple(arr),before,through,3*before<E and 3*through>2*E))
        others=[ci for ci in range(3) if ci!=cx]
        gs=[sum(POS[y]<POS[x] for y in chains[ci]) for ci in others]
        ct=sum(all(sum(p[y]<p[x] for y in chains[ci])==g for ci,g in zip(others,gs)) for p in positions)
        cells.append((x,tuple(others),tuple(gs),ct))
    return rows,cells
rows,cells=cover_stats(chains)
assert all(81*c[3]>E for c in cells)

print("POS3 SHARP TWO-DISTINGUISHER ADVERSARY")
print(f"N={N}")
print(f"E={E}")
print("covers="+",".join(f"{a}<{b}" for a,b in COVERS))
print(f"width_witness_3={anti3}")
print("width=3")
print("incomparability_connected=True")
print(f"incomparable_pairs={len(inc)}")
print(f"nontrivial_proper_autonomous_subsets={len(mods)}")
print(f"LMAJ={LMAJ}")
print(f"simple_majority_order_transitive={maj_ok}")
print(f"balanced_pairs={len(balanced)}")
print("ALL_INCOMPARABLE_PAIR_PROBABILITIES p(a<b):")
for a,b in inc:
    q=Fraction(pc[(a,b)],E)
    tag="BALANCED" if E<=3*pc[(a,b)]<=2*E else "UNBALANCED"
    print(f"  ({a},{b}) {q.numerator}/{q.denominator} count={pc[(a,b)]}/{E} {tag}")
print("DISTINGUISHED_PAIR:")
print(f"  pair=(3,13)")
print(f"  p(3<13)=1207/1810")
print(f"  strong_threshold_slack=3*1207-2*1810={3*1207-2*1810}")
print(f"  p_minus_2_3={Fraction(1207,1810)-Fraction(2,3)}")
print(f"  distinguishers={dist}")
print(f"  lower_distinguisher=12")
print(f"  upper_distinguisher=9")
print(f"  Pred(13)=Pred(3)+{{12}}: {sorted(Pred(13))}")
print(f"  Succ(3)=Succ(13)+{{9}}: {sorted(Succ(3))}")
print(f"  distinguisher_relation_12_lt_9={bool((reach[12]>>9)&1)}")
print(f"unlabeled_three_chain_covers={len(chain_covers)}")
print(f"extreme_asymmetric_cover_count={len(extreme)}")
print(f"chosen_extreme_cover={chains}")
print(f"chosen_extreme_cover_sizes={tuple(sorted(map(len,chains)))}")
print(f"chosen_extreme_relevant_rows={len(rows)}")
print(f"chosen_extreme_band_failures={sum(not r[-1] for r in rows)}")
print(f"chosen_extreme_min_pinned_cell={min(c[3] for c in cells)}/{E}={Fraction(min(c[3] for c in cells),E)}")
print(f"chosen_extreme_all_pinned_cells_gt_1_81={all(81*c[3]>E for c in cells)}")
print("ORDINAL_CHAIN_PADDING:")
print("  For every s,t>=0, C_s ordinal-sum P ordinal-sum C_t preserves")
print("  all 17 incomparable-pair probabilities and the exact two-distinguisher pair;")
print("  width stays 3 and no new incomparable pair is created.")
print("POS3_SHARP_TWO_DISTINGUISHER_PASS")
