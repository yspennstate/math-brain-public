from fractions import Fraction as F
from itertools import combinations
from collections import Counter

names=['O']+[f'i{k}' for k in range(6)]+['h0','h1']+[f'a{k}' for k in range(1,6)]
idx={v:i for i,v in enumerate(names)}
# Coordinate representation (x, y0) means (x, y0*sqrt(3)).
coord={
'O':(F(0),F(0)), 'i0':(F(1,2),F(1,6)), 'i1':(F(0),F(1,3)),
'i2':(F(-1,2),F(1,6)), 'i3':(F(-1,2),F(-1,6)), 'i4':(F(0),F(-1,3)),
'i5':(F(1,2),F(-1,6)), 'h0':(F(1),F(0)), 'h1':(F(1,2),F(1,2)),
'a1':(F(1),F(1,3)), 'a2':(F(1),F(2,3)), 'a3':(F(1,2),F(5,6)),
'a4':(F(3,2),F(1,6)), 'a5':(F(3,2),F(-1,6)),
}
def edge(a,b):
    return tuple(sorted((idx[a],idx[b])))
def d2(a,b):
    xa,ya=coord[a]; xb,yb=coord[b]
    return (xa-xb)**2 + 3*(ya-yb)**2

bydist={F(1,3):set(),F(1):set(),F(4):set()}
other=[]
for a,b in combinations(names,2):
    q=d2(a,b)
    if q in bydist: bydist[q].add(edge(a,b))
    else: other.append((a,b,q))
assert [len(bydist[F(1,3)]),len(bydist[F(1)]),len(bydist[F(4)])]==[27,18,5]
# Scale all coordinates by sqrt(3). Then these become squared distances 1,3,12.
unit=set(bydist[F(1,3)])
candidates=sorted(bydist[F(1)]|bydist[F(4)])
ctype={e:('sqrt3' if e in bydist[F(1)] else '2sqrt3') for e in candidates}

n=len(names)
adj=[0]*n
for a,b in unit:
    adj[a]|=1<<b; adj[b]|=1<<a
deg=[adj[i].bit_count() for i in range(n)]
order=sorted(range(n), key=lambda i:(-deg[i],i))
color=[-1]*n
masks=[]
colorings=[]

def rec(pos,maxc):
    if pos==n:
        m=0
        for j,(a,b) in enumerate(candidates):
            if color[a]==color[b]: m|=1<<j
        masks.append(m); colorings.append(tuple(color)); return
    v=order[pos]
    # Restricted-growth normalization removes color permutations.
    for c in range(min(maxc+1,4)+1):
        if c>maxc+1: continue
        if any(color[u]==c and ((adj[v]>>u)&1) for u in range(n)):
            continue
        color[v]=c; rec(pos+1,max(maxc,c)); color[v]=-1

color[order[0]]=0
rec(1,0)
assert len(masks)==50261
uniq=sorted(set(masks), key=lambda m:(m.bit_count(),m))
mins=[]
for m in uniq:
    if not any((a&m)==a for a in mins): mins.append(m)
assert len(mins)==19 and Counter(m.bit_count() for m in mins)==Counter({1:18,2:1})
mandatory=[]; twomask=None
for m in mins:
    bits=[j for j in range(len(candidates)) if (m>>j)&1]
    if len(bits)==1: mandatory.append(bits[0])
    else: twomask=bits
assert len(mandatory)==18 and len(twomask)==2
assert Counter(ctype[candidates[j]] for j in mandatory)==Counter({'sqrt3':13,'2sqrt3':5})
assert all(ctype[candidates[j]]=='sqrt3' for j in twomask)

# Both minimum completions are 19-edge candidate sets and kill every normalized 5-coloring.
completions=[]
for q in twomask:
    S=set(mandatory+[q]); completions.append(S)
    Smask=sum(1<<j for j in S)
    assert all(m & Smask for m in masks)
    assert len(S)==19

# No <=18 candidate-edge completion can work: 18 singleton masks force all mandatory edges,
# and the remaining size budget leaves no room to hit the independent 2-mask constraint.
# More strongly, exact structure of every minimum completion is mandatory + exactly one of twomask.

def classes(c):
    out=[]
    for k in range(5):
        cls=[names[i] for i,x in enumerate(c) if x==k]
        if cls: out.append(tuple(cls))
    return out
witness={}
for m in mins:
    k=next(i for i,x in enumerate(masks) if x==m)
    witness[m]=classes(colorings[k])

# Choose completion using a2-a4 when possible (it preserves the A-subgraph used in G14's human proof).
def label(j):
    a,b=candidates[j]
    return f'{names[a]}--{names[b]}[{ctype[candidates[j]]}]'
choice=next(j for j in twomask if set((names[candidates[j][0]],names[candidates[j][1]]))==set(('a2','a4')))
S=set(mandatory+[choice])
E=unit|{candidates[j] for j in S}
assert len(E)==46
# Exact independence number by brute force.
def independent(sub):
    st=set(sub)
    return all(not (a in st and b in st) for a,b in E)
a=0; ex=None
for r in range(n+1):
    anyr=False
    for C in combinations(range(n),r):
        if independent(C): a=r; ex=C; anyr=True
    if not anyr: break
assert a==3
# Poor vertices i0,a1 lie in no independent triple and are adjacent (unit after scaling).
for vname in ('i0','a1'):
    v=idx[vname]
    assert not any(v in C and independent(C) for C in combinations(range(n),3))
assert edge('i0','a1') in E
# Hence no 5-coloring: alpha<=3 gives class sizes 3,3,3,3,2; both poor adjacent vertices must be in unique <=2 class.
# Verify explicit 6-coloring from G14 remains valid.
six=[('i0','i3'),('a1','O'),('i1','h0','a2'),('i5','a3','i2'),('a5','h1','i4'),('a4',)]
for cls in six:
    ids=[idx[x] for x in cls]
    assert independent(ids)
assert sorted(x for cls in six for x in cls)==sorted(names)

print('G14_SCALED_EXACT_DISTANCE_COUNTS unit=27 sqrt3=18 2sqrt3=5')
print('UNIT_BASE_NORMALIZED_5_COLORINGS',len(masks))
print('DISTINCT_VIOLATION_MASKS',len(uniq))
print('INCLUSION_MINIMAL_MASKS',len(mins),'sizes',dict(Counter(m.bit_count() for m in mins)))
print('MANDATORY_NONUNIT_EDGES',len(mandatory))
for j in mandatory: print('  M',label(j))
print('EITHER_ONE_OF')
for j in twomask: print('  A',label(j))
print('MINIMUM_NONUNIT_EDGE_COUNT 19')
for t,S0 in enumerate(completions,1):
    print('COMPLETION',t,'sqrt3',sum(ctype[candidates[j]]=='sqrt3' for j in S0),'2sqrt3',sum(ctype[candidates[j]]=='2sqrt3' for j in S0))
print('CHOSEN_COMPLETION_EDGES_TOTAL',len(E),'ALPHA',a,'EXAMPLE_MAX_INDEPENDENT',tuple(names[i] for i in ex))
print('CHOSEN_COMPLETION_6_COLORING',six)
print('MINIMAL_MASK_WITNESSES')
for m in mins:
    bits=[j for j in range(len(candidates)) if (m>>j)&1]
    print(' ',[label(j) for j in bits],':',witness[m])
print('ALL_CHECKS_PASSED')
