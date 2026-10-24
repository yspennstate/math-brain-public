from itertools import combinations
from fractions import Fraction

def connected(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(seen)==n

def colorings(n, edges, k):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    order=sorted(range(n), key=lambda v:(-len(adj[v]),v))
    c=[-1]*n
    out=[]
    def bt(i):
        if i==n:
            out.append(tuple(c)); return
        v=order[i]
        used={c[w] for w in adj[v] if c[w]>=0}
        for z in range(k):
            if z not in used:
                c[v]=z
                bt(i+1)
        c[v]=-1
    bt(0)
    return out

def chromatic_number(n, edges, kmax=5):
    for k in range(1,kmax+1):
        if colorings(n,edges,k):
            return k
    return None

def bichromatic_connected(n, edges, c, x, y):
    allowed={c[x],c[y]}
    adj=[[] for _ in range(n)]
    for a,b in edges:
        if c[a] in allowed and c[b] in allowed:
            adj[a].append(b); adj[b].append(a)
    seen={x}; stack=[x]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return y in seen

def cut_size(edges, U):
    U=set(U)
    return sum((a in U) ^ (b in U) for a,b in edges)

def verify_haugland_scaffold():
    # Coordinates represented as a+b*sqrt(3), pair (a,b) for each coordinate.
    # A=(-1,0), B=(0,0), C=(1,0), D=(-1/2,sqrt(3)/2), E=(1/2,sqrt(3)/2)
    pts=[
        ((Fraction(-1),Fraction(0)),(Fraction(0),Fraction(0))),
        ((Fraction(0),Fraction(0)),(Fraction(0),Fraction(0))),
        ((Fraction(1),Fraction(0)),(Fraction(0),Fraction(0))),
        ((Fraction(-1,2),Fraction(0)),(Fraction(0),Fraction(1,2))),
        ((Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(1,2))),
    ]
    def sub(x,y): return (x[0]-y[0],x[1]-y[1])
    def sq(z):
        # (a+b*sqrt3)^2 = (a^2+3b^2) + 2ab sqrt3
        a,b=z
        return (a*a+3*b*b,2*a*b)
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    def dsq(p,q):
        dx=sub(p[0],q[0]); dy=sub(p[1],q[1])
        return add(sq(dx),sq(dy))
    vals={}
    for i,j in combinations(range(5),2):
        vals[(i,j)]=dsq(pts[i],pts[j])
        assert vals[(i,j)][1]==0
    omitted=(0,2)
    constrained={vals[e][0] for e in vals if e!=omitted}
    assert constrained=={Fraction(1),Fraction(3)}
    assert vals[omitted][0]==4
    print("Haugland_5point_scaffold_constrained_squared_distances",sorted(constrained))
    print("Haugland_5point_scaffold_missing_pair_squared_distance",vals[omitted][0])

def verify_regular_hexagon():
    # Exact coordinates using Q(sqrt(3)).
    pts=[
        ((Fraction(1),Fraction(0)),(Fraction(0),Fraction(0))),
        ((Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(1,2))),
        ((Fraction(-1,2),Fraction(0)),(Fraction(0),Fraction(1,2))),
        ((Fraction(-1),Fraction(0)),(Fraction(0),Fraction(0))),
        ((Fraction(-1,2),Fraction(0)),(Fraction(0),Fraction(-1,2))),
        ((Fraction(1,2),Fraction(0)),(Fraction(0),Fraction(-1,2))),
    ]
    def sub(x,y): return (x[0]-y[0],x[1]-y[1])
    def sq(z):
        a,b=z
        return (a*a+3*b*b,2*a*b)
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    def dsq(p,q):
        x=add(sq(sub(p[0],q[0])),sq(sub(p[1],q[1])))
        assert x[1]==0
        return x[0]
    hist={Fraction(1):0,Fraction(3):0,Fraction(4):0}
    for i,j in combinations(range(6),2):
        d=dsq(pts[i],pts[j])
        assert d in hist
        hist[d]+=1
    assert hist=={Fraction(1):6,Fraction(3):6,Fraction(4):3}
    print("regular_hexagon_squared_distance_multiplicities",dict(hist))

def verify_k6_minus_edge():
    n=6
    missing=(0,1)
    edges=[e for e in combinations(range(n),2) if e!=missing]
    cols=colorings(n,edges,5)
    assert cols
    assert all(c[0]==c[1] for c in cols)
    assert sum(0 in e for e in edges)==4
    print("K6_minus_edge_5colorings",len(cols))
    print("K6_minus_edge_forced_pair",missing,"terminal_degree",4)

def main():
    graphs=rainbow_sets=kempe_checks=cut_checks=forced_degree_cases=0
    by_n={}
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        gn=rs=kc=cc=fd=0
        for mask in range(1,1<<len(pairs)):
            edges=[pairs[i] for i in range(len(pairs)) if (mask>>i)&1]
            if not connected(n,edges):
                continue
            chi=chromatic_number(n,edges,4)
            if chi not in (3,4):
                continue
            gn+=1
            cols=colorings(n,edges,chi)

            for S in combinations(range(n),chi):
                if all(len({c[v] for v in S})==chi for c in cols):
                    rs+=1
                    for c in cols:
                        for x,y in combinations(S,2):
                            assert bichromatic_connected(n,edges,c,x,y)
                            kc+=1
                    SS=set(S)
                    for r in range(1,n):
                        for U in combinations(range(n),r):
                            t=len(SS.intersection(U))
                            if 0<t<chi:
                                assert cut_size(edges,U) >= t*(chi-t)
                                cc+=1

            edge_set={tuple(sorted(e)) for e in edges}
            for u,v in combinations(range(n),2):
                if (u,v) in edge_set:
                    continue
                if not all(c[u]==c[v] for c in cols):
                    continue
                for term,partner in ((u,v),(v,u)):
                    if sum(term in e for e in edges) != chi-1:
                        continue
                    verts=[q for q in range(n) if q!=term]
                    idx={q:i for i,q in enumerate(verts)}
                    hedges=[(idx[a],idx[b]) for a,b in edges if term not in (a,b)]
                    hcols=colorings(n-1,hedges,chi)
                    neigh=[q for q in range(n) if q!=term and tuple(sorted((term,q))) in edge_set]
                    S=[idx[q] for q in neigh]+[idx[partner]]
                    assert len(S)==chi and len(set(S))==chi
                    assert all(len({c[s] for s in S})==chi for c in hcols)
                    fd+=1

        by_n[n]=(gn,rs,kc,cc,fd)
        graphs+=gn; rainbow_sets+=rs; kempe_checks+=kc; cut_checks+=cc; forced_degree_cases+=fd

    print("connected_chi3_or4_graphs_checked",graphs)
    print("universal_rainbow_sets_checked",rainbow_sets)
    print("bichromatic_Kempe_connectivity_checks",kempe_checks)
    print("rooted_cut_inequality_checks",cut_checks)
    print("degree_k_minus_1_forced_terminal_cases",forced_degree_cases)
    for n in sorted(by_n):
        print("n",n,"stats",by_n[n])
    verify_k6_minus_edge()
    verify_haugland_scaffold()
    verify_regular_hexagon()
    print("ALL_CHECKS_PASSED")

if __name__=="__main__":
    main()
