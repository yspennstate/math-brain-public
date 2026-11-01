#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction
from functools import lru_cache

V = tuple(range(11))
COVERS = (
    (0,1),(0,5),(1,2),(1,6),(1,10),(2,3),(4,1),(4,5),(5,3),(5,6),
    (6,7),(8,9),(8,0),(9,5),(9,10),(10,3),(10,7),
)
CHAINS = ((0,1,2,3),(4,5,6,7),(8,9,10))
WIDTH_WITNESS = (0,4,9)

def closure(covers):
    n=len(V)
    lt=[[False]*n for _ in range(n)]
    for a,b in covers:
        lt[a][b]=True
    for k in V:
        for i in V:
            if lt[i][k]:
                for j in V:
                    if lt[k][j]:
                        lt[i][j]=True
    return lt

LT=closure(COVERS)
PRED=[0]*len(V)
for v in V:
    for u in V:
        if LT[u][v]:
            PRED[v] |= 1<<u

def incomparable(a,b):
    return not LT[a][b] and not LT[b][a]

def enumerate_extensions(vertices=V, pred_masks=None):
    vertices=tuple(vertices)
    active=sum(1<<v for v in vertices)
    if pred_masks is None:
        pred_masks=PRED
    out=[]
    def rec(mask, arr):
        if mask==active:
            out.append(tuple(arr))
            return
        for v in vertices:
            bit=1<<v
            if mask & bit:
                continue
            if pred_masks[v] & active & ~mask == 0:
                rec(mask|bit, arr+(v,))
    rec(0,())
    return out

EXTS=enumerate_extensions()
E=len(EXTS)
POS=[{v:i for i,v in enumerate(ext)} for ext in EXTS]

def count_before(a,b, positions=POS):
    return sum(p[a] < p[b] for p in positions)

def fstr(num,den):
    return f"{num}/{den}"

def rel(z,v):
    if LT[z][v]: return -1
    if LT[v][z]: return 1
    return 0

def distinguisher_set(u,v):
    return {z for z in V if z not in (u,v) and rel(z,u) != rel(z,v)}

# Width certificate.
assert all(LT[c[i]][c[i+1]] for c in CHAINS for i in range(len(c)-1))
assert all(incomparable(a,b) for a,b in combinations(WIDTH_WITNESS,2))
assert set().union(*map(set,CHAINS)) == set(V)

# Connected incomparability graph.
seen={V[0]}
front=[V[0]]
while front:
    u=front.pop()
    for v in V:
        if v not in seen and incomparable(u,v):
            seen.add(v); front.append(v)
assert seen == set(V)

# Exhaustive autonomy check. A subset M is autonomous if every outside vertex has
# the same relation to every member of M.
autonomous=[]
for mask in range(1,1<<len(V)):
    if mask & (mask-1)==0 or mask==(1<<len(V))-1:
        continue
    M=[v for v in V if mask>>v&1]
    ok=True
    for z in V:
        if z in M: continue
        rr={rel(z,m) for m in M}
        if len(rr)>1:
            ok=False; break
    if ok:
        autonomous.append(tuple(M))
assert not autonomous

# Heavy cover: 5 lessdot 6, pivot 10.
assert (5,6) in COVERS and incomparable(5,10) and incomparable(6,10)
n_5_10=count_before(5,10)
n_6_10=count_before(6,10)
H=sum(p[5] < p[10] < p[6] for p in POS)
assert n_5_10 == 374 and n_6_10 == 161 and H == 213
assert H == n_5_10 - n_6_10
assert 3*n_5_10 > 2*E and 3*n_6_10 < E and 3*H > E

D5=distinguisher_set(5,10)
D6=distinguisher_set(6,10)
external=(D5-{6}) | (D6-{5})
assert D5 == {1,6} and D6 == {3,5} and external == {1,3}

local_pairs=[(1,5),(3,6),(5,10),(6,10)]
local_counts={pair:count_before(*pair) for pair in local_pairs}
assert local_counts == {(1,5):387,(3,6):88,(5,10):374,(6,10):161}
for c in local_counts.values():
    assert not (E <= 3*c <= 2*E)

# Natural witness-minority events A={5<1}, B={3<6}.
A=lambda p: p[5] < p[1]
B=lambda p: p[3] < p[6]
Hg=lambda p: p[5] < p[10] < p[6]
nA=sum(A(p) for p in POS)
nB=sum(B(p) for p in POS)
nAB=sum(A(p) and B(p) for p in POS)
nUnion=sum(A(p) or B(p) for p in POS)
patterns=Counter((A(p),B(p)) for p in POS if Hg(p))
assert (nA,nB,nAB,nUnion)==(128,88,16,200)
assert patterns[(False,False)]==105
assert patterns[(True,False)]==56
assert patterns[(False,True)]==36
assert patterns[(True,True)]==16
assert nUnion < H

