#!/usr/bin/env python3
"""Numerical audit of the exact balanced half-activation identity."""
from math import log, log2
import random


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def hu(v):
    N = len(v)
    n = N.bit_length() - 1
    w = fwht(v)
    p = [z * z / (N * N) for z in w]
    q = p[:]
    for j in range(n):
        for s in range(N):
            if not ((s >> j) & 1):
                q[s] += q[s | (1 << j)]
    H = sum(-x * log2(x) for x in p if x)
    U = sum(x * log2(q[s] / x) for s, x in enumerate(p) if x)
    return H, U, w


def child(v, j, b):
    return [v[x] for x in range(len(v)) if ((x >> j) & 1) == b]


def stats(v):
    n = len(v).bit_length() - 1
    H, U, w = hu(v)
    I = 0.0
    G = 0.0
    for j in range(n):
        I += sum(v[x] != v[x ^ (1 << j)] for x in range(len(v))) / len(v)
        G += U - (hu(child(v, j, 0))[1] + hu(child(v, j, 1))[1]) / 2
    N = len(v)
    a = [w[1 << j] / N for j in range(n)]
    L1 = sum(x * x * log2(1 / (x * x)) for x in a if x)
    W1 = sum(x * x for x in a)
    return H, I, G, L1, W1, a


def scalar_s(t):
    left = 0.0 if t == 1 else -2 * (1 - t) ** 2 * log2(1 - t)
    right = 0.0 if t == 0 else -t * t * log2(t)
    return left + right - t * t


def D(a):
    return scalar_s(0.5) - (scalar_s((1 + a) / 2) + scalar_s((1 - a) / 2)) / 2


def activate(v):
    return [1] * len(v) + list(v)


c0 = 9 / (8 * log(2)) - 0.5
max_error = 0.0
min_bound_slack = 1e100
balanced_count = 0
for n in range(1, 5):
    N = 1 << n
    for mask in range(1 << (N - 1)):
        v = [1 if (mask >> x) & 1 else -1 for x in range(N)]
        if sum(v) != 0:
            continue
        H, I, G, L1, W1, a = stats(v)
        HF, IF, GF, _, _, _ = stats(activate(v))
        lhs = (HF + IF - GF) - 0.5 * (H + I - G)
        rhs = 1.5 - 0.5 * L1 - sum(D(x) for x in a)
        bound_rhs = 1.5 - 0.5 * L1 - c0 * W1
        max_error = max(max_error, abs(lhs - rhs))
        min_bound_slack = min(min_bound_slack, lhs - bound_rhs)
        balanced_count += 1

rng = random.Random(20261013)
random_count = 0
for n, trials in ((5, 2000), (6, 1000), (7, 250)):
    N = 1 << n
    for _ in range(trials):
        plus = set(rng.sample(range(N), N // 2))
        v = [1 if x in plus else -1 for x in range(N)]
        H, I, G, L1, W1, a = stats(v)
        HF, IF, GF, _, _, _ = stats(activate(v))
        lhs = (HF + IF - GF) - 0.5 * (H + I - G)
        rhs = 1.5 - 0.5 * L1 - sum(D(x) for x in a)
        bound_rhs = 1.5 - 0.5 * L1 - c0 * W1
        max_error = max(max_error, abs(lhs - rhs))
        min_bound_slack = min(min_bound_slack, lhs - bound_rhs)
        random_count += 1

print("B01 A003 balanced half-activation two-component audit")
print(f"c0={c0:.16f}")
print(f"exhaustive_balanced_mod_output_sign_n_le_4={balanced_count}")
print(f"deterministic_random_balanced_n_5_to_7={random_count}")
print(f"max_identity_roundoff={max_error:.3e}")
print(f"min_bound_slack={min_bound_slack:.3e}")
assert max_error < 2e-12
assert min_bound_slack > -2e-12
print("NUMERICAL_AUDIT_PASS_ANALYTIC_PROOF_REQUIRED")
