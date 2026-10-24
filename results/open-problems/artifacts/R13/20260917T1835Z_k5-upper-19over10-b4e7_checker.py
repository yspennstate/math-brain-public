#!/usr/bin/env python3
"""Exact self-check for R13-C36: K_5^* <= 19/10.

All acceptance decisions are exact rational/integer comparisons. Floating point is
used only to choose which one of 126 rational diagonal weights to verify first;
the selected weight is then rechecked with fractions.Fraction, and a full exact
fallback scan is used if necessary.

Dependency preserved from the earlier exact R13-C33 certificate:
M_k = max ||sum_{s in U} t_s||_2^2 over k distinct projective 5-cube
classes with independent orientations.  The table is re-enumerated here for
k<=8 (the only sizes entering the four-row finite core); k=9,...,16 are reused
from C33 for the >=5-row energy DP.
"""
from itertools import combinations, product
from fractions import Fraction

S = [tuple([1] + [1 if (mask >> j) & 1 else -1 for j in range(4)])
     for mask in range(16)]
TARGET_T = Fraction(19, 10)
TARGET_C = Fraction(100, 361)       # 1 / (19/10)^2
TOTAL_CAP = 5 * TARGET_C            # 500/361
M = [None, 5, 16, 29, 48, 61, 80, 101, 128,
     133, 144, 157, 176, 189, 208, 229, 256]


def oriented_blocks(k, keep_norms=None):
    """Yield (support_mask, v, ||v||^2) once modulo global orientation."""
    for C in combinations(range(16), k):
        base = S[C[0]]  # fix first chosen projective class to + orientation
        if k == 1:
            v = base
            nrm = sum(x*x for x in v)
            if keep_norms is None or nrm in keep_norms:
                yield (1 << C[0], v, nrm)
            continue
        for signs in product((-1, 1), repeat=k-1):
            vv = list(base)
            for idx,sgn in zip(C[1:], signs):
                ss = S[idx]
                for j in range(5):
                    vv[j] += sgn * ss[j]
            v = tuple(vv)
            nrm = sum(x*x for x in v)
            if keep_norms is None or nrm in keep_norms:
                mask = 0
                for idx in C:
                    mask |= 1 << idx
                yield (mask, v, nrm)


# Re-enumerate exact possible aggregate norms for k<=8 and verify the C33 M_k table there.
possible_norms = {}
for k in range(1, 9):
    ns = set()
    for _,_,nrm in oriented_blocks(k):
        ns.add(nrm)
    possible_norms[k] = tuple(sorted(ns))
    assert max(ns) == M[k], (k, max(ns), M[k])

# Exact >=5-row energy lower bound using the certified C33 M_k table.
f = [None] + [Fraction(k*k, M[k]) for k in range(1,17)]
INF = None
# dp[q][s] = min sum f(k_i), k_i>=1, sum k_i=s
dp = [[INF]*17 for _ in range(17)]
dp[0][0] = Fraction(0)
for q in range(1,17):
    for s in range(1,17):
        best = None
        for k in range(1,s+1):
            prev = dp[q-1][s-k]
            if prev is None:
                continue
            val = prev + f[k]
            if best is None or val < best:
                best = val
        dp[q][s] = best
min_ge5 = min(dp[q][16] for q in range(5,17) if dp[q][16] is not None)
assert min_ge5 == Fraction(89,60), min_ge5
assert min_ge5 > TOTAL_CAP

# Enumerate every sorted 4-block size profile and retain only aggregate norms
# that are not already contradicted by total energy.
profiles = []
for a in range(1,17):
    for b in range(a,17):
        for c in range(b,17):
            d = 16-a-b-c
            if d < c or d < 1 or d > 16:
                continue
            ks = (a,b,c,d)
            base = sum(f[k] for k in ks)
            if base >= TOTAL_CAP:
                continue
            allowed = []
            ok = True
            for pos,k in enumerate(ks):
                # q=4 plus TOTAL_CAP<1.4 forces k<=8 in every surviving profile.
                assert k <= 8
                others = sum(f[kk] for i,kk in enumerate(ks) if i != pos)
                vals = tuple(nrm for nrm in possible_norms[k]
                             if nrm > 0 and Fraction(k*k,nrm) + others < TOTAL_CAP)
                if not vals:
                    ok = False
                    break
                allowed.append(vals)
            if ok:
                profiles.append((ks, tuple(allowed)))

expected_profiles = {
    (1,1,6,8), (1,1,7,7), (1,2,5,8), (1,3,4,8), (1,4,4,7),
    (2,2,4,8), (2,3,3,8), (2,3,4,7), (2,4,4,6), (4,4,4,4)
}
assert {p[0] for p in profiles} == expected_profiles, [p[0] for p in profiles]

# Build only the oriented blocks needed by those exact profile/norm survivors.
needed = {}
for ks, allowed in profiles:
    for k, norms in zip(ks, allowed):
        needed.setdefault(k,set()).update(norms)
states = {}
for k, norms in sorted(needed.items()):
    for mask,v,nrm in oriented_blocks(k, norms):
        states.setdefault((k,nrm), []).append((mask,v))

