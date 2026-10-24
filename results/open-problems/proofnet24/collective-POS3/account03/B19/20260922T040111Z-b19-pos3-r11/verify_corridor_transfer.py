#!/usr/bin/env python3
from itertools import combinations

N = 12
COVERS = [
    (0,1),(0,10),(1,2),(1,5),(2,3),(3,6),(3,11),
    (4,5),(4,11),(5,6),(6,7),(8,1),(8,9),(9,2),
    (9,10),(10,3),(10,5)
]
MAJORITY_ORDER = [8,0,9,4,1,10,2,5,3,6,11,7]
CORRIDORS = [
    # x,y,d,u, N(x<y), six word counts A,C,X,Y,Z,W
    (10,2,1,5,568,(265,265,90,159,54,0)),
    (1,10,9,2,620,(213,213,159,142,106,0)),
    (9,1,0,10,585,(248,248,142,124,71,0)),
    (0,9,8,1,638,(195,195,124,195,124,0)),
]

succ = [set() for _ in range(N)]
for a,b in COVERS:
    succ[a].add(b)
for k in range(N):
    for i in range(N):
        if k in succ[i]:
            succ[i] |= succ[k]
pred = [set() for _ in range(N)]
for i in range(N):
    for j in succ[i]:
        pred[j].add(i)

def comparable(a,b):
    return b in succ[a] or a in succ[b]

extensions = []
def rec(prefix, remaining):
    if not remaining:
        extensions.append(tuple(prefix))
        return
    avail = [v for v in sorted(remaining) if not (pred[v] & remaining)]
    for v in avail:
        rec(prefix+[v], remaining-{v})
rec([], set(range(N)))
E = len(extensions)
assert E == 833, E
positions = [{v:i for i,v in enumerate(L)} for L in extensions]

def count_before(a,b):
    return sum(1 for pos in positions if pos[a] < pos[b])

width = 0
witness = None
verts = range(N)
for r in range(1,N+1):
    found = False
    for S in combinations(verts,r):
        if all(not comparable(a,b) for a,b in combinations(S,2)):
            width = r
            witness = S
            found = True
            break
    if not found:
        break
assert width == 3, (width,witness)

rank = {v:i for i,v in enumerate(MAJORITY_ORDER)}
for a,b in combinations(range(N),2):
    if b in succ[a]:
        assert rank[a] < rank[b]
    elif a in succ[b]:
        assert rank[b] < rank[a]
    else:
        c = count_before(a,b)
        if c > E/2:
            assert rank[a] < rank[b], (a,b,c)
        else:
            assert rank[b] < rank[a], (a,b,c)

balanced = []
for a,b in combinations(range(N),2):
    if comparable(a,b):
        continue
    c = count_before(a,b)
    if E <= 3*c <= 2*E:
        balanced.append((a,b,c))
assert balanced == [(0,8,319),(1,4,377),(3,5,416),(4,9,352),(6,11,486)], balanced

def six_words(x,y,d,u):
    # Account02/B10 convention with a=y, b=x, so A is the minority event y<x:
    # A=d y x u, C=d x y u, X=d x u y,
    # Y=x d y u, Z=x d u y, W=x u d y.
    patterns = [
        (d,y,x,u),(d,x,y,u),(d,x,u,y),
        (x,d,y,u),(x,d,u,y),(x,u,d,y)
    ]
    out = []
    for pat in patterns:
        out.append(sum(1 for pos in positions
                       if all(pos[pat[i]] < pos[pat[i+1]] for i in range(3))))
    return tuple(out)

As = []
Ks = []
for idx,(x,y,d,u,nxy,expected_words) in enumerate(CORRIDORS):
    assert pred[y] - pred[x] == {d}, (idx,pred[y]-pred[x])
    assert pred[x] <= pred[y]
    assert succ[x] - succ[y] == {u}, (idx,succ[x]-succ[y])
    assert succ[y] <= succ[x]
    assert not comparable(x,y)
    assert not comparable(x,d)
    assert not comparable(y,u)
    assert d in pred[y]
    assert u in succ[x]

    got_nxy = count_before(x,y)
    assert got_nxy == nxy, (idx,got_nxy,nxy)
    assert 3*got_nxy > 2*E
    assert rank[d] < rank[x] < rank[y] < rank[u], (idx,d,x,y,u)

    words = six_words(x,y,d,u)
    assert words == expected_words, (idx,words,expected_words)
    A,C,X,Y,Z,W = words
    assert A == C
    assert W == 0
    assert A == E - got_nxy
    As.append(A)
    Ks.append(A+Z)

print("extensions", E)
print("width", width, "antichain_witness", witness)
print("majority_order", *MAJORITY_ORDER)
print("balanced_pairs", " ".join(f"{a},{b}:{c}/{E}" for a,b,c in balanced))
for i,(x,y,d,u,nxy,_) in enumerate(CORRIDORS):
    A,C,X,Y,Z,W = six_words(x,y,d,u)
    print("corridor", i, "x", x, "y", y, "d", d, "u", u,
          "Nxy", nxy, "fraction", f"{nxy}/{E}",
          "words", A,C,X,Y,Z,W, "K", A+Z)

for i in range(len(CORRIDORS)-1):
    A,C,X,Y,Z,W = six_words(*CORRIDORS[i][:4])
    A2,C2,X2,Y2,Z2,W2 = six_words(*CORRIDORS[i+1][:4])
    predicted = (Y+Z, Y, A+X-Y-Z, A-Y)
    observed = (A2,X2,Y2,Z2)
    assert observed == predicted, (i,observed,predicted)
    assert A+Z == A2+Z2
    print("transfer", i, "to", i+1, "observed", *observed, "predicted", *predicted)

assert len(set(Ks)) == 1
K = Ks[0]
print("invariant_K", K)

for i in range(1,len(As)-1):
    lhs = As[i-1] + 3*As[i] + As[i+1]
    rhs = E + K
    assert lhs == rhs
    print("second_order", i, "lhs", lhs, "rhs", rhs)

exit_minor = count_before(0,8)
assert exit_minor == K == 319
assert E <= 3*exit_minor <= 2*E
A,C,X,Y,Z,W = six_words(*CORRIDORS[-1][:4])
assert Y+Z == exit_minor
lhs = As[-2] + 3*As[-1] + exit_minor
assert lhs == E + K
print("balanced_exit_pair", 0, 8, "count", exit_minor, "fraction", f"{exit_minor}/{E}")
print("terminal_second_order", "lhs", lhs, "rhs", E+K)
print("POS3_B19_CORRIDOR_TRANSFER_PASS")
