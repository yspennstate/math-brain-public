"""Finite checks of the identities used in the paper.

(1) Enumeration of all recursive trees with n <= 8 vertices: the mean profile equals the coefficients of
    prod_{j<n} (1 + z/j), and the mean number of ordered pairs of distinct vertices both at depth k equals
        sum_j (1/j) sum_{d<k} f_{j,d} q_{j,2(k-d)-1} binom(2(k-d), k-d),
    where q_{j,l} = [t^l] prod_{l'=j+1}^{n-1} (1 + t/l').
(2) Monte Carlo on K_n, n = 3..6, with Exp(1) weights: E N_{n,k} = (n/2) sum_{d>=k} f_{n,d} and
    P(M_n = n-1) = n/(2 (n-1)!).

usage:  python check_small.py [reps] [seed] [out.json]
"""
import itertools
import json
import math
import random
import sys
from fractions import Fraction


def profile_exact(n):
    f = [Fraction(1)]
    for j in range(1, n):
        g = f + [Fraction(0)]
        for d in range(len(f), 0, -1):
            g[d] += f[d - 1] / j
        f = g
    return f


def q_coeffs(j, n):
    """Coefficients of prod_{l=j+1}^{n-1} (1 + t/l)."""
    q = [Fraction(1)]
    for l in range(j + 1, n):
        g = q + [Fraction(0)]
        for d in range(len(q), 0, -1):
            g[d] += q[d - 1] / l
        q = g
    return q


def pair_formula(n, k):
    total = Fraction(0)
    for j in range(1, n):
        f = profile_exact(j)
        q = q_coeffs(j, n)
        for d in range(0, k):
            s = k - d
            if d < len(f) and 2 * s - 1 < len(q):
                total += Fraction(1, j) * f[d] * q[2 * s - 1] * math.comb(2 * s, s)
    return total


def enumerate_trees(n):
    """Mean profile and mean number of ordered distinct pairs at equal depth k, over all recursive trees."""
    prof = [Fraction(0)] * n
    pairs = [Fraction(0)] * n
    count = 0
    for parents in itertools.product(*[range(i) for i in range(1, n)]):
        depth = [0]
        for p in parents:
            depth.append(depth[p] + 1)
        z = [0] * n
        for d in depth:
            z[d] += 1
        for d in range(n):
            prof[d] += z[d]
            pairs[d] += z[d] * (z[d] - 1)
        count += 1
    assert count == math.factorial(n - 1)
    return [x / count for x in prof], [x / count for x in pairs]


def monte_carlo(n, reps, rng):
    """All-pairs hopcounts of minimum-weight paths in K_n by Floyd-Warshall."""
    counts = [0] * n          # counts[k] = number of (graph, pair) with hopcount >= k
    top = 0
    for _ in range(reps):
        dist = [[0.0] * n for _ in range(n)]
        hop = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                x = rng.expovariate(1.0)
                dist[i][j] = dist[j][i] = x
                hop[i][j] = hop[j][i] = 1
        for m in range(n):
            dm = dist[m]
            hm = hop[m]
            for i in range(n):
                if i == m:
                    continue
                di = dist[i]
                dim = di[m]
                for j in range(n):
                    if j == i or j == m:
                        continue
                    nd = dim + dm[j]
                    if nd < di[j]:
                        di[j] = nd
                        hop[i][j] = hop[i][m] + hm[j]
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                h = hop[i][j]
                best = max(best, h)
                for k in range(1, h + 1):
                    counts[k] += 1
        if best == n - 1:
            top += 1
    return [c / reps for c in counts], top / reps


def main():
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261111
    out = {"reps": reps, "seed": seed, "trees": {}, "graphs": {}}

    for n in range(2, 9):
        prof, pairs = enumerate_trees(n)
        assert prof == profile_exact(n), n
        for k in range(1, n):
            assert pairs[k] == pair_formula(n, k), (n, k)
        out["trees"][n] = {"profile": [str(x) for x in prof], "pairs_at_depth_k": [str(x) for x in pairs]}
        print("recursive trees, n=%d: profile and pair formula agree with the enumeration of %d trees"
              % (n, math.factorial(n - 1)))

    rng = random.Random(seed)
    for n in range(3, 7):
        f = profile_exact(n)
        est, top = monte_carlo(n, reps, rng)
        exact = [float(Fraction(n, 2) * sum(f[k:])) for k in range(1, n)]
        ptop = n / (2.0 * math.factorial(n - 1))
        se_top = math.sqrt(ptop * (1 - ptop) / reps)
        out["graphs"][n] = {"EN_exact": exact, "EN_estimate": est[1:], "P_top_exact": ptop, "P_top_estimate": top,
                            "P_top_standard_error": se_top}
        print("K_%d, %d graphs: P(M=n-1) exact %.5f, estimate %.5f (s.e. %.5f)" % (n, reps, ptop, top, se_top))
        print("      E N_{n,k} exact:    " + " ".join("%.4f" % x for x in exact))
        print("      E N_{n,k} estimate: " + " ".join("%.4f" % x for x in est[1:]))

    if len(sys.argv) > 3:
        with open(sys.argv[3], "w") as fh:
            json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
