#!/usr/bin/env python3
"""
P05 binary LCS: exact uncapped geometric-tail Bellman lower certificate.

State semantics.
Fresh binary run lengths have P(G=k)=2^{-k}. Fix M. A fresh run is encoded
exactly as category j<M when G=j, and as tail category M when G>=M. In the
tail category G=M+E with P(E=e)=2^{-(e+1)}, e>=0.

After matching the common part of a same-symbol active pair, a crossing state
is either
  E(d): exact residual d, |d|<=M-1, or
  T+(r), T-(r): a signed tail residual r+E, 1<=r<=M.
Three future categories per source are retained. At a crossing, L deletes the
residual and R deletes the shorter source's intervening opposite-symbol run.
Only one fresh quota Q that is present in both candidate next states is exposed
before the L/R choice; branch-unique fresh quotas are averaged before max.
Thus every policy action is source-valid and every epoch completes exactly two
original runs total.

Geometric memorylessness closes the tail states exactly. In particular, for
E,F iid on {0,1,...} with P(E=e)=2^{-(e+1)},
  P(E-F=0)=1/3,
  P(E-F=+k)=P(E-F=-k)=2^{-k}/3, k>=1.
This makes the uncapped tail compression finite rather than a truncation.

Candidate generation uses floating relative value iteration. Final proof
recomputes every Bellman residual with exact int64 arithmetic after clearing a
common denominator C=6*2^(M-1). The only theorem claim supported by the script
is the exact minimum Bellman residual and the corresponding lower bound.
"""

from fractions import Fraction
import hashlib
import numpy as np

