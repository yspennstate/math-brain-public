from fractions import Fraction
from itertools import combinations

N = 11
COVERS = {
    (0,1),(0,5),(1,2),(1,6),(1,10),(2,3),
    (4,1),(4,5),(5,3),(5,6),(6,7),
    (8,9),(8,0),(9,5),(9,10),(10,3),(10,7),
}

def transitive_closure(n, edges):
    r = [[False]*n for _ in range(n)]
    for a,b in edges:
        r[a][b] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    return {(i,j) for i in range(n) for j in range(n) if r[i][j]}

REL = transitive_closure(N, COVERS)
assert all((j,i) not in REL for i,j in REL)

def is_cover(a,b):
    return (a,b) in REL and not any((a,z) in REL and (z,b) in REL for z in range(N))

assert {(a,b) for a,b in REL if is_cover(a,b)} == COVERS

def incomparable(a,b):
    return a != b and (a,b) not in REL and (b,a) not in REL

def enumerate_extensions():
    pred = [set() for _ in range(N)]
    for a,b in REL:
        pred[b].add(a)
    out = []
    def rec(prefix, remaining):
        if not remaining:
            out.append(tuple(prefix))
            return
        for x in sorted(remaining):
            if pred[x].isdisjoint(remaining):
                rec(prefix+[x], remaining-{x})
    rec([], set(range(N)))
    return out

EXT = enumerate_extensions()
E = len(EXT)
assert E == 515
POS = [{v:i for i,v in enumerate(L)} for L in EXT]

def count_event(*orders):
    return sum(all(pos[a] < pos[b] for a,b in orders) for pos in POS)

def prob(a,b):
    return Fraction(count_event((a,b)), E)

def width():
    best = ()
    for r in range(1,N+1):
        for S in combinations(range(N),r):
            if all(incomparable(a,b) for a,b in combinations(S,2)):
                best = S
    return len(best), best

w, _ = width()
CHAIN_COVER = ((0,1,2,3),(4,5,6,7),(8,9,10))
assert w == 3
for C in CHAIN_COVER:
    assert all((a,b) in REL for a,b in combinations(C,2))
assert all(incomparable(a,b) for a,b in combinations((0,4,9),2))

