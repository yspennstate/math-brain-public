#!/usr/bin/env python3
"""
P26 independent exact audit for R06 ROMERO max-minus-four finite theorem T_{9,32}.

This deliberately does NOT reproduce R06's S_6 x C_2 canonicalization.
Instead it uses a hand-derived exhaustive list of the 21 marked defect types:
  S3: 4, P4: 5, P3+K2: 7, K3: 2, 3K2: 3.
For each marked type it computes the full exact split coefficient vector
by integer root-component recurrence and checks coefficientwise domination
by the terminal-centered four-star defect.

The accompanying mathematical audit proves separately that the 21 listed
types are exhaustive and that the terminal-edge swap is coefficientwise:
every successful j-edge split subgraph of G with st present omits st and
therefore injects, unchanged, into G-st+e.
"""
from math import comb

N = 9
S, T = 0, 1

def norm_edges(es):
    return tuple(sorted((a,b) if a < b else (b,a) for a,b in es))

# Exhaustive marked-type list, derived by abstract 3-edge shape and allowed
# placements of the unordered terminal pair (st may not itself be in D).
REPS = {
    # K_1,3
    "S3_both_iso": ((2,3),(2,4),(2,5)),
    "S3_center_s": ((0,2),(0,3),(0,4)),       # candidate D_*
    "S3_leaf_s": ((0,2),(2,3),(2,4)),
    "S3_leaves_st": ((0,2),(1,2),(2,3)),
    # P_4
    "P4_both_iso": ((2,3),(3,4),(4,5)),
    "P4_endpoint_s": ((0,2),(2,3),(3,4)),
    "P4_internal_s": ((2,0),(0,3),(3,4)),
    "P4_endpoints_st": ((0,2),(2,3),(3,1)),
    "P4_endpoint_internal_st": ((0,2),(2,1),(1,3)),
    # P_3 disjoint union K_2
    "P3K2_both_iso": ((2,3),(2,4),(5,6)),
    "P3K2_center_s": ((0,2),(0,3),(4,5)),
    "P3K2_leaf_s": ((0,2),(2,3),(4,5)),
    "P3K2_match_s": ((2,3),(2,4),(0,5)),
    "P3K2_leaves_st": ((0,2),(1,2),(3,4)),
    "P3K2_center_match_st": ((0,2),(0,3),(1,4)),
    "P3K2_leaf_match_st": ((0,2),(2,3),(1,4)),
    # K_3
    "K3_both_iso": ((2,3),(2,4),(3,4)),
    "K3_vertex_s": ((0,2),(0,3),(2,3)),
    # 3K_2
    "3K2_both_iso": ((2,3),(4,5),(6,7)),
    "3K2_one_s": ((0,2),(3,4),(5,6)),
    "3K2_st_separate": ((0,2),(1,3),(4,5)),
}
REPS = {k: norm_edges(v) for k,v in REPS.items()}

assert len(REPS) == 21
assert len(set(REPS.values())) == 21
assert sum(name.startswith("S3_") for name in REPS) == 4
assert sum(name.startswith("P4_") for name in REPS) == 5
assert sum(name.startswith("P3K2_") for name in REPS) == 7
assert sum(name.startswith("K3_") for name in REPS) == 2
assert sum(name.startswith("3K2_") for name in REPS) == 3
assert all((0,1) not in D for D in REPS.values())

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def split_coeffs(n, missing, s=0, t=1):
    """
    N_j = number of j-edge spanning subgraphs with exactly two connected
    components, one containing s and the other t.

    For each nonempty A, C_A(z) is the connected spanning-subgraph polynomial
    of G[A].  Root-component decomposition gives
      C_A=(1+z)^e(A) - sum_{B proper subset A, r in B}
                       C_B(z)(1+z)^e(A minus B).
    """
    miss = set(norm_edges(missing))
    E = [e for e in all_edges(n) if e not in miss]
    ecount = [0]*(1<<n)
    for mask in range(1<<n):
        c = 0
        for a,b in E:
            if ((mask>>a)&1) and ((mask>>b)&1):
                c += 1
        ecount[mask] = c

    bysize = [[] for _ in range(n+1)]
    for A in range(1,1<<n):
        bysize[A.bit_count()].append(A)

    C = [None]*(1<<n)
    for size in range(1,n+1):
        for A in bysize[size]:
            eA = ecount[A]
            poly = [comb(eA,j) for j in range(eA+1)]
            root = A & -A
            rest = A ^ root
            sub = rest
            while True:
                B = root | sub
                if B != A:
                    U = A ^ B
                    cb = C[B]
                    eU = ecount[U]
                    bins = [comb(eU,j) for j in range(eU+1)]
                    need = len(cb)+eU
                    if len(poly) < need:
                        poly += [0]*(need-len(poly))
                    for i,ci in enumerate(cb):
                        if ci:
                            for j,bj in enumerate(bins):
                                poly[i+j] -= ci*bj
                if sub == 0:
                    break
                sub = (sub-1) & rest
            assert all(x >= 0 for x in poly)
            while len(poly) > 1 and poly[-1] == 0:
                poly.pop()
            C[A] = poly

    ans = [0]*(len(E)+1)
    full = (1<<n)-1
    for A in range(1,full):
        if ((A>>s)&1) and not ((A>>t)&1):
            B = full ^ A
            ca, cb = C[A], C[B]
            for i,x in enumerate(ca):
                if x:
                    for j,y in enumerate(cb):
                        if y:
                            ans[i+j] += x*y
    return ans

candidate_D = REPS["S3_center_s"]
candidate_missing = ((0,1),) + candidate_D
cand = split_coeffs(N, candidate_missing)

expected_owner = [
0,0,0,0,0,0,0,606528,2685207,7152472,14572672,24412032,34613820,
42146743,44429640,40725504,32511099,22586343,13616310,7087488,
3161889,1196765,379044,98580,20500,3277,378,28,1,0,0,0,0
]
assert cand == expected_owner

violations = []
ties = []
j28 = {}
first_positive = {}
for name,D in REPS.items():
    vec = split_coeffs(N, ((0,1),)+D)
    gaps = [a-b for a,b in zip(cand,vec)]
    bad = [(j,d) for j,d in enumerate(gaps) if d < 0]
    if bad:
        violations.append((name,bad))
    if vec == cand:
        ties.append(name)
    j28[name] = gaps[28]
    pos = [(j,d) for j,d in enumerate(gaps) if d > 0]
    first_positive[name] = pos[0] if pos else None

assert violations == []
assert ties == ["S3_center_s"]
assert j28["S3_center_s"] == 0
assert all(j28[name] == 1 for name in REPS if name != "S3_center_s")

print("P26 independent audit: ROMERO max-minus-four T_{9,32}")
print("architecture=explicit_21_marked_types_no_group_canonicalization")
print("marked_type_counts=S3:4,P4:5,P3+K2:7,K3:2,3K2:3")
print("types_checked=21")
print("coefficientwise_violations=0")
print("exact_ties=1 candidate=S3_center_s")
print("j28_extremal_signature=candidate_gap_0_all_20_noncandidates_gap_1")
print("candidate_split_coefficients=" + ",".join(map(str,cand)))
print("NOTE: global st-present cases are covered mathematically by the")
print("coefficientwise terminal-edge-swap injection, not by extra enumeration.")
print("ALL_P26_T932_EXACT_CHECKS_PASS")
