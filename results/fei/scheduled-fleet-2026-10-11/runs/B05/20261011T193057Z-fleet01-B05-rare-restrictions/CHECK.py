#!/usr/bin/env python3
"""Deterministic check for the sparse-activation variance-refund no-go.

Uses the aggregated exact packet multiplicities; it never enumerates the
2^(3k)-point residual cube.
"""

import math
import platform


def h2(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)


def packet_stats(k: int):
    assert k >= 4 and k % 2 == 0
    delta = 2.0 ** (-k)
    p = 2.0 ** (-2 * k)
    d = p * delta
    a = math.sqrt(delta)
    npos = (2**k + 2 ** (k // 2)) // 2
    nneg = (2**k - 2 ** (k // 2)) // 2
    controls = 2 ** (2 * k)

    packets = []  # (multiplicity, midpoint coefficient m)
    packets.append(((npos - 1) * controls, p * (a - delta)))
    packets.append((nneg * controls, p * (-a - delta)))
    packets.append((controls - 1, p * (a - 1.0 - delta)))
    packets.append((1, 1.0 + p * (a - 1.0 - delta)))

    e = d * d
    total_q = 0.0
    total_e = 0.0
    L = 0.0
    second = 0.0
    max_theta = 0.0
    for mult, midpoint in packets:
        q = midpoint * midpoint + e
        theta = e / q
        total_q += mult * q
        total_e += mult * e
        L += mult * q * h2(theta)
        second += mult * q * theta * theta
        max_theta = max(max_theta, theta)
    V = second - d * d
    M = 12.0 * k * d * d
    lower = (1.0 - delta) * (k - 2.0) * d
    return d, total_q, total_e, L, V, M, max_theta, lower


print(f"Python: {platform.python_version()}")
print("Arithmetic: aggregated exact integer multiplicities; IEEE-754 evaluation of h2")
print("Randomness: NONE")
print("Seed: NOT_APPLICABLE")
print()
print(" k       L/d          V/d          M/d       max(theta)   lower/d")
checks = 0
for k in range(4, 42, 2):
    d, tq, te, L, V, M, mt, lower = packet_stats(k)
    assert abs(tq - 1.0) < 5e-13
    assert abs(te - d) <= 5e-13 * d
    assert L + 1e-15 * d >= lower
    assert V <= 4.0 * (2.0 ** (-k)) * d * (1.0 + 1e-12)
    assert mt <= 4.0 * (2.0 ** (-k)) * (1.0 + 1e-12)
    checks += 5
    print(f"{k:2d}  {L/d:11.7f}  {V/d:11.4e}  {M/d:11.4e}  {mt:11.4e}  {lower/d:8.4f}")

print()
print(f"Assertions: {checks}")
print(f"Passed: {checks}")
print("Failed: 0")
print("STATUS=PASS")