# 126 positive rational diagonal weights lambda_j=a_j/10.
weights = []
D = 10
for a in range(1,D-3):
    for b in range(1,D-a-2):
        for c in range(1,D-a-b-1):
            for d in range(1,D-a-b-c):
                e = D-a-b-c-d
                if e >= 1:
                    weights.append((a,b,c,d,e))
assert len(weights) == 126


def exact_score(vs, ks, w):
    ans = Fraction(0)
    for v,k in zip(vs,ks):
        den = sum(Fraction(D * vj*vj, aj) for vj,aj in zip(v,w))
        if den == 0:
            return Fraction(10**9)
        ans += Fraction(k*k,1) / den
    return ans


def float_score(vs, ks, w):
    ans = 0.0
    for v,k in zip(vs,ks):
        den = sum(D * (vj*vj) / aj for vj,aj in zip(v,w))
        if den == 0:
            return 1e99
        ans += (k*k)/den
    return ans

ALL = (1<<16)-1
profile_counts = {}
min_certificate = None
min_data = None

for ks, allowed in profiles:
    chosen = [None]*4
    count_box = [0]

    def dfs(pos, used):
        global min_certificate, min_data
        if pos == 4:
            if used != ALL:
                return
            count_box[0] += 1
            vs = tuple(x[1] for x in chosen)
            # Floating point merely nominates a rational weight; exact Fraction decides acceptance.
            w0 = max(weights, key=lambda w: float_score(vs, ks, w))
            cert = exact_score(vs, ks, w0)
            if cert <= TARGET_C:
                # exact fallback, so no claim is ever accepted by floating point
                cert = Fraction(-1)
                wbest = None
                for w in weights:
                    z = exact_score(vs, ks, w)
                    if z > cert:
                        cert, wbest = z, w
                w0 = wbest
            assert cert > TARGET_C, (ks, vs, cert, w0)
            if min_certificate is None or cert < min_certificate:
                min_certificate = cert
                min_data = (ks, vs, w0)
            return
        k = ks[pos]
        prev_mask = None
        if pos > 0 and ks[pos-1] == k:
            prev_mask = chosen[pos-1][0]
        for nrm in allowed[pos]:
            for mask,v in states[(k,nrm)]:
                if mask & used:
                    continue
                if prev_mask is not None and mask <= prev_mask:
                    continue
                chosen[pos] = (mask,v)
                dfs(pos+1, used|mask)

    dfs(0,0)
    profile_counts[ks] = count_box[0]

expected_counts = {
    (1,1,6,8):480, (1,1,7,7):640, (1,2,5,8):960, (1,3,4,8):960,
    (1,4,4,7):3040, (2,2,4,8):240, (2,3,3,8):720,
    (2,3,4,7):2880, (2,4,4,6):1680, (4,4,4,4):1070,
}
assert profile_counts == expected_counts, profile_counts
assert sum(profile_counts.values()) == 12670
assert min_certificate == Fraction(7,24), min_certificate
assert min_certificate > TARGET_C

# Exact propagation of B_5<=19/10 through the previously proved five-block composition.
improved_n = []
for n in range(5,76):
    q = (n+4)//5
    # New five-block square = (19/10)^2 q. It strictly improves the prior envelope
    # iff it is below the balanced-four square 3n/4; it is automatically below
    # the old five-block coefficient (sqrt(2)+1/2)^2 = 9/4+sqrt(2).
    if 361*q < 75*n:
        improved_n.append(n)
expected_improved = [5,10,15,20,25,29,30,34,35,39,40,44,45,49,50,
                     53,54,55,58,59,60,63,64,65,68,69,70,73,74,75]
assert improved_n == expected_improved
assert len(improved_n) == 30

# At n=76 the existing universal GFL bound remains smaller than both finite terms:
# 18*pi < 18*(22/7)=396/7 < 57 = 3*76/4 < (19/10)^2*16.
assert Fraction(396,7) < Fraction(57,1)
assert Fraction(57,1) < Fraction(361*16,100)

print('R13 K5 <= 19/10 exact checker')
print('M_1_to_8_reenumerated=', M[1:9])
print('min_ge5_total_energy=', min_ge5)
print('scaled_total_energy_cap=', TOTAL_CAP)
print('four_row_profiles=', len(profiles))
for ks,_ in profiles:
    print(' profile', ks, 'configs', profile_counts[ks])
print('oriented_four_row_configurations=', sum(profile_counts.values()))
print('diagonal_weight_grid=', len(weights), 'denominator=', D)
print('smallest_selected_exact_certificate=', min_certificate)
print('target_column_energy_cap=', TARGET_C)
print('smallest_certificate_minus_target=', min_certificate-TARGET_C)
print('worst_configuration_profile=', min_data[0])
print('worst_configuration_vectors=', min_data[1])
print('worst_configuration_weight=', min_data[2])
print('strict_Bn_improvements=', len(improved_n), improved_n)
print('R13_K5_19_10_EXACT_PASS')