M = 8
ITERATIONS = 55
SCALE = 10_000_000
D = 2 ** (M - 1)
C = 6 * D
W = np.array([D // (2 ** k) for k in range(1, M)] + [1], dtype=np.int64)
P = W.astype(np.float64) / float(D)

SH0 = (2 * M - 1,) + (M,) * 6
SHT = (2, M) + (M,) * 6  # sign 0=positive, 1=negative; base r index r-1
BASE = (M - 1,) + (0,) * 6


def avg_a4(sub):
    return np.tensordot(sub, P, axes=([2], [0]))


def avg_b5(sub):
    return np.tensordot(sub, P, axes=([5], [0]))


def bellman_float(phi0, phiT):
    left = np.empty((M,) * 7, dtype=np.float64)
    for ia in range(M):
        x = ia + 1
        for ib in range(M):
            y = ib + 1
            if x < M and y < M:
                val = min(x, y) + avg_a4(phi0[(x - y) + (M - 1)])
            elif x == M and y < M:
                val = y + avg_a4(phiT[0, M - y - 1])
            elif x < M and y == M:
                val = x + avg_a4(phiT[1, M - x - 1])
            else:
                mix = (phi0[M - 1] + phiT[0, 0] + phiT[1, 0]) / 3.0
                val = M + 1.0 / 3.0 + avg_a4(mix)
            left[ia, :, :, ib, :, :, :] = val

    out0 = np.empty_like(phi0)
    outT = np.empty_like(phiT)
    out0[M - 1] = np.tensordot(left, P, axes=([6], [0]))

    for d in range(1, M):
        right = np.empty((M,) * 6, dtype=np.float64)
        for ib2 in range(M):
            b = ib2 + 1
            if b < M:
                val = min(d, b) + avg_b5(phi0[(d - b) + (M - 1)])
            else:
                val = d + avg_b5(phiT[1, M - d - 1])
            right[:, :, :, ib2, :, :] = val
        choose = np.maximum(left, right[:, :, :, None, :, :, :])
        out0[M - 1 + d] = np.tensordot(choose, P, axes=([6], [0]))
        out0[M - 1 - d] = np.transpose(
            out0[M - 1 + d], (3, 4, 5, 0, 1, 2)
        )

    for r in range(1, M + 1):
        right = np.empty((M,) * 6, dtype=np.float64)
        for ib2 in range(M):
            b = ib2 + 1
            if b < M:
                if r > b:
                    mix = phiT[0, r - b - 1]
                    reward = float(b)
                elif r == b:
                    mix = 0.5 * phi0[M - 1] + 0.5 * phiT[0, 0]
                    reward = float(b)
                else:
                    q = b - r
                    mix = np.zeros_like(phi0[M - 1])
                    for e in range(q):
                        p = 2.0 ** (-(e + 1))
                        j = q - e
                        mix += p * phi0[(M - 1) - j]
                    p = 2.0 ** (-(q + 1))
                    mix += p * phi0[M - 1] + p * phiT[0, 0]
                    reward = r + 1.0 - 2.0 ** (-q)
                val = reward + avg_b5(mix)
            else:
                q = M - r
                mix = np.zeros_like(phi0[M - 1])
                p = (1.0 / 3.0) * 2.0 ** (-q)
                mix += p * phiT[0, 0] + p * phi0[M - 1]
                if q >= 1:
                    for j in range(1, q):
                        mix += ((1.0 / 3.0) * 2.0 ** (-(q - j))) * phi0[
                            (M - 1) - j
                        ]
                    mix += (1.0 / 3.0) * phi0[(M - 1) - q]
                    mix += (1.0 / 3.0) * phiT[1, q]
                else:
                    mix += (1.0 / 3.0) * phiT[1, 0]
                reward = r + 1.0 - (2.0 ** (1 - q)) / 3.0
                val = reward + avg_b5(mix)
            right[:, :, :, ib2, :, :] = val

        choose = np.maximum(left, right[:, :, :, None, :, :, :])
        outT[0, r - 1] = np.tensordot(choose, P, axes=([6], [0]))
        outT[1, r - 1] = np.transpose(
            outT[0, r - 1], (3, 4, 5, 0, 1, 2)
        )

    return out0, outT


phi0 = np.zeros(SH0, dtype=np.float64)
phiT = np.zeros(SHT, dtype=np.float64)
for _ in range(ITERATIONS):
    F0, FT = bellman_float(phi0, phiT)
    base = float(F0[BASE])
    phi0 = F0 - base
    phiT = FT - base

P0 = np.rint(phi0 * SCALE).astype(np.int64)
PT = np.rint(phiT * SCALE).astype(np.int64)

assert np.array_equal(P0[M - 1], np.transpose(P0[M - 1], (3, 4, 5, 0, 1, 2)))
for d in range(1, M):
    assert np.array_equal(
        P0[M - 1 - d], np.transpose(P0[M - 1 + d], (3, 4, 5, 0, 1, 2))
    )
for r in range(M):
    assert np.array_equal(PT[1, r], np.transpose(PT[0, r], (3, 4, 5, 0, 1, 2)))

sha0 = hashlib.sha256(P0.tobytes(order="C")).hexdigest()
shaT = hashlib.sha256(PT.tobytes(order="C")).hexdigest()

left = np.empty((M,) * 7, dtype=np.int64)
for ia in range(M):
    x = ia + 1
    for ib in range(M):
        y = ib + 1
        if x < M and y < M:
            hnum = min(x, y) * SCALE * C + P0[x - y + M - 1] * C
        elif x == M and y < M:
            hnum = y * SCALE * C + PT[0, M - y - 1] * C
        elif x < M and y == M:
            hnum = x * SCALE * C + PT[1, M - x - 1] * C
        else:
            hnum = (
                M * SCALE * C
                + (SCALE * C) // 3
                + (C // 3) * (P0[M - 1] + PT[0, 0] + PT[1, 0])
            )
        left[ia, :, :, ib, :, :, :] = np.tensordot(
            hnum, W, axes=([2], [0])
        )

DEN = SCALE * C * D * D
min_num = None
max_num = None
argmin = None
state_count = 0

future = np.tensordot(left, W, axes=([6], [0]))
res = future - P0[M - 1] * (C * D * D)
idx = np.unravel_index(int(np.argmin(res)), res.shape)
min_num = int(res[idx])
max_num = int(res.max())
argmin = ("E", 0) + tuple(int(i) + 1 for i in idx)
state_count += res.size

for d in range(1, M):
    right = np.empty((M,) * 6, dtype=np.int64)
    for ib2 in range(M):
        b = ib2 + 1
        if b < M:
            hnum = min(d, b) * SCALE * C + P0[d - b + M - 1] * C
        else:
            hnum = d * SCALE * C + PT[1, M - d - 1] * C
        right[:, :, :, ib2, :, :] = np.tensordot(hnum, W, axes=([5], [0]))
    choose = np.maximum(left, right[:, :, :, None, :, :, :])
    future = np.tensordot(choose, W, axes=([6], [0]))
    res = future - P0[M - 1 + d] * (C * D * D)
    idx = np.unravel_index(int(np.argmin(res)), res.shape)
    value = int(res[idx])
    if value < min_num:
        min_num = value
        argmin = ("E", d) + tuple(int(i) + 1 for i in idx)
    max_num = max(max_num, int(res.max()))
    state_count += 2 * res.size

for r in range(1, M + 1):
    right = np.empty((M,) * 6, dtype=np.int64)
    for ib2 in range(M):
        b = ib2 + 1
        if b < M:
            if r > b:
                hnum = b * SCALE * C + PT[0, r - b - 1] * C
            elif r == b:
                hnum = b * SCALE * C + (C // 2) * (P0[M - 1] + PT[0, 0])
            else:
                q = b - r
                hnum = ((r + 1) * C - C // (2 ** q)) * SCALE
                mix = np.zeros_like(P0[M - 1])
                for e in range(q):
                    j = q - e
                    mix += (C // (2 ** (e + 1))) * P0[M - 1 - j]
                coeff = C // (2 ** (q + 1))
                mix += coeff * P0[M - 1] + coeff * PT[0, 0]
                hnum += mix
        else:
            q = M - r
            penalty = (2 * C) // 3 if q == 0 else C // (3 * (2 ** (q - 1)))
            hnum = ((r + 1) * C - penalty) * SCALE
            mix = np.zeros_like(P0[M - 1])
            coeff = C // (3 * (2 ** q))
            mix += coeff * PT[0, 0] + coeff * P0[M - 1]
            if q >= 1:
                for j in range(1, q):
                    mix += (C // (3 * (2 ** (q - j)))) * P0[M - 1 - j]
                mix += (C // 3) * P0[M - 1 - q]
                mix += (C // 3) * PT[1, q]
            else:
                mix += (C // 3) * PT[1, 0]
            hnum += mix
        right[:, :, :, ib2, :, :] = np.tensordot(hnum, W, axes=([5], [0]))

    choose = np.maximum(left, right[:, :, :, None, :, :, :])
    future = np.tensordot(choose, W, axes=([6], [0]))
    res = future - PT[0, r - 1] * (C * D * D)
    idx = np.unravel_index(int(np.argmin(res)), res.shape)
    value = int(res[idx])
    if value < min_num:
        min_num = value
        argmin = ("T+", r) + tuple(int(i) + 1 for i in idx)
    max_num = max(max_num, int(res.max()))
    state_count += 2 * res.size

expected_states = (4 * M - 1) * (M ** 6)
assert state_count == expected_states
assert min_num > 0

average_reward_lower = Fraction(min_num, DEN)
gamma_lower = average_reward_lower / 2

print("M =", M)
print("iterations =", ITERATIONS)
print("exact_crossing_types =", 2 * M - 1)
print("tail_crossing_types =", 2 * M)
print("future_category_states_checked =", state_count)
print("expected_state_count =", expected_states)
print("probability_denominator_D =", D)
print("internal_common_denominator_C =", C)
print("potential_scale =", SCALE)
print("exact_potential_min_E =", int(P0.min()))
print("exact_potential_max_E =", int(P0.max()))
print("exact_potential_min_T =", int(PT.min()))
print("exact_potential_max_T =", int(PT.max()))
print("potential_sha256_E =", sha0)
print("potential_sha256_T =", shaT)
print("source_exchange_symmetry_exact =", True)
print("exact_min_bellman_residual_numerator =", min_num)
print("exact_bellman_residual_denominator =", DEN)
print("exact_min_bellman_residual_argmin =", argmin)
print("exact_max_bellman_residual_numerator =", max_num)
print("average_matched_reward_per_epoch_lower =", average_reward_lower)
print("average_matched_reward_per_epoch_decimal =", format(float(average_reward_lower), ".15f"))
print("gamma_2_lower_from_this_certificate =", gamma_lower)
print("gamma_2_lower_decimal =", format(float(gamma_lower), ".15f"))
print("previous_four_quota_M9_lower_decimal = 0.775848824648284")
print("renewal_route_increment =", format(float(gamma_lower) - 0.775848824648284, ".15f"))
print("published_global_lower_baseline = 0.792665992")
print("beats_published_global_lower =", float(gamma_lower) > 0.792665992)
print("FIXED_GLOBAL_ENDPOINT_MOVEMENT =", False)
print("EXACT_UNCAPPED_GEOMETRIC_TAIL_BELLMAN_PASS")
