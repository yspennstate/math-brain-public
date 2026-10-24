#!/usr/bin/env python3
"""Exact verifier for HARD8-01 checkpoint 4.

Checks the canonical rank-reducing normal form for automata whose letters are
permutations or simple idempotents, and the generator-sensitive formula for the
regular one-idempotent synchronizing case.

All computations are finite and exact; no floating point or external solver is
used.
"""
from collections import deque
from itertools import permutations, combinations
from math import gcd
from random import Random


def compose(g, h):
    """Right-action product: apply g, then h."""
    return tuple(h[g[i]] for i in range(len(g)))


def inverse(g):
    inv = [0] * len(g)
    for i, j in enumerate(g):
        inv[j] = i
    return tuple(inv)


def generated_group(n, gens):
    ident = tuple(range(n))
    arr = [ident]
    idx = {ident: 0}
    q = deque([ident])
    while q:
        g = q.popleft()
        for p in gens:
            h = compose(g, p)
            if h not in idx:
                idx[h] = len(arr)
                arr.append(h)
                q.append(h)
    return arr, idx


def simple_idempotent(n, s, t):
    a = list(range(n))
    a[s] = t
    return tuple(a)


def apply_mask(mask, trans):
    out = 0
    while mask:
        bit = mask & -mask
        i = bit.bit_length() - 1
        out |= 1 << trans[i]
        mask -= bit
    return out


def ordinary_rank_thresholds(n, perm_gens, singulars):
    letters = list(perm_gens) + [simple_idempotent(n, s, t) for s, t in singulars]
    full = (1 << n) - 1
    q = deque([full])
    dist = {full: 0}
    best = [None] * (n + 1)
    while q:
        mask = q.popleft()
        d = dist[mask]
        k = mask.bit_count()
        if best[k] is None or d < best[k]:
            best[k] = d
        for tr in letters:
            nxt = apply_mask(mask, tr)
            if nxt not in dist:
                dist[nxt] = d + 1
                q.append(nxt)
    return best


def canonical_rank_thresholds(n, perm_gens, singulars):
    """BFS in the conjugated-hole normal form.

    Permutation letters move the current group prefix. A simple idempotent is
    allowed only when its conjugated defect arc has both endpoints live, so it
    removes exactly its source. The theorem predicts equality with ordinary
    thresholds at every reachable rank.
    """
    G, idx = generated_group(n, perm_gens)
    ident = tuple(range(n))
    invs = [inverse(g) for g in G]
    gnext = [[idx[compose(g, p)] for p in perm_gens] for g in G]
    arcs = [[(inv[s], inv[t]) for (s, t) in singulars] for inv in invs]

    full = (1 << n) - 1
    start = (full, idx[ident])
    q = deque([start])
    dist = {start: 0}
    best = [None] * (n + 1)
    while q:
        mask, gi = q.popleft()
        d = dist[(mask, gi)]
        k = mask.bit_count()
        if best[k] is None or d < best[k]:
            best[k] = d

        for gj in gnext[gi]:
            st = (mask, gj)
            if st not in dist:
                dist[st] = d + 1
                q.append(st)

        for r, t in arcs[gi]:
            if ((mask >> r) & 1) and ((mask >> t) & 1):
                nxt = mask & ~(1 << r)
                st = (nxt, gi)
                if st not in dist:
                    dist[st] = d + 1
                    q.append(st)
    return best


def min_rank_from_thresholds(best):
    return min(k for k in range(1, len(best)) if best[k] is not None)


def exhaustive_normal_form_checks():
    total = 0
    sync = 0

    for n in range(2, 6):
        ps = list(permutations(range(n)))
        es = [(s, t) for s in range(n) for t in range(n) if s != t]
        for p in ps:
            for e in es:
                a = ordinary_rank_thresholds(n, [p], [e])
                b = canonical_rank_thresholds(n, [p], [e])
                assert a == b, (n, p, e, a, b)
                total += 1
                sync += a[1] is not None

    n = 4
    ps = list(permutations(range(n)))
    es = [(s, t) for s in range(n) for t in range(n) if s != t]

    for P in combinations(ps, 2):
        for e in es:
            a = ordinary_rank_thresholds(n, list(P), [e])
            b = canonical_rank_thresholds(n, list(P), [e])
            assert a == b, ("2p1e", P, e, a, b)
            total += 1
            sync += a[1] is not None

    for p in ps:
        for E in combinations(es, 2):
            a = ordinary_rank_thresholds(n, [p], list(E))
            b = canonical_rank_thresholds(n, [p], list(E))
            assert a == b, ("1p2e", p, E, a, b)
            total += 1
            sync += a[1] is not None

    rng = Random(801)
    n = 5
    ps = list(permutations(range(n)))
    es = [(s, t) for s in range(n) for t in range(n) if s != t]
    for _ in range(1000):
        P = rng.sample(ps, 2)
        E = rng.sample(es, 2)
        a = ordinary_rank_thresholds(n, P, E)
        b = canonical_rank_thresholds(n, P, E)
        assert a == b, ("sample-2p2e", P, E, a, b)
        total += 1
        sync += a[1] is not None

    return total, sync


