#!/usr/bin/env python3
"""
P05 binary LCS: exact five-quota uncapped geometric-tail Bellman lower certificate.

This is the K=4-future extension of the exact renewal/crossing quotient used in
P05.  A state stores:
  * one crossing type c (exact signed residual or signed geometric-tail residual),
  * four future run categories for source A,
  * four future run categories for source B.

Fresh binary run lengths are Geom(1/2) on {1,2,...}.  Fix M.  Category j<M
means the run has exact length j; category M means G>=M, in which case
G=M+E with P(E=e)=2^(-(e+1)), e>=0.  Geometric memorylessness makes the
uncapped residual process finite:
  E(d), |d|<=M-1,
  T+(r), T-(r), 1<=r<=M.

At a positive crossing the policy chooses between:
  L: delete the active residual, then align a1 with b1;
  R: delete b1, then align the active residual with b2.
It may inspect one fresh category Q=b5 before the choice because Q survives in
both candidate next states.  The L-only A5 and the R-only B6 are averaged
before the max.  Thus there is no branch-specific reveal-and-forget defect.

Candidate generation uses floating relative-value iteration.  The final pass
clears all probabilities with a common denominator and recomputes every
Bellman residual in int64 arithmetic.  Only the final exact residual minimum
is a proof certificate.

For M=6, K=4 this script checks (4M-1) M^(2K)=38,631,168 states and proves
gamma_2 >= 159561363199 / 204800000000.
"""

from fractions import Fraction
import hashlib
import numpy as np

M = 6
K = 4
ITERATIONS = 35
SCALE = 100_000_000

