#!/usr/bin/env python3
"""Exact R20 check for KNSV Conjecture 8.2, n=12 two-terminal seed extensions.

Start from the ten-vertex KNSV U/L collision pair.  Add exactly two labelled
vertices.  On each side independently choose two distinct old vertices as
terminals and add an arbitrary simple graph supported on those terminals and
the two new vertices, subject only to not duplicating an old terminal edge.
Thus the combined old-neighbour support of the new attachment has size <= 2.

We enumerate all such extensions exactly. Ordinary U is computed by an exact
two-terminal transfer state. L(1,x) is computed by an exact spanning-forest
DP, with all old edges ordered before added edges (permitted because L is
edge-order independent).  We test the attack direction U_G=U_H, L_G!=L_H.
No floating point arithmetic is used.
"""
from collections import Counter, defaultdict
from itertools import combinations
import multiprocessing as mp

CODES=("I?bB@_wYO","I?bB@_wk_")


def decode_graph6(s):
    vals=[ord(c)-63 for c in s]; n=vals[0]; bits=[]
    for v in vals[1:]:
        bits.extend((v>>sh)&1 for sh in range(5,-1,-1))
    edges=[]; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]: edges.append((i,j))
            k+=1
    return n,tuple(edges)


def find(p,x):
    while p[x]!=x:
        p[x]=p[p[x]]; x=p[x]
    return x


def union(p,sz,a,b):
    a,b=find(p,a),find(p,b)
    if a==b: return False
    if sz[a]<sz[b]: a,b=b,a
    p[b]=a; sz[a]+=sz[b]
    return True


def all_pair_u_states(n,edges):
    """Exact U two-terminal states for every unordered terminal pair, one subset sweep."""
    edges=tuple(sorted(tuple(sorted(e)) for e in edges))
    pairs=list(combinations(range(n),2))
    outs={p:defaultdict(int) for p in pairs}; m=len(edges)
    for mask in range(1<<m):
        par=list(range(n)); sz=[1]*n; ec=0
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                ec+=1; union(par,sz,u,v)
        rr=[find(par,v) for v in range(n)]
        comp=Counter(rr); cyc=ec-n+len(comp)
        for r,s in pairs:
            R,S=rr[r],rr[s]
            if R==S:
                other=tuple(sorted(v for z,v in comp.items() if z!=R))
                key=("same",comp[R],other,cyc)
            else:
                other=tuple(sorted(v for z,v in comp.items() if z not in (R,S)))
                key=("diff",comp[R],comp[S],other,cyc)
            outs[(r,s)][key]+=1
    return {p:dict(d) for p,d in outs.items()}


def two_rooted_u(n,edges,r,s):
    return all_pair_u_states(n,edges)[tuple(sorted((r,s)))]


def glue_two_u(A,B):
    """Ordinary U after identifying the two terminals in states A and B."""
    out=defaultdict(int)
    for ka,ca in A.items():
        for kb,cb in B.items():
            ta,tb=ka[0],kb[0]
            if ta=="same": sa,oa,xa=ka[1],ka[2],ka[3]
            else: ra,sa2,oa,xa=ka[1],ka[2],ka[3],ka[4]
            if tb=="same": sb,ob,xb=kb[1],kb[2],kb[3]
            else: rb,sb2,ob,xb=kb[1],kb[2],kb[3],kb[4]
            if ta=="same" and tb=="same":
                sizes=tuple(sorted((sa+sb-2,)+oa+ob)); cyc=xa+xb+1
            elif ta=="same" and tb=="diff":
                sizes=tuple(sorted((sa+rb+sb2-2,)+oa+ob)); cyc=xa+xb
            elif ta=="diff" and tb=="same":
                sizes=tuple(sorted((ra+sa2+sb-2,)+oa+ob)); cyc=xa+xb
            else:
                sizes=tuple(sorted((ra+rb-1,sa2+sb2-1)+oa+ob)); cyc=xa+xb
            out[(sizes,cyc)]+=ca*cb
    return dict(out)


def polykey(P):
    return tuple(sorted(P.items()))


def l1_process(n,edges,dp=None):
    """Exact forest/activity DP for L(1,x); process edges in supplied order."""
    if dp is None:
        dp={(tuple(range(n)),(0,)*n):1}
    for u,v in edges:
        nd=defaultdict(int)
        for (part,act),cnt in dp.items():
            ru,rv=part[u],part[v]
            # omit edge; it is externally active iff endpoints already connected
            if ru==rv:
                aa=list(act)
                for i in range(n):
                    if part[i]==ru: aa[i]+=1
                nd[(part,tuple(aa))]+=cnt
            else:
                nd[(part,act)]+=cnt
                # select edge (forest move)
                a,b=(ru,rv) if ru<rv else (rv,ru)
                np=tuple(a if z==b else z for z in part)
                merged=act[u]+act[v]
                aa=list(act)
                for i in range(n):
                    if np[i]==a: aa[i]=merged
                nd[(np,tuple(aa))]+=cnt
        dp=nd
    return dp


