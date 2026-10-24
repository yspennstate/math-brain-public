#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-16 04Z checkpoint.

Finite enumeration is adversarial self-checking only, except the fixed five-vertex
core calculation, which is an exact exhaustive certificate for that finite core.

Checks representative adjacent/disjoint distinguished pairs through n=7 for:
  * the final |R|=8 partition 5+1+1+1;
  * P4 singleton-pair geometry and direct-edge pattern;
  * compression of the missing middle pair to an exact-two R graph;
  * exact K4 exchange matching and decorated K5-minus-edge confinement;
  * exact factorization Delta = 148 * alpha_1 * alpha_2;
  * reconnaissance for |R|=9 partitions.
"""
from collections import Counter, defaultdict
from itertools import combinations


def norm(e): return tuple(sorted(e))


def forest_components(n, edges, mask):
    parent=list(range(n)); rank=[0]*n
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,(a,b) in enumerate(edges):
        if not ((mask>>i)&1): continue
        a,b=find(a),find(b)
        if a==b: return None
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
    for i in range(n): parent[i]=find(i)
    return parent


def fixed_R_arrays(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H)
    r=bytearray(N)
    a,b=e; c,d=f
    for mask in range(N):
        comp=forest_components(n,H,mask)
        if comp is None: continue
        ra,rb,rc,rd=comp[a],comp[b],comp[c],comp[d]
        if ra==rb or rc==rd: continue
        if rc in (ra,rb) and rd in (ra,rb) and rc!=rd:
            r[mask]=1
    root=bytearray(N)
    for mask in range(N):
        if not r[mask]: continue
        x=mask; mini=True
        while x:
            bit=x&-x
            if r[mask^bit]:
                mini=False; break
            x-=bit
        if mini: root[mask]=1
    counts=list(r)
    for i in range(len(H)):
        bit=1<<i
        for mask in range(N):
            if mask&bit:
                counts[mask]+=counts[mask^bit]
    return H,r,root,counts


def edge_set(H,m):
    return {H[i] for i in range(len(H)) if (m>>i)&1}


def root_fibers(Rs,roots):
    return {P:[A for A in Rs if (P&~A)==0] for P in roots}


def classify(M,r_masks,root_masks):
    Rs=[A for A in r_masks if (A&~M)==0]
    roots=[P for P in root_masks if (P&~M)==0]
    fib=root_fibers(Rs,roots)
    return tuple(sorted((len(v) for v in fib.values()),reverse=True)),Rs,roots,fib


def extension_single_edges(H,P,fiber):
    out=[]
    for A in fiber:
        if A==P: continue
        d=A^P
        if d.bit_count()!=1: return None
        out.append(H[(d&-d).bit_length()-1])
    return out


def direct_delta(n,E,e,f):
    E=sorted(set(map(norm,E))); e,f=norm(e),norm(f)
    ie,jf=E.index(e),E.index(f)
    A=B=C=D=0
    for m in range(1<<len(E)):
        if forest_components(n,E,m) is None: continue
        he=(m>>ie)&1; hf=(m>>jf)&1
        if not he and not hf: A+=1
        elif he and not hf: B+=1
        elif hf and not he: C+=1
        else: D+=1
    return B*C-A*D,(A,B,C,D)


def alpha_terminal(n,edges,q,s,t):
    edges=sorted(set(map(norm,edges))); q=norm(q)
    iq=edges.index(q)
    D=C=Dq=Cq=0
    for m in range(1<<len(edges)):
        comp=forest_components(n,edges,m)
        if comp is None: continue
        conn=comp[s]==comp[t]
        hasq=(m>>iq)&1
        if conn:
            C+=1
            if hasq: Cq+=1
        else:
            D+=1
            if hasq: Dq+=1
    return D*Cq-C*Dq


def path_components(n,edges):
    adj=defaultdict(list); verts=set()
    for u,v in edges:
        adj[u].append(v); adj[v].append(u); verts|={u,v}
    seen=set(); out=[]
    for v in verts:
        if v in seen: continue
        st=[v]; seen.add(v); comp=set()
        while st:
            x=st.pop(); comp.add(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); st.append(y)
        out.append(comp)
    return out


def core_certificate():
    # K5 - {bc}; distinguished abstract edges ac and bd.
    a,b,c,d,w=0,1,2,3,4
    E=set(combinations(range(5),2))-{norm((b,c))}
    e=norm((a,c)); f=norm((b,d))
    edges=sorted(E); ie=edges.index(e); jf=edges.index(f)
    cells={k:Counter() for k in "ABCD"}
    for m in range(1<<len(edges)):
        if forest_components(5,edges,m) is None: continue
        he=(m>>ie)&1; hf=(m>>jf)&1
        key="D" if he and hf else "B" if he else "C" if hf else "A"
        cells[key][m.bit_count()]+=1
    totals={k:sum(v.values()) for k,v in cells.items()}
    assert totals=={"A":82,"B":46,"C":46,"D":24}
    assert totals["B"]*totals["C"]-totals["A"]*totals["D"]==148
    return cells,totals


def check_pair(n,e,f):
    H,r,root,counts=fixed_R_arrays(n,e,f)
    r_masks=[m for m,x in enumerate(r) if x]
    root_masks=[m for m,x in enumerate(root) if x]
    count5111=0
    factor=Counter()
    r9=Counter()
    for M,total in enumerate(counts):
        if total==9:
            part,_,_,_=classify(M,r_masks,root_masks)
            r9[part]+=1
        if total!=8: continue
        part,Rs,roots,fib=classify(M,r_masks,root_masks)
        if part!=(5,1,1,1): continue
        count5111+=1
        E=edge_set(H,M)|{norm(e),norm(f)}
        P=next(P for P in roots if len(fib[P])==5)
        atoms=extension_single_edges(H,P,fib[P])
        assert atoms is not None and len(atoms)==4
        common=set(atoms[0])
        for at in atoms[1:]: common&=set(at)
        assert len(common)==1
        w=next(iter(common))
        attach={at:next(v for v in at if v!=w) for at in atoms}

        qpair={}
        pairs=[]
        for Q in roots:
            if len(fib[Q])!=1: continue
            Qe=edge_set(H,Q)
            p=tuple(sorted(attach[a] for a in atoms if a in Qe))
            assert len(p)==2
            pairs.append(p); qpair[p]=Q
        assert len(set(pairs))==3

        deg=Counter()
        for x,y in pairs:
            deg[x]+=1; deg[y]+=1
        assert sorted(deg.values())==[1,1,2,2]  # P4

        mid=next(p for p in pairs if deg[p[0]]==2 and deg[p[1]]==2)
        b,c=mid
        endpairs=[p for p in pairs if p!=mid]
        a=next(y if x==b else x for x,y in endpairs if b in (x,y))
        d=next(y if x==c else x for x,y in endpairs if c in (x,y))
        ab=norm((a,b)); bc=norm((b,c)); cd=norm((c,d)); ad=norm((a,d))

        assert ab in E and cd in E and bc not in E
        Pe=edge_set(H,P)
        assert ab in Pe and cd in Pe

        Qm=qpair[tuple(sorted(mid))]
        Qme=edge_set(H,Qm)
        assert ab not in Qme and cd not in Qme

        # Compress the missing middle ear to bc.
        MB=M
        for at in atoms:
            MB &= ~(1<<H.index(at))
        MB |= 1<<H.index(bc)
        partB,RsB,rootsB,_=classify(MB,r_masks,root_masks)
        assert partB==(1,1) and len(RsB)==len(rootsB)==2

        Qp=next(Q for Q in rootsB if bc in edge_set(H,Q))
        Pp=next(Q for Q in rootsB if bc not in edge_set(H,Q))
        assert Pp==P
        dP=edge_set(H,Pp)-edge_set(H,Qp)
        dQ=edge_set(H,Qp)-edge_set(H,Pp)
        assert dP=={ab,cd}
        assert dQ=={bc,ad}
        assert ad in E

        # Exact-two K4 leaves the complementary matching ac,bd as the
        # distinguished two-terminal branches. Recover their vertex supports
        # from the principal cycle after deleting the P-exchange edges.
        cycle_edges=(Pe|{norm(e),norm(f)})-{ab,cd}
        comps=path_components(n,cycle_edges)
        assert len(comps)==2
        assert {frozenset(S & {a,b,c,d}) for S in comps} == {
            frozenset((a,c)), frozenset((b,d))
        }
        assert sum(set(e)<=S for S in comps)==1
        assert sum(set(f)<=S for S in comps)==1
        assert not any(set(e)<=S and set(f)<=S for S in comps)

        # Full G is decorated K5-bc: aside from the four spokes and
        # literal exchange edges ab,cd,ad, every edge is branch-local.
        spokes=set(atoms)
        literals={ab,cd,ad}
        for ed in E:
            if ed in spokes or ed in literals: continue
            assert any(set(ed)<=S for S in comps), (ed,E,comps)

        alphas=[]
        for S in comps:
            KE={ed for ed in E if set(ed)<=S}
            q=norm(e) if set(e)<=S else norm(f)
            terminals=tuple(S & {a,b,c,d})
            assert len(terminals)==2
            alphas.append(alpha_terminal(n,KE,q,*terminals))
        gap,_=direct_delta(n,E,e,f)
        assert gap==148*alphas[0]*alphas[1]
        factor[(alphas[0],alphas[1],gap)]+=1
    return count5111,factor,r9


def main():
    cells,totals=core_certificate()
    print("bare_core_cell_size_distributions",
          {k:dict(sorted(v.items())) for k,v in cells.items()})
    print("bare_core_totals",totals,"gap",148)
    configs=[
        (6,(0,1),(0,2),"n6_adjacent"),
        (6,(0,1),(2,3),"n6_disjoint"),
        (7,(0,1),(0,2),"n7_adjacent"),
        (7,(0,1),(2,3),"n7_disjoint"),
    ]
    for n,e,f,label in configs:
        c,factor,r9=check_pair(n,e,f)
        print(label)
        print(" 5+1+1+1_count",c)
        print(" factor_triples",dict(factor))
        print(" R9_partitions",dict(r9))


if __name__=="__main__":
    main()
