#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

NAMES = ("r","x","p","s","y","a","t","q","z")
IDX = {x:i for i,x in enumerate(NAMES)}
COVERS_NAMED = (
    ("r","x"), ("r","s"), ("r","a"),
    ("x","y"),
    ("p","y"), ("p","a"),
    ("s","q"), ("s","z"),
    ("y","t"),
    ("a","t"), ("a","z"),
)
COVERS = tuple((IDX[x],IDX[y]) for x,y in COVERS_NAMED)
N=len(NAMES)

reach=[0]*N
for x,y in COVERS:
    reach[x] |= 1<<y
changed=True
while changed:
    changed=False
    for x in range(N):
        new=reach[x]
        bits=reach[x]
        while bits:
            bit=bits & -bits
            y=bit.bit_length()-1
            new |= reach[y]
            bits -= bit
        if new!=reach[x]:
            reach[x]=new
            changed=True
assert all(((reach[i]>>i)&1)==0 for i in range(N))

pred=[0]*N
for x in range(N):
    bits=reach[x]
    while bits:
        bit=bits & -bits
        y=bit.bit_length()-1
        pred[y] |= 1<<x
        bits -= bit

extensions=[]
def rec(mask, seq):
    if mask==(1<<N)-1:
        extensions.append(tuple(seq))
        return
    for x in range(N):
        if ((mask>>x)&1)==0 and (pred[x] & ~mask)==0:
            rec(mask | (1<<x), seq+[x])
rec(0,[])
E=len(extensions)
assert E==499

def relation(z,x):
    if (reach[z]>>x)&1: return -1
    if (reach[x]>>z)&1: return 1
    return 0

def is_cover(x,y):
    if not ((reach[x]>>y)&1):
        return False
    return not any(k not in (x,y)
                   and ((reach[x]>>k)&1)
                   and ((reach[k]>>y)&1)
                   for k in range(N))

pair_count={}
for i,j in combinations(range(N),2):
    if relation(i,j)!=0:
        continue
    c=0
    for L in extensions:
        pos={v:k for k,v in enumerate(L)}
        c += pos[i] < pos[j]
    pair_count[(i,j)]=c

def p_before(x,y):
    i,j=IDX[x],IDX[y]
    if relation(i,j)==-1: return Fraction(1,1)
    if relation(i,j)==1: return Fraction(0,1)
    if i<j:
        return Fraction(pair_count[(i,j)],E)
    return 1-Fraction(pair_count[(j,i)],E)

# exact width three
chain_cover=(("r","s","q"),("p","a","z"),("x","y","t"))
for C in chain_cover:
    for x,y in zip(C,C[1:]):
        assert (reach[IDX[x]]>>IDX[y])&1
antichain=("x","p","s")
for x,y in combinations(antichain,2):
    assert relation(IDX[x],IDX[y])==0

# connected incomparability graph
adj=[[] for _ in range(N)]
for i,j in pair_count:
    adj[i].append(j); adj[j].append(i)
seen={0}; stack=[0]
while stack:
    x=stack.pop()
    for y in adj[x]:
        if y not in seen:
            seen.add(y); stack.append(y)
assert len(seen)==N

# autonomous-prime
modules=[]
for mask in range(1,1<<N):
    k=mask.bit_count()
    if k<=1 or k==N:
        continue
    A=[i for i in range(N) if (mask>>i)&1]
    ok=True
    for z0 in range(N):
        if (mask>>z0)&1:
            continue
        if len({relation(z0,x) for x in A}) != 1:
            ok=False
            break
    if ok:
        modules.append(tuple(NAMES[i] for i in A))
assert modules==[]

# sharp heavy-cover bridge
x,y,a=map(IDX.__getitem__,("x","y","a"))
assert is_cover(x,y)
assert relation(x,a)==0 and relation(y,a)==0
pxa=p_before("x","a")
pya=p_before("y","a")
assert pxa==Fraction(343,499)
assert pya==Fraction(142,499)
heavy=pxa-pya
assert heavy==Fraction(201,499) > Fraction(1,3)

Dx={z for z in range(N) if z not in (x,a) and relation(z,x)!=relation(z,a)}
Dy={z for z in range(N) if z not in (y,a) and relation(z,y)!=relation(z,a)}
W=(Dx-{y}) | (Dy-{x})
assert tuple(NAMES[z] for z in sorted(W)) == ("p","z")
assert tuple(NAMES[z] for z in sorted(Dx)) == ("p","y","z")
assert tuple(NAMES[z] for z in sorted(Dy)) == ("x","z")

local=("x","y","a","p","z")
local_probs=[]
for u,v in combinations(local,2):
    if relation(IDX[u],IDX[v])==0:
        q=p_before(u,v)
        local_probs.append((u,v,q))
        assert not (Fraction(1,3)<=q<=Fraction(2,3))
assert local_probs==[
    ("x","a",Fraction(343,499)),
    ("x","p",Fraction(126,499)),
    ("x","z",Fraction(470,499)),
    ("y","a",Fraction(142,499)),
    ("y","z",Fraction(374,499)),
]

balanced=[]
for (i,j),c in sorted(pair_count.items()):
    q=Fraction(c,E)
    if Fraction(1,3)<=q<=Fraction(2,3):
        balanced.append((NAMES[i],NAMES[j],q))
assert len(pair_count)==18
assert balanced==[
    ("x","s",Fraction(253,499)),
    ("y","q",Fraction(306,499)),
    ("t","z",Fraction(195,499)),
    ("q","z",Fraction(306,499)),
]

# exact gap event count
gap=0
for L in extensions:
    pos={v:k for k,v in enumerate(L)}
    gap += pos[x] < pos[a] < pos[y]
assert gap==201

print("POS3_HEAVY_COVER_TWO_WITNESS_LOCAL_TRAP")
print("elements",N)
print("extensions",E)
print("width",3)
print("chain_cover",";".join("<".join(C) for C in chain_cover))
print("antichain",",".join(antichain))
print("incomparability_connected",True)
print("proper_nontrivial_autonomous_subsets",len(modules))
print("heavy_cover","x<.y","a||x,y")
print("Pr(x<a)",pxa)
print("Pr(y<a)",pya)
print("Pr(x<a<y)",Fraction(gap,E))
print("external_distinguisher_union",",".join(NAMES[z] for z in sorted(W)))
print("Dx",",".join(NAMES[z] for z in sorted(Dx)))
print("Dy",",".join(NAMES[z] for z in sorted(Dy)))
print("local_incomparable_probabilities")
for u,v,q in local_probs:
    print(f"  {u}<{v} {q} complement={1-q} UNBALANCED")
print("all_incomparable_pair_probabilities")
for (i,j),c in sorted(pair_count.items()):
    q=Fraction(c,E)
    mark="BALANCED" if Fraction(1,3)<=q<=Fraction(2,3) else "UNBALANCED"
    print(f"  {NAMES[i]}<{NAMES[j]} {c}/{E}={q} {mark}")
print("balanced_pair_count",len(balanced))
print("balanced_pairs",";".join(f"{u}<{v}={q}" for u,v,q in balanced))
print("ordinal_padding","C_L + P + C_R preserves all internal incomparable-pair probabilities")
print("POS3_HEAVY_COVER_TWO_WITNESS_LOCAL_TRAP_PASS")
