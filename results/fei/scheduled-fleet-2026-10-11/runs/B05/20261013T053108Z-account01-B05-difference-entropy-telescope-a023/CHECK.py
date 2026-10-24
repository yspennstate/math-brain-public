#!/usr/bin/env python3
"""Independent finite checks for the retained-difference entropy telescope.

The all-parameter theorem is analytic.  This program checks normalization,
the one-node identities, the scalar bounds, and the complete tree telescope
on genuine Boolean functions.  It also checks the previously obstructing
sparse bent-core surgery family at small parameters.
"""

from __future__ import annotations

import itertools
import math
import random

LN2 = math.log(2.0)
C = 3.0 / LN2
TOL = 2.0e-11


def walsh(values):
    a = [float(x) for x in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def raw_entropy(coeffs):
    ans = 0.0
    for x in coeffs:
        p = x * x
        if p:
            ans += p * math.log2(1.0 / p)
    return ans


def upper_u(coeffs):
    p = [x * x for x in coeffs]
    pi = p[:]
    nbits = (len(p) - 1).bit_length()
    for b in range(nbits):
        bit = 1 << b
        for mask in range(len(p)):
            if not (mask & bit):
                pi[mask] += pi[mask | bit]
    ans = 0.0
    for x, cap in zip(p, pi):
        if x:
            ans += x * math.log2(cap / x)
    return ans


def entropy_and_u(values):
    c = walsh(values)
    return raw_entropy(c), upper_u(c), c


def combine(g, h):
    """Selector is the new most significant truth-table coordinate."""
    return list(g) + list(h)


def one_node(g, h):
    hg, ug, a = entropy_and_u(g)
    hh, uh, b = entropy_and_u(h)
    f = combine(g, h)
    hf, uf, _ = entropy_and_u(f)
    u = [(x + y) / 2.0 for x, y in zip(a, b)]
    v = [(x - y) / 2.0 for x, y in zip(a, b)]
    m = [x * x + y * y for x, y in zip(u, v)]
    q = sum(x * x for x in v)
    ld = raw_entropy(v)
    hm = sum(x * math.log2(1.0 / x) for x in m if x)
    js = hm - (hg + hh) / 2.0
    pair = 0.0
    for x, y, mass in zip(u, v, m):
        if not mass:
            continue
        pu, pv = x * x / mass, y * y / mass
        if pu:
            pair += mass * pu * math.log2(1.0 / pu)
        if pv:
            pair += mass * pv * math.log2(1.0 / pv)
    vg, vh, vf = hg - ug, hh - uh, hf - uf
    lhs = uf - (ug + uh) / 2.0
    rhs = -vf + (vg + vh) / 2.0 + ld + C * q
    return {
        "entropy_identity_error": abs((hf - (hg + hh) / 2.0) - (js + pair)),
        "js_slack": 2.0 * q / LN2 - js,
        "pair_slack": ld + q / LN2 - pair,
        "local_slack": rhs - lhs,
        "q": q,
        "ld": ld,
        "lhs": lhs,
        "rhs": rhs,
    }


def all_boolean_functions(n):
    size = 1 << n
    for code in range(1 << size):
        yield [1.0 if (code >> i) & 1 else -1.0 for i in range(size)]


def exhaustive_pairs():
    rows = 0
    min_js = min_pair = min_local = float("inf")
    max_id_err = 0.0
    for n in range(4):
        fs = list(all_boolean_functions(n))
        for g in fs:
            for h in fs:
                z = one_node(g, h)
                rows += 1
                max_id_err = max(max_id_err, z["entropy_identity_error"])
                min_js = min(min_js, z["js_slack"])
                min_pair = min(min_pair, z["pair_slack"])
                min_local = min(min_local, z["local_slack"])
                assert z["entropy_identity_error"] >= -TOL
                assert z["entropy_identity_error"] <= TOL
                assert z["js_slack"] >= -TOL
                assert z["pair_slack"] >= -TOL
                assert z["local_slack"] >= -TOL
    return rows, max_id_err, min_js, min_pair, min_local


def extend_data_leaf(leaf, data_n, total_n):
    mask = (1 << data_n) - 1
    return [leaf[i & mask] for i in range(1 << total_n)]


def chain_subtree(leaves, data_n, depth, start):
    total_n = data_n + depth
    if start == depth:
        return extend_data_leaf(leaves[depth], data_n, total_n)
    left = extend_data_leaf(leaves[start], data_n, total_n)
    right = chain_subtree(leaves, data_n, depth, start + 1)
    selector_bit = data_n + start
    return [right[i] if ((i >> selector_bit) & 1) else left[i]
            for i in range(1 << total_n)]


def random_chain_checks(trials=100, data_n=3, depth=4):
    rng = random.Random(20261013)
    min_slack = float("inf")
    max_telescope_err = 0.0
    for _ in range(trials):
        leaves = [[rng.choice((-1.0, 1.0)) for _ in range(1 << data_n)]
                  for _ in range(depth + 1)]
        subtrees = [chain_subtree(leaves, data_n, depth, j)
                    for j in range(depth + 1)]
        total_n = data_n + depth
        extended_leaves = [extend_data_leaf(x, data_n, total_n) for x in leaves]
        hu_sub = [entropy_and_u(x)[:2] for x in subtrees]
        hu_leaf = [entropy_and_u(x)[:2] for x in extended_leaves]
        root_h, root_u = hu_sub[0]
        terminal_u = sum((2.0 ** (-(j + 1))) * hu_leaf[j][1]
                         for j in range(depth)) + (2.0 ** (-depth)) * hu_leaf[-1][1]
        terminal_v = sum((2.0 ** (-(j + 1))) * (hu_leaf[j][0] - hu_leaf[j][1])
                         for j in range(depth)) + (2.0 ** (-depth)) * (hu_leaf[-1][0] - hu_leaf[-1][1])
        sum_ld = 0.0
        isel = 0.0
        local_sum = 0.0
        for j in range(depth):
            w = 2.0 ** (-j)
            g = extended_leaves[j]
            h = subtrees[j + 1]
            z = one_node(g, h)
            sum_ld += w * z["ld"]
            isel += w * z["q"]
            local_sum += w * z["lhs"]
        telescope_err = abs(local_sum - (root_u - terminal_u))
        max_telescope_err = max(max_telescope_err, telescope_err)
        rhs = terminal_v - (root_h - root_u) + sum_ld + C * isel
        slack = rhs - (root_u - terminal_u)
        min_slack = min(min_slack, slack)
        assert telescope_err <= 5 * TOL
        assert slack >= -5 * TOL
    return trials, max_telescope_err, min_slack


def sparse_bent_pair(r):
    n = 2 * r
    size = 1 << n
    s = (r + 2) // 3
    g = []
    edited = set()
    all_ones_y = (1 << r) - 1
    for y_tail in range(1 << (r - s)):
        y = ((1 << s) - 1) | (y_tail << s)
        if y != all_ones_y:
            edited.add(((1 << r) - 1) | (y << r))
    for idx in range(size):
        x = idx & ((1 << r) - 1)
        y = idx >> r
        val = -1.0 if ((x & y).bit_count() & 1) else 1.0
        g.append(val)
    h = [(-val if i in edited else val) for i, val in enumerate(g)]
    return g, h, len(edited)


def sparse_checks():
    out = []
    for r in range(2, 7):
        g, h, m = sparse_bent_pair(r)
        z = one_node(g, h)
        expected_q = m / float(1 << (2 * r))
        assert abs(z["q"] - expected_q) <= TOL
        assert z["local_slack"] >= -TOL
        out.append((r, m, z["q"], z["ld"], z["lhs"], z["local_slack"]))
    return out


def main():
    rows, err, sjs, spair, slocal = exhaustive_pairs()
    print("retained-difference entropy telescope checker")
    print(f"constant 3/ln(2) = {C:.15f}")
    print(f"exhaustive genuine-Boolean child pairs: {rows}")
    print(f"maximum entropy identity error: {err:.3e}")
    print(f"minimum JS-bound slack: {sjs:.3e}")
    print(f"minimum pair-splitting slack: {spair:.3e}")
    print(f"minimum local U-bound slack: {slocal:.3e}")
    trials, terr, tslack = random_chain_checks()
    print(f"random shared-data rare chains: {trials}")
    print(f"maximum tree telescope error: {terr:.3e}")
    print(f"minimum complete-tree slack: {tslack:.3e}")
    print("sparse bent-core surgery controls:")
    for r, m, q, ld, lhs, slack in sparse_checks():
        print(f"  r={r:2d} m={m:3d} q={q:.9g} L(d)={ld:.9g} "
              f"J_U={lhs:.9g} slack={slack:.9g}")
    print("PASS")


if __name__ == "__main__":
    main()
