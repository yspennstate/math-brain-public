"""Exact checks for "Moments of level widths in conditioned Galton-Watson trees".

Part 1. Lemma 2.1 of the paper: for a truncated tree t with N vertices of depth < k and l >= 1
vertices at depth k,

    P(T_n^(k) = t) = P_GW(T^(k) = t) * W_n(t),
    W_n(t) = n * l * P(S_{n-N} = n-N-l) / ((n-N) * P(S_n = n-1)).

For each offspring law below, every plane tree with n vertices and all outdegrees in the support is
enumerated with its Galton-Watson weight and the conditional law of the truncation at depth k is computed
exactly. Separately, every possible truncation t with N + l <= n is generated from the support alone, and
the formula is compared with the enumerated probability for each of them (so a truncation that never occurs
must get formula value 0). Truncations with l = 0 (whole trees of height < k) are compared with
P_GW(T = t) / P(|T| = n). P(S_M = j) comes from exact convolution powers of the law, independently of the
enumeration. Also checked: P(|T| = n) = P(S_n = n-1) / n (Otter-Dwass).

Part 2. Lemma 2.3 of the paper on the four finite-support laws, for m = 1..4 and g = i - j = 1..3:
E[Z_g | Z_0 = m] = m; for s in {1, 2, 3}, exactly, E[Z_g^s | Z_0 = m] <= m^s E[Z_g^s | Z_0 = 1] <= m^s (E xi^s)^g;
for s in {1/2, 3/2, 5/2}, in floating point, E[Z_g^s | Z_0 = m] <= m^s (s < 1), or
E[Z_g^s | Z_0 = m] <= m^s E[Z_g^s | Z_0 = 1] <= m^s (E xi^s)^g (s > 1).

Standard library only. Part 1 and the integer moments in Part 2 use exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import sys

LAWS = {
    # name: (pi as {degree: probability}, span)
    # geometric(1/2) gives uniformly random plane trees; degrees above 39 never occur for n <= 12
    "geometric(1/2)": ({d: F(1, 2 ** (d + 1)) for d in range(0, 40)}, 1),
    "binomial(2,1/2)": ({0: F(1, 4), 1: F(1, 2), 2: F(1, 4)}, 1),
    "{0,2} (span 2)": ({0: F(1, 2), 2: F(1, 2)}, 2),
    "{0,1,3}": ({0: F(1, 2), 1: F(1, 4), 3: F(1, 4)}, 1),
    "{0,3} (span 3)": ({0: F(2, 3), 3: F(1, 3)}, 3),
}
N_MAX = 12
KS = (1, 2, 3)


def mean(pi):
    return sum(d * p for d, p in pi.items())


def convolution_powers(pi, mmax, jmax):
    """P(S_M = j) for 0 <= M <= mmax, 0 <= j <= jmax, exactly."""
    base = [F(0)] * (jmax + 1)
    for d, p in pi.items():
        if d <= jmax:
            base[d] += p
    out = [[F(1)] + [F(0)] * jmax]
    for _ in range(mmax):
        prev = out[-1]
        nxt = [F(0)] * (jmax + 1)
        for a, pa in enumerate(prev):
            if pa == 0:
                continue
            for d, p in enumerate(base):
                if p == 0 or a + d > jmax:
                    continue
                nxt[a + d] += pa * p
        out.append(nxt)
    return out


@lru_cache(maxsize=None)
def compositions(total, parts):
    if parts == 1:
        return ((total,),) if total >= 1 else ()
    res = []
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            res.append((first,) + rest)
    return tuple(res)


_TREES = {}


def trees(n, support):
    """All plane trees with n vertices whose outdegrees lie in support, as nested tuples."""
    key = tuple(sorted(support))
    if key not in _TREES:
        @lru_cache(maxsize=None)
        def tr(m):
            res = []
            for d in key:
                if d == 0:
                    if m == 1:
                        res.append(())
                    continue
                if m - 1 < d:
                    break
                for parts in compositions(m - 1, d):
                    for kids in product(*(tr(p) for p in parts)):
                        res.append(tuple(kids))
            return tuple(res)
        _TREES[key] = tr
    return _TREES[key](n)


def gw_weight_tree(t, pi):
    w = pi.get(len(t), F(0))
    for c in t:
        w *= gw_weight_tree(c, pi)
    return w


def truncate(t, k):
    """Truncation at depth k: depth-k vertices become markers (None). Returns (tt, N, l)."""
    def rec(node, depth):
        if depth == k:
            return None
        return tuple(rec(c, depth + 1) for c in node)

    tt = rec(t, 0)

    def count(node):
        if node is None:
            return 0, 1
        N, l = 1, 0
        for c in node:
            a, b = count(c)
            N += a
            l += b
        return N, l

    N, l = count(tt)
    return tt, N, l


def gw_weight_trunc(tt, pi):
    """P_GW(T^(k) = tt): product of pi over the vertices of depth < k."""
    if tt is None:
        return F(1)
    w = pi.get(len(tt), F(0))
    for c in tt:
        w *= gw_weight_trunc(c, pi)
    return w


def all_truncations(support, k, budget):
    """Every truncation at depth k whose depth-<k outdegrees lie in support and with N + l <= budget."""
    sup = tuple(sorted(support))

    @lru_cache(maxsize=None)
    def gen(depth, b):
        if b < 1:
            return ()
        if depth == k:
            return ((None, 0, 1),)
        res = []
        for d in sup:
            if 1 + d > b:
                break
            partial = [((), 1, 0)]
            for c in range(d):
                left = d - c - 1                  # children still to place, each needs >= 1
                new = []
                for kids, Nn, ll in partial:
                    for sub, a, bb in gen(depth + 1, b - Nn - ll - left):
                        new.append((kids + (sub,), Nn + a, ll + bb))
                partial = new
            res.extend(partial)
        return tuple(res)

    return gen(0, budget)


def part1():
    fails = 0
    compared = 0
    for name, (pi, span) in LAWS.items():
        if not name.startswith("geometric"):
            assert sum(pi.values()) == 1 and mean(pi) == 1, name
        S = convolution_powers(pi, N_MAX, N_MAX)
        n_trees = n_cmp = n_pos = n_bad = 0
        for n in range(2, N_MAX + 1):
            ts = trees(n, pi.keys())
            weights = [gw_weight_tree(t, pi) for t in ts]
            Z = sum(weights)                                  # P(|T| = n)
            if Z != S[n][n - 1] / n:                          # Otter-Dwass
                print("  OTTER-DWASS FAIL", name, n)
                n_bad += 1
            if Z == 0:
                continue
            n_trees += len(ts)
            for k in KS:
                law = {}
                for t, w in zip(ts, weights):
                    tt, N, l = truncate(t, k)
                    law[tt] = law.get(tt, F(0)) + w / Z
                seen = 0
                for tt, N, l in all_truncations(pi.keys(), k, n):
                    if l >= 1:
                        formula = (gw_weight_trunc(tt, pi) * F(n * l) * S[n - N][n - N - l]
                                   / (F(n - N) * S[n][n - 1]))
                    else:
                        formula = gw_weight_trunc(tt, pi) / Z if N == n else F(0)
                    p = law.get(tt, F(0))
                    if p:
                        seen += 1
                        n_pos += 1
                    n_cmp += 1
                    if formula != p:
                        n_bad += 1
                        if n_bad <= 3:
                            print("   MISMATCH", name, "n=%d k=%d N=%d l=%d" % (n, k, N, l), p, formula)
                if seen != len(law):
                    print("  GENERATION FAIL", name, n, k, seen, len(law))
                    n_bad += 1
        print(f"  {name:16s} n = 2..{N_MAX}, k = 1,2,3: {n_trees:6d} trees, {n_cmp:6d} truncations compared "
              f"({n_pos} of positive probability), mismatches {n_bad}")
        fails += n_bad
        compared += n_cmp
    return fails, compared


def dist_after(m, g, spow):
    """Exact law of Z_g given Z_0 = m."""
    dist = {m: F(1)}
    for _ in range(g):
        new = {}
        for z, pz in dist.items():
            for v, pv in enumerate(spow[z]):
                if pv:
                    new[v] = new.get(v, F(0)) + pz * pv
        dist = new
    return dist


def part2():
    fails = 0
    count = 0
    for name, (pi, span) in LAWS.items():
        if name.startswith("geometric"):
            continue                                       # Part 2 uses the four finite-support laws
        dmax = max(pi)
        mmax = 4 * dmax ** 2                               # Z_{g-1} <= m dmax^(g-1) <= 4 dmax^2
        spow = convolution_powers(pi, mmax, dmax * mmax)
        mom = {s: sum(F(d) ** s * p for d, p in pi.items()) for s in (1, 2, 3)}
        for g in (1, 2, 3):
            base = dist_after(1, g, spow)
            for m in range(1, 5):
                dist = dist_after(m, g, spow)
                count += 1
                if sum(dist.values()) != 1 or sum(z * p for z, p in dist.items()) != m:
                    fails += 1
                    print("  MEAN FAIL", name, m, g)
                for s in (1, 2, 3):
                    lhs = sum(F(z) ** s * p for z, p in dist.items())
                    one = sum(F(z) ** s * p for z, p in base.items())
                    count += 1
                    if not (lhs <= F(m) ** s * one <= F(m) ** s * mom[s] ** g):
                        fails += 1
                        print("  MOMENT FAIL", name, m, g, s)
                for s in (0.5, 1.5, 2.5):
                    lhs = sum(float(z) ** s * float(p) for z, p in dist.items())
                    if s < 1:
                        bound = float(m) ** s
                    else:
                        bound = float(m) ** s * sum(float(z) ** s * float(p) for z, p in base.items())
                        top = float(m) ** s * sum(float(d) ** s * float(p) for d, p in pi.items()) ** g
                        if bound > top * (1 + 1e-12):
                            bound = float("inf")           # E Z_g^s <= (E xi^s)^g fails: count as a failure below
                    count += 1
                    if lhs > bound * (1 + 1e-12) or bound == float("inf"):
                        fails += 1
                        print("  MOMENT FAIL (float)", name, m, g, s)
    return fails, count


if __name__ == "__main__":
    print("Part 1: Lemma 2.1 (law of the first k generations of T_n), exact")
    f1, c1 = part1()
    print(f"  total: {c1} truncations compared, {f1} failures")
    print("Part 2: Lemma 2.3 (conditional moments of generation sizes)")
    f2, c2 = part2()
    print(f"  total: {c2} checks, {f2} failures")
    ok = (f1 == 0 and f2 == 0)
    print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
    sys.exit(0 if ok else 1)
