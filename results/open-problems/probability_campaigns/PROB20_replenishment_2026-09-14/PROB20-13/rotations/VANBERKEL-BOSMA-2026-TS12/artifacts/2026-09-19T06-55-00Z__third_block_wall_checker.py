#!/usr/bin/env python3
"""Exact self-check for the third accepted block in VANBERKEL-BOSMA-2026-TS12.

The mathematical report proves the generic complement-component lemma and the
affine wall formulas.  This script independently specializes them to the twelve
source cases using exact integer arithmetic and the strict three-distinct-summand
greedy rule.
"""
from itertools import combinations

CASES = [
    (4,6,17),(4,5,19),(1,9,24),(7,9,26),
    (1,11,29),(1,12,31),(5,7,26),(6,13,37),
    (6,7,27),(5,6,31),(7,13,38),(1,15,38),
]
FAMILY8 = {
    (1,9,24),(1,11,29),(1,12,31),(5,7,26),
    (6,13,37),(6,7,27),(7,13,38),(1,15,38),
}
DELTA2 = {(4,6,17),(7,9,26)}


def sum3(vals):
    return {a+b+c for a,b,c in combinations(vals,3)}


def first_complement_after(last, forbidden):
    x = last + 1
    while x in forbidden:
        x += 1
    u = x
    while x not in forbidden:
        x += 1
    return (u, x-1)


def greedy(init, max_n):
    vals = list(init)
    pair_sums = {a+b for a,b in combinations(vals,2)}
    triples = sum3(vals)
    S = set(vals)
    for n in range(vals[-1]+1, max_n+1):
        if n not in triples:
            for p in tuple(pair_sums):
                triples.add(n+p)
            for a in vals:
                pair_sums.add(n+a)
            vals.append(n)
            S.add(n)
    return S


rows = []
for c in CASES:
    f,g,h = c
    q = f+g
    delta = (h-g)+1-q
    A = 2*q+h
    r0 = min(delta,q)
    I = (h,h+q-1)
    J = (A,A+r0-1)

    P = [f,g] + list(range(I[0],I[1]+1)) + list(range(J[0],J[1]+1))
    K = first_complement_after(J[1], sum3(P))

    if c in FAMILY8:
        U = 2*A+h+q+2*delta-3
        V = 3*A+2
        assert K == (U,V)
        assert V-U+1 == q-2*delta+6
    elif c in DELTA2:
        assert K == (2*A+h-1,2*A+h)

    P2 = P + list(range(K[0],K[1]+1))
    H = first_complement_after(K[1], sum3(P2))
    w = H[1]-H[0]+1
    assert w <= 2*q

    # Generic <=2q complement-component theorem predicts exactly this prefix.
    R = (H[0], H[0]+min(q,w)-1)
    S = greedy(c, H[1]+2*q+5)
    assert all(x in S for x in range(R[0],R[1]+1))
    assert all(x not in S for x in range(R[1]+1,H[1]+1))
    assert all(x not in S for x in range(K[1]+1,H[0]))

    wall = None
    if c in FAMILY8:
        left_jjj = 3*A+3*delta-6
        left_kfg = K[1]+q
        right_fIK = f+h+K[0]
        assert H == (max(left_jjj,left_kfg)+1, right_fIK-1)
        expected_w = min(q+1,3*delta-7)
        expected_r = min(q,3*delta-7)
        assert w == expected_w
        assert R[1]-R[0]+1 == expected_r
        wall = 3*delta-q-8
        if wall >= 0:
            assert left_jjj >= left_kfg
            assert w == q+1
        else:
            assert left_kfg > left_jjj
            assert w == 3*delta-7
    elif c in DELTA2:
        assert w == q-1

    rows.append((c,q,delta,K,H,w,R,R[1]-R[0]+1,wall))

print("THIRD_BLOCK_EXACT_TABLE")
for row in rows:
    print(row)
print("FAMILY8_FORMULA")
for row in rows:
    if row[0] in FAMILY8:
        print(row[0], "q", row[1], "delta", row[2], "wall", row[-1],
              "old_gap_width", row[5], "accepted_len", row[7])
print("DELTA2_FORMULA")
for row in rows:
    if row[0] in DELTA2:
        print(row[0], "q", row[1], "width", row[5], "accepted_len", row[7])
print("ALL_EXACT_CHECKS_PASS")
