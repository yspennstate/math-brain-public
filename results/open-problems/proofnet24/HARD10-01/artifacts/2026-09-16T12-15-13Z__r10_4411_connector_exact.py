#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

def norm(e): return tuple(sorted(e))

def comps(n, edges, mask):
    p=list(range(n)); r=[0]*n
    def f(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(a,b) in enumerate(edges):
        if not ((mask>>i)&1): continue
        a,b=f(a),f(b)
        if a==b: return None
        if r[a]<r[b]: a,b=b,a
        p[b]=a
        if r[a]==r[b]: r[a]+=1
    return [f(i) for i in range(n)]

def fixed_R(n,e,f):
    e,f=norm(e),norm(f)
    H=[g for g in combinations(range(n),2) if g not in (e,f)]
    N=1<<len(H)
    R=bytearray(N); root=bytearray(N)
    a,b=e; c,d=f
    for m in range(N):
        C=comps(n,H,m)
        if C is None: continue
        ra,rb,rc,rd=C[a],C[b],C[c],C[d]
        if ra!=rb and rc!=rd and {ra,rb}=={rc,rd}: R[m]=1
    for m in range(N):
        if not R[m]: continue
        x=m
        while x:
            bit=x&-x
            if R[m^bit]: break
            x-=bit
        else:
            root[m]=1
    cnt=list(R)
    for i in range(len(H)):
        bit=1<<i
        for m in range(N):
            if m&bit: cnt[m]+=cnt[m^bit]
    return H,R,root,cnt

def contained_partition(M,rlist,roots):
    rs=[a for a in rlist if not(a&~M)]
    ro=[p for p in roots if not(p&~M)]
    fs=tuple(sorted((sum(1 for a in rs if not(p&~a)) for p in ro),reverse=True))
    return fs,rs,ro

def bit_edge(H,b): return H[b.bit_length()-1]
def edges_of(H,m): return {H[i] for i in range(len(H)) if (m>>i)&1}

def star_info(H,P,F):
    atoms=[]
    for A in F:
        d=A^P
        if d and not(d&(d-1)): atoms.append(d)
    if len(F)!=4 or len(atoms)!=3: return None
    E=[bit_edge(H,b) for b in atoms]
    common=set(E[0])&set(E[1])&set(E[2])
    if len(common)!=1: return None
    w=next(iter(common))
    ats=[]
    for a,b in E: ats.append(b if a==w else a)
    return w,tuple(sorted(ats))

def cell_counts(n, full_edges, e, f):
    E=list(map(norm,full_edges)); e=norm(e); f=norm(f)
    ie=E.index(e); jf=E.index(f)
    A=B=C=D=0
    for m in range(1<<len(E)):
        if comps(n,E,m) is None: continue
        be=(m>>ie)&1; bf=(m>>jf)&1
        if be and bf: D+=1
        elif be: B+=1
        elif bf: C+=1
        else: A+=1
    return A,B,C,D,B*C-A*D

def weighted_gap_coeffs(n, full_edges, e, f, marked):
    # Return polynomial coefficients indexed by exponents of marked edges.
    E=list(map(norm,full_edges)); e=norm(e); f=norm(f)
    marked=[norm(x) for x in marked]
    pos=[E.index(x) for x in marked]
    ie=E.index(e); jf=E.index(f)
    cells=[defaultdict(int) for _ in range(4)]
    for m in range(1<<len(E)):
        if comps(n,E,m) is None: continue
        ex=tuple((m>>j)&1 for j in pos)
        be=(m>>ie)&1; bf=(m>>jf)&1
        idx=3 if (be and bf) else 1 if be else 2 if bf else 0
        cells[idx][ex]+=1
    def mul(P,Q):
        R=defaultdict(int)
        for a,ca in P.items():
            for b,cb in Q.items():
                R[tuple(x+y for x,y in zip(a,b))]+=ca*cb
        return R
    BC=mul(cells[1],cells[2]); AD=mul(cells[0],cells[3])
    keys=set(BC)|set(AD)
    return {k:BC.get(k,0)-AD.get(k,0) for k in sorted(keys)
            if BC.get(k,0)-AD.get(k,0)}

def two_terminal_counts(n, edges, s, t):
    D=C=0
    for m in range(1<<len(edges)):
        cc=comps(n,edges,m)
        if cc is None: continue
        if cc[s]==cc[t]: C+=1
        else: D+=1
    return D,C

def scan_4411(n,e,f):
    H,R,root,cnt=fixed_R(n,e,f)
    rlist=[m for m,x in enumerate(R) if x]
    roots=[m for m,x in enumerate(root) if x]
    stats=Counter()
    failures=[]
    total=0
    for M,v in enumerate(cnt):
        if v!=10: continue
        part,rs,ro=contained_partition(M,rlist,roots)
        if part!=(4,4,1,1): continue
        total+=1
        fib={p:[A for A in rs if not(p&~A)] for p in ro}
        L=[p for p in ro if len(fib[p])==4]
        S=[p for p in ro if len(fib[p])==1]
        infos=[star_info(H,p,fib[p]) for p in L]
        if not all(infos):
            failures.append(("nonstar",M)); continue
        (w,A),(x,B)=infos
        full=edges_of(H,M)|{norm(e),norm(f)}
        if w==x:
            pairs=[]
            for s in S:
                cyc=edges_of(H,s)|{norm(e),norm(f)}
                pairs.append(tuple(sorted(a for a in A if norm((w,a)) in cyc)))
            stats[("same-center","same-pair" if pairs[0]==pairs[1] else "distinct-pairs")]+=1
            continue
        P,Q=L
        CP=edges_of(H,P)|{norm(e),norm(f)}
        CQ=edges_of(H,Q)|{norm(e),norm(f)}
        tA={a for a in A if norm((w,a)) in CQ}
        tB={b for b in B if norm((x,b)) in CP}
        connector=norm((w,x)) in full
        if connector:
            usage=[]
            for s in S:
                cyc=edges_of(H,s)|{norm(e),norm(f)}
                usage.append(norm((w,x)) in cyc)
            stats[("distinct","connector",len(tA&tB))]+=1
            if usage != [True,True] or len(tA&tB) not in (1,2):
                failures.append(("connector-structure",M,tA,tB,usage))
        else:
            ua=set(A)-tA; ub=set(B)-tB
            stats[("distinct","no-connector",len(tA&tB))]+=1
            if len(tA&tB)!=1 or len(tA|tB)!=3 or len(ua)!=1 or len(ub)!=1 or ua!=ub:
                failures.append(("no-connector-structure",M,tA,tB,ua,ub))
            else:
                z=next(iter(ua))
                if z in tA|tB:
                    failures.append(("third-not-fourth",M,z,tA,tB))
    return total,stats,failures

def main():
    # Five canonical n=6 cores (e=01, f=23), taken up to relabeling.
    cores = {
      "same_distinct_124": [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4)],
      "same_same_264": [(0,1),(0,4),(0,5),(1,2),(1,3),(1,5),(2,3),(2,4),(3,4),(4,5)],
      "distinct_no_connector_280": [(0,1),(0,2),(0,3),(0,4),(0,5),(1,4),(1,5),(2,3),(2,5),(3,4)],
      "distinct_connector_equal_480": [(0,1),(0,4),(0,5),(1,3),(2,3),(2,4),(2,5),(4,5)],
      "distinct_connector_shared_288": [(0,1),(0,3),(0,5),(1,3),(1,4),(2,3),(2,4),(2,5),(4,5)],
    }
    expected={
      "same_distinct_124":124, "same_same_264":264,
      "distinct_no_connector_280":280,
      "distinct_connector_equal_480":480,
      "distinct_connector_shared_288":288,
    }
    print("canonical core cell counts / gaps")
    for name,E in cores.items():
        vals=cell_counts(6,E,(0,1),(2,3))
        print(name, vals)
        assert vals[-1]==expected[name]

    # Marked connector polynomial for the shared-endpoint connector core.
    # variable t is edge 45; coefficient dict exponent -> coeff.
    c=weighted_gap_coeffs(6,cores["distinct_connector_shared_288"],(0,1),(2,3),[(4,5)])
    print("shared-endpoint connector polynomial coeffs",c)
    # 18(2 t^2 + 7 t + 7)
    assert c == {(0,):126,(1,):126,(2,):36}

    # No-connector core: p=edge04, q=edge05.
    c2=weighted_gap_coeffs(6,cores["distinct_no_connector_280"],(0,1),(2,3),[(0,4),(0,5)])
    print("no-connector two-spoke polynomial coeffs",c2)
    # 2(12 p^2 - 9pq +31p +12q^2 +31q +63)
    assert c2 == {(0,0):126,(0,1):62,(0,2):24,(1,0):62,(1,1):-18,(2,0):24}

    # Equal-endpoint connector gadget N = K4 - uv, terminals u=0,v=1.
    N=[(0,2),(2,1),(0,3),(3,1),(2,3)]
    print("equal-endpoint connector gadget (D,C)", two_terminal_counts(4,N,0,1))
    assert two_terminal_counts(4,N,0,1)==(14,10)

    cases=[
      ("n6_adj",6,(0,1),(0,2)),
      ("n6_dis",6,(0,1),(2,3)),
      ("n7_adj",7,(0,1),(0,2)),
      ("n7_dis",7,(0,1),(2,3)),
    ]
    for name,n,e,f in cases:
        total,stats,fail=scan_4411(n,e,f)
        print(name,"total",total,"regimes",dict(stats),"failures",len(fail))
        assert not fail
    print("All tested connector examples use the connector in both singleton cycles.")
    print("All tested no-connector distinct-center examples have one shared traversed endpoint")
    print("and a common third attachment equal to the fourth compressed K4 branch vertex.")
    print("OK")

if __name__=="__main__":
    main()
