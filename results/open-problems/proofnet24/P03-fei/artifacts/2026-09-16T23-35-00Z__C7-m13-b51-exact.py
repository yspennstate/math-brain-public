#!/usr/bin/env python3
from collections import defaultdict, Counter

N4 = 16
N5 = 32
N7 = 128
M = 13
E_INTERNAL = 20
BND = 7*M - 2*E_INTERNAL
assert BND == 51

def internal_edges(mask, d):
    e = 0
    for x in range(1<<d):
        if (mask >> x) & 1:
            for i in range(d):
                y = x ^ (1<<i)
                if x < y and ((mask >> y) & 1):
                    e += 1
    return e

def Emax(t):
    return sum(x.bit_count() for x in range(t))

# Exact defect arithmetic used in the written classifier.
assert Emax(13) == 22
assert Emax(12) == 20
gamma13 = [Emax(13)-Emax(13-b)-Emax(b)-b for b in range(1,7)]
gamma12 = [Emax(12)-Emax(12-b)-Emax(b)-b for b in range(1,7)]
assert gamma13 == [1,2,2,1,0,0]
assert gamma12 == [2,2,2,0,1,0]
# If a 12-set has defect 1 and a least-used active direction has c<=3,
# the only arithmetic possibility is b=4,c=3 with both sections extremal.
poss12 = []
for b,g in enumerate(gamma12, start=1):
    for c in range(1, min(b,3)+1):
        for da in range(0,2):
            for db in range(0,2):
                if g + da + db + (b-c) == 1:
                    poss12.append((b,c,da,db))
assert poss12 == [(4,3,0,0)]
# For a 13-set of defect 2 and c<=3, these are the only section-defect budgets.
poss13 = []
for b,g in enumerate(gamma13, start=1):
    for c in range(1, min(b,3)+1):
        for da in range(0,3):
            for db in range(0,3):
                if g + da + db + (b-c) == 2:
                    poss13.append((b,c,da,db))
expected13 = {
    (1,1,0,1),(1,1,1,0),
    (2,2,0,0),
    (3,3,0,0),
    (4,3,0,0),
    (5,3,0,0),
}
assert set(poss13) == expected13

# Enumerate all Q4 subsets once and group by (size, internal edges).
groups = defaultdict(list)
for mask in range(1<<N4):
    groups[(mask.bit_count(), internal_edges(mask,4))].append(mask)
# Exact Harper maxima in Q4 for relevant sizes.
for t in range(1,14):
    if t <= N4:
        emax_observed = max(e for (s,e) in groups if s == t)
        assert emax_observed == Emax(t)

# Walsh histogram on nonempty Q7 characters for a set contained in a d-face.
def q7_hist_from_face_mask(mask, d):
    n = 1<<d
    vals = []
    pts = [x for x in range(n) if (mask>>x)&1]
    for s in range(n):
        F = 0
        for x in pts:
            F += -1 if ((s & x).bit_count() & 1) else 1
        vals.append(abs(F))
    lift = 1 << (7-d)
    h = Counter()
    # For projection s=0, all lift characters have the same F, but one is the
    # global empty character and must be excluded.
    h[vals[0]] += lift-1
    for s in range(1,n):
        h[vals[s]] += lift
    if 0 in h and h[0] == 0:
        del h[0]
    assert sum(h.values()) == 127
    return tuple(sorted(h.items()))

# Exact multiplicative comparison equivalent to L_7(M)>0 for m=13,B=51.
# No floating point or transcendental approximation is used.
def exact_gap_positive(hist):
    c0 = 24576*(BND-7)
    left = (1 << c0) * (64-M)**(7*(64-M)*(64-M))
    for a,cnt in hist:
        if a <= 1:
            continue
        left *= a**(7*a*a*cnt)
    right = 63**(3969*BND)
    return left > right, left.bit_length(), right.bit_length()

# Branch A: active dimension <=4. Enumerate every actual 13-subset of Q4
# with 20 internal edges; embedding into Q7 is accounted for by multiplicity.
q4_masks = groups[(13,20)]
assert len(q4_masks) == 208
q4_hists = Counter(q7_hist_from_face_mask(mask,4) for mask in q4_masks)

# Branch B: active dimension exactly 5. Choose a least-used active direction,
# so 1<=c<=4. After swapping halves, b<=6. Enumerate every actual Q4 section
# pair satisfying |A|+|B|=13 and e(A)+e(B)+|A cap B|=20.
q5_masks = set()
section_specs = Counter()
for b in range(1,7):
    a = 13-b
    for (sa,ea), LA in list(groups.items()):
        if sa != a:
            continue
        for (sb,eb), LB in list(groups.items()):
            if sb != b:
                continue
            c = 20-ea-eb
            if c < 1 or c > min(b,4):
                continue
            for A in LA:
                for B in LB:
                    if (A & B).bit_count() == c:
                        m5 = A | (B<<16)
                        assert m5.bit_count() == 13
                        assert internal_edges(m5,5) == 20
                        q5_masks.add(m5)
                        section_specs[(b,ea,eb,c)] += 1
assert len(q5_masks) == 17088
q5_hists = Counter(q7_hist_from_face_mask(mask,5) for mask in q5_masks)

# Branch C: disconnected equality case. By the written Harper-equality proof,
# the 12-vertex component is cube-isomorphic to the canonical Q4 extremal
# {0,...,11}. Fix it in Q7 and enumerate every isolated 13th vertex.
component = set(range(12))
assert internal_edges(sum(1<<x for x in component),7) == 20
iso_hists = Counter()
iso_vertices = []
for y in range(N7):
    if y in component:
        continue
    if any((y ^ (1<<i)) in component for i in range(7)):
        continue
    pts = component | {y}
    mask7 = sum(1<<x for x in pts)
    assert mask7.bit_count() == 13
    assert internal_edges(mask7,7) == 20
    # direct Q7 Walsh histogram
    h = Counter()
    for s in range(1,N7):
        F = 0
        for x in pts:
            F += -1 if ((s & x).bit_count() & 1) else 1
        h[abs(F)] += 1
    iso_hists[tuple(sorted(h.items()))] += 1
    iso_vertices.append(y)
assert len(iso_vertices) == 76

all_hists = set(q4_hists) | set(q5_hists) | set(iso_hists)
assert len(all_hists) == 8
for hist in all_hists:
    ok, lb, rb = exact_gap_positive(hist)
    assert ok

print('P03-C7-M13-B51-EXACT-CHECKER')
print('BND=', BND)
print('gamma13=', gamma13)
print('gamma12=', gamma12)
print('defect1_12_possible=', poss12)
print('defect2_13_possible=', sorted(poss13))
print('q4_actual_sets=', len(q4_masks))
print('q5_section_pair_unique_sets=', len(q5_masks))
print('q5_section_specs=', sorted(section_specs.items()))
print('disconnected_isolated_positions=', len(iso_vertices))
print('unique_walsh_histograms=', len(all_hists))
for hist in sorted(all_hists):
    ok, lb, rb = exact_gap_positive(hist)
    print('hist=', hist, 'left_bits=', lb, 'right_bits=', rb, 'exact_positive=', ok)
print('P03-C7-M13-B51-CERTIFICATE=PASS')
