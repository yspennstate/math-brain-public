#!/usr/bin/env python3
"""Exact route checks for R20 / KNSV-2026-LOOPY-U.

Two source-driven searches, all over Z:

A. Exhaust every labelled rooted simple gadget on root + three new vertices
   (64 patterns) attached by a one-vertex sum to each root of the KNSV
   10-vertex collision pair.  Rooted-U and pointed-L(1,x) are computed once
   and glued by exact bilinear convolution.  This covers 640 extensions on
   each side and all 409600 cross pairs.

B. Start from KNSV Theorem 8.10 / Example 8.11, the 5-vertex loopless
   multigraph pair with equal U and distinct L.  Keep one direct edge on each
   of the six underlying edges and replace the four extra parallel copies by
   internally disjoint paths.  At n=12 there are seven internal vertices
   distributed positively over the four extra paths, hence 20 compositions
   on each side and 400 exact cross pairs.

No floating point arithmetic is used.  A negative result is PARTIAL only.
"""
from collections import defaultdict, Counter
from itertools import combinations
import hashlib

CODES = ("I?bB@_wYO", "I?bB@_wk_")

# KNSV Example 8.11, vertices changed from 1..5 to 0..4.
BASE5 = ((0,2),(2,4),(4,1),(1,3),(3,0),(0,4))
MULT1 = (1,2,2,3,1,1)
MULT2 = (1,2,1,2,3,1)

def decode_graph6(s):
    vals = [ord(c)-63 for c in s]
    n = vals[0]
    bits = []
    for v in vals[1:]:
        bits.extend((v >> sh) & 1 for sh in range(5,-1,-1))
    edges=[]; k=0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                edges.append((i,j))
            k += 1
    return n, tuple(edges)

