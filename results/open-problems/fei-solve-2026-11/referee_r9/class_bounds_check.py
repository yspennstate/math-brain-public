"""Brute-force checks of FEIB31 sections 2 and 3 on random small functions (not a proof; a falsification attempt).

(3.1) every positive-influence leaf of a read-once AND/OR formula has E_i/Inf_i < pi/ln 2.
(2.1) every coordinate of every Boolean f: E_i/Inf_i <= 2 + log2 e + log2(1 + Var/Inf_i).
(2)   every width-w DNF has a coordinate with E_i/Inf_i <= 2 + log2 e + log2(2^(w+1) - 1).
"""
import math
import random
import sys

import numpy as np

PI_LN2 = math.pi / math.log(2)
LOG2E = 1 / math.log(2)


def spectrum(t, n):
    c = t.astype(float).copy()
    for k in range(n):
        c = c.reshape(-1, 2, 1 << k)
        v0, v1 = c[:, 0, :].copy(), c[:, 1, :].copy()
        c[:, 0, :], c[:, 1, :] = (v0 + v1) / 2, (v0 - v1) / 2
        c = c.reshape(-1)
    return c ** 2


def ratios(t, n):
    p = spectrum(t, n)
    idx = np.arange(1 << n)
    out = []
    for i in range(n):
        bi = 1 << i
        S = idx[(idx & bi) == 0]
        w0, w1 = p[S], p[S | bi]
        tot = w0 + w1
        m = (tot > 1e-300) & (w0 > 0) & (w1 > 0)
        q = w1[m] / tot[m]
        Ei = float((tot[m] * (-q * np.log2(q) - (1 - q) * np.log2(1 - q))).sum())
        Inf = float(w1.sum())
        out.append((Ei / Inf if Inf > 1e-12 else None, Inf))
    return out, 1 - p[0]


def rand_readonce(n, rng):
    """random read-once AND/OR tree on n leaves; returns +-1 truth table."""
    X = np.arange(1 << n)
    leaves = [np.where((X >> i) & 1, -1.0, 1.0) for i in range(n)]  # -1 = true
    nodes = leaves[:]
    rng.shuffle(nodes)
    while len(nodes) > 1:
        k = min(len(nodes), rng.choice([2, 2, 2, 3]))
        grp, nodes = nodes[:k], nodes[k:]
        if rng.random() < 0.5:   # AND: true iff all true
            v = np.where(np.all(np.stack(grp) < 0, axis=0), -1.0, 1.0)
        else:                    # OR
            v = np.where(np.any(np.stack(grp) < 0, axis=0), -1.0, 1.0)
        nodes.insert(rng.randrange(len(nodes) + 1), v)
    return nodes[0]


def rand_dnf(n, w, rng):
    X = np.arange(1 << n)
    out = np.zeros(1 << n, bool)
    for _ in range(rng.randint(1, 3 * n)):
        k = rng.randint(1, w)
        vars_ = rng.sample(range(n), k)
        term = np.ones(1 << n, bool)
        for v in vars_:
            lit = ((X >> v) & 1).astype(bool)
            term &= lit if rng.random() < 0.6 else ~lit
        out |= term
    return np.where(out, -1.0, 1.0)


def main():
    rng = random.Random(20261110)
    worst_ro, worst_21, worst_w = 0.0, -1e9, -1e9
    for trial in range(400):
        n = rng.randint(3, 13)
        t = rand_readonce(n, rng)
        rs, V = ratios(t, n)
        for r, inf in rs:
            if r is not None:
                worst_ro = max(worst_ro, r)
                worst_21 = max(worst_21, r - (2 + LOG2E + math.log2(1 + V / inf)))
    print(f"read-once: max leaf ratio {worst_ro:.6f} vs pi/ln2 {PI_LN2:.6f}; (2.1) max slack {worst_21:+.4f} (<=0 ok)")
    for trial in range(600):
        n = rng.randint(3, 11)
        w = rng.randint(1, min(4, n))
        t = rand_dnf(n, w, rng)
        if abs(t.sum()) == len(t):
            continue
        rs, V = ratios(t, n)
        good = [r for r, inf in rs if r is not None]
        bound = 2 + LOG2E + math.log2(2 ** (w + 1) - 1)
        worst_w = max(worst_w, min(good) - bound)
        for r, inf in rs:
            if r is not None:
                worst_21 = max(worst_21, r - (2 + LOG2E + math.log2(1 + V / inf)))
    print(f"width-w DNF: max (best coord - bound) {worst_w:+.4f} (<=0 ok); (2.1) overall max slack {worst_21:+.4f}")


if __name__ == "__main__":
    sys.exit(main())