# Exact deletion law for c=8. Q=P\{8}, S={z:z||8}={4}.
Q=tuple(v for v in V if v!=8)
QEXT=enumerate_extensions(Q)
QPOS=[{v:i for i,v in enumerate(ext)} for ext in QEXT]
S={z for z in Q if incomparable(z,8)}
assert S == {4}
def kappa(ext):
    k=0
    for v in ext:
        if v in S: k += 1
        else: break
    return k
Ws=[kappa(ext)+1 for ext in QEXT]
assert set(Ws)=={1,2}
assert sum(Ws)==E
qpair=sum(p[4] < p[9] for p in QPOS)
qstarts4=sum(ext[0]==4 for ext in QEXT)
weighted=sum(W for ext,W in zip(QEXT,Ws)
             if ext.index(4)<ext.index(9))
assert len(QEXT)==376 and qpair==229 and qstarts4==139 and weighted==368
assert Fraction(qpair,len(QEXT)) >= Fraction(1,3)
assert Fraction(qpair,len(QEXT)) <= Fraction(2,3)
assert Fraction(weighted,E) > Fraction(2,3)

# Every incomparable-pair probability.
all_probs=[]
balanced=[]
for a,b in combinations(V,2):
    if incomparable(a,b):
        c=count_before(a,b)
        all_probs.append(((a,b),Fraction(c,E)))
        if E <= 3*c <= 2*E:
            balanced.append((a,b,Fraction(c,E)))
expected_balanced=[
    (0,4,Fraction(188,515)),
    (0,9,Fraction(319,515)),
    (2,6,Fraction(66,103)),
    (2,10,Fraction(49,103)),
    (3,7,Fraction(277,515)),
]
assert balanced==expected_balanced

# Independent subset-DP counts after adding optional ordering constraints.
def dp_count(extra=(), vertices=V):
    vertices=tuple(vertices)
    active=sum(1<<v for v in vertices)
    pm=PRED[:]
    for a,b in extra:
        pm[b] |= 1<<a
    # close added predecessors transitively by constructing augmented relation
    aug=[row[:] for row in LT]
    for a,b in extra:
        aug[a][b]=True
    for k in V:
        for i in V:
            if aug[i][k]:
                for j in V:
                    if aug[k][j]:
                        aug[i][j]=True
    for i in V:
        if aug[i][i]:
            return 0
    pm=[0]*len(V)
    for j in V:
        for i in V:
            if aug[i][j]:
                pm[j] |= 1<<i
    @lru_cache(None)
    def f(mask):
        if mask==active: return 1
        s=0
        for v in vertices:
            bit=1<<v
            if mask&bit==0 and pm[v]&active&~mask==0:
                s += f(mask|bit)
        return s
    return f(0)

assert dp_count()==515
assert dp_count(((5,10),(10,6)))==213
assert dp_count(((5,1),))==128
assert dp_count(((3,6),))==88
assert dp_count(((5,1),(3,6)))==16
assert dp_count(vertices=Q)==376
assert dp_count(((4,9),),vertices=Q)==229
# Q-starts-4 equals extensions after first choosing 4.
Q_without4=tuple(v for v in Q if v!=4)
# Since 4 is minimal in Q, force it first by removing it from the remaining poset.
assert sum(1 for ext in QEXT if ext[0]==4)==139

print("extensions", E)
print("width_certificate", list(CHAINS), WIDTH_WITNESS)
print("incomparability_connected", True)
print("nontrivial_autonomous_subsets", len(autonomous))
print("heavy_cover", (5,6), "pivot", 10)
print("P(5<10)", fstr(n_5_10,E))
print("P(6<10)", fstr(n_6_10,E))
print("P(5<10<6)", fstr(H,E))
print("D(5,10)", sorted(D5), "D(6,10)", sorted(D6), "external", sorted(external))
print("local_block_probabilities")
for a,b in local_pairs:
    print(f"  P({a}<{b})={Fraction(local_counts[(a,b)],E)}")
print("witness_minority_counts A=5<1", nA, "B=3<6", nB, "intersection", nAB, "union", nUnion)
print("heavy_gap_minus_witness_union", H-nUnion)
print("heavy_gap_witness_pattern_counts neither", patterns[(False,False)],
      "A_only", patterns[(True,False)], "B_only", patterns[(False,True)],
      "both", patterns[(True,True)])
print("deletion_c", 8, "Q_extensions", len(QEXT), "S", sorted(S), "W_values", sorted(set(Ws)))
print("M", Fraction(sum(Ws),len(QEXT)), "P(J=0)", Fraction(len(QEXT),E))
print("Q_pair_4_9", Fraction(qpair,len(QEXT)), "weighted_pair_4_9", Fraction(weighted,E),
      "Q_starts_4", qstarts4)
print("all_incomparable_probabilities")
for (a,b),q in all_probs:
    print(f"  ({a},{b}) {q}")
print("balanced_pairs", [(a,b,str(q)) for a,b,q in balanced])
print("POS3_TWO_CHANNEL_OVERLAP_ADVERSARY_PASS")
