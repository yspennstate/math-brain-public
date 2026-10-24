"""Exact certificate: indispensable K6 colored-matching generators in degrees 6..10.

For each seed:
  * build the 90 balanced 3-colorings of six vertices;
  * verify equal colored-edge marginals;
  * verify the target is square-free in every color block;
  * exhaust the full A-fibre via the square-free matching lemma;
  * verify the fibre has exactly the two disjoint seed monomials;
  * compute the unsigned S6 x S3 relation orbit.
No floating point arithmetic is used.
"""
import itertools

V=tuple(range(6)); COLORS=tuple(range(3))
EDGES=list(itertools.combinations(V,2)); EID={e:i for i,e in enumerate(EDGES)}

ST=[]; COL=[]; TR=[]
for col in itertools.product(COLORS, repeat=6):
    if all(col.count(c)==2 for c in COLORS):
        x=[0]*45; tr=[]
        for c in COLORS:
            pts=tuple(v for v in V if col[v]==c)
            x[15*c+EID[pts]]=1
            tr.append(EID[pts])
        ST.append(tuple(x)); COL.append(tuple(col)); TR.append(tuple(tr))
assert len(ST)==90
TRIPLE_TO_STATE={tr:i for i,tr in enumerate(TR)}
INDEX={col:i for i,col in enumerate(COL)}

SEEDS={
 6:((2,18,33,53,73,89),(0,8,48,56,64,86),1080),
 7:((15,22,59,66,78,82,84),(24,27,39,72,79,83,87),4320),
 8:((11,19,27,30,34,71,72,89),(7,9,24,35,59,60,70,84),2160),
 9:((10,17,19,27,39,44,56,65,73),(11,13,20,28,34,47,51,66,72),4320),
10:((2,24,27,30,41,46,54,70,72,76),(4,17,22,35,42,50,58,62,65,81),2160),
}

def marginal(P):
    z=[0]*45
    for s in P:
        for k,a in enumerate(ST[s]):
            z[k]+=a
    return tuple(z)

def full_squarefree_fibre(P):
    d=len(P)
    lists=[[TR[s][c] for s in P] for c in COLORS]
    assert all(len(set(L))==d for L in lists)
    A,B,C=lists
    Cset=set(C)
    opts=[]
    for i,a in enumerate(A):
        ea=set(EDGES[a]); row=[]
        for j,b in enumerate(B):
            eb=set(EDGES[b])
            if ea & eb:
                continue
            comp=tuple(sorted(set(V)-ea-eb))
            if len(comp)!=2:
                continue
            ce=EID[comp]
            if ce in Cset:
                row.append((j,ce,TRIPLE_TO_STATE[(a,b,ce)]))
        opts.append(tuple(row))
        assert row

    out=set(); assigned=[None]*d
    def rec(rem, used_b, used_c):
        if not rem:
            out.add(tuple(sorted(assigned)))
            return
        # Exact branching heuristic only; it does not prune any valid solution.
        best=None; choices=None
        for i in rem:
            ch=[o for o in opts[i] if o[0] not in used_b and o[1] not in used_c]
            if not ch:
                return
            if choices is None or len(ch)<len(choices):
                best=i; choices=ch
        nxt=tuple(i for i in rem if i!=best)
        for j,ce,s in choices:
            assigned[best]=s
            rec(nxt, used_b|{j}, used_c|{ce})
    rec(tuple(range(d)), frozenset(), frozenset())
    return out

def state_map(vperm=None,cperm=None):
    if vperm is None: vperm=list(range(6))
    if cperm is None: cperm=list(range(3))
    out=[]
    for col in COL:
        new=[None]*6
        for v in V:
            new[vperm[v]]=cperm[col[v]]
        out.append(INDEX[tuple(new)])
    return tuple(out)

GENS=[]
for a in range(5):
    p=list(range(6)); p[a],p[a+1]=p[a+1],p[a]
    GENS.append(state_map(vperm=p))
for a in range(2):
    p=list(range(3)); p[a],p[a+1]=p[a+1],p[a]
    GENS.append(state_map(cperm=p))

def relkey(P,N):
    a=tuple(sorted(P)); b=tuple(sorted(N))
    return min((a,b),(b,a))

def orbit(P,N):
    seed=relkey(P,N); seen={seed}; stack=[seed]
    while stack:
        p,n=stack.pop()
        for g in GENS:
            k=relkey([g[s] for s in p],[g[s] for s in n])
            if k not in seen:
                seen.add(k); stack.append(k)
    return seen

total=0
for d,(P,N,want_orbit) in SEEDS.items():
    assert len(P)==len(N)==d
    assert set(P).isdisjoint(N)
    assert marginal(P)==marginal(N)
    m=marginal(P)
    for c in COLORS:
        block=m[15*c:15*(c+1)]
        assert sum(block)==d and set(block)<= {0,1}
    fib=full_squarefree_fibre(P)
    assert fib=={tuple(sorted(P)),tuple(sorted(N))}
    orb=orbit(P,N)
    assert len(orb)==want_orbit
    total+=len(orb)
    print("degree",d,
          "fibre_size",len(fib),
          "orbit_size",len(orb),
          "P",P,
          "N",N)
assert total==14040
print("certified_degree_6_to_10_orbit_total",total)
print("ALL EXACT CHECKS PASSED")