def find(p,x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(p,sz,a,b):
    a,b=find(p,a),find(p,b)
    if a==b:
        return False
    if sz[a] < sz[b]:
        a,b=b,a
    p[b]=a; sz[a]+=sz[b]
    return True

def u_poly(n, edges):
    """Ordinary U in basis prod z_size * (y-1)^cyclomatic."""
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    init = tuple(range(n))
    dp = {(init,0):1}
    for u,v in edges:
        nd=defaultdict(int)
        for (part,ec),cnt in dp.items():
            nd[(part,ec)] += cnt
            ru,rv=part[u],part[v]
            if ru==rv:
                p2=part
            else:
                a,b=(ru,rv) if ru<rv else (rv,ru)
                p2=tuple(a if x==b else x for x in part)
            nd[(p2,ec+1)] += cnt
        dp=nd
    out=defaultdict(int)
    for (part,ec),cnt in dp.items():
        mult=Counter(part)
        sizes=tuple(sorted(mult.values()))
        cyc=ec-n+len(mult)
        out[(sizes,cyc)] += cnt
    return dict(out)

def rooted_u(n,edges,root):
    """Rooted U: root-component size, other sizes, total cyclomatic number."""
    edges=tuple(sorted(tuple(sorted(e)) for e in edges))
    m=len(edges); out=defaultdict(int)
    for mask in range(1<<m):
        p=list(range(n)); sz=[1]*n; ec=0
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                ec += 1
                union(p,sz,u,v)
        rr=[find(p,v) for v in range(n)]
        comp=Counter(rr)
        r0=rr[root]
        out[(comp[r0], tuple(sorted(s for r,s in comp.items() if r!=r0)),
             ec-n+len(comp))] += 1
    return dict(out)

def pointed_l1(n,edges,root):
    """Pointed L(1,x): root exponent separated from other component exponents."""
    edges=tuple(sorted(tuple(sorted(e)) for e in edges))
    m=len(edges); out=defaultdict(int)
    for mask in range(1<<m):
        p=list(range(n)); sz=[1]*n; ok=True
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1 and not union(p,sz,u,v):
                ok=False; break
        if not ok:
            continue
        rr=[find(p,v) for v in range(n)]
        comp=Counter(rr)
        eps={r:0 for r in comp}
        # Choose the max-edge activity convention: an omitted edge i is
        # active iff its endpoints are connected by selected earlier edges.
        pp=list(range(n)); ss=[1]*n
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                union(pp,ss,u,v)
            elif find(pp,u)==find(pp,v):
                eps[rr[u]] += 1
        r0=rr[root]
        root_exp=(comp[r0]-1)+eps[r0]
        others=tuple(sorted((s-1)+eps[r] for r,s in comp.items() if r!=r0))
        out[(root_exp,others)] += 1
    return dict(out)

def unpoint_l(P):
    out=defaultdict(int)
    for (r,others),c in P.items():
        out[tuple(sorted((r,)+others))] += c
    return dict(out)

def glue_u(RA,RB):
    out=defaultdict(int)
    for (sa,oa,ca),va in RA.items():
        for (sb,ob,cb),vb in RB.items():
            out[(tuple(sorted((sa+sb-1,)+oa+ob)),ca+cb)] += va*vb
    return dict(out)

def glue_l(PA,PB):
    out=defaultdict(int)
    for (ea,oa),va in PA.items():
        for (eb,ob),vb in PB.items():
            out[tuple(sorted((ea+eb,)+oa+ob))] += va*vb
    return dict(out)

def polykey(P):
    return tuple(sorted(P.items()))

def digest(P):
    return hashlib.sha256(repr(polykey(P)).encode()).hexdigest()

def compositions_positive(total,k):
    if k==1:
        yield (total,)
    else:
        for first in range(1,total-k+2):
            for rest in compositions_positive(total-first,k-1):
                yield (first,)+rest

def simpleify(mult, counts):
    """One direct edge per support edge; each extra copy becomes a path."""
    n=5; edges=[]; j=0
    for (u,v),m in zip(BASE5,mult):
        edges.append((u,v))
        for _ in range(m-1):
            internal=counts[j]; j+=1
            prev=u
            for _ in range(internal):
                w=n; n+=1
                edges.append((prev,w)); prev=w
            edges.append((prev,v))
    assert j==len(counts)
    E=tuple(tuple(sorted(e)) for e in edges)
    assert len(E)==len(set(E))
    assert all(u!=v for u,v in E)
    return n,E

def main():
    seeds=[decode_graph6(c) for c in CODES]
    U=[u_poly(*g) for g in seeds]
    assert U[0]==U[1]
    P0=[pointed_l1(*seeds[0],r) for r in range(10)]
    P1=[pointed_l1(*seeds[1],r) for r in range(10)]
    assert unpoint_l(P0[0])==unpoint_l(P1[0])

    R0=[rooted_u(*seeds[0],r) for r in range(10)]
    R1=[rooted_u(*seeds[1],r) for r in range(10)]
    rooted_u_matches=[(i,j) for i in range(10) for j in range(10)
                      if R0[i]==R1[j]]
    pointed_l_matches=[(i,j) for i in range(10) for j in range(10)
                       if P0[i]==P1[j]]

    # All labelled simple rooted graphs on four vertices, root 0.
    E4=tuple(combinations(range(4),2))
    gadgets=[]
    for mask in range(1<<len(E4)):
        ed=tuple(e for i,e in enumerate(E4) if (mask>>i)&1)
        gadgets.append((mask, rooted_u(4,ed,0), pointed_l1(4,ed,0)))

    ext=[{},{}]
    for side,(RR,PP) in enumerate(((R0,P0),(R1,P1))):
        for r in range(10):
            for mask,rg,pg in gadgets:
                ext[side][(r,mask)] = (glue_u(RR[r],rg), glue_l(PP[r],pg))

    groups=[defaultdict(list),defaultdict(list)]
    for side in (0,1):
        for key,(uu,ll) in ext[side].items():
            groups[side][polykey(uu)].append((key,ll))

    common=set(groups[0]).intersection(groups[1])
    u_equal_pairs=0; sep=[]
    for uk in common:
        A=groups[0][uk]; B=groups[1][uk]
        u_equal_pairs += len(A)*len(B)
        for k0,l0 in A:
            l0k=polykey(l0)
            for k1,l1 in B:
                if l0k != polykey(l1):
                    sep.append((k0,k1))

    # Minimal n=12 variable-subdivision simpleification.
    comps=list(compositions_positive(7,4))
    assert len(comps)==20
    sg=[{},{}]
    for side,mult in enumerate((MULT1,MULT2)):
        for c in comps:
            G=simpleify(mult,c)
            assert G[0]==12 and len(G[1])==17
            sg[side][c]=u_poly(*G)

    sub_u_equal=[]
    gsub=[defaultdict(list),defaultdict(list)]
    for side in (0,1):
        for c,uu in sg[side].items():
            gsub[side][polykey(uu)].append(c)
    for uk in set(gsub[0]).intersection(gsub[1]):
        for c0 in gsub[0][uk]:
            for c1 in gsub[1][uk]:
                sub_u_equal.append((c0,c1))

    print("R20 KNSV-2026-LOOPY-U exact next-route checks")
    print(f"seed_graph6={CODES[0]} ; {CODES[1]}")
    print(f"seed_U_equal={U[0]==U[1]} seed_U_sha256={digest(U[0])}")
    print(f"rooted_U_cross_matches={rooted_u_matches}")
    print(f"pointed_L1_cross_matches={pointed_l_matches}")
    print(f"rooted_match_relations_identical={rooted_u_matches==pointed_l_matches}")
    print("ROUTE_A=root-plus-3-new-vertices")
    print("labelled_rooted_gadgets=64")
    print("extensions_per_seed=640")
    print("cross_extension_pairs=409600")
    print(f"U_equal_cross_pairs={u_equal_pairs}")
    print(f"U_equal_but_L1_different_pairs={len(sep)}")
    print(f"separators={sep[:20]}")
    print("ROUTE_B=Example8.11-variable-subdivision-simpleification-at-n12")
    print("support_edges=6 edge_copies=10 extra_parallel_copies=4")
    print("internal_vertices=7 n=12 m=17")
    print("positive_compositions_per_side=20 cross_pairs=400")
    print(f"U_equal_cross_pairs={len(sub_u_equal)}")
    print(f"U_equal_pairs={sub_u_equal[:20]}")
    print("VERDICT=PASS: neither source-generated route yields a simple U/L separator.")
    print("SCOPE=PARTIAL_ONLY: N_sep remains >11; general simple graphs on 12+ vertices are not excluded.")

if __name__=="__main__":
    main()
