#!/usr/bin/env python3
"""Exact verifier for HARD8-08 G14 pair-alignment self-gluing search.

Coordinates live in Q(sqrt(3)).  A scalar is represented by a pair
(a,b) meaning a + b*sqrt(3), with a,b exact fractions.

Search family:
  * U is the 14-point scaled G14 point set from the preceding HARD8-08 report.
  * For every unordered source pair {A,B} in U and unordered target pair {C,D}
    in U with equal nonzero distance, enumerate both target orders and both
    orientation choices.  This is exactly the set of Euclidean isometries
    sending the ordered source pair to the ordered target pair.
  * Deduplicate the resulting transformed 14-point sets.
  * Form W, the union of U and every distinct transformed copy.
  * Put every exact unit-distance edge among W into G(W).

The decisive certificate is an explicit proper 3-coloring of G(W).  Hence every
subgraph obtainable from any selection of the enumerated copies, even after
adding all cross-copy unit-distance edges, is 3-colorable.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from hashlib import sha256
from pathlib import Path

# ---------------- Q(sqrt(3)) exact arithmetic ----------------

def qadd(x,y): return (x[0]+y[0], x[1]+y[1])
def qsub(x,y): return (x[0]-y[0], x[1]-y[1])
def qneg(x): return (-x[0], -x[1])
def qmul(x,y):
    return (x[0]*y[0] + 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def qdiv_rat(x,r): return (x[0]/r, x[1]/r)
def q(a=0,b=0): return (F(a),F(b))

def vadd(A,B): return (qadd(A[0],B[0]), qadd(A[1],B[1]))
def vsub(A,B): return (qsub(A[0],B[0]), qsub(A[1],B[1]))
def smul(s,A): return (qmul(s,A[0]), qmul(s,A[1]))
def dot(A,B): return qadd(qmul(A[0],B[0]), qmul(A[1],B[1]))
def cross(A,B): return qsub(qmul(A[0],B[1]), qmul(A[1],B[0]))
def norm2(A): return dot(A,A)
def dist2(A,B): return norm2(vsub(A,B))
def is_unit(A,B): return dist2(A,B) == (F(1),F(0))

# ---------------- scaled exact G14 coordinates ----------------
# Each coordinate is (a,b) = a+b*sqrt(3).
# This is the original G14 coordinate list scaled globally by sqrt(3).
NAMES = ["O","i0","i1","i2","i3","i4","i5","h0","h1","a1","a2","a3","a4","a5"]
P = [
    (q(0), q(0)),
    (q(0,F(1,2)), q(F(1,2))),
    (q(0), q(1)),
    (q(0,-F(1,2)), q(F(1,2))),
    (q(0,-F(1,2)), q(-F(1,2))),
    (q(0), q(-1)),
    (q(0,F(1,2)), q(-F(1,2))),
    (q(0,1), q(0)),
    (q(0,F(1,2)), q(F(3,2))),
    (q(0,1), q(1)),
    (q(0,1), q(2)),
    (q(0,F(1,2)), q(F(5,2))),
    (q(0,F(3,2)), q(F(1,2))),
    (q(0,F(3,2)), q(-F(1,2))),
]
assert len(P) == 14 and len(set(P)) == 14

# Exact base-distance classification.
by_d2 = defaultdict(list)
for i,j in combinations(range(14),2):
    d = dist2(P[i],P[j])
    assert d[1] == 0 and d[0] > 0
    by_d2[d[0]].append((i,j))
expected_hist = {F(1):27,F(3):18,F(4):14,F(7):18,F(9):5,F(12):5,F(13):4}
assert {k:len(v) for k,v in by_d2.items()} == expected_hist
BASE_UNIT = [(i,j) for i,j in combinations(range(14),2) if is_unit(P[i],P[j])]
assert len(BASE_UNIT) == 27

# ---------------- exact pair-aligned isometries ----------------

def transform_points(a,b,c,d,orientation):
    """Return image of all P under the unique isometry with
       P[a]->P[c], P[b]->P[d] and determinant sign orientation (+1/-1)."""
    A,B,C,D = P[a],P[b],P[c],P[d]
    u = vsub(B,A); v = vsub(D,C)
    qu = norm2(u); qv = norm2(v)
    assert qu == qv and qu[1] == 0 and qu[0] > 0
    r = qu[0]
    Jv = (qneg(v[1]), v[0])
    out=[]
    for X in P:
        w=vsub(X,A)
        alpha=qdiv_rat(dot(w,u),r)
        beta=qdiv_rat(cross(u,w),r)
        if orientation < 0:
            beta=qneg(beta)
        Y=vadd(C, vadd(smul(alpha,v), smul(beta,Jv)))
        out.append(Y)
    assert out[a] == C and out[b] == D
    # Exact isometry sanity check on all base unit edges.
    for i,j in BASE_UNIT:
        assert is_unit(out[i],out[j])
    return tuple(out)

raw_count=0
placements={}
for d2v in sorted(by_d2):
    pairs=by_d2[d2v]
    for a,b in pairs:
        for c,d in pairs:
            for cc,dd in ((c,d),(d,c)):
                for orientation in (+1,-1):
                    raw_count += 1
                    T=transform_points(a,b,cc,dd,orientation)
                    key=tuple(sorted(set(T)))
                    assert len(key)==14
                    placements.setdefault(key,(d2v,a,b,cc,dd,orientation))

assert raw_count == 6556, raw_count
assert len(placements) == 518, len(placements)

# ---------------- global exact unit-distance supergraph ----------------
W=set(P)
for S in placements:
    W.update(S)
W=sorted(W)
assert len(W)==505, len(W)
idx={p:i for i,p in enumerate(W)}
EDGES=[]
ADJ=[set() for _ in W]
for i,j in combinations(range(len(W)),2):
    if is_unit(W[i],W[j]):
        EDGES.append((i,j)); ADJ[i].add(j); ADJ[j].add(i)
assert len(EDGES)==2008, len(EDGES)

# ---------------- deterministic exact 3-color certificate ----------------
def dsatur_3color(adj):
    n=len(adj)
    color=[-1]*n
    uncolored=set(range(n))
    sat=[set() for _ in range(n)]
    nodes=0
    # deterministic symmetry break
    v0=max(range(n), key=lambda v:(len(adj[v]),-v))
    color[v0]=0; uncolored.remove(v0)
    for w in adj[v0]: sat[w].add(0)

    def rec():
        nonlocal nodes
        nodes+=1
        if not uncolored:
            return True
        v=max(uncolored, key=lambda x:(len(sat[x]),len(adj[x]),-x))
        used=max(color)+1
        # canonical color introduction: existing colors plus at most one fresh color.
        for c in range(min(3,used+1)):
            if c in sat[v]:
                continue
            color[v]=c; uncolored.remove(v)
            changed=[]; bad=False
            for w in adj[v]:
                if color[w]==c:
                    bad=True; break
                if color[w] < 0 and c not in sat[w]:
                    sat[w].add(c); changed.append(w)
            if not bad and rec():
                return True
            for w in changed: sat[w].remove(c)
            uncolored.add(v); color[v]=-1
        return False

    ok=rec()
    assert ok
    return color,nodes

COLOR,nodes = dsatur_3color(ADJ)
assert set(COLOR) <= {0,1,2} and min(COLOR)>=0
for i,j in EDGES:
    assert COLOR[i] != COLOR[j]
counts=[COLOR.count(c) for c in range(3)]

# Verify that every enumerated transformed copy sits inside W and every copy edge
# is among the complete exact unit edges of the supergraph.
edge_set=set(EDGES)
for S in placements:
    Sset=set(S)
    assert Sset <= set(W)
# Stronger direct check using one stored transformation for each deduplicated copy.
for S,meta in placements.items():
    d2v,a,b,c,d,orientation=meta
    T=transform_points(a,b,c,d,orientation)
    for i,j in BASE_UNIT:
        e=tuple(sorted((idx[T[i]],idx[T[j]])))
        assert e in edge_set

# Write an independently checkable explicit certificate when run from a writable dir.
def fs(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator!=1 else str(x.numerator)
def qs(x):
    a,b=x
    return f"({fs(a)})+({fs(b)})*sqrt3"
def ps(p):
    return qs(p[0])+"\t"+qs(p[1])

cert_lines=["index\tx\ty\tcolor"]
for i,p in enumerate(W):
    cert_lines.append(f"{i}\t{ps(p)}\t{COLOR[i]}")
cert_text="\n".join(cert_lines)+"\n"
cert_hash=sha256(cert_text.encode()).hexdigest()
Path('/mnt/data/hard8_08_g14_pair_alignment_3color_certificate.tsv').write_text(cert_text,encoding='utf-8')

# Complete edge certificate too: index pairs only; coordinates + checker prove unit length.
edge_text="\n".join(f"{i}\t{j}" for i,j in EDGES)+"\n"
edge_hash=sha256(edge_text.encode()).hexdigest()
Path('/mnt/data/hard8_08_g14_pair_alignment_unit_edges.tsv').write_text(edge_text,encoding='utf-8')

print('MODEL_RUNTIME_METADATA_NOT_CHECKED_BY_SCRIPT')
print('BASE_VERTICES',len(P))
print('BASE_UNIT_EDGES',len(BASE_UNIT))
print('BASE_DISTANCE_HIST',' '.join(f'{int(k)}:{len(by_d2[k])}' for k in sorted(by_d2)))
print('RAW_PAIR_ALIGNED_ISOMETRIES',raw_count)
print('DISTINCT_TRANSFORMED_COPIES',len(placements))
print('GLOBAL_UNION_VERTICES',len(W))
print('GLOBAL_UNIT_EDGES',len(EDGES))
print('GLOBAL_DEGREE_MIN_MAX',min(map(len,ADJ)),max(map(len,ADJ)))
print('THREE_COLOR_COUNTS',*counts)
print('DSATUR_SEARCH_NODES',nodes)
print('THREE_COLOR_VECTOR',''.join(map(str,COLOR)))
print('COLOR_CERT_SHA256',cert_hash)
print('EDGE_CERT_SHA256',edge_hash)
print('PAIR_ALIGNMENT_FAMILY_CERTIFIED_3_COLORABLE',len(placements))
print('ALL_EXACT_CHECKS_PASSED')
