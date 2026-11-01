from itertools import combinations
from collections import Counter
from fractions import Fraction


def forest_and_components(n, edges, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1:
            ru,rv=find(u),find(v)
            if ru==rv:
                return False,None
            parent[rv]=ru
    for i in range(n):
        parent[i]=find(i)
    return True,parent


def precompute_R(n,e,f):
    allE=list(combinations(range(n),2))
    H=[x for x in allE if x not in (e,f)]
    m=len(H)
    N=1<<m
    rind=bytearray(N)
    for mask in range(N):
        ok,comp=forest_and_components(n,H,mask)
        if not ok:
            continue
        a,b=e; c,d=f
        ra,rb,rc,rd=comp[a],comp[b],comp[c],comp[d]
        if ra==rb or rc==rd:
            continue
        # Adding e joins exactly the two components containing a,b.
        # Adding f then cycles iff c,d occupy those two components in opposite order.
        if rc in (ra,rb) and rd in (ra,rb) and rc!=rd:
            rind[mask]=1
    return H,rind


def zeta_counts(rind,m):
    arr=list(rind)
    N=1<<m
    for i in range(m):
        bit=1<<i
        for mask in range(N):
            if mask & bit:
                arr[mask]+=arr[mask^bit]
    return arr


def r_subsets(M,rind):
    out=[]
    s=M
    while True:
        if rind[s]: out.append(s)
        if s==0: break
        s=(s-1)&M
    return out


def classify(M,rind):
    R=r_subsets(M,rind)
    mins=[]
    for a in R:
        if not any(b!=a and (b&a)==b for b in R):
            mins.append(a)
    fib={p:[a for a in R if (a&p)==p] for p in mins}
    part=tuple(sorted((len(fib[p]) for p in mins),reverse=True))
    return part,mins,fib,R


def vertices_of_cycle_root(P,H,e,f):
    es=[H[i] for i in range(len(H)) if P>>i&1]+[e,f]
    deg=Counter()
    for u,v in es:
        deg[u]+=1; deg[v]+=1
    assert es and all(d==2 for d in deg.values()), (P,es,deg)
    return set(deg)


def weighted_delta(n, graph_edges, e, f, special_edge=None, special_weight=Fraction(1,1)):
    m=len(graph_edges)
    eidx=graph_edges.index(e); fidx=graph_edges.index(f)
    sidx=graph_edges.index(special_edge) if special_edge is not None else None
    I=Fraction(0); Ie=Fraction(0); If=Fraction(0); Ief=Fraction(0)
    for mask in range(1<<m):
        ok,_=forest_and_components(n,graph_edges,mask)
        if not ok: continue
        w=Fraction(1)
        if sidx is not None and (mask>>sidx)&1:
            w*=special_weight
        I+=w
        if (mask>>eidx)&1: Ie+=w
        if (mask>>fidx)&1: If+=w
        if (mask>>eidx)&1 and (mask>>fidx)&1: Ief+=w
    return Ie*If-I*Ief


def check_pair(n,e,f):
    H,rind=precompute_R(n,e,f)
    m=len(H)
    z=zeta_counts(rind,m)
    part_counts=Counter()
    shape_counts=Counter()
    direct_counts=Counter()
    gap_counts=Counter()
    checked=0
    for M,cnt in enumerate(z):
        if cnt!=8: continue
        part,mins,fib,R=classify(M,rind)
        part_counts[part]+=1
        if part!=(7,1):
            continue
        checked+=1
        P=max(mins,key=lambda p:len(fib[p]))
        Q=min(mins,key=lambda p:len(fib[p]))
        profile=Counter((a & ~P).bit_count() for a in fib[P])
        shape_counts[tuple(sorted(profile.items()))]+=1
        assert profile==Counter({0:1,1:3,2:3}), profile
        atoms=[]
        for a in fib[P]:
            ext=a&~P
            if ext.bit_count()==1:
                atoms.append(ext.bit_length()-1)
        assert len(atoms)==3
        # all three pairs occur, triple does not
        for i,j in combinations(atoms,2):
            assert (P | (1<<i) | (1<<j)) in fib[P]
        assert (P | sum(1<<i for i in atoms)) not in R
        T=[H[i] for i in atoms]
        deg=Counter()
        for u,v in T:
            deg[u]+=1; deg[v]+=1
        ends=[v for v,d in deg.items() if d==1]
        ints=[v for v,d in deg.items() if d==2]
        assert len(ends)==2 and len(ints)==2 and len(deg)==4, (T,deg)
        Cverts=vertices_of_cycle_root(P,H,e,f)
        assert set(ends)<=Cverts, (T,ends,Cverts)
        assert not (set(ints)&Cverts), (T,ints,Cverts)
        # every graph edge with an endpoint outside C_P is one of the three T edges
        Tset={tuple(sorted(x)) for x in T}
        for i,h in enumerate(H):
            if not (M>>i)&1: continue
            if h[0] not in Cverts or h[1] not in Cverts:
                assert h in Tset, (h,T,Cverts)
        # singleton uses all three path edges
        for i in atoms:
            assert (Q>>i)&1, (Q,T)
        u,v=sorted(ends)
        g=(u,v)
        gidx=H.index(g)
        graph=[e,f]+[H[i] for i in range(m) if (M>>i)&1]
        full_gap=weighted_delta(n,graph,e,f)
        assert full_gap.denominator==1 and full_gap>0
        gap_counts[int(full_gap)]+=1
        Tmask=sum(1<<i for i in atoms)
        M0=M & ~Tmask
        if (M>>gidx)&1:
            direct_counts['present']+=1
            # Deleting T leaves exactly the unique root P.
            p0,mins0,fib0,R0=classify(M0,rind)
            assert p0==(1,) and R0==[P] or (p0==(1,) and set(R0)=={P})
            assert (P>>gidx)&1
            # direct edge in parallel with unit length-3 path: D=7,C=8, y_eff=8/7.
            pred=49*weighted_delta(n,[e,f]+[H[i] for i in range(m) if (M0>>i)&1],e,f,g,Fraction(8,7))
            assert pred==full_gap, (pred,full_gap)
            # singleton formula additionally gives 120*2^{|P|-1}.
            closed=120*(2**(P.bit_count()-1))
            assert full_gap==closed,(full_gap,closed,P.bit_count())
        else:
            direct_counts['absent']+=1
            # Suppress T to a new direct edge: exact-two compressed graph.
            MB=M0 | (1<<gidx)
            pB,minsB,fibB,RB=classify(MB,rind)
            assert pB==(1,1), (pB,RB)
            assert len(minsB)==2
            # replacing new unit abstract edge by unit 3-path has D=7,C=1, y_eff=1/7.
            Bgraph=[e,f]+[H[i] for i in range(m) if (MB>>i)&1]
            pred=49*weighted_delta(n,Bgraph,e,f,g,Fraction(1,7))
            assert pred==full_gap,(pred,full_gap)
    return {
        'partition_counts':part_counts,
        'seven_plus_one_checked':checked,
        'seven_fiber_profiles':shape_counts,
        'direct_edge_cases':direct_counts,
        'gap_counts':gap_counts,
    }


def main():
    for n,e,f,label in [
        (6,(0,1),(0,2),'n6_adjacent'),
        (6,(0,1),(2,3),'n6_disjoint'),
        (7,(0,1),(0,2),'n7_adjacent'),
        (7,(0,1),(2,3),'n7_disjoint'),
    ]:
        ans=check_pair(n,e,f)
        print(label)
        for k,v in ans.items():
            print(' ',k,dict(v) if isinstance(v,Counter) else v)

if __name__=='__main__':
    main()
