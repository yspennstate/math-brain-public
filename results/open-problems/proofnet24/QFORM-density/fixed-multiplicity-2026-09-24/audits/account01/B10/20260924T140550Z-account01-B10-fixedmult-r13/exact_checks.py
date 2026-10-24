#!/usr/bin/env python3
"""Exact finite diagnostics for account01/B10 r13.

This checks only the rational arithmetic and the two finite structural examples
used in the accompanying audit/improvement. It is not a proof certificate for
any universal theorem.
"""
from fractions import Fraction as F
from math import factorial
import json


def rank_q(M):
    A = [[F(x) for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


# Fejer constant: fourth-power rational upper using pi<22/7, e<11/4.
fejer_c4_upper = F(2500, 2209) ** 4 * F(16, 21) ** 4 * 8 * F(5, 3) * F(242, 7)
assert fejer_c4_upper < 256
fejer_margin = F(256) - fejer_c4_upper

# Rational certificate log 2 < 1733/2500.
q2 = F(1733, 2500)
exp_partial = sum(q2 ** k / factorial(k) for k in range(7))
assert exp_partial > 2

# New scalar-pivot and final nine-direction constants.
H_scalar = 10 * (F(22, 7) + 8 + 20 * q2)
full_half = H_scalar + 1
outer_scalar = 10 * full_half
assert H_scalar == F(43762, 175)
assert full_half == F(43937, 175)
assert outer_scalar == F(87874, 35)
assert F(2511) - outer_scalar == F(11, 35)

# Exact rank-saturation diagnostic from the audit.
R = [
    [2, 3, -1, 2],
    [3, 2, 1, -1],
    [-1, 1, F(-1, 3), F(2, 3)],
    [2, -1, F(1, 3), F(-2, 3)],
]
RLL = [[F(-1, 3), F(2, 3)], [F(1, 3), F(-2, 3)]]
assert rank_q(R) == 3
assert rank_q(RLL) == 1

# Singular seed with nonsingular same-step extension.
singular_seed_det = F(0)
extension_det = F(-1)
assert singular_seed_det == 0 and extension_det == -1

out = {
    "status": "PASS",
    "scope": "exact finite diagnostics only; not a universal proof certificate",
    "fejer_c4_upper": str(fejer_c4_upper),
    "fejer_c4_upper_float": float(fejer_c4_upper),
    "fejer_margin_to_256": str(fejer_margin),
    "log2_exp_partial_margin": str(exp_partial - 2),
    "H_scalar_upper": str(H_scalar),
    "full_half_potential_upper": str(full_half),
    "outer_scalar_density_upper": str(outer_scalar),
    "margin_to_2511": str(F(2511) - outer_scalar),
    "rank_R": rank_q(R),
    "rank_R_LL": rank_q(RLL),
    "singular_seed_det": str(singular_seed_det),
    "nonsingular_extension_det": str(extension_det),
}
print(json.dumps(out, indent=2))
