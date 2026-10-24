#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations

NAMES = ("r","s","d","a","b","t","u","v","w","z")
IDX = {x:i for i,x in enumerate(NAMES)}
COVERS_NAMED = (
    ("r","a"), ("r","b"),
    ("s","t"), ("s","w"),
    ("d","a"), ("d","u"), ("d","v"),
    ("a","w"), ("a","z"),
    ("b","u"), ("b","v"), ("b","w"),
    ("t","u"), ("t","z"),
    ("v","z"),
)
COVERS = tuple((IDX[x],IDX[y]) for x,y in COVERS_NAMED)
N = len(NAMES)

reach = [0]*N
for x,y in COVERS:
    reach[x] |= 1 << y
changed = True
while changed:
    changed = False
    for x in range(N):
        new = reach[x]
        bits = reach[x]
        while bits:
            bit = bits & -bits
            y = bit.bit_length()-1
            new |= reach[y]
            bits -= bit
        if new != reach[x]:
            reach[x] = new
            changed = True
assert all(((reach[i] >> i) & 1) == 0 for i in range(N))

pred = [0]*N
for x in range(N):
    bits = reach[x]
    while bits:
        bit = bits & -bits
        y = bit.bit_length()-1
        pred[y] |= 1 << x
        bits -= bit

extensions = []
def rec(mask, seq):
    if mask == (1<<N)-1:
        extensions.append(tuple(seq))
        return
    for x in range(N):
        if ((mask>>x)&1)==0 and (pred[x] & ~mask)==0:
            rec(mask | (1<<x), seq + [x])
rec(0, [])
E = len(extensions)
assert E == 1919

pair_count = {}
for i,j in combinations(range(N),2):
    if ((reach[i]>>j)&1) or ((reach[j]>>i)&1):
        continue
    c = 0
    for L in extensions:
        pos = {x:k for k,x in enumerate(L)}
        c += pos[i] < pos[j]
    pair_count[(i,j)] = c

def p_before(x,y):
    i,j=IDX[x],IDX[y]
    if (reach[i]>>j)&1:
        return Fraction(1,1)
    if (reach[j]>>i)&1:
        return Fraction(0,1)
    if i<j:
        return Fraction(pair_count[(i,j)], E)
    return 1-Fraction(pair_count[(j,i)], E)

# Width exactly three.
chain_cover = (("d","a","w"), ("s","t","u"), ("r","b","v","z"))
for C in chain_cover:
    for x,y in zip(C,C[1:]):
        assert (reach[IDX[x]] >> IDX[y]) & 1
antichain = ("r","s","d")
for x,y in combinations(antichain,2):
    assert p_before(x,y) not in (Fraction(0,1), Fraction(1,1))
# A 3-chain cover gives width <=3 and this antichain gives width >=3.

# Incomparability graph connected.
adj = [[] for _ in range(N)]
for (i,j) in pair_count:
    adj[i].append(j); adj[j].append(i)
seen={0}; stack=[0]
while stack:
    x=stack.pop()
    for y in adj[x]:
        if y not in seen:
            seen.add(y); stack.append(y)
assert len(seen)==N

# No proper nontrivial autonomous subset.
def relation(z,x):
    if (reach[z]>>x)&1: return -1
    if (reach[x]>>z)&1: return 1
    return 0
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
            ok=False; break
    if ok:
        modules.append(tuple(NAMES[i] for i in A))
assert modules == []

a,b,d,u,v = map(IDX.__getitem__, ("a","b","d","u","v"))
D = pred[a] & ~pred[b]
U = reach[b] & ~reach[a]
assert tuple(NAMES[i] for i in range(N) if (D>>i)&1) == ("d",)
U_names = tuple(NAMES[i] for i in range(N) if (U>>i)&1)
assert U_names == ("u","v")
M=[]
for x in range(N):
    if not ((U>>x)&1):
        continue
    if (pred[x] & U)==0:
        M.append(x)
assert tuple(NAMES[x] for x in M) == ("u","v")

