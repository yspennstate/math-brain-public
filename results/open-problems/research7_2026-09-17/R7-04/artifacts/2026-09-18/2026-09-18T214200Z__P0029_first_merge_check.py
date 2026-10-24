#!/usr/bin/env python3
"""Exact self-check for R7-04 / P0029 first-merge theorem.

For every labeled connected simple graph on n<=5 vertices:
  * brute-force W(r,v), the number of permutations whose births are exactly r,v;
  * compute the positive first-merge decomposition;
  * verify the ordered identity pair-by-pair;
  * verify the unordered Pascal-mixture identity;
  * verify h_C(r)=sum_{s~r} F_C({r,s}) on every connected induced C.

All arithmetic is exact integers. No randomness.
"""
from functools import lru_cache
from itertools import permutations
from math import comb


def graph_adj_from_edges(n, edge_mask):
    adj = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (edge_mask >> k) & 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            k += 1
    return adj


def components(adj, mask):
    rem = mask
    out = []
    while rem:
        b = rem & -rem
        root = b.bit_length() - 1
        seen = b
        stack = [root]
        while stack:
            u = stack.pop()
            m = adj[u] & rem & ~seen
            while m:
                q = m & -m
                seen |= q
                stack.append(q.bit_length() - 1)
                m ^= q
        out.append(seen)
        rem &= ~seen
    return out


def connected(adj, mask):
    return mask != 0 and len(components(adj, mask)) == 1


def make_F(adj, universe):
    @lru_cache(None)
    def F(mask):
        if mask == universe:
            return 1
        frontier = 0
        m = mask
        while m:
            b = m & -m
            frontier |= adj[b.bit_length() - 1]
            m ^= b
        frontier &= universe & ~mask
        ans = 0
        m = frontier
        while m:
            b = m & -m
            ans += F(mask | b)
            m ^= b
        return ans
    return F


def h_root(adj, C, r):
    verts = [x for x in range(len(adj)) if (C >> x) & 1 and x != r]
    ans = 0
    for tail in permutations(verts):
        S = 1 << r
        ok = True
        for x in tail:
            if not (adj[x] & S):
                ok = False
                break
            S |= 1 << x
        ans += int(ok)
    return ans


def brute_W(adj, r, v):
    n = len(adj)
    ans = 0
    for p in permutations(range(n)):
        if p[0] != r:
            continue
        S = 0
        births = []
        for x in p:
            if not (adj[x] & S):
                births.append(x)
            S |= 1 << x
        ans += int(births == [r, v])
    return ans


def ordered_merge_W(adj, r, v, F):
    n = len(adj)
    ans = 0
    for S in range(1 << n):
        if not ((S >> r) & 1 and (S >> v) & 1):
            continue
        cc = components(adj, S)
        if len(cc) != 2:
            continue
        A = next((C for C in cc if (C >> r) & 1), None)
        B = next((C for C in cc if (C >> v) & 1), None)
        if A is None or B is None or A == B:
            continue
        g = 0
        for x in range(n):
            if (S >> x) & 1:
                continue
            if (adj[x] & A) and (adj[x] & B):
                g += F(S | (1 << x))
        if not g:
            continue
        ans += (h_root(adj, A, r) * h_root(adj, B, v)
                * comb(S.bit_count() - 1, A.bit_count() - 1) * g)
    return ans


def unordered_merge_H(adj, r, v, F):
    n = len(adj)
    ans = 0
    for S in range(1 << n):
        if not ((S >> r) & 1 and (S >> v) & 1):
            continue
        cc = components(adj, S)
        if len(cc) != 2:
            continue
        A = next((C for C in cc if (C >> r) & 1), None)
        B = next((C for C in cc if (C >> v) & 1), None)
        if A is None or B is None or A == B:
            continue
        g = 0
        for x in range(n):
            if (S >> x) & 1:
                continue
            if (adj[x] & A) and (adj[x] & B):
                g += F(S | (1 << x))
        if not g:
            continue
        ans += (h_root(adj, A, r) * h_root(adj, B, v)
                * comb(S.bit_count(), A.bit_count()) * g)
    return ans


def induced_conductance_check(adj, C):
    if C.bit_count() == 1:
        return True
    FC = make_F(adj, C)
    for r in range(len(adj)):
        if not ((C >> r) & 1):
            continue
        lhs = h_root(adj, C, r)
        rhs = 0
        m = adj[r] & C
        while m:
            b = m & -m
            rhs += FC((1 << r) | b)
            m ^= b
        if lhs != rhs:
            return False
    return True


def main():
    total_connected = 0
    total_ordered_pairs = 0
    total_unordered_pairs = 0
    total_connected_induced = 0
    by_n = []
    for n in range(2, 6):
        E = n * (n - 1) // 2
        cn = op = up = ci = 0
        full = (1 << n) - 1
        for em in range(1 << E):
            adj = graph_adj_from_edges(n, em)
            if not connected(adj, full):
                continue
            cn += 1
            F = make_F(adj, full)

            for C in range(1, 1 << n):
                if connected(adj, C):
                    assert induced_conductance_check(adj, C)
                    ci += 1

            for r in range(n):
                for v in range(n):
                    if r == v or ((adj[r] >> v) & 1):
                        continue
                    brute = brute_W(adj, r, v)
                    merge = ordered_merge_W(adj, r, v, F)
                    assert brute == merge, (n, em, r, v, brute, merge)
                    op += 1

            for r in range(n):
                for v in range(r + 1, n):
                    if (adj[r] >> v) & 1:
                        continue
                    brute = brute_W(adj, r, v) + brute_W(adj, v, r)
                    merge = unordered_merge_H(adj, r, v, F)
                    assert brute == merge, ("unordered", n, em, r, v, brute, merge)
                    up += 1

        by_n.append((n, cn, op, up, ci))
        total_connected += cn
        total_ordered_pairs += op
        total_unordered_pairs += up
        total_connected_induced += ci

    print("R7-04 P0029 exact first-merge theorem self-check")
    print("arithmetic=exact_integer")
    print("randomness=none")
    for n, cn, op, up, ci in by_n:
        print(f"n={n} connected_graphs={cn} ordered_pairs={op} "
              f"unordered_pairs={up} connected_induced_checks={ci}")
    print(f"TOTAL connected_graphs={total_connected}")
    print(f"TOTAL ordered_pair_identities={total_ordered_pairs}")
    print(f"TOTAL unordered_pair_identities={total_unordered_pairs}")
    print(f"TOTAL rooted_conductance_graph_subset_checks={total_connected_induced}")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