D = 2 ** (M - 1)
C = 6 * D
W = np.array([D // (2 ** k) for k in range(1, M)] + [1], dtype=np.int64)
P = W.astype(np.float64) / float(D)
ZERO = M - 1

SH0 = (2 * M - 1,) + (M,) * (2 * K)
SHT = (2, M) + (M,) * (2 * K)
BASE = (ZERO,) + (0,) * (2 * K)
EXCHANGE = tuple(range(K, 2 * K)) + tuple(range(0, K))


def avg_A_last(sub):
    """Average the branch-unique newest A category."""
    return np.tensordot(sub, P, axes=([K - 1], [0]))


def avg_B_last(sub):
    """Average the branch-unique newest B category."""
    return np.tensordot(sub, P, axes=([2 * K - 1], [0]))


def bellman_float(phi0, phiT):
    # left has state futures (a1..a4,b1..b4) plus shared fresh Q=b5.
    left = np.empty((M,) * (2 * K + 1), dtype=np.float64)

    for ia in range(M):
        x = ia + 1
        for ib in range(M):
            y = ib + 1

            if x < M and y < M:
                val = min(x, y) + avg_A_last(phi0[ZERO + x - y])
            elif x == M and y < M:
                val = y + avg_A_last(phiT[0, M - y - 1])
            elif x < M and y == M:
                val = x + avg_A_last(phiT[1, M - x - 1])
            else:
                mix = (phi0[ZERO] + phiT[0, 0] + phiT[1, 0]) / 3.0
                val = M + 1.0 / 3.0 + avg_A_last(mix)

            sl = [slice(None)] * (2 * K + 1)
            sl[0] = ia
            sl[K] = ib
            left[tuple(sl)] = val

    out0 = np.empty_like(phi0)
    outT = np.empty_like(phiT)

    out0[ZERO] = np.tensordot(left, P, axes=([2 * K], [0]))

    for d in range(1, M):
        right = np.empty((M,) * (2 * K), dtype=np.float64)

        for ib2 in range(M):
            b = ib2 + 1
            if b < M:
                val = min(d, b) + avg_B_last(phi0[ZERO + d - b])
            else:
                val = d + avg_B_last(phiT[1, M - d - 1])

            sl = [slice(None)] * (2 * K)
            sl[K] = ib2
            right[tuple(sl)] = val

        shape = list(right.shape)
        shape.insert(K, 1)
        choose = np.maximum(left, right.reshape(shape))
        out0[ZERO + d] = np.tensordot(choose, P, axes=([2 * K], [0]))
        out0[ZERO - d] = np.transpose(out0[ZERO + d], EXCHANGE)

    for r in range(1, M + 1):
        right = np.empty((M,) * (2 * K), dtype=np.float64)

        for ib2 in range(M):
            b = ib2 + 1

            if b < M:
                if r > b:
                    mix = phiT[0, r - b - 1]
                    reward = float(b)

                elif r == b:
                    mix = 0.5 * phi0[ZERO] + 0.5 * phiT[0, 0]
                    reward = float(b)

                else:
                    q = b - r
                    mix = np.zeros_like(phi0[ZERO])
                    for e in range(q):
                        p = 2.0 ** (-(e + 1))
                        j = q - e
                        mix += p * phi0[ZERO - j]
                    p = 2.0 ** (-(q + 1))
                    mix += p * phi0[ZERO] + p * phiT[0, 0]
                    reward = r + 1.0 - 2.0 ** (-q)

                val = reward + avg_B_last(mix)

            else:
                q = M - r
                mix = np.zeros_like(phi0[ZERO])
                p = (1.0 / 3.0) * 2.0 ** (-q)
                mix += p * phiT[0, 0] + p * phi0[ZERO]

                if q >= 1:
                    for j in range(1, q):
                        mix += ((1.0 / 3.0) * 2.0 ** (-(q - j))) * phi0[
                            ZERO - j
                        ]
                    mix += (1.0 / 3.0) * phi0[ZERO - q]
                    mix += (1.0 / 3.0) * phiT[1, q]
                else:
                    mix += (1.0 / 3.0) * phiT[1, 0]

                reward = r + 1.0 - (2.0 ** (1 - q)) / 3.0
                val = reward + avg_B_last(mix)

            sl = [slice(None)] * (2 * K)
            sl[K] = ib2
            right[tuple(sl)] = val

        shape = list(right.shape)
        shape.insert(K, 1)
        choose = np.maximum(left, right.reshape(shape))
        outT[0, r - 1] = np.tensordot(choose, P, axes=([2 * K], [0]))
        outT[1, r - 1] = np.transpose(outT[0, r - 1], EXCHANGE)

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

assert np.array_equal(P0[ZERO], np.transpose(P0[ZERO], EXCHANGE))
for d in range(1, M):
    assert np.array_equal(
        P0[ZERO - d], np.transpose(P0[ZERO + d], EXCHANGE)
    )
for r in range(M):
    assert np.array_equal(PT[1, r], np.transpose(PT[0, r], EXCHANGE))

sha0 = hashlib.sha256(P0.tobytes(order="C")).hexdigest()
shaT = hashlib.sha256(PT.tobytes(order="C")).hexdigest()

left = np.empty((M,) * (2 * K + 1), dtype=np.int64)

for ia in range(M):
    x = ia + 1
    for ib in range(M):
        y = ib + 1

        if x < M and y < M:
            hnum = min(x, y) * SCALE * C + P0[ZERO + x - y] * C

        elif x == M and y < M:
            hnum = y * SCALE * C + PT[0, M - y - 1] * C

        elif x < M and y == M:
            hnum = x * SCALE * C + PT[1, M - x - 1] * C

        else:
            hnum = (
                M * SCALE * C
                + (SCALE * C) // 3
                + (C // 3) * (P0[ZERO] + PT[0, 0] + PT[1, 0])
            )

        avg = np.tensordot(hnum, W, axes=([K - 1], [0]))
        sl = [slice(None)] * (2 * K + 1)
        sl[0] = ia
        sl[K] = ib
        left[tuple(sl)] = avg

DEN = SCALE * C * D * D
min_num = None
max_num = None
argmin = None
state_count = 0

future = np.tensordot(left, W, axes=([2 * K], [0]))
residual = future - P0[ZERO] * (C * D * D)
idx = np.unravel_index(int(np.argmin(residual)), residual.shape)
min_num = int(residual[idx])
max_num = int(residual.max())
argmin = ("E", 0) + tuple(int(i) + 1 for i in idx)
state_count += residual.size

for d in range(1, M):
    right = np.empty((M,) * (2 * K), dtype=np.int64)

    for ib2 in range(M):
        b = ib2 + 1

        if b < M:
            hnum = min(d, b) * SCALE * C + P0[ZERO + d - b] * C
        else:
            hnum = d * SCALE * C + PT[1, M - d - 1] * C

        avg = np.tensordot(hnum, W, axes=([2 * K - 1], [0]))
        sl = [slice(None)] * (2 * K)
        sl[K] = ib2
        right[tuple(sl)] = avg

    shape = list(right.shape)
    shape.insert(K, 1)
    choose = np.maximum(left, right.reshape(shape))
    future = np.tensordot(choose, W, axes=([2 * K], [0]))
    residual = future - P0[ZERO + d] * (C * D * D)

    idx = np.unravel_index(int(np.argmin(residual)), residual.shape)
    value = int(residual[idx])
    if value < min_num:
        min_num = value
        argmin = ("E", d) + tuple(int(i) + 1 for i in idx)

    max_num = max(max_num, int(residual.max()))
    state_count += 2 * residual.size

for r in range(1, M + 1):
    right = np.empty((M,) * (2 * K), dtype=np.int64)

    for ib2 in range(M):
        b = ib2 + 1

        if b < M:
            if r > b:
                hnum = b * SCALE * C + PT[0, r - b - 1] * C

            elif r == b:
                hnum = (
                    b * SCALE * C
                    + (C // 2) * (P0[ZERO] + PT[0, 0])
                )

            else:
                q = b - r
                hnum = ((r + 1) * C - C // (2 ** q)) * SCALE
                mix = np.zeros_like(P0[ZERO])

                for e in range(q):
                    j = q - e
                    mix += (C // (2 ** (e + 1))) * P0[ZERO - j]

                coeff = C // (2 ** (q + 1))
                mix += coeff * P0[ZERO] + coeff * PT[0, 0]
                hnum += mix

        else:
            q = M - r
            penalty = (
                (2 * C) // 3
                if q == 0
                else C // (3 * (2 ** (q - 1)))
            )
            hnum = ((r + 1) * C - penalty) * SCALE
            mix = np.zeros_like(P0[ZERO])

            coeff = C // (3 * (2 ** q))
            mix += coeff * PT[0, 0] + coeff * P0[ZERO]

            if q >= 1:
                for j in range(1, q):
                    mix += (
                        C // (3 * (2 ** (q - j)))
                    ) * P0[ZERO - j]

                mix += (C // 3) * P0[ZERO - q]
                mix += (C // 3) * PT[1, q]
            else:
                mix += (C // 3) * PT[1, 0]

            hnum += mix

        avg = np.tensordot(hnum, W, axes=([2 * K - 1], [0]))
        sl = [slice(None)] * (2 * K)
        sl[K] = ib2
        right[tuple(sl)] = avg

    shape = list(right.shape)
    shape.insert(K, 1)
    choose = np.maximum(left, right.reshape(shape))
    future = np.tensordot(choose, W, axes=([2 * K], [0]))
    residual = future - PT[0, r - 1] * (C * D * D)

    idx = np.unravel_index(int(np.argmin(residual)), residual.shape)
    value = int(residual[idx])
    if value < min_num:
        min_num = value
        argmin = ("T+", r) + tuple(int(i) + 1 for i in idx)

    max_num = max(max_num, int(residual.max()))
    state_count += 2 * residual.size

expected_states = (4 * M - 1) * (M ** (2 * K))
assert state_count == expected_states
assert min_num > 0

average_reward_lower = Fraction(min_num, DEN)
gamma_lower = average_reward_lower / 2
previous_uncapped_lower = Fraction(63588313173, 81920000000)
published_global_lower = Fraction(99083249, 125000000)

print("M =", M)
print("K_future_per_source =", K)
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
print("previous_uncapped_lower =", previous_uncapped_lower)
print("renewal_route_increment =", gamma_lower - previous_uncapped_lower)
print("renewal_route_increment_decimal =", format(float(gamma_lower - previous_uncapped_lower), ".15f"))
print("published_global_lower_baseline =", published_global_lower)
print("beats_published_global_lower =", gamma_lower > published_global_lower)
print("gap_to_published_global_lower =", published_global_lower - gamma_lower)
print("gap_to_published_global_lower_decimal =", format(float(published_global_lower - gamma_lower), ".15f"))
print("FIXED_GLOBAL_ENDPOINT_MOVEMENT =", "NO")
print("EXACT_FIVE_QUOTA_UNCAPPED_BELLMAN_PASS")
