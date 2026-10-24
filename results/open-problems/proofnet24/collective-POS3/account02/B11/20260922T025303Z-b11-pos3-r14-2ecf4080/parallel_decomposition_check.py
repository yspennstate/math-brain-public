#!/usr/bin/env python3
"""Exact finite self-check for the POS3 parallel-decomposition reduction.

Enumerates naturally labelled transitively closed posets through n=6.
For every nonchain of width <=3 whose comparability graph is disconnected:
  1. verifies the parallel-product extension-count formula;
  2. verifies internal pair probabilities are unchanged by shuffling components;
  3. checks directly that the full poset has a 1/3--2/3 balanced pair.

This is a finite self-check of a symbolic theorem, not arbitrary-size closure.
"""
from itertools import combinations
from math import factorial

def is_transitive(n, edges):
    for i, j in edges:
        for jj, k in edges:
            if jj == j and (i, k) not in edges:
                return False
    return True

def pred_masks(n, edges):
    p = [0] * n
    for i, j in edges:
        p[j] |= 1 << i
    return p

def count_extensions(pred):
    n = len(pred)
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1 << n):
        if dp[mask] == 0:
            continue
        for x in range(n):
            if not (mask >> x) & 1 and pred[x] & ~mask == 0:
                dp[mask | (1 << x)] += dp[mask]
    return dp[-1]

def pair_numerator(pred, a, b):
    q = pred.copy()
    q[b] |= 1 << a
    return count_extensions(q)

def comparability_components(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    seen, out = set(), []
    for v in range(n):
        if v in seen:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        out.append(sorted(comp))
    return out

def poset_width(n, edges):
    comparable = {frozenset((i, j)) for i, j in edges}
    best = 0
    for mask in range(1, 1 << n):
        if mask.bit_count() <= best:
            continue
        xs = [i for i in range(n) if (mask >> i) & 1]
        if all(frozenset((a, b)) not in comparable for a, b in combinations(xs, 2)):
            best = len(xs)
    return best

def induced_pred(vertices, edges):
    idx = {v: i for i, v in enumerate(vertices)}
    return pred_masks(
        len(vertices),
        [(idx[i], idx[j]) for i, j in edges if i in idx and j in idx],
    )

def multinomial(sizes):
    out = factorial(sum(sizes))
    for s in sizes:
        out //= factorial(s)
    return out

def has_balanced_pair(n, edges, pred):
    E = count_extensions(pred)
    for a, b in combinations(range(n), 2):
        if (a, b) in edges or (b, a) in edges:
            continue
        num = pair_numerator(pred, a, b)
        if E <= 3 * num <= 2 * E:
            return True
    return False

def main():
    grand_total = grand_eligible = 0
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        total = disconnected = eligible = balanced = 0
        for bits in range(1 << len(pairs)):
            edges = {pairs[k] for k in range(len(pairs)) if (bits >> k) & 1}
            if not is_transitive(n, edges):
                continue
            total += 1
            comps = comparability_components(n, edges)
            if len(comps) <= 1:
                continue
            disconnected += 1
            if poset_width(n, edges) > 3:
                continue
            pred = pred_masks(n, edges)
            E = count_extensions(pred)

            local = []
            local_E = []
            for comp in comps:
                cp = induced_pred(comp, edges)
                local.append(cp)
                local_E.append(count_extensions(cp))

            predicted = multinomial([len(c) for c in comps])
            for ec in local_E:
                predicted *= ec
            assert E == predicted

            for comp, cp, Ec in zip(comps, local, local_E):
                idx = {v: i for i, v in enumerate(comp)}
                for a, b in combinations(comp, 2):
                    if (a, b) in edges or (b, a) in edges:
                        continue
                    num_full = pair_numerator(pred, a, b)
                    num_local = pair_numerator(cp, idx[a], idx[b])
                    assert num_full * Ec == num_local * E

            assert has_balanced_pair(n, edges, pred)
            eligible += 1
            balanced += 1

        grand_total += total
        grand_eligible += eligible
        print(
            f"n={n} transitively_closed={total} "
            f"comparability_disconnected={disconnected} "
            f"width_le_3_nonchain_checked={eligible} balanced={balanced}"
        )

    print(f"TOTAL_TRANSITIVELY_CLOSED_N2_TO_N6={grand_total}")
    print(f"TOTAL_DISCONNECTED_COMPARABILITY_WIDTH_LE_3_CHECKED={grand_eligible}")
    print("POS3_PARALLEL_DECOMPOSITION_CHECK_PASS")

if __name__ == "__main__":
    main()
