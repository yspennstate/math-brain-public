#!/usr/bin/env python3
"""Independent exact/high-precision audit of B05_A023_QUADRATIC_ADAPTIVE_TREE_v1."""

from fractions import Fraction
from functools import lru_cache
import math


def fwht(a):
    a = list(a)
    step = 1
    while step < len(a):
        for b in range(0, len(a), 2 * step):
            for j in range(step):
                x, y = a[b + j], a[b + j + step]
                a[b + j], a[b + j + step] = x + y, x - y
        step *= 2
    return a


def quadratic(n, edge_mask, linear_mask):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    ans = []
    for x in range(1 << n):
        e = (x & linear_mask).bit_count() & 1
        for k, (i, j) in enumerate(edges):
            e ^= ((edge_mask >> k) & 1) & ((x >> i) & 1) & ((x >> j) & 1)
        ans.append(1 if e == 0 else -1)
    return tuple(ans)


def restrict_table(f, i, bit):
    return tuple(f[x] for x in range(len(f)) if ((x >> i) & 1) == bit)


def exact_upper_u_for_quadratic(f):
    w = fwht(f)
    supp = [s for s, z in enumerate(w) if z]
    mags = {abs(w[s]) for s in supp}
    assert len(mags) == 1
    acc = 0
    for s in supp:
        count = sum(1 for t in supp if (t & s) == s)
        assert count > 0 and count & (count - 1) == 0
        acc += count.bit_length() - 1
    return Fraction(acc, len(supp))


def influence(f, i):
    return Fraction(sum(f[x] != f[x ^ (1 << i)] for x in range(len(f))), len(f))


def reindex_restriction(f, remaining, chosen_original, bit):
    pos = remaining.index(chosen_original)
    return restrict_table(f, pos, bit), remaining[:pos] + remaining[pos + 1:]


def all_tree_summaries(f, remaining, root_n):
    """Every finite pruned adaptive tree on the remaining coordinates.

    Summary = (terminal U, accumulated Delta U, owned influence vector,
               internal nodes, leaves).
    Weights are relative to the current node.
    """
    u = exact_upper_u_for_quadratic(f)
    stop = (u, Fraction(0), (Fraction(0),) * root_n, 0, 1)
    out = [stop]
    for chosen in remaining:
        pos = remaining.index(chosen)
        q = influence(f, pos)
        f0, rem = reindex_restriction(f, remaining, chosen, 0)
        f1, _ = reindex_restriction(f, remaining, chosen, 1)
        u0 = exact_upper_u_for_quadratic(f0)
        u1 = exact_upper_u_for_quadratic(f1)
        delta = u - (u0 + u1) / 2
        assert delta <= 3 * q
        left = all_tree_summaries(f0, rem, root_n)
        right = all_tree_summaries(f1, rem, root_n)
        for a in left:
            for b in right:
                owned = tuple((a[2][j] + b[2][j]) / 2 for j in range(root_n))
                owned = tuple(z + (q if j == chosen else 0) for j, z in enumerate(owned))
                out.append(((a[0] + b[0]) / 2,
                            delta + (a[1] + b[1]) / 2,
                            owned, 1 + a[3] + b[3], a[4] + b[4]))
    return out


def general_upper_u(f):
    n = (len(f).bit_length() - 1)
    w = fwht(f)
    den = 1 << (2 * n)
    masses = [Fraction(z * z, den) for z in w]
    ans = 0.0
    for s, p in enumerate(masses):
        if not p:
            continue
        cap = sum((masses[t] for t in range(len(masses)) if (t & s) == s), Fraction())
        pf = p.numerator / p.denominator
        capf = cap.numerator / cap.denominator
        ans += pf * math.log2(capf / pf)
    return ans


def tensor_truth(f, g):
    # f variables occupy lower bits, g variables upper bits.
    return tuple(f[x] * g[y] for y in range(len(g)) for x in range(len(f)))