p = p_before("a","b")
qd = p_before("b","d")
qu = p_before("u","a")
qv = p_before("v","a")
assert (p,qd,qu,qv) == (
    Fraction(506,1919),
    Fraction(471,1919),
    Fraction(240,1919),
    Fraction(564,1919),
)
assert all(q < Fraction(1,3) for q in (p,qd,qu,qv))

# Every incomparable pair in the five-point selector block is unbalanced.
local=("d","b","a","u","v")
local_incomp=[]
for x,y in combinations(local,2):
    px=p_before(x,y)
    if px not in (Fraction(0,1),Fraction(1,1)):
        local_incomp.append((x,y,px))
        assert not (Fraction(1,3) <= px <= Fraction(2,3))
assert [(x,y,q) for x,y,q in local_incomp] == [
    ("d","b",Fraction(1448,1919)),
    ("b","a",Fraction(1413,1919)),
    ("a","u",Fraction(1679,1919)),
    ("a","v",Fraction(1355,1919)),
    ("u","v",Fraction(25,101)),
]

# Exact three-channel blocker identity and support-essentiality.
patterns=Counter()
for L in extensions:
    pos={x:k for k,x in enumerate(L)}
    A = pos[IDX["a"]] < pos[IDX["b"]]
    Ed = pos[IDX["b"]] < pos[IDX["d"]]
    Eu = pos[IDX["u"]] < pos[IDX["a"]]
    Ev = pos[IDX["v"]] < pos[IDX["a"]]
    patterns[(A,Ed,Eu,Ev)] += 1

Bminus = sum(c for bits,c in patterns.items() if bits[1] or bits[2] or bits[3])
assert Bminus == 907
assert Fraction(Bminus,E) == 1 - 2*p
unique = {}
for idx,name in ((1,"Ed"),(2,"Eu"),(3,"Ev")):
    unique[name]=sum(c for bits,c in patterns.items()
                     if bits[idx] and not any(bits[j] for j in (1,2,3) if j!=idx))
assert unique == {"Ed":253, "Eu":60, "Ev":276}
assert all(c>0 for c in unique.values())

balanced=[]
for (i,j),c in sorted(pair_count.items()):
    q=Fraction(c,E)
    if Fraction(1,3) <= q <= Fraction(2,3):
        balanced.append((NAMES[i],NAMES[j],q))
assert len(pair_count)==21
assert len(balanced)==7

print("POS3_PRIME_FULL_ARITY3_ADVERSARY")
print("elements", N)
print("extensions", E)
print("width", 3)
print("chain_cover", ";".join("<".join(C) for C in chain_cover))
print("antichain", ",".join(antichain))
print("incomparability_connected", True)
print("proper_nontrivial_autonomous_subsets", len(modules))
print("selector", "a||b", "D={d}", "M={u,v}")
print("minorities", f"a<b={p}", f"b<d={qd}", f"u<a={qu}", f"v<a={qv}")
print("local_unbalanced")
for x,y,q in local_incomp:
    print(f"  {x}<{y} {q} complement={1-q}")
print("blocker_union", Fraction(Bminus,E), "identity_rhs", 1-2*p)
print("unique_blocker_mass", "Ed="+str(Fraction(unique["Ed"],E)),
      "Eu="+str(Fraction(unique["Eu"],E)), "Ev="+str(Fraction(unique["Ev"],E)))
print("pattern_counts")
for bits,c in sorted(patterns.items()):
    print(" ", "".join("1" if z else "0" for z in bits), c)
print("all_incomparable_pair_probabilities")
for (i,j),c in sorted(pair_count.items()):
    q=Fraction(c,E)
    mark="BALANCED" if Fraction(1,3) <= q <= Fraction(2,3) else "UNBALANCED"
    print(f"  {NAMES[i]}<{NAMES[j]} {c}/{E}={q} {mark}")
print("balanced_pair_count", len(balanced))
print("ordinal_padding", "C_s + P + C_t preserves all incomparable-pair probabilities")
print("POS3_PRIME_FULL_ARITY3_ADVERSARY_PASS")
