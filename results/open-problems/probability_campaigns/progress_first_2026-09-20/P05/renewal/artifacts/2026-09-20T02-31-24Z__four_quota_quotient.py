#!/usr/bin/env python3
"""
P05 exact four-quota quotient Bellman certificate for the binary LCS constant.

This is a complementary renewal/finite-state lower-bound certificate.
It uses four capped run quotas per source, but quotients out the common level
of the two active same-symbol quotas.  A quotient state is

    (d ; a1,a2,a3 ; b1,b2,b3),

where d=a0-b0 lies in {-(M-1),...,M-1}.  The lifted potential is

    h(a0,a1,a2,a3 ; b0,b1,b2,b3)
      = min(a0,b0) + phi(d;a1,a2,a3;b1,b2,b3).

At a mismatch, the policy may delete the longer active residual or delete the
shorter string's intervening opposite-symbol run.  It may reveal only the one
fresh quota Q which appears in BOTH candidate next quotient states before
choosing.  Branch-unique fresh quotas are averaged after the choice.  Thus the
lookahead is a legal finite-state policy, not hidden conditioning.

Candidate generation uses floating-point relative value iteration only to find
an integer potential.  Final verification recomputes every Bellman residual
with exact int64 arithmetic.  The script explicitly checks a deterministic
upper bound keeping all exact integer operations below 2^63.
"""

from fractions import Fraction
import hashlib
import numpy as np

M = 9
SCALE = 10_000_000
ITERATIONS = 40
D = 2 ** (M - 1)
D2 = D * D

W = np.zeros(M, dtype=np.int64)
for k in range(1, M):
    W[k - 1] = D // (2 ** k)
W[M - 1] = 1
assert int(W.sum()) == D
P = W.astype(np.float64) / float(D)

SHAPE = (2 * M - 1,) + (M,) * 6
BASE = (M - 1,) + (0,) * 6


def quotient_operator_float(phi):
    out = np.empty_like(phi)
    left = np.empty((M,) * 7, dtype=np.float64)
    for a1 in range(M):
        for b1 in range(M):
            didx = (a1 - b1) + (M - 1)
            sub = phi[didx]
            exp_a4 = np.tensordot(sub, P, axes=([2], [0]))
            left[a1, :, :, b1, :, :, :] = min(a1 + 1, b1 + 1) + exp_a4

    out[M - 1] = np.tensordot(left, P, axes=([6], [0]))

    for d in range(1, M):
        didx = d + (M - 1)
        right = np.empty((M,) * 6, dtype=np.float64)
        for b2 in range(M):
            ridx = (d - (b2 + 1)) + (M - 1)
            sub = phi[ridx]
            exp_b5 = np.tensordot(sub, P, axes=([5], [0]))
            right[:, :, :, b2, :, :] = min(d, b2 + 1) + exp_b5

        choose = np.maximum(left, right[:, :, :, None, :, :, :])
        out[didx] = np.tensordot(choose, P, axes=([6], [0]))
        out[M - 1 - d] = np.transpose(out[didx], (3, 4, 5, 0, 1, 2))

    return out


phi = np.zeros(SHAPE, dtype=np.float64)
for _ in range(ITERATIONS):
    F = quotient_operator_float(phi)
    phi = F - float(F[BASE])

PHI = np.rint(phi * SCALE).astype(np.int64)

assert np.array_equal(PHI[M - 1], np.transpose(PHI[M - 1], (3, 4, 5, 0, 1, 2)))
for d in range(1, M):
    assert np.array_equal(
        PHI[M - 1 - d],
        np.transpose(PHI[M - 1 + d], (3, 4, 5, 0, 1, 2)),
    )

assert int(PHI.min()) == 0
assert int(PHI.max()) == 24 * SCALE
potential_sha256 = hashlib.sha256(PHI.tobytes(order="C")).hexdigest()