def residue_distance(n, steps, target):
    q = deque([0])
    dist = {0: 0}
    while q:
        x = q.popleft()
        if x == target:
            return dist[x]
        for s in steps:
            y = (x + s) % n
            if y not in dist:
                dist[y] = dist[x] + 1
                q.append(y)
    return None


def cyclic_regular_formula_checks(max_n=10):
    checked = 0
    for n in range(2, max_n + 1):
        increments = list(range(1, n))
        for mask in range(1, 1 << len(increments)):
            steps = [increments[i] for i in range(len(increments)) if (mask >> i) & 1]
            g = n
            for s in steps:
                g = gcd(g, s)
            if g != 1:
                continue
            P = [tuple((i + s) % n for i in range(n)) for s in steps]
            for h in range(1, n):
                if gcd(n, h) != 1:
                    continue
                ell = residue_distance(n, steps, (-h) % n)
                assert ell is not None
                predicted = (n - 1) + (n - 2) * ell
                actual = ordinary_rank_thresholds(n, P, [(0, h)])[1]
                assert actual == predicted, (n, steps, h, ell, actual, predicted)
                checked += 1
    return checked


def perm_mul(a, b):
    return tuple(b[a[i]] for i in range(3))


def perm_order(a):
    ident = (0, 1, 2)
    x = ident
    for k in range(1, 20):
        x = perm_mul(x, a)
        if x == ident:
            return k
    raise AssertionError("order too large")


def regular_action(group_elems, mul, generators, h):
    idx = {g: i for i, g in enumerate(group_elems)}
    n = len(group_elems)
    P = []
    for a in generators:
        P.append(tuple(idx[mul(g, a)] for g in group_elems))
    ident = group_elems[0]
    return n, P, idx[ident], idx[h]


def noncyclic_regular_minrank_checks():
    checks = []

    V4 = [0, 1, 2, 3]
    mul_v4 = lambda a, b: a ^ b
    for h in [1, 2, 3]:
        n, P, s, t = regular_action(V4, mul_v4, [1, 2], h)
        best = ordinary_rank_thresholds(n, P, [(s, t)])
        actual = min_rank_from_thresholds(best)
        predicted = n // 2
        assert actual == predicted, ("V4", h, actual, predicted)
        checks.append(("V4", h, actual))

    S3 = list(permutations(range(3)))
    ident = (0, 1, 2)
    S3.remove(ident)
    S3.insert(0, ident)
    transposition = (1, 0, 2)
    cycle3 = (1, 2, 0)
    for h in [transposition, cycle3]:
        n, P, s, t = regular_action(S3, perm_mul, [transposition, cycle3], h)
        best = ordinary_rank_thresholds(n, P, [(s, t)])
        actual = min_rank_from_thresholds(best)
        predicted = n // perm_order(h)
        assert actual == predicted, ("S3", h, actual, predicted)
        checks.append(("S3", perm_order(h), actual))

    return checks


def prior_cyclic_family_bridge_checks(max_n=13):
    checked = 0
    for n in range(2, max_n + 1):
        a = tuple((i + 1) % n for i in range(n))
        for d in range(1, n):
            best = ordinary_rank_thresholds(n, [a], [(0, d)])
            if gcd(n, d) == 1:
                predicted = (n - 2) * (n - d) + n - 1
                assert best[1] == predicted, (n, d, best[1], predicted)
            else:
                assert best[1] is None, (n, d, best[1])
            checked += 1
    return checked


def main():
    total, sync = exhaustive_normal_form_checks()
    cyclic = cyclic_regular_formula_checks()
    reg = noncyclic_regular_minrank_checks()
    bridge = prior_cyclic_family_bridge_checks()

    print("HARD8-01 checkpoint 4 exact verifier: PASS")
    print(f"small SI threshold comparisons: {total} automata; synchronizing={sync}")
    print(f"regular cyclic generator-sensitive formula checks: {cyclic}")
    print(f"regular noncyclic minimum-rank checks: {len(reg)} -> {reg}")
    print(f"prior cyclic-family bridge checks: {bridge}")


if __name__ == "__main__":
    main()