def review():
    local_checks = adaptive_trees = ownership_checks = tensor_checks = sharp_checks = 0
    largest_tree_ratio = Fraction(-10)

    # Independent coordinate reconstruction through n=5.
    for n in range(1, 6):
        ecount = n * (n - 1) // 2
        for e in range(1 << ecount):
            for lin in range(1 << n):
                f = quadratic(n, e, lin)
                u = exact_upper_u_for_quadratic(f)
                for i in range(n):
                    f0 = restrict_table(f, i, 0)
                    f1 = restrict_table(f, i, 1)
                    delta = u - (exact_upper_u_for_quadratic(f0) +
                                 exact_upper_u_for_quadratic(f1)) / 2
                    assert delta <= 3 * influence(f, i)
                    local_checks += 1

    # Exhaust every adaptive/pruned physical tree through n=3.
    expected_tree_counts = {1: 2, 2: 9, 3: 244}
    for n in range(1, 4):
        ecount = n * (n - 1) // 2
        for e in range(1 << ecount):
            for lin in range(1 << n):
                f = quadratic(n, e, lin)
                root_u = exact_upper_u_for_quadratic(f)
                root_inf = tuple(influence(f, i) for i in range(n))
                summaries = all_tree_summaries(f, tuple(range(n)), n)
                assert len(summaries) == expected_tree_counts[n]
                for terminal, charge, owned, _, _ in summaries:
                    assert charge == root_u - terminal
                    assert charge <= 3 * sum(owned, Fraction())
                    for i in range(n):
                        assert owned[i] <= root_inf[i]
                        ownership_checks += 1
                    assert sum(owned, Fraction()) <= sum(root_inf, Fraction())
                    if sum(owned, Fraction()):
                        largest_tree_ratio = max(largest_tree_ratio,
                                                 charge / sum(owned, Fraction()))
                    adaptive_trees += 1

    # Explicit arbitrary two-variable Boolean cores for all n=2 quadratics
    # and all adaptive/pruned control trees: direct Walsh reconstruction.
    for e in range(2):
        for lin in range(4):
            q = quadratic(2, e, lin)
            q_u = general_upper_u(q)
            q_summaries = all_tree_summaries(q, (0, 1), 2)
            for bits in range(16):
                g = tuple(1 if ((bits >> x) & 1) == 0 else -1 for x in range(4))
                g_u = general_upper_u(g)
                F = tensor_truth(q, g)
                assert abs(general_upper_u(F) - q_u - g_u) < 1e-12
                for terminal_q, charge_q, owned, _, _ in q_summaries:
                    terminal_F = terminal_q + g_u
                    charge_F = general_upper_u(F) - terminal_F
                    assert abs(charge_F - float(charge_q)) < 1e-12
                    owned_sum = sum(owned, Fraction())
                    if owned_sum:
                        assert charge_F <= 3 * float(owned_sum) + 1e-12
                    else:
                        assert abs(charge_F) < 1e-12
                    tensor_checks += 1

    # Claimed one-node sharp family: clique quadratics in even dimension.
    for n in range(2, 11, 2):
        ecount = n * (n - 1) // 2
        f = quadratic(n, (1 << ecount) - 1, 0)
        u = exact_upper_u_for_quadratic(f)
        f0, f1 = restrict_table(f, 0, 0), restrict_table(f, 0, 1)
        delta = u - (exact_upper_u_for_quadratic(f0) + exact_upper_u_for_quadratic(f1)) / 2
        ratio = delta / influence(f, 0)
        assert ratio == 3 - Fraction(1, 1 << (n - 2))
        sharp_checks += 1

    print(f"local_coordinate_checks={local_checks}")
    print(f"all_adaptive_pruned_trees_through_n3={adaptive_trees}")
    print(f"coordinate_ownership_checks={ownership_checks}")
    print(f"explicit_arbitrary_core_tree_checks={tensor_checks}")
    print(f"sharp_clique_checks={sharp_checks}")
    print(f"largest_tree_charge_over_owned_influence={largest_tree_ratio}")
    print("randomness=none")
    print("RESULT=PASS")


if __name__ == "__main__":
    review()