INT64_BOUND = D2 * int(PHI.max()) + M * SCALE * D2
assert INT64_BOUND < 2**63


def exact_verify(phi_int):
    left_num = np.empty((M,) * 7, dtype=np.int64)
    for a1 in range(M):
        for b1 in range(M):
            didx = (a1 - b1) + (M - 1)
            sub = phi_int[didx]
            exp_a4_num = np.tensordot(sub, W, axes=([2], [0]))
            left_num[a1, :, :, b1, :, :, :] = (
                min(a1 + 1, b1 + 1) * SCALE * D + exp_a4_num
            )

    min_num = None
    max_num = None
    argmin = None
    state_count = 0

    future_num = np.tensordot(left_num, W, axes=([6], [0]))
    residual = future_num - phi_int[M - 1] * D2
    idx = np.unravel_index(int(np.argmin(residual)), residual.shape)
    min_num = int(residual[idx])
    max_num = int(residual.max())
    argmin = (0,) + tuple(int(i) + 1 for i in idx)
    state_count += residual.size

    for d in range(1, M):
        right_num = np.empty((M,) * 6, dtype=np.int64)
        for b2 in range(M):
            ridx = (d - (b2 + 1)) + (M - 1)
            sub = phi_int[ridx]
            exp_b5_num = np.tensordot(sub, W, axes=([5], [0]))
            right_num[:, :, :, b2, :, :] = (
                min(d, b2 + 1) * SCALE * D + exp_b5_num
            )

        choose_num = np.maximum(
            left_num,
            right_num[:, :, :, None, :, :, :],
        )
        future_num = np.tensordot(choose_num, W, axes=([6], [0]))
        residual = future_num - phi_int[M - 1 + d] * D2

        idx = np.unravel_index(int(np.argmin(residual)), residual.shape)
        value = int(residual[idx])
        if value < min_num:
            min_num = value
            argmin = (d,) + tuple(int(i) + 1 for i in idx)
        max_num = max(max_num, int(residual.max()))
        state_count += 2 * residual.size

    return state_count, min_num, max_num, argmin


state_count, min_num, max_num, argmin = exact_verify(PHI)
assert state_count == (2 * M - 1) * (M ** 6)

average_reward_lower = Fraction(min_num, SCALE * D2)
gamma_lower = average_reward_lower / 2

print("M =", M)
print("lookahead_quotas_per_source = 4")
print("quotient_state_count =", state_count)
print("full_unquotiented_state_count =", M ** 8)
print("probability_denominator =", D)
print("potential_scale =", SCALE)
print("candidate_iterations =", ITERATIONS)
print("potential_min =", int(PHI.min()))
print("potential_max =", int(PHI.max()))
print("potential_sha256 =", potential_sha256)
print("exchange_symmetry_exact =", True)
print("int64_safety_bound =", INT64_BOUND)
print("int64_safety_check =", INT64_BOUND < 2**63)
print("exact_min_bellman_residual_numerator =", min_num)
print("exact_min_bellman_residual_denominator =", SCALE * D2)
print("exact_min_bellman_residual_argmin =", argmin)
print("exact_max_bellman_residual_numerator =", max_num)
print("average_reward_lower =", average_reward_lower)
print("average_reward_lower_decimal =", format(float(average_reward_lower), ".15f"))
print("gamma_2_lower_from_this_certificate =", gamma_lower)
print("gamma_2_lower_decimal =", format(float(gamma_lower), ".15f"))
print("previous_three_quota_M10_lower_decimal = 0.770918990441703")
print(
    "renewal_route_increment =",
    format(float(gamma_lower) - 0.770918990441703, ".15f"),
)
print("published_global_lower_baseline = 0.792665992")
print("beats_published_global_lower =", float(gamma_lower) > 0.792665992)
print("FIXED_GLOBAL_ENDPOINT_MOVEMENT =", False)
print("EXACT_FOUR_QUOTA_QUOTIENT_BELLMAN_PASS")