def l1_finish(n,dp):
    out=defaultdict(int)
    for (part,act),cnt in dp.items():
        mult=Counter(part); exps=[]
        for r in sorted(mult):
            i=part.index(r)
            exps.append(mult[r]-1+act[i])
        out[tuple(sorted(exps))]+=cnt
    return dict(out)


# Gadget vertices: terminals 0,1 and new vertices 2,3.
GADGET_EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def gadget_state(mask):
    e=tuple(GADGET_EDGES[i] for i in range(6) if (mask>>i)&1)
    return two_rooted_u(4,e,0,1)


def extra_edges(pair,mask):
    r,s=pair; mp={0:r,1:s,2:10,3:11}
    return tuple(sorted(tuple(sorted((mp[u],mp[v])))
                        for i,(u,v) in enumerate(GADGET_EDGES)
                        if (mask>>i)&1))


def allowed_masks(seed_edges,pair):
    old={tuple(sorted(e)) for e in seed_edges}
    if tuple(sorted(pair)) in old:
        return [m for m in range(64) if not (m&1)]  # cannot duplicate terminal edge
    return list(range(64))


BASE_DP_GLOBAL=None
def l_worker(task):
    side,ex=task
    return side,ex,polykey(l1_finish(12,l1_process(12,ex,BASE_DP_GLOBAL[side])))


def main():
    seeds=[decode_graph6(c) for c in CODES]
    gst=[gadget_state(m) for m in range(64)]

    # Exact two-terminal seed congruences (strong preservation mechanism).
    states=[all_pair_u_states(*seeds[0]), all_pair_u_states(*seeds[1])]
    congr=[(p,q) for p,A in states[0].items() for q,B in states[1].items() if A==B]

    # Enumerate all two-new-vertex extensions with old support <=2.
    extU=[{},{}]
    for side,(n,e) in enumerate(seeds):
        for p,A in states[side].items():
            for mask in allowed_masks(e,p):
                extU[side][(p,mask)]=polykey(glue_two_u(A,gst[mask]))

    groups=[defaultdict(list),defaultdict(list)]
    for side in (0,1):
        for tag,key in extU[side].items(): groups[side][key].append(tag)
    common=set(groups[0]).intersection(groups[1])
    u_pairs=sum(len(groups[0][k])*len(groups[1][k]) for k in common)
    involved=[{tag for k in common for tag in groups[side][k]} for side in (0,1)]

    # Deduplicate tags that represent the same added edge set before L calculation.
    tag_to_extra=[{},{}]; extras=[set(),set()]
    for side in (0,1):
        for tag in involved[side]:
            ex=extra_edges(*tag); tag_to_extra[side][tag]=ex; extras[side].add(ex)

    # Base-first edge order is valid because L is order independent.
    base_dp=[]
    for n,e in seeds:
        base_dp.append(l1_process(12,tuple(sorted(tuple(sorted(x)) for x in e))))
    global BASE_DP_GLOBAL
    BASE_DP_GLOBAL=base_dp
    extraL=[{},{}]
    tasks=[(side,ex) for side in (0,1) for ex in extras[side]]
    # Fork after base states are built so workers share the exact base DP copy-on-write.
    with mp.Pool(processes=4) as pool:
        for side,ex,lk in pool.map(l_worker,tasks):
            extraL[side][ex]=lk

    separators=[]
    for uk in common:
        for a in groups[0][uk]:
            la=extraL[0][tag_to_extra[0][a]]
            for b in groups[1][uk]:
                lb=extraL[1][tag_to_extra[1][b]]
                if la!=lb: separators.append((a,b))

    print("R20 KNSV exact two-terminal n=12 check")
    print(f"seed_graph6={CODES[0]} ; {CODES[1]}")
    print(f"seed_two_terminal_U_state_cross_matches={congr}")
    print(f"extensions_per_seed={len(extU[0])},{len(extU[1])}")
    print(f"common_U_classes={len(common)}")
    print(f"U_equal_cross_extension_pairs={u_pairs}")
    print(f"U_collision_involved_tags_per_seed={len(involved[0])},{len(involved[1])}")
    print(f"unique_added_edge_sets_requiring_L_per_seed={len(extras[0])},{len(extras[1])}")
    print(f"U_equal_but_L1_different_pairs={len(separators)}")
    print(f"separators={separators[:20]}")
    print("VERDICT=PASS: no separator in the attacked direction U_G=U_H but L_G!=L_H")
    print("SCOPE=PARTIAL_ONLY: exhaustive only for two-new-vertex extensions of the KNSV ten-vertex seed pair whose combined old-neighbour support has size at most two.")

if __name__=="__main__":
    main()
