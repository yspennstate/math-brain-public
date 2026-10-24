#!/usr/bin/env python3
"""POS3 double-predecessor-fan -> dual strict-chain corridor regression.

This is a development-side exact checker for analytic statements in the
accompanying report.  It enumerates naturally labelled transitively closed
posets through n=6 and checks every width<=3 successor-free double-predecessor
fan.  It also checks one explicit 9-point adversary to an over-strong local
shortcut.  Finite enumeration is NOT used as arbitrary-size closure.
"""
from functools import lru_cache
from fractions import Fraction

def closure_from_mask(n, mask):
    rows = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> k) & 1:
                rows[i] |= 1 << j
            k += 1
    for j in range(n - 1, -1, -1):
        for i in range(j):
            if (rows[i] >> j) & 1:
                rows[i] |= rows[j]
    return tuple(rows)

def closure_from_edges(n, edges):
    rows = [0] * n
    for i, j in edges:
        assert i < j
        rows[i] |= 1 << j
    for j in range(n - 1, -1, -1):
        for i in range(j):
            if (rows[i] >> j) & 1:
                rows[i] |= rows[j]
    return tuple(rows)

def comparable(rows, x, y):
    return bool(((rows[x] >> y) & 1) or ((rows[y] >> x) & 1))

def pred_succ(rows):
    n = len(rows)
    succ = [{j for j in range(n) if (rows[i] >> j) & 1} for i in range(n)]
    pred = [{i for i in range(n) if (rows[i] >> j) & 1} for j in range(n)]
    return pred, succ

def poset_width(rows):
    n = len(rows)
    best = 0
    for mask in range(1 << n):
        if mask.bit_count() <= best:
            continue
        xs = [i for i in range(n) if (mask >> i) & 1]
        if all(not comparable(rows, xs[i], xs[j])
               for i in range(len(xs)) for j in range(i + 1, len(xs))):
            best = len(xs)
    return best

def maximal_in(D, succ):
    return {d for d in D if not any(e != d and e in succ[d] for e in D)}

def is_chain(S, rows):
    xs = list(S)
    return all(comparable(rows, xs[i], xs[j])
               for i in range(len(xs)) for j in range(i + 1, len(xs)))

def is_cover(rows, x, y):
    if not ((rows[x] >> y) & 1):
        return False
    n = len(rows)
    return not any(k != x and k != y and
                   ((rows[x] >> k) & 1) and ((rows[k] >> y) & 1)
                   for k in range(n))

