"""Candidate universal code (EVIDENCE): for Boolean f, take a decision tree that queries variables in a fixed
order pi, skipping variables irrelevant to the current subfunction ("reduced ordered DT"). Gates = cells of the
1-leaves (conjunctions, M = 1), law = paper's Q_{1,1} (a = 6/5), path order inside each gate, code length via
the SUM over all single-root witnesses (Lemma 3.2). Also the complement representation (0-leaves). Report
  code(f) = min over orders and over {f, -f} of [h(v) + v Lambda + sum_A fhat(A)^2 log(1/Q(A))],
and max over all f on n <= 4 variables (by NPN class) of code(f)/I(f), with the min-witness variant too.
"""
import itertools
import math
import sys
import fei_core as fc
from queue_cost import h2, elem_sym

A_EXP = 6.0 / 5.0


def reduced_dt_leaves(T, n, order):
    """Return list of leaves (path as list of (var, value_bit), output) of the reduced ordered DT."""
    leaves = []

    def rec(fixed, idx):
        # fixed: dict var -> bit (0: x=+1, 1: x=-1)
        free = [v for v in range(n) if v not in fixed]
        vals = set()
        for assign in range(1 << len(free)):
            x = 0
            for v, b in fixed.items():
                if b:
                    x |= 1 << v
            for k, v in enumerate(free):
                if (assign >> k) & 1:
                    x |= 1 << v
            vals.add(T[x])
            if len(vals) > 1:
                break
        if len(vals) == 1:
            leaves.append((dict(fixed), vals.pop()))
            return
        # next relevant variable in order
        for v in order[idx:]:
            if v in fixed:
                continue
            # relevant in subfunction?
            rel = False
            free2 = [u for u in free if u != v]
            for assign in range(1 << len(free2)):
                x = 0
                for u, b in fixed.items():
                    if b:
                        x |= 1 << u
                for k, u in enumerate(free2):
                    if (assign >> k) & 1:
                        x |= 1 << u
                if T[x] != T[x | (1 << v)]:
                    rel = True
                    break
            if rel:
                for b in (0, 1):
                    fixed[v] = b
                    rec(fixed, order.index(v) + 1)
                    del fixed[v]
                return
        raise RuntimeError("nonconstant subfunction without relevant variable")

    rec({}, 0)
    return leaves


def code_from_leaves(masses, v, leaves, target, n):
    """Gates: leaves with output == target. Path order = order of insertion (dict preserves query order)."""
    gates = []
    for fixed, out in leaves:
        if out != target:
            continue
        path = list(fixed.keys())
        p = 2.0 ** (-len(path))
        gates.append((min(p, 0.5), {u: i + 1 for i, u in enumerate(path)}))
    Lam = sum(math.log1p(pi) for pi, _ in gates) / math.log(2)
    tot_sum = h2(v) + v * Lam
    tot_min = tot_sum
    for S, m in masses.items():
        if S == 0:
            continue
        s = fc.popcount(S)
        terms = []
        for pi, ranks in gates:
            if any(((S >> u) & 1) and u not in ranks for u in range(n)):
                continue
            th = [min(1.0, (s / r) ** A_EXP) for r in ranks.values()]
            if s > len(th):
                continue
            Z = elem_sym(th, s)[s]
            lp = math.log2(pi) - math.log2(s * (s + 1)) - 1 - math.log2(Z)
            for u in range(n):
                if (S >> u) & 1:
                    lp += math.log2(min(1.0, (s / ranks[u]) ** A_EXP))
            terms.append(lp)
        if not terms:
            return math.inf, math.inf
        tot_sum += m * (-math.log2(sum(2.0 ** t for t in terms)))
        tot_min += m * (-max(terms))
    return tot_sum, tot_min


def transforms(n):
    out = []
    for perm in itertools.permutations(range(n)):
        for neg in range(1 << n):
            out.append((perm, neg))
    return out


def apply(T, n, perm, neg, oneg):
    R = [0] * (1 << n)
    for x in range(1 << n):
        y = 0
        for i in range(n):
            if (x >> i) & 1:
                y |= 1 << perm[i]
        y ^= neg
        R[y] = -T[x] if oneg else T[x]
    return R


if __name__ == '__main__':
    n = int(sys.argv[1])
    N = 1 << n
    tr = transforms(n)
    seen = set()
    worst_sum = (0, None)
    worst_min = (0, None)
    worst_H = (0, None)
    classes = 0
    for code in range(1 << N):
        if code in seen:
            continue
        T = [1 - 2 * ((code >> x) & 1) for x in range(N)]
        for perm, neg in tr:
            for oneg in (0, 1):
                R = apply(T, n, perm, neg, oneg)
                c = sum(((1 - r) // 2) << x for x, r in enumerate(R))
                seen.add(c)
        classes += 1
        H, I, var, masses = fc.entropy_influence_exact(T)
        if I == 0:
            continue
        fm = {S: float(m) for S, m in masses.items()}
        v = float(var)
        best_sum = math.inf
        best_min = math.inf
        for order in itertools.permutations(range(n)):
            leaves = reduced_dt_leaves(T, n, list(order))
            for target in (1, -1):
                cs, cm = code_from_leaves(fm, v, leaves, target, n)
                best_sum = min(best_sum, cs)
                best_min = min(best_min, cm)
        r_sum, r_min, r_H = best_sum / float(I), best_min / float(I), H / float(I)
        if r_sum > worst_sum[0]:
            worst_sum = (r_sum, T)
        if r_min > worst_min[0]:
            worst_min = (r_min, T)
        if r_H > worst_H[0]:
            worst_H = (r_H, T)
    print(f"n={n}: NPN classes={classes}; max over f of min-over-DT code/I: witness-sum {worst_sum[0]:.4f}, "
          f"min-witness {worst_min[0]:.4f}; max H/I {worst_H[0]:.4f}")
    print("worst witness-sum table:", worst_sum[1])
