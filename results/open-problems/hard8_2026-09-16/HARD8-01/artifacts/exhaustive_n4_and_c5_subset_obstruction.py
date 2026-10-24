"""Exact finite checks supporting HARD8-01 first research checkpoint.

This script does two things using only exact finite-state BFS.

1. Enumerates every labeled ordered binary DFA on four states: 4^4 choices for
   the first transformation and 4^4 for the second, hence 65,536 automata.
   It filters to strongly connected synchronizing automata and checks the
   candidate two-rank amortization inequality

       d_2(S) <= 4*(n-|S|)+4

   for every reachable subset S with |S| >= 3, where d_2(S) is the shortest
   length of a word reducing the subset cardinality by at least two.

2. Certifies an exact five-state obstruction in the standard Cerny automaton:
   a(i)=i+1 mod 5 and b(0)=1 with b fixing 1,2,3,4.  The reachable subset
   S={1,3,4} has exact shortest synchronization distance 13, exceeding the
   proposed paired budget 12.  The word baab reaches S from Q and the word
   aabaaaabaaaab synchronizes S.

No floating-point arithmetic or heuristic search is used for the certificates.
"""

from collections import deque
from itertools import product


def apply_mask(mask, f, n):
    out = 0
    for q in range(n):
        if mask & (1 << q):
            out |= 1 << f[q]
    return out


def popcount(mask):
    return mask.bit_count()


def strongly_connected(trans, n):
    adj = [set() for _ in range(n)]
    radj = [set() for _ in range(n)]
    for f in trans:
        for q, r in enumerate(f):
            adj[q].add(r)
            radj[r].add(q)

    def reaches_all(graph):
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == n

    return reaches_all(adj) and reaches_all(radj)


def reachable_masks(trans, n):
    full = (1 << n) - 1
    seen = {full}
    queue = deque([full])
    while queue:
        s = queue.popleft()
        for f in trans:
            t = apply_mask(s, f, n)
            if t not in seen:
                seen.add(t)
                queue.append(t)
    return seen


def reset_threshold(trans, n):
    full = (1 << n) - 1
    seen = {full}
    queue = deque([(full, 0)])
    while queue:
        s, d = queue.popleft()
        if popcount(s) == 1:
            return d
        for f in trans:
            t = apply_mask(s, f, n)
            if t not in seen:
                seen.add(t)
                queue.append((t, d + 1))
    return None


def shortest_word(trans, n, start_mask, predicate):
    parent = {start_mask: (None, None)}
    queue = deque([start_mask])
    alphabet = "ab"
    while queue:
        s = queue.popleft()
        if predicate(s):
            letters = []
            cur = s
            while parent[cur][0] is not None:
                prev, letter = parent[cur]
                letters.append(letter)
                cur = prev
            return "".join(reversed(letters)), s
        for i, f in enumerate(trans):
            t = apply_mask(s, f, n)
            if t not in parent:
                parent[t] = (s, alphabet[i])
                queue.append(t)
    return None, None


def distance_drop_by_two(trans, n, start_mask):
    k = popcount(start_mask)
    target = k - 2
    word, target_mask = shortest_word(
        trans,
        n,
        start_mask,
        lambda s: popcount(s) <= target,
    )
    return len(word), word, target_mask


def exhaustive_n4_check():
    n = 4
    maps = list(product(range(n), repeat=n))
    full = (1 << n) - 1

    total = 0
    sc_sync = 0
    reachable_subset_checks = 0
    max_gap = -10**9
    tight = None

    for a in maps:
        for b in maps:
            total += 1
            trans = (a, b)
            if not strongly_connected(trans, n):
                continue
            rt = reset_threshold(trans, n)
            if rt is None:
                continue
            sc_sync += 1

            for s in reachable_masks(trans, n):
                k = popcount(s)
                if k < 3:
                    continue
                d, word, target = distance_drop_by_two(trans, n, s)
                budget = 4 * (n - k) + 4
                gap = d - budget
                reachable_subset_checks += 1
                if gap > max_gap:
                    max_gap = gap
                    tight = (a, b, s, k, d, budget, rt, word, target)
                assert d <= budget, (
                    "two-rank inequality failed at n=4",
                    a,
                    b,
                    s,
                    d,
                    budget,
                    rt,
                )

    assert total == 65536
    assert sc_sync == 18648
    assert reachable_subset_checks == 50232
    assert max_gap == 0

    print("N=4 EXACT ENUMERATION")
    print("ordered_binary_DFAs", total)
    print("strongly_connected_synchronizing", sc_sync)
    print("reachable_subset_checks_k_ge_3", reachable_subset_checks)
    print("max_gap", max_gap)
    print("tight_witness", tight)


def cerny_c5_obstruction():
    n = 5
    a = tuple((i + 1) % n for i in range(n))
    b = (1, 1, 2, 3, 4)
    trans = (a, b)
    full = (1 << n) - 1
    s = (1 << 1) | (1 << 3) | (1 << 4)  # {1,3,4}

    assert strongly_connected(trans, n)
    assert reset_threshold(trans, n) == 16

    reach_word, reached = shortest_word(trans, n, full, lambda x: x == s)
    sync_word, singleton = shortest_word(
        trans, n, s, lambda x: popcount(x) == 1
    )
    full_reset_word, full_singleton = shortest_word(
        trans, n, full, lambda x: popcount(x) == 1
    )

    paired_budget = 4 * (n - popcount(s)) + 4

    assert reached == s
    assert reach_word == "baab"
    assert len(sync_word) == 13
    assert sync_word == "aabaaaabaaaab"
    assert paired_budget == 12
    assert len(sync_word) > paired_budget
    assert len(full_reset_word) == 16
    assert full_reset_word == "baaaabaaaabaaaab"

    print("C5 EXACT OBSTRUCTION")
    print("a", a)
    print("b", b)
    print("reachable_subset", "{1,3,4}")
    print("Q_to_S_shortest_word", reach_word, "length", len(reach_word))
    print("S_reset_shortest_word", sync_word, "length", len(sync_word))
    print("paired_budget", paired_budget)
    print("full_reset_shortest_word", full_reset_word, "length", len(full_reset_word))


if __name__ == "__main__":
    exhaustive_n4_check()
    cerny_c5_obstruction()
