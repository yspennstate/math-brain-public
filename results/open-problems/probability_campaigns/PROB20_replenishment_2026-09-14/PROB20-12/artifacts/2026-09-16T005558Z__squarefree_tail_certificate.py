#!/usr/bin/env python3
"""Exact certificate for PROB20-12 square-free two-monomial tail, K6 rank (2,2,2).

Pure Python / integer arithmetic. It proves:
  * every square-free degree-11 fibre of size 2 lies in one of five S6 x S3
    unsigned binomial orbits, and all five have a nontrivial gcd, cancelling to
    degrees 7,10,6,6,9 respectively;
  * no square-free degree-12, 13, or 14 target has fibre size 2;
  * the unique degree-15 square-free target has exactly 6336 monomials.

State numbering is lexicographic over balanced colorings of six vertices by 0,1,2.
"""
import itertools, collections
V=tuple(range(6)); C=tuple(range(3))
EDGES=list(itertools.combinations(V,2)); EID={e:i for i,e in enumerate(EDGES)}
FULL=(1<<15)-1
COL=[]; TRIPLE_TO_STATE={}
for col in itertools.product(C,repeat=6):
    if all(col.count(c)==2 for c in C):
        tr=tuple(EID[tuple(v for v in V if col[v]==c)] for c in C)
        TRIPLE_TO_STATE[tr]=len(COL); COL.append(col)
assert len(COL)==90
SINDEX={c:i for i,c in enumerate(COL)}
COMPAT=[]
for ia,a in enumerate(EDGES):
    sa=set(a); arr=[]
    for ib,b in enumerate(EDGES):
        if sa.isdisjoint(b):
            ic=EID[tuple(sorted(set(V)-sa-set(b)))]
            arr.append((ib,ic,TRIPLE_TO_STATE[(ia,ib,ic)]))
    COMPAT.append(tuple(arr))
    assert len(arr)==6
PERMS=list(itertools.permutations(V))
def emap(p,i):
    e=EDGES[i]; return EID[tuple(sorted((p[e[0]],p[e[1]])))]
def maskmap(p,m):
    out=0
    for i in range(15):
        if (m>>i)&1: out |= 1<<emap(p,i)
    return out

def omitted_orbit_reps(k):
    masks={sum(1<<i for i in comb) for comb in itertools.combinations(range(15),k)}
    reps=[]
    while masks:
        m=min(masks); orb={maskmap(p,m) for p in PERMS}
        masks -= orb; reps.append((m,len(orb)))
    return reps

def all_selected_masks(miss):
    return [FULL ^ sum(1<<i for i in comb) for comb in itertools.combinations(range(15),miss)]

def fibres_by_cmask(amask,bmask,store_solutions=False):
    """Enumerate rainbow perfect matchings A->B and group exactly by forced C mask."""
    rows=tuple(i for i in range(15) if (amask>>i)&1)
    if store_solutions: out=collections.defaultdict(list)
    else: out=collections.Counter()
    def rec(rem,bm,cm,states):
        if not rem:
            if store_solutions: out[cm].append(tuple(sorted(states)))
            else: out[cm]+=1
            return
        best=None; optsbest=None
        for i in rem:
            opts=[(b,c,s) for b,c,s in COMPAT[i] if ((bm>>b)&1) and not ((cm>>c)&1)]
            if not opts: return
            if optsbest is None or len(opts)<len(optsbest): best=i; optsbest=opts
        nr=tuple(i for i in rem if i!=best)
        for b,c,s in optsbest:
            rec(nr,bm^(1<<b),cm|(1<<c),states+(s,))
    rec(rows,bmask,0,tuple())
    return out

GROUP=[]
for vp in PERMS:
    for cp in itertools.permutations(C):
        mp=[]
        for col in COL:
            t=[None]*6
            for v in V: t[vp[v]]=cp[col[v]]
            mp.append(SINDEX[tuple(t)])
        GROUP.append(tuple(mp))
assert len(GROUP)==4320

def canon_trade(P,N):
    best=None
    for mp in GROUP:
        a=tuple(sorted(mp[i] for i in P)); b=tuple(sorted(mp[i] for i in N))
        if b<a: a,b=b,a
        z=(a,b)
        if best is None or z<best: best=z
    return best

def orbit_size(P,N):
    seen=set()
    for mp in GROUP:
        a=tuple(sorted(mp[i] for i in P)); b=tuple(sorted(mp[i] for i in N))
        if b<a: a,b=b,a
        seen.add((a,b))
    return len(seen)

reps11=omitted_orbit_reps(4)
assert len(reps11)==9, reps11
B11=all_selected_masks(4)
two11=[]
for miss0,_ in reps11:
    am=FULL^miss0
    for bm in B11:
        fib=fibres_by_cmask(am,bm,store_solutions=True)
        for cm,sols in fib.items():
            if len(sols)==2:
                two11.append((sols[0],sols[1],miss0,bm,cm))
assert len(two11)==76, len(two11)
classes=collections.defaultdict(list)
for item in two11:
    classes[canon_trade(item[0],item[1])].append(item)
assert len(classes)==5, len(classes)
class_data=[]
for ca,items in sorted(classes.items()):
    P,N=ca; common=set(P)&set(N); residual_degree=11-len(common)
    class_data.append((orbit_size(P,N),len(common),residual_degree,P,N,len(items)))
assert [(o,g,d) for o,g,d,_,_,_ in class_data]==[
    (4320,4,7),(2160,1,10),(2160,5,6),(2160,5,6),(720,2,9)
]
union=set()
for _,_,_,P,N,_ in class_data:
    for mp in GROUP:
        a=tuple(sorted(mp[i] for i in P)); b=tuple(sorted(mp[i] for i in N))
        if b<a: a,b=b,a
        union.add((a,b))
assert len(union)==11520
print('degree11 omitted_graph_orbits',len(reps11))
print('degree11 normalized_size2_targets',len(two11))
print('degree11 binomial_orbits',len(class_data))
for k,(o,g,d,P,N,ninst) in enumerate(class_data):
    print('d11_class',k,'orbit',o,'normalized_instances',ninst,'gcd_degree',g,'residual_degree',d)
    print('  P',P)
    print('  N',N)
print('degree11 union_orbit_size',len(union))

for d in (12,13,14):
    miss=15-d
    reps=omitted_orbit_reps(miss)
    Bmasks=all_selected_masks(miss)
    size_hist=collections.Counter(); positive=0; size2=0
    for miss0,_ in reps:
        am=FULL^miss0
        for bm in Bmasks:
            fib=fibres_by_cmask(am,bm,store_solutions=False)
            for cm,k in fib.items():
                positive+=1; size_hist[k]+=1
                if k==2: size2+=1
    assert size2==0, (d,size2)
    print('degree',d,'omitted_graph_orbits',len(reps),'normalized_positive_targets',positive,'size2',size2,'min_positive',min(size_hist) if size_hist else None,'hist',dict(sorted(size_hist.items())))

f15=fibres_by_cmask(FULL,FULL,store_solutions=False)
assert set(f15)=={FULL}
assert f15[FULL]==6336, f15[FULL]
print('degree15 fibre_size',f15[FULL])
print('ALL EXACT CHECKS PASSED')
