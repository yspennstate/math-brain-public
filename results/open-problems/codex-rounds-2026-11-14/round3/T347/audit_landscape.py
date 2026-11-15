#!/usr/bin/env python3
"""Find and exactly verify a Hopfield profile/local-minimum counterexample.

Run with one BLAS thread. Search uses NumPy; certificate uses Python integers.
"""
import argparse
import itertools
import json
import os
from pathlib import Path
import time


def search():
    import numpy as np
    rng = np.random.default_rng(347)
    n = 12
    spins = np.array(list(itertools.product((-1, 1), repeat=n)), dtype=np.int64)
    masks = np.arange(1 << n)
    errors = (n - spins.sum(axis=1)) // 2
    neighbors = masks[:, None] ^ (1 << np.arange(n))
    started = time.monotonic()
    for trial in range(1, 20001):
        count = int(rng.integers(5, 33))
        patterns = rng.choice((-1, 1), size=(count, n))
        patterns[0, :] = 1
        q = ((spins @ patterns.T) ** 2).sum(axis=1)
        profile = [int(q[errors == d].max()) for d in range(n // 2 + 1)]
        if any(a > b for a, b in zip(profile, profile[1:])):
            continue
        stable = (q[:, None] > q[neighbors]).all(axis=1)
        shell_max = np.array(profile + profile[-2::-1])
        candidates = np.flatnonzero(stable & (errors >= 1) & (errors <= 2)
                                    & (q < shell_max[errors]))
        if len(candidates):
            at = int(candidates[0])
            result = dict(n=n, m=count, trial=trial, seed=347,
                          patterns=patterns.tolist(), sigma=spins[at].tolist(),
                          search_seconds=round(time.monotonic() - started, 4))
            Path("counterexample.json").write_text(json.dumps(result, indent=2) + "\n")
            print("search", {k: result[k] for k in
                             ("n", "m", "trial", "seed", "search_seconds")})
            return result
    raise RuntimeError("No example in the prescribed search budget")


def verify(data):
    # Independent of NumPy, neighbor array indexing, and search intermediates.
    n, patterns, sigma = data["n"], data["patterns"], data["sigma"]
    m = len(patterns)
    assert data["m"] == m
    assert all(len(p) == n and set(p) <= {-1, 1} for p in patterns)
    assert patterns[0] == [1] * n
    assert len(sigma) == n and set(sigma) <= {-1, 1}

    def q(s):
        return sum(sum(x * y for x, y in zip(p, s)) ** 2 for p in patterns)

    # An independent quadratic-form expression includes all diagonal terms.
    gram = [[sum(p[i] * p[j] for p in patterns) for j in range(n)]
            for i in range(n)]
    profile = [-1] * (n + 1)
    witnesses = [None] * (n + 1)
    for s in itertools.product((-1, 1), repeat=n):
        value = q(s)
        alternate = sum(gram[i][j] * s[i] * s[j]
                        for i in range(n) for j in range(n))
        assert value == alternate
        d = sum(x == -1 for x in s)
        if value > profile[d]:
            profile[d], witnesses[d] = value, s
    assert profile == profile[::-1]
    half_profile = profile[:n // 2 + 1]
    assert all(a <= b for a, b in zip(half_profile, half_profile[1:]))
    value = q(sigma)
    differences = []
    for i in range(n):
        neighbor = sigma.copy()
        neighbor[i] *= -1
        diff = value - q(neighbor)
        # Q(s)-Q(s^i) = 4 s_i sum_{j != i} Gram_ij s_j.
        assert diff == 4 * sigma[i] * sum(gram[i][j] * sigma[j]
                                        for j in range(n) if j != i)
        assert diff > 0
        differences.append(diff)
    d = sum(s == -1 for s in sigma)
    assert 1 <= d <= 2
    assert value < profile[d]
    print("verified with exact Python integers")
    print("N", n, "M", m, "alpha", f"{m}/{n}")
    print("sigma", sigma)
    print("errors", d, "overlap", f"{n - 2*d}/{n}")
    print("Q(sigma)", value)
    print("max Q by errors d=0,...,N/2", half_profile)
    print("Q(sigma)-Q(single-flip neighbor)", differences)
    print("min energy increase", f"{min(differences)}/{2*n}")
    print("shell-maximum witness at same d", list(witnesses[d]))
    print("all", 1 << n, "states checked twice")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", action="store_true")
    args = parser.parse_args()
    print("priority", os.getpriority(os.PRIO_PROCESS, 0))
    print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))
    verify(search() if args.search else
           json.loads(Path("counterexample.json").read_text()))
