"""A rule for the pair (i, pi) of the filtration witness (FLOW section 12(j)(1)): minimum certificates.

A certificate is a subcube {x : x_C = c} on which f is constant.  For every certificate C of minimum size and every
i in C, two constrained shortest paths over orderings of the other coordinates:
    out-first :  the coordinates outside C first (in the best order), then the mates C - i (in the best order);
    mates-first: the mates first, then the outside.
Printed per function: minE = min_i E_i/Inf_i, F = unconstrained min over (i, pi) of L^pi_i/Inf_i (filt_cs), and the
minimum over (C, i) of each rule, per unit of Inf_i.

usage:
  python rule_cs.py fam nmax
  python rule_cs.py file n PATH
  python rule_cs.py rand n count seed
"""
import sys
import math
import numpy as np
from local_cs import wht, phi, families
from filt_cs import zeta, best_order


def phis(p, q):
    def eta(x):
        return -x * math.log2(x) if x > 1e-300 else 0.0
    return eta(p) + eta(q) - eta(p + q)


def min_certificates(f, n, cap=64):
    """all certificates of minimum size, as (mask, value pattern) -> returned as list of masks (deduplicated)."""
    N = 1 << n
    idx = np.arange(N)
    by_size = {}
    for C in range(N):
        by_size.setdefault(bin(C).count("1"), []).append(C)
    for s in range(n + 1):
        found = []
        for C in by_size.get(s, []):
            keys = idx & C
            mn = np.full(N, 2.0)
            mx = np.full(N, -2.0)
            np.minimum.at(mn, keys, f)
            np.maximum.at(mx, keys, f)
            if np.any((mn == mx) & (mn > -2.0) & (mx < 2.0)):
                found.append(C)
        if found:
            return s, found[:cap], len(found)
    return n, [N - 1], 1


def constrained(a, b, first, second):
    """shortest path: add the coordinates of mask `first` (best order), then those of `second` (best order).
    a, b: zeta transforms indexed by subsets of the m compressed coordinates."""
    def stage(start, startcost, mask):
        bits = [j for j in range(mask.bit_length()) if (mask >> j) & 1]
        cost = {0: startcost}
        subs = sorted(range(1 << len(bits)), key=lambda s: bin(s).count("1"))
        for s in subs[1:]:
            R = start
            for t, j in enumerate(bits):
                if (s >> t) & 1:
                    R |= 1 << j
            bestv = float("inf")
            for t, j in enumerate(bits):
                if (s >> t) & 1:
                    prev = R ^ (1 << j)
                    v = cost[s ^ (1 << t)] + phis(max(float(a[R] - a[prev]), 0.0), max(float(b[R] - b[prev]), 0.0))
                    bestv = min(bestv, v)
            cost[s] = bestv
        return cost[(1 << len(bits)) - 1]
    c0 = phis(float(a[0]), float(b[0]))
    c1 = stage(0, c0, first)
    return stage(first, c1, second)


def compress(mask, i):
    """mask over [n] (without bit i) -> mask over the n-1 compressed coordinates."""
    low = mask & ((1 << i) - 1)
    high = mask >> (i + 1)
    return low | (high << i)


def report(name, f, n):
    mu = wht(f, n) ** 2
    idx = np.arange(1 << n)
    m = n - 1
    per = {}
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p, q = mu[lo], mu[lo | (1 << i)]
        inf = float(q.sum())
        if inf < 1e-12:
            continue
        val, _, _ = best_order(p, q, m)
        per[i] = dict(inf=inf, E=float(phi(p, q).sum()) / inf, F=val / inf, a=zeta(p, m), b=zeta(q, m))
    if not per:
        return None
    s, certs, total = min_certificates(f, n)
    full = (1 << n) - 1
    r_out, r_mates = float("inf"), float("inf")
    arg = None
    for C in certs:
        for i in range(n):
            if not (C >> i) & 1 or i not in per:
                continue
            mates = compress(C & ~(1 << i), i)
            out = compress(full & ~C, i)
            d = per[i]
            v1 = constrained(d["a"], d["b"], out, mates) / d["inf"]
            v2 = constrained(d["a"], d["b"], mates, out) / d["inf"]
            if v1 < r_out:
                r_out, arg = v1, (C, i)
            r_mates = min(r_mates, v2)
    minE = min(d["E"] for d in per.values())
    F = min(d["F"] for d in per.values())
    print("%-14s n=%2d minE=%.4f F=%.4f | cert size %d (%d of them) | out-first %.4f  mates-first %.4f  (C=%x i=%d)"
          % (name, n, minE, F, s, total, r_out, r_mates, arg[0], arg[1]), flush=True)
    return minE, F, r_out, r_mates


def main():
    mode = sys.argv[1]
    tops = [0.0] * 4
    worst_ratio = 0.0

    def take(r):
        nonlocal tops, worst_ratio
        if r:
            tops = [max(x, y) for x, y in zip(tops, r)]
            if r[1] > 1e-9:
                worst_ratio = max(worst_ratio, r[2] / r[1])
    if mode == "fam":
        for name, n, f in families(int(sys.argv[2])):
            take(report(name, f, n))
    elif mode == "rand":
        n, count, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        rng = np.random.default_rng(seed)
        for c in range(count):
            if c % 2 == 0:
                f = rng.choice([-1.0, 1.0], 1 << n)
            else:
                f = np.where(rng.random(1 << n) < rng.choice([0.05, 0.1, 0.25]), -1.0, 1.0)
            take(report("rand%d" % c, f, n))
    elif mode == "file":
        n = int(sys.argv[2])
        with open(sys.argv[3], encoding="utf-8") as fh:
            for ln, line in enumerate(fh):
                tok = line.split()
                if not tok:
                    continue
                try:
                    v = int(tok[-1], 16)
                except ValueError:
                    continue
                f = np.array([-1.0 if (v >> x) & 1 else 1.0 for x in range(1 << n)])
                take(report("line%d" % ln, f, n))
    print("sup:  minE %.4f  F %.4f  out-first %.4f  mates-first %.4f   largest out-first/F %.3f"
          % (tops[0], tops[1], tops[2], tops[3], worst_ratio))


if __name__ == "__main__":
    main()
