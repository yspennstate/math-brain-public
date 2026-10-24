#!/usr/bin/env python3
"""Exact finite final-recovery checker for VANBERKEL-BOSMA-2026-TS12.

Targeted special case: S_(4,6,17), greedy strict 3-sumfree.
All arithmetic is exact Python integer/bitset arithmetic.

This checker does NOT prove periodicity or nonperiodicity. It verifies:
(1) exact cluster macro-structure through 10^6;
(2) exact failure counts of the two-anchor reduction;
(3) a second-layer finite portal reduction using accepted values <= 10000;
(4) the 67 remaining deep defects and their P=219526 chain structure.
"""
from collections import Counter

LIMIT = 1_000_000
F, G, H = 4, 6, 17
ANCHORS = (4, 6, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37, 38)
P = 219_526
BMAX = 10_000

EXPECTED_RESIDUAL = [
53405,73073,77174,81275,100943,173002,177103,181204,192670,196771,
200872,272931,285423,292599,296700,300801,320394,320469,377150,392528,
396629,400730,412121,412196,416297,420398,473985,492457,496558,503848,
512125,516226,520327,539920,539995,565712,612054,616155,620256,631647,
631722,635823,639924,662547,711983,716084,718521,720185,723374,727550,
731651,735752,739853,754274,831580,835681,839782,855349,859450,931509,
935610,938047,939711,947076,951177,955278,959379
]

def greedy_strict3(limit):
    mask = (1 << (limit + 1)) - 1
    s_bits = (1 << F) | (1 << G) | (1 << H)
    vals = [F, G, H]
    pair_bits = (1 << (F + G)) | (1 << (F + H)) | (1 << (G + H))
    triple_bits = 1 << (F + G + H)
    for n in range(H + 1, limit + 1):
        if ((triple_bits >> n) & 1) == 0:
            old_s = s_bits
            triple_bits = (triple_bits | (pair_bits << n)) & mask
            pair_bits = (pair_bits | (old_s << n)) & mask
            s_bits |= 1 << n
            vals.append(n)
    return s_bits, vals, mask

def two_anchor_triples(s_bits, mask):
    out = 0
    for i, a in enumerate(ANCHORS):
        for b in ANCHORS[i+1:]:
            source = s_bits & ~(1 << a) & ~(1 << b)
            out |= (source << (a+b)) & mask
    return out

def positions(bits):
    out = []
    while bits:
        low = bits & -bits
        out.append(low.bit_length()-1)
        bits ^= low
    return out

def accepted_runs(vals, lo=90):
    out=[]
    st=pr=None
    for x in vals:
        if x < lo:
            continue
        if st is None:
            st=pr=x
        elif x == pr+1:
            pr=x
        else:
            out.append((st,pr))
            st=pr=x
    if st is not None:
        out.append((st,pr))
    return out

def clusters_from_runs(runs):
    clusters=[]
    cur=[]
    for r in runs:
        if not cur:
            cur=[r]
            continue
        gap = r[0]-cur[-1][1]-1
        if gap < 64:
            cur.append(r)
        else:
            clusters.append(cur)
            cur=[r]
    if cur:
        clusters.append(cur)
    return clusters

def signature(cluster):
    base=cluster[0][0]
    return tuple((a-base,b-a+1) for a,b in cluster)

def main():
    s_bits, vals, mask = greedy_strict3(LIMIT)
    domain = mask ^ ((1 << (H+1))-1)
    excluded = (~s_bits) & mask & domain

    runs = accepted_runs(vals)
    clusters = clusters_from_runs(runs)
    starts = [c[0][0] for c in clusters]
    steps = [b-a for a,b in zip(starts,starts[1:])]
    sigs = [signature(c) for c in clusters]
    step_counts = Counter(steps)
    macro_starts = [starts[2623*k] for k in range(5)]
    macro_mismatches = []
    for k in range(3):
        u=sigs[k*2623:(k+1)*2623]
        v=sigs[(k+1)*2623:(k+2)*2623]
        macro_mismatches.append(sum(a != b for a,b in zip(u,v)))
    assert step_counts == Counter({85:9650, 73:1113, 84:1077, 74:107})
    assert macro_starts == [90,219616,439142,658668,878194]
    assert macro_mismatches == [35,85,59]

    two = two_anchor_triples(s_bits, mask) & domain
    e2 = excluded & ~two
    assert e2.bit_count() == 21401

    aset=set(ANCHORS)
    secondary=[x for x in vals if x <= BMAX and x not in aset]
    cover = 0
    for a in ANCHORS:
        abit = 1 << a
        for b in secondary:
            source = s_bits & ~abit & ~(1 << b)
            cover |= (source << (a+b)) & mask

    residual_bits = e2 & ~cover
    residual = positions(residual_bits)
    assert residual == EXPECTED_RESIDUAL
    assert len(secondary) == 1166
    assert len(residual) == 67

    rset=set(residual)
    chain_starts=[x for x in residual if x-P not in rset]
    chains=[]
    for x in chain_starts:
        c=[]
        y=x
        while y in rset:
            c.append(y)
            y += P
        chains.append(c)
    chain_lengths=Counter(map(len,chains))
    singleton=[c[0] for c in chains if len(c)==1]
    forward_edges=sum(len(c)-1 for c in chains)
    assert chain_lengths == Counter({1:6,2:6,4:5,5:4,3:3})
    assert forward_edges == 43
    assert singleton == [285423,377150,473985,565712,662547,754274]
    assert singleton[2]-singleton[0] == 188562
    assert singleton[4]-singleton[2] == 188562
    assert singleton[3]-singleton[1] == 188562
    assert singleton[5]-singleton[3] == 188562

    print(f"LIMIT={LIMIT}")
    print(f"ACCEPTED_COUNT={len(vals)}")
    print(f"EXCLUDED_COUNT={excluded.bit_count()}")
    print(f"CLUSTER_COUNT={len(clusters)}")
    print("CLUSTER_STEP_COUNTS=" + repr(dict(sorted(step_counts.items()))))
    print("MACRO_CLUSTER_SHIFT=2623")
    print(f"MACRO_INTEGER_SHIFT={P}")
    print("MACRO_STARTS=" + repr(macro_starts))
    print("CONSECUTIVE_MACRO_SIGNATURE_MISMATCHES=" + repr(macro_mismatches))
    print(f"TWO_ANCHOR_RESIDUAL_COUNT={e2.bit_count()}")
    print(f"SECONDARY_PORTAL_BOUND={BMAX}")
    print(f"SECONDARY_PORTAL_COUNT={len(secondary)}")
    print(f"DEEP_RESIDUAL_COUNT={len(residual)}")
    print("DEEP_RESIDUALS=" + repr(residual))
    print("P_CHAIN_LENGTH_COUNTS=" + repr(dict(sorted(chain_lengths.items()))))
    print(f"P_CHAIN_FORWARD_EDGES={forward_edges}")
    print("P_CHAIN_SINGLETONS=" + repr(singleton))
    print("SINGLETON_SECOND_SCALE=188562")
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
