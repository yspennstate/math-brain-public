#!/usr/bin/env python3
"""
Exact finite-state Bellman subsolution certificate for P05 (binary LCS).

State: three capped run quotas per source,
    (a0,a1,a2 ; b0,b1,b2) in {1,...,M}^6,
with a0,b0 same-phase active runs.  At a mismatch, the policy may either
discard the longer active residual or discard the shorter string's next
opposite-symbol run.  It is allowed to reveal the one fresh run quota that
appears in BOTH candidate next states before choosing; branch-unique fresh
quotas are averaged after the choice.  Hence there is no illicit conditioning
on a future run that is later forgotten.

Candidate potential generation uses integer-scaled relative value iteration.
The actual certificate check below recomputes every Bellman residual using
Python arbitrary-precision integers.  Thus the final inequality does not rely
on floating point or on convergence of value iteration.
"""
from fractions import Fraction
import hashlib
import numpy as np

M = 10
SCALE = 10_000_000
ITERATIONS = 70
D = 2 ** (M - 1)
D2 = D * D

# Exact capped geometric law p(k)=2^{-k}, k<M; p(M)=2^{-(M-1)},
# represented by integer weights over common denominator D.
W = np.zeros(M, dtype=np.int64)
for k in range(1, M):
    W[k - 1] = D // (2 ** k)
W[M - 1] = 1
assert int(W.sum()) == D

SHAPE = (M,) * 6
BASE = (0,) * 6


def operator_numerators_int64(H):
    """Return numerators for SCALE*T(H/SCALE), common denominator D^2.

    This is only used to construct a candidate potential.  Exact verification
    is performed separately with Python ints.
    """
    # Tie: both current runs finish; shift both three-quota windows by one.
    tie = np.einsum("i,j,abicdj->abcd", W, W, H, optimize=True)

    # x>y crossing.  di encodes residual d=di+1.  For common fresh quota q:
    # branch L: (a1,a2,A3 ; b1,b2,q), average over branch-unique A3;
    # branch R: (d,a1,a2 ; b2,q,B4), average over branch-unique B4.
    cross = np.empty((M, M, M, M, M), dtype=np.int64)
    for di in range(M):
        for a1 in range(M):
            for a2 in range(M):
                for b1 in range(M):
                    for b2 in range(M):
                        left_by_q = W @ H[a1, a2, :, b1, b2, :]
                        right_by_q = H[di, a1, a2, b2, :, :] @ W
                        cross[di, a1, a2, b1, b2] = int(
                            W @ np.maximum(left_by_q, right_by_q)
                        )

    Tnum = np.empty(SHAPE, dtype=np.int64)
    for a0 in range(M):
        for a1 in range(M):
            for a2 in range(M):
                for b0 in range(M):
                    reward = min(a0 + 1, b0 + 1)
                    for b1 in range(M):
                        for b2 in range(M):
                            if a0 == b0:
                                future = tie[a1, a2, b1, b2]
                            elif a0 > b0:
                                future = cross[a0 - b0 - 1, a1, a2, b1, b2]
                            else:
                                future = cross[b0 - a0 - 1, b1, b2, a1, a2]
                            Tnum[a0, a1, a2, b0, b1, b2] = (
                                reward * SCALE * D2 + future
                            )
    return Tnum