def connected(edges):
    adj=[set() for _ in range(N)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for z in adj[v]:
            if z not in seen:
                seen.add(z); stack.append(z)
    return len(seen)==N

comp_edges={(a,b) for a,b in combinations(range(N),2) if (a,b) in REL or (b,a) in REL}
inc_edges={(a,b) for a,b in combinations(range(N),2) if incomparable(a,b)}
assert connected(comp_edges)
assert connected(inc_edges)

def autonomous(M):
    M=set(M)
    for z in set(range(N))-M:
        signatures=set()
        for m in M:
            if (z,m) in REL: signatures.add(-1)
            elif (m,z) in REL: signatures.add(1)
            else: signatures.add(0)
        if len(signatures) != 1:
            return False
    return True

proper_modules=[]
for r in range(2,N):
    for M in combinations(range(N),r):
        if autonomous(M):
            proper_modules.append(M)
assert proper_modules == []

all_pairs=[]
balanced=[]
for a,b in combinations(range(N),2):
    if incomparable(a,b):
        p=prob(a,b)
        all_pairs.append((a,b,p))
        if Fraction(1,3) <= p <= Fraction(2,3):
            balanced.append((a,b,p))
assert len(all_pairs)==15
assert balanced == [
    (0,4,Fraction(188,515)),
    (0,9,Fraction(319,515)),
    (2,6,Fraction(66,103)),
    (2,10,Fraction(49,103)),
    (3,7,Fraction(277,515)),
]

STAR=set(REL)
for a,b,p in all_pairs:
    if p > Fraction(2,3):
        STAR.add((a,b))
    elif p < Fraction(1,3):
        STAR.add((b,a))

def max_elements(S):
    return {x for x in S if not any(x != y and (x,y) in REL for y in S)}

def min_elements(S):
    return {x for x in S if not any(x != y and (y,x) in REL for y in S)}

def canonical_state(x,y,a):
    assert is_cover(x,y)
    assert incomparable(a,x) and incomparable(a,y)
    TL=max_elements({t for t in range(N) if (t,a) in REL and incomparable(t,x)})
    UL=min_elements({s for s in range(N) if (x,s) in REL and incomparable(s,a)})
    UR=min_elements({u for u in range(N) if (a,u) in REL and incomparable(u,y)})
    TR=max_elements({r for r in range(N) if (r,y) in REL and incomparable(r,a)})
    CL=TL | (UL-{y})
    CR=UR | (TR-{x})
    p=prob(x,a)
    q=prob(y,a)
    H=p-q
    mids=[pos for pos in POS if pos[x] < pos[a] < pos[y]]
    left={v:0 for v in CL}
    right={v:0 for v in CR}
    for pos in mids:
        between_left=[v for v in CL if pos[x] < pos[v] < pos[a]]
        between_right=[v for v in CR if pos[a] < pos[v] < pos[y]]
        if between_left:
            v=min(between_left,key=lambda z:pos[z])
            left[v]+=1
        if between_right:
            v=min(between_right,key=lambda z:pos[z])
            right[v]+=1
    return dict(x=x,y=y,a=a,p=p,q=q,H=H,TL=TL,UL=UL,UR=UR,TR=TR,
                CL=CL,CR=CR,left_weights=left,right_weights=right,
                middle_count=len(mids))

def interior(u,v):
    return tuple(r for r in range(N)
                 if r not in (u,v) and (u,r) in STAR and (r,v) in STAR)

S0=canonical_state(5,6,10)
S1=canonical_state(1,10,5)

# Heavy state S0: 5<.6 with pivot 10.
assert S0["p"] == Fraction(374,515)
assert S0["q"] == Fraction(161,515)
assert S0["H"] == Fraction(213,515) > Fraction(1,3)
assert S0["CL"] == {1} and S0["CR"] == {3}
assert S0["left_weights"] == {1:72}
assert S0["right_weights"] == {3:52}
assert interior(5,10)==() and interior(10,6)==()
assert prob(1,5)==Fraction(387,515) > Fraction(2,3)  # t=1 is outward left
assert prob(5,1)==Fraction(128,515) < Fraction(1,3)
assert is_cover(1,10)
assert 72 > 52  # unique heaviest canonical channel is t=1.

# Recycling the heaviest S0 channel t=1 gives cover 1<.10 with pivot 5 = S1.
assert S1["p"] == Fraction(387,515)
assert S1["q"] == Fraction(141,515)
assert S1["H"] == Fraction(246,515) > Fraction(1,3)
assert S1["CL"] == {2,9} and S1["CR"] == {6}
assert S1["left_weights"] == {2:55,9:63}
assert S1["right_weights"] == {6:105}
assert interior(1,5)==() and interior(5,10)==()
assert prob(10,6)==Fraction(354,515) > Fraction(2,3)  # u=6 is outward right
assert prob(6,10)==Fraction(161,515) < Fraction(1,3)
assert is_cover(5,6)
assert 105 > 63 and 105 > 55  # unique heaviest canonical channel is u=6.

# Recycling the heaviest S1 channel u=6 gives cover 5<.6 with pivot 10 = S0.
print("POS3_CANONICAL_HEAVY_GREEDY_2CYCLE_PASS")
print("extensions", E)
print("width", w, "antichain", (0,4,9), "chain_cover", CHAIN_COVER)
print("comparability_connected", connected(comp_edges),
      "incomparability_connected", connected(inc_edges))
print("proper_autonomous_modules", len(proper_modules))
print("incomparable_pairs", len(all_pairs))
for a,b,p in all_pairs:
    print("pair", a,b, "P(first<second)", f"{p.numerator}/{p.denominator}",
          "balanced", Fraction(1,3) <= p <= Fraction(2,3))
print("balanced_pairs",
      [(a,b,f"{p.numerator}/{p.denominator}") for a,b,p in balanced])
for name,S in (("S0",S0),("S1",S1)):
    print(name, "triple", (S["x"],S["y"],S["a"]),
          "p", str(S["p"]), "q", str(S["q"]), "H", str(S["H"]),
          "TL", sorted(S["TL"]), "UL", sorted(S["UL"]),
          "UR", sorted(S["UR"]), "TR", sorted(S["TR"]),
          "CL", sorted(S["CL"]), "CR", sorted(S["CR"]),
          "left_weights", S["left_weights"], "right_weights", S["right_weights"])
print("S0_no_strong_interior", interior(5,10), interior(10,6))
print("S1_no_strong_interior", interior(1,5), interior(5,10))
print("greedy_transition_S0_left_t1_to_S1",
      (5,6,10), "->", (1,10,5), "active_weight", 72)
print("greedy_transition_S1_right_u6_to_S0",
      (1,10,5), "->", (5,6,10), "active_weight", 105)
print("ordinal_family",
      "Q(k,s,t)=C_s ordinal-sum P^k ordinal-sum C_t; "
      "width=3; e(Q)=515^k; all incomparable pairs are internal to one P block "
      "and retain the 15 probabilities above.")