def graph_connected(rows, incomparability=False):
    n = len(rows)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            is_comp = comparable(rows, i, j)
            if is_comp != incomparability:
                adj[i].add(j)
                adj[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    return len(seen) == n

def linear_extensions(rows):
    n = len(rows)
    pm = [0] * n
    for i in range(n):
        for j in range(n):
            if (rows[i] >> j) & 1:
                pm[j] |= 1 << i
    @lru_cache(None)
    def rec(mask):
        if mask == (1 << n) - 1:
            return ((),)
        out = []
        for x in range(n):
            if not ((mask >> x) & 1) and (pm[x] & ~mask) == 0:
                for tail in rec(mask | (1 << x)):
                    out.append((x,) + tail)
        return tuple(out)
    return rec(0)

def pair_count(exts, x, y):
    return sum(L.index(x) < L.index(y) for L in exts)

def balanced(num, den):
    return den <= 3 * num <= 2 * den

def exhaustive_regression():
    total = width3 = fans = eq = strict = 0
    fork_configs = fork_equal = fork_strict = 0
    for n in range(2, 7):
        seen = set()
        npairs = n * (n - 1) // 2
        for mask in range(1 << npairs):
            rows = closure_from_mask(n, mask)
            if rows in seen:
                continue
            seen.add(rows)
            total += 1
            if poset_width(rows) > 3:
                continue
            width3 += 1
            pred, succ = pred_succ(rows)

            # General fork-sibling strengthening of the account01/B11 nesting lemma.
            for a0 in range(n):
                for b0 in range(n):
                    if a0 == b0 or comparable(rows, a0, b0):
                        continue
                    if not (pred[b0] <= pred[a0]):
                        continue
                    ups = [u for u in range(n)
                           if is_cover(rows, a0, u) and not comparable(rows, u, b0)]
                    for ii in range(len(ups)):
                        for jj in range(ii + 1, len(ups)):
                            u, v = ups[ii], ups[jj]
                            if comparable(rows, u, v):
                                continue
                            fork_configs += 1
                            pu, pv = pred[u], pred[v]
                            assert pu <= pv or pv <= pu
                            if pu == pv:
                                fork_equal += 1
                            else:
                                fork_strict += 1
                                Duv = (pu - pv) if pv < pu else (pv - pu)
                                assert Duv and is_chain(Duv, rows)

            for a in range(n):
                for b in range(n):
                    if a == b or comparable(rows, a, b):
                        continue
                    if not (pred[b] < pred[a]):
                        continue
                    D = pred[a] - pred[b]
                    T = maximal_in(D, succ)
                    if len(T) != 2:
                        continue
                    # U empty: no successor of b is incomparable with a.
                    if any(not comparable(rows, z, a) for z in succ[b]):
                        continue
                    fans += 1
                    # U=empty implies Succ(b) subseteq Succ(a).
                    assert succ[b] <= succ[a]
                    t1, t2 = tuple(T)
                    assert not comparable(rows, t1, t2)
                    assert not comparable(rows, t1, b)
                    assert not comparable(rows, t2, b)
                    assert is_cover(rows, t1, a)
                    assert is_cover(rows, t2, a)

                    # New analytic reduction: dual fork nesting.
                    s1, s2 = succ[t1], succ[t2]
                    assert s1 <= s2 or s2 <= s1
                    if s1 == s2:
                        eq += 1
                    else:
                        strict += 1
                        V = (s1 - s2) if s2 < s1 else (s2 - s1)
                        assert V
                        assert is_chain(V, rows)
    return total, width3, fork_configs, fork_equal, fork_strict, fans, eq, strict

def adversary_regression():
    # Transitive reduction on 0,...,8.
    covers = [
        (0,4), (1,2), (2,3), (3,4),
        (3,7), (4,8), (4,5), (6,8),
    ]
    rows = closure_from_edges(9, covers)
    assert poset_width(rows) == 3
    assert graph_connected(rows, incomparability=False)
    assert graph_connected(rows, incomparability=True)
    pred, succ = pred_succ(rows)
    a, b = 8, 7
    T = maximal_in(pred[a] - pred[b], succ)
    assert pred[b] == {1,2,3}
    assert pred[a] == {0,1,2,3,4,6}
    assert T == {4,6}
    assert succ[a] == succ[b] == set()
    assert not comparable(rows, a, b)
    assert all(not comparable(rows, b, t) for t in T)
    assert not comparable(rows, 4, 6)
    assert succ[6] < succ[4]
    assert succ[4] - succ[6] == {5}
    assert is_chain(succ[4] - succ[6], rows)

    exts = linear_extensions(rows)
    E = len(exts)
    assert E == 243
    Nab = pair_count(exts, a, b)
    Nb4 = pair_count(exts, b, 4)
    Nb6 = pair_count(exts, b, 6)
    N46 = pair_count(exts, 4, 6)
    H = sum(L.index(b) < L.index(4) and L.index(b) < L.index(6) for L in exts)
    R = Nb4 + Nb6 - H
    assert (Nab, Nb4, Nb6, N46, H, R) == (76, 75, 43, 63, 27, 91)
    assert R == E - 2 * Nab
    # Endpoint and all three fan-local pairs are unbalanced.
    assert not balanced(Nab, E)
    assert not balanced(Nb4, E)
    assert not balanced(Nb6, E)
    assert not balanced(N46, E)
    # Yet a global balanced escape exists; the poset is not a POS3 counterexample.
    N02 = pair_count(exts, 0, 2)
    assert N02 == 114 and balanced(N02, E)
    return {
        "E": E,
        "a_before_b": Fraction(Nab, E),
        "b_before_t1": Fraction(Nb4, E),
        "b_before_t2": Fraction(Nb6, E),
        "t1_before_t2": Fraction(N46, E),
        "reverse_union": Fraction(R, E),
        "balanced_escape_0_before_2": Fraction(N02, E),
    }

if __name__ == "__main__":
    total, width3, fork_configs, fork_equal, fork_strict, fans, eq, strict = exhaustive_regression()
    adv = adversary_regression()
    print("naturally_labelled_transitive_posets_n2_to_n6", total)
    print("width_at_most_3", width3)
    print("fork_sibling_configurations", fork_configs)
    print("fork_equal_predecessor_siblings", fork_equal)
    print("fork_strict_predecessor_siblings", fork_strict)
    print("fork_strict_chain_differences", fork_strict)
    print("successor_free_double_predecessor_fans", fans)
    print("equal_successor_fans", eq)
    print("strict_successor_fans", strict)
    print("strict_chain_difference_fans", strict)
    print("adversary_extensions", adv["E"])
    for k in ["a_before_b","b_before_t1","b_before_t2","t1_before_t2",
              "reverse_union","balanced_escape_0_before_2"]:
        print(k, adv[k])
    print("POS3_DOUBLE_FAN_DUAL_CORRIDOR_V1_PASS")
