#!/usr/bin/env python3
"""Exact R20/KNSV check: all independent two-terminal network replacements at n=12.

Scope.
-----
KNSV Example 8.11 gives two 5-vertex loopless multigraphs with the same
ordinary U-polynomial and different loopy polynomial.  They have common
simple support

    (0,2),(2,4),(4,1),(1,3),(3,0),(0,4)

and multiplicities

    M1=(1,2,2,3,1,1),  M2=(1,2,1,2,3,1).

Thus each side has four excess parallel-edge copies.  Keep one direct edge
on each support edge.  Replace each excess copy by a connected simple
2-terminal network, internally vertex-disjoint from every other replacement,
with no terminal edge.  Give the four replacement networks positive numbers
of internal vertices summing to 7, so every resulting simple graph has 12
vertices.

For r=1,2,3,4 internal vertices, every labelled connected network is
enumerated and quotiented by an exact boundary-transfer signature.  The
signature records, for every selected edge subset, terminal connectivity,
internal vertices attached to each terminal component, sizes of closed
internal components, and selected-edge count.  This is sufficient to recover
the ordinary U-polynomial after gluing into any host.

Rather than compute U for all quotient representatives, we use an exact
necessary invariant.  The forest part of U determines det(z I + L) by the
matrix-forest theorem, hence U equality implies equality of every Laplacian
power trace tr(L^k).  Exact signed 64-bit arithmetic is safe here for k<=9:
all graphs are simple on n=12, so Delta<=11 and every dot-product magnitude
in the recurrence L^k=L^(k-1)L is < 12*11*22^8 < 2^63.

The checker shows that the two sides have no common trace vector
(tr L,...,tr L^9), hence no U-collision in this entire replacement family.
The last candidates surviving through k=8 are recomputed by two independent
exact U routes (direct graph DP and transfer-state gluing) as a consistency
check.  No floating-point arithmetic is used.

This is a PARTIAL route-level no-go only.  It does not prove N_sep>12 and does
not settle KNSV Conjecture 8.2 for arbitrary simple graphs.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import hashlib
import numpy as np

BASE5=((0,2),(2,4),(4,1),(1,3),(3,0),(0,4))
MULT1=(1,2,2,3,1,1)
MULT2=(1,2,1,2,3,1)
SLOTS1=(1,2,3,3)  # one slot for each excess copy of M1
SLOTS2=(1,3,4,4)  # one slot for each excess copy of M2
N=12
KMAX=9
I64_MAX=(1<<63)-1
SAFE_BOUND=12*11*(2*11)**8
assert SAFE_BOUND < I64_MAX


def dsu_components(n, edges):
    p=list(range(n)); sz=[1]*n
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for a,b in edges:
        a=find(a); b=find(b)
        if a==b:
            continue
        if sz[a]<sz[b]:
            a,b=b,a
        p[b]=a; sz[a]+=sz[b]
    rr=[find(i) for i in range(n)]
    comps={}
    for i,r in enumerate(rr):
        comps.setdefault(r,[]).append(i)
    return rr,comps


def network_signature(r, mask):
    """Boundary transfer signature, or None if the full network is disconnected."""
    n=r+2
    allowed=[e for e in combinations(range(n),2) if e!=(0,1)]
    E=[allowed[i] for i in range(len(allowed)) if (mask>>i)&1]
    _,full=dsu_components(n,E)
    if len(full)!=1:
        return None
    out=defaultdict(int)
    m=len(E)
    for sm in range(1<<m):
        sel=[E[i] for i in range(m) if (sm>>i)&1]
        rr,comps=dsu_components(n,sel)
        r0,r1=rr[0],rr[1]
        if r0==r1:
            bint=len(comps[r0])-2
            closed=tuple(sorted(len(v) for q,v in comps.items() if q!=r0))
            state=(1,bint,closed,len(sel))
        else:
            sint=len(comps[r0])-1
            tint=len(comps[r1])-1
            closed=tuple(sorted(len(v) for q,v in comps.items() if q not in (r0,r1)))
            state=(0,sint,tint,closed,len(sel))
        out[state]+=1
    return tuple(sorted(out.items()))


def enumerate_transfer_types(r):
    n=r+2
    allowed=[e for e in combinations(range(n),2) if e!=(0,1)]
    reps={}; multiplicity=Counter(); connected=0
    for mask in range(1<<len(allowed)):
        sig=network_signature(r,mask)
        if sig is None:
            continue
        connected+=1
        multiplicity[sig]+=1
        reps.setdefault(sig,mask)
    sigs=list(reps)
    edges=[]
    for sig in sigs:
        mask=reps[sig]
        edges.append(tuple(allowed[i] for i in range(len(allowed)) if (mask>>i)&1))
    return {
        'allowed':allowed,
        'sigs':sigs,
        'rep_masks':[reps[s] for s in sigs],
        'rep_edges':edges,
        'signature_multiplicity':multiplicity,
        'connected_labelled':connected,
    }


def positive_compositions(total,k,prefix=()):
    if k==1:
        yield prefix+(total,)
        return
    for a in range(1,total-k+2):
        yield from positive_compositions(total-a,k-1,prefix+(a,))


def all_assignments(types):
    for comp in positive_compositions(7,4):
        ranges=[range(len(types[r]['sigs'])) for r in comp]
        for ids in product(*ranges):
            yield tuple(zip(comp,ids))


def build_graph(types, slot_edges, assn):
    edges={tuple(sorted(e)) for e in BASE5}
    nxt=5
    for eidx,(r,sid) in zip(slot_edges,assn):
        a,b=BASE5[eidx]
        mapping={0:a,1:b}
        for j in range(r):
            mapping[2+j]=nxt+j
        for x,y in types[r]['rep_edges'][sid]:
            X,Y=mapping[x],mapping[y]
            e=tuple(sorted((X,Y)))
            assert e not in edges
            edges.add(e)
        nxt+=r
    assert nxt==12
    return tuple(sorted(edges))


def laplacian_trace_moments(edges,kmax=KMAX):
    L=np.zeros((N,N),dtype=np.int64)
    for a,b in edges:
        L[a,a]+=1; L[b,b]+=1
        L[a,b]-=1; L[b,a]-=1
    assert int(np.max(np.diag(L)))<=11
    P=L.copy(); out=[]
    for k in range(1,kmax+1):
        out.append(int(np.trace(P)))
        assert int(np.max(np.abs(P))) < I64_MAX
        if k<kmax:
            P=P@L
    return tuple(out)


def canonical_part(part):
    """Relabel component representatives by first occurrence."""
    mp={}; nxt=0; out=[]
    for x in part:
        if x not in mp:
            mp[x]=nxt; nxt+=1
        out.append(mp[x])
    return tuple(out)


def direct_u_poly(edges):
    """Exact ordinary U in basis (component-size partition, total cyclomatic)."""
    dp={(tuple(range(N)),0):1}
    for u,v in edges:
        nd=defaultdict(int)
        for (part,ec),cnt in dp.items():
            nd[(part,ec)]+=cnt
            ru,rv=part[u],part[v]
            if ru==rv:
                p2=part
            else:
                a,b=(ru,rv) if ru<rv else (rv,ru)
                p2=canonical_part(tuple(a if x==b else x for x in part))
            nd[(p2,ec+1)]+=cnt
        dp=nd
    out=defaultdict(int)
    for (part,ec),cnt in dp.items():
        comp=Counter(part)
        sizes=tuple(sorted(comp.values()))
        cyc=ec-N+len(comp)
        assert cyc>=0
        out[(sizes,cyc)]+=cnt
    return dict(out)


def sort_blocks(blocks):
    return tuple(sorted(blocks,key=lambda me:(me[0]&-me[0])))

START_BOUND=tuple((1<<i,0) for i in range(5))


def add_network_state(bound,closed,u,v,state):
    blocks=list(bound)
    iu=next(i for i,(m,_) in enumerate(blocks) if (m>>u)&1)
    iv=next(i for i,(m,_) in enumerate(blocks) if (m>>v)&1)
    if state[0]==1:
        _,bint,inside,eadd=state
        if iu==iv:
            m,e=blocks[iu]; blocks[iu]=(m,e+bint)
        else:
            if iu>iv: iu,iv=iv,iu
            m1,e1=blocks[iu]; m2,e2=blocks[iv]
            blocks.pop(iv); blocks.pop(iu)
            blocks.append((m1|m2,e1+e2+bint))
    else:
        _,sint,tint,inside,eadd=state
        if iu==iv:
            m,e=blocks[iu]; blocks[iu]=(m,e+sint+tint)
        else:
            mu,eu=blocks[iu]; mv,ev=blocks[iv]
            blocks[iu]=(mu,eu+sint); blocks[iv]=(mv,ev+tint)
    return sort_blocks(blocks),tuple(sorted(closed+tuple(inside))),eadd


def add_base_edge(bound,u,v):
    blocks=list(bound)
    iu=next(i for i,(m,_) in enumerate(blocks) if (m>>u)&1)
    iv=next(i for i,(m,_) in enumerate(blocks) if (m>>v)&1)
    if iu!=iv:
        if iu>iv: iu,iv=iv,iu
        m1,e1=blocks[iu]; m2,e2=blocks[iv]
        blocks.pop(iv); blocks.pop(iu)
        blocks.append((m1|m2,e1+e2))
    return sort_blocks(blocks)


def transfer_u_poly(types,slot_edges,assn):
    dp={(START_BOUND,(),0):1}
    for eidx,(r,sid) in zip(slot_edges,assn):
        u,v=BASE5[eidx]
        nd=defaultdict(int)
        sig=dict(types[r]['sigs'][sid])
        for (bound,closed,ec),cnt in dp.items():
            for state,mult in sig.items():
                nb,nc,eadd=add_network_state(bound,closed,u,v,state)
                nd[(nb,nc,ec+eadd)]+=cnt*mult
        dp=nd
    for u,v in BASE5:
        nd=defaultdict(int)
        for (bound,closed,ec),cnt in dp.items():
            nd[(bound,closed,ec)]+=cnt
            nd[(add_base_edge(bound,u,v),closed,ec+1)]+=cnt
        dp=nd
    out=defaultdict(int)
    for (bound,closed,ec),cnt in dp.items():
        sizes=list(closed)
        for mask,extra in bound:
            sizes.append(mask.bit_count()+extra)
        sizes=tuple(sorted(sizes))
        cyc=ec-N+len(sizes)
        assert cyc>=0
        out[(sizes,cyc)]+=cnt
    return dict(out)


def graph6(n,edges):
    E={tuple(sorted(e)) for e in edges}
    bits=[]
    for j in range(1,n):
        for i in range(j):
            bits.append(1 if (i,j) in E else 0)
    while len(bits)%6:
        bits.append(0)
    chars=[chr(n+63)]
    for q in range(0,len(bits),6):
        x=0
        for b in bits[q:q+6]:
            x=(x<<1)|b
        chars.append(chr(x+63))
    return ''.join(chars)


def digest_poly(P):
    return hashlib.sha256(repr(tuple(sorted(P.items()))).encode()).hexdigest()


def main():
    types={r:enumerate_transfer_types(r) for r in range(1,5)}
    print('R20 KNSV exact independent-two-terminal-network n=12 check')
    print('model_arithmetic=integer; numpy.int64 only for exact Laplacian products under proved no-overflow bound')
    print(f'int64_safety_bound={SAFE_BOUND} int64_max={I64_MAX}')
    for r in range(1,5):
        print(f'r={r} connected_labelled_networks={types[r]["connected_labelled"]} transfer_types={len(types[r]["sigs"])}')

    comps=list(positive_compositions(7,4))
    print(f'positive_compositions_7_into_4={len(comps)}')
    formula=sum(np.prod([len(types[r]["sigs"]) for r in c],dtype=np.int64) for c in comps)
    print(f'transfer_assignments_per_side={int(formula)}')
    assert int(formula)==11284

    rec=[[],[]]
    for side,slots in enumerate((SLOTS1,SLOTS2)):
        for assn in all_assignments(types):
            E=build_graph(types,slots,assn)
            tr=laplacian_trace_moments(E,KMAX)
            rec[side].append((assn,E,tr))
        assert len(rec[side])==11284

    print('moment_prefix_elimination:')
    common8=None
    for k in range(1,KMAX+1):
        C=[]
        for side in (0,1):
            C.append(Counter(row[2][:k] for row in rec[side]))
        common=set(C[0])&set(C[1])
        pairs=sum(C[0][x]*C[1][x] for x in common)
        print(f'  k={k} common_moment_vectors={len(common)} cross_pairs={pairs}')
        if k==8:
            common8=common
        if k==9:
            assert not common and pairs==0

    assert common8 is not None and len(common8)==1
    key8=next(iter(common8))
    near=[[],[]]
    for side in (0,1):
        near[side]=[row for row in rec[side] if row[2][:8]==key8]
    assert [len(x) for x in near]==[2,1]
    print(f'last_common_trace_1_to_8={key8}')
    print(f'last_candidates_counts={len(near[0])},{len(near[1])}')
    print(f'last_side0_trace9={[x[2][8] for x in near[0]]}')
    print(f'last_side1_trace9={[x[2][8] for x in near[1]]}')
    assert all(x[2][8]==84587130 for x in near[0])
    assert near[1][0][2][8]==84587076

    # Count the last obstruction twice: direct U-DP and transfer gluing.
    a0,e0,t0=near[0][0]
    a1,e1,t1=near[1][0]
    U0d=direct_u_poly(e0); U1d=direct_u_poly(e1)
    U0t=transfer_u_poly(types,SLOTS1,a0); U1t=transfer_u_poly(types,SLOTS2,a1)
    assert U0d==U0t and U1d==U1t
    assert U0d!=U1d
    firstdiff=next(q for q in sorted(set(U0d)|set(U1d)) if U0d.get(q,0)!=U1d.get(q,0))
    print(f'near_side0_assignment={a0}')
    print(f'near_side1_assignment={a1}')
    print(f'near_side0_graph6={graph6(12,e0)}')
    print(f'near_side1_graph6={graph6(12,e1)}')
    print(f'near_side0_edges={e0}')
    print(f'near_side1_edges={e1}')
    print(f'direct_transfer_U_match_side0={U0d==U0t} side1={U1d==U1t}')
    print(f'near_U_equal={U0d==U1d}')
    print(f'near_U_sha256_side0={digest_poly(U0d)}')
    print(f'near_U_sha256_side1={digest_poly(U1d)}')
    print(f'first_U_difference={firstdiff} side0={U0d.get(firstdiff,0)} side1={U1d.get(firstdiff,0)}')

    print('VERDICT=PASS: no ordinary-U collision exists in the full independent connected two-terminal replacement family at n=12.')
    print('SCOPE=PARTIAL_ONLY: arbitrary simple 12-vertex graphs and cross-coupled/shared-internal-vertex replacements are not covered; N_sep remains >11.')

if __name__=='__main__':
    main()