# Deterministically build an integer potential.  Rounding here is harmless:
# the final potential is subsequently checked exactly.
H = np.zeros(SHAPE, dtype=np.int64)
for _ in range(ITERATIONS):
    Tnum = operator_numerators_int64(H)
    scaled_T = (Tnum + D2 // 2) // D2
    H = scaled_T - int(scaled_T[BASE])

# Exchange symmetry is exact.
assert np.array_equal(H, np.transpose(H, (3, 4, 5, 0, 1, 2)))
assert int(H.min()) == 0
# These observed bounds plus M,SCALE,D show the int64 construction is far
# inside range; the proof check itself below uses arbitrary-precision ints.
assert int(H.max()) <= 100 * SCALE

potential_sha256 = hashlib.sha256(H.tobytes(order="C")).hexdigest()


def exact_verify(H):
    """Recompute min_s [r(s)+E h(S')-h(s)] exactly with Python ints."""
    w = [int(x) for x in W]

    # Exact tie expectations.
    tie = np.empty((M, M, M, M), dtype=object)
    for a1 in range(M):
        for a2 in range(M):
            for b1 in range(M):
                for b2 in range(M):
                    total = 0
                    for aa in range(M):
                        for bb in range(M):
                            total += (
                                w[aa] * w[bb]
                                * int(H[a1, a2, aa, b1, b2, bb])
                            )
                    tie[a1, a2, b1, b2] = total

    # Exact mismatch expectations.
    cross = np.empty((M, M, M, M, M), dtype=object)
    for di in range(M):
        for a1 in range(M):
            for a2 in range(M):
                for b1 in range(M):
                    for b2 in range(M):
                        total = 0
                        for q in range(M):
                            left = sum(
                                w[aa] * int(H[a1, a2, aa, b1, b2, q])
                                for aa in range(M)
                            )
                            right = sum(
                                w[bb] * int(H[di, a1, a2, b2, q, bb])
                                for bb in range(M)
                            )
                            total += w[q] * max(left, right)
                        cross[di, a1, a2, b1, b2] = total

    min_num = None
    argmin = None
    max_num = None
    state_count = 0

    for a0 in range(M):
        for a1 in range(M):
            for a2 in range(M):
                for b0 in range(M):
                    reward = min(a0 + 1, b0 + 1)
                    for b1 in range(M):
                        for b2 in range(M):
                            if a0 == b0:
                                future = int(tie[a1, a2, b1, b2])
                            elif a0 > b0:
                                future = int(cross[a0 - b0 - 1, a1, a2, b1, b2])
                            else:
                                future = int(cross[b0 - a0 - 1, b1, b2, a1, a2])

                            # Exact numerator over denominator SCALE*D^2.
                            num = (
                                reward * SCALE * D2
                                + future
                                - int(H[a0, a1, a2, b0, b1, b2]) * D2
                            )
                            if min_num is None or num < min_num:
                                min_num = num
                                argmin = (a0 + 1, a1 + 1, a2 + 1,
                                          b0 + 1, b1 + 1, b2 + 1)
                            if max_num is None or num > max_num:
                                max_num = num
                            state_count += 1

    return state_count, int(min_num), argmin, int(max_num)


state_count, min_num, argmin, max_num = exact_verify(H)

# Average matched symbols per epoch is at least g.  Each epoch completes
# exactly two original runs total; source-exchange symmetry gives one run per
# source asymptotically, and original Geom(1/2) runs have mean 2 symbols.
# Therefore gamma_2 >= g/2.
g = Fraction(min_num, SCALE * D2)
gamma_lower = g / 2

print("M =", M)
print("lookahead_state_quotas_per_source = 3")
print("state_count =", state_count)
print("probability_denominator =", D)
print("potential_scale =", SCALE)
print("candidate_iterations =", ITERATIONS)
print("potential_min =", int(H.min()))
print("potential_max =", int(H.max()))
print("potential_sha256 =", potential_sha256)
print("exchange_symmetry_exact =", True)
print("exact_min_bellman_residual_numerator =", min_num)
print("exact_min_bellman_residual_denominator =", SCALE * D2)
print("exact_min_bellman_residual_argmin =", argmin)
print("exact_max_bellman_residual_numerator =", max_num)
print("average_reward_lower =", g)
print("average_reward_lower_decimal =", format(float(g), ".15f"))
print("gamma_2_lower_from_this_certificate =", gamma_lower)
print("gamma_2_lower_decimal =", format(float(gamma_lower), ".15f"))
print("previous_one_residual_M32_lower_decimal = 0.745254942600970")
print("renewal_route_increment =", format(float(gamma_lower) - 0.745254942600970, ".15f"))
print("published_global_lower_baseline = 0.792665992")
print("beats_published_global_lower =", float(gamma_lower) > 0.792665992)
print("FIXED_GLOBAL_ENDPOINT_MOVEMENT =", False)
print("EXACT_THREE_QUOTA_BELLMAN_SUBSOLUTION_PASS")
