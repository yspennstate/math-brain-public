#!/usr/bin/env python3
"""Self-check for the uniform Gamma_0=0 specialization of the restriction-margin ledger.

Exhaustive through n=3, plus deterministic random n=4 tests.  Standard library only.
"""
import itertools
import math
import random
from functools import lru_cache


def walsh_probs(vals):
    a = [float(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    N = len(a)
    return [(x / N) ** 2 for x in a]


@lru_cache(None)
def metrics(vals):
    vals = list(vals)
    p = walsh_probs(vals)
    H = -sum(x * math.log2(x) for x in p if x > 0.0)
    I = sum(mask.bit_count() * x for mask, x in enumerate(p))
    mean = sum(vals) / len(vals)
    V = 1.0 - mean * mean
    P = (I - V) / 4.0
    return H, I, P, mean


def restrict(vals, labels, label, bit):
    pos = labels.index(label)
    out = [x for idx, x in enumerate(vals) if ((idx >> pos) & 1) == bit]
    new_labels = list(labels)
    new_labels.pop(pos)
    return tuple(out), tuple(new_labels)


def fixed_policy(order):
    order = tuple(order)
    def choose(vals, labels, depth):
        for label in order:
            if label in labels:
                return label
    return choose


def adaptive_policy(vals, labels, depth):
    # Deliberately history/value dependent.
    mean = sum(vals) / len(vals)
    return min(labels) if mean >= 0 else max(labels)


def ledger(vals, policy):
    labels = tuple(range(len(vals).bit_length() - 1))

    def rec(v, labs, depth):
        H, _, P, _ = metrics(v)
        if not labs:
            return 0.0, 0.0, 0.0, 0.0
        label = policy(v, labs, depth)
        v0, l0 = restrict(v, labs, label, 0)
        v1, l1 = restrict(v, labs, label, 1)
        H0, _, P0, _ = metrics(v0)
        H1, _, P1, _ = metrics(v1)
        L = H - 0.5 * (H0 + H1)
        Q = P - 0.5 * (P0 + P1)
        a = rec(v0, l0, depth + 1)
        b = rec(v1, l1, depth + 1)
        return (
            L + 0.5 * (a[0] + b[0]),
            Q + 0.5 * (a[1] + b[1]),
            min(Q, a[2], b[2]),
            max(abs(L) if abs(Q) < 1e-12 else 0.0, a[3], b[3]),
        )

    return rec(tuple(vals), labels, 0)


def main():
    max_Herr = 0.0
    max_Perr = 0.0
    min_Q = 1.0
    max_qzero_L = 0.0
    paths = 0
    functions = 0

    for n in range(1, 4):
        N = 1 << n
        for tt in range(1 << N):
            vals = tuple(1 if (tt >> i) & 1 else -1 for i in range(N))
            H, _, P, _ = metrics(vals)
            functions += 1
            policies = [fixed_policy(order) for order in itertools.permutations(range(n))]
            policies.append(adaptive_policy)
            for policy in policies:
                sL, sQ, qmin, q0bad = ledger(vals, policy)
                max_Herr = max(max_Herr, abs(H - sL))
                max_Perr = max(max_Perr, abs(P - sQ))
                min_Q = min(min_Q, qmin)
                max_qzero_L = max(max_qzero_L, q0bad)
                paths += 1

    rng = random.Random(20260922)
    for _ in range(1000):
        vals = tuple(rng.choice((-1, 1)) for _ in range(16))
        H, _, P, _ = metrics(vals)
        policies = [adaptive_policy, fixed_policy((0, 1, 2, 3)), fixed_policy((3, 2, 1, 0))]
        for policy in policies:
            sL, sQ, qmin, q0bad = ledger(vals, policy)
            max_Herr = max(max_Herr, abs(H - sL))
            max_Perr = max(max_Perr, abs(P - sQ))
            min_Q = min(min_Q, qmin)
            max_qzero_L = max(max_qzero_L, q0bad)
            paths += 1

    assert max_Herr < 1e-12
    assert max_Perr < 1e-12
    assert min_Q >= -1e-12
    assert max_qzero_L < 1e-12

    print("PASS")
    print("functions_exhaustive_n_le_3", functions)
    print("restriction_paths_checked", paths)
    print("max_entropy_telescope_error", max_Herr)
    print("max_currency_telescope_error", max_Perr)
    print("min_local_Q", min_Q)
    print("max_abs_L_when_Q_zero", max_qzero_L)


if __name__ == "__main__":
    main()
