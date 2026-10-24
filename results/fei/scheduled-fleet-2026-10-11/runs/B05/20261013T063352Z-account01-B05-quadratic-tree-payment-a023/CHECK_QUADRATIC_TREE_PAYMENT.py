#!/usr/bin/env python3
"""Exact diagnostic for the adaptive quadratic retained-U tree theorem."""

from fractions import Fraction


def fwht_int(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def quadratic_truth(n, edges, linear):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    for x in range(1 << n):
        bit = (linear & x).bit_count() & 1
        for k, (i, j) in enumerate(pairs):
            if ((edges >> k) & 1) and ((x >> i) & 1) and ((x >> j) & 1):
                bit ^= 1
        out.append(-1 if bit else 1)
    return tuple(out)


def restrict(values, local_i, bit):
    return tuple(v for x, v in enumerate(values) if ((x >> local_i) & 1) == bit)


def support(values):
    w = fwht_int(values)
    ans = tuple(i for i, z in enumerate(w) if z)
    assert ans and len({abs(w[i]) for i in ans}) == 1
    return ans


def upper_u(values):
    C = support(values)
    total = 0
    for x in C:
        count = sum((x & ~y) == 0 for y in C)
        assert count and not (count & (count - 1))
        total += count.bit_length() - 1
    return Fraction(total, len(C))


def influence(values, local_i):
    flips = sum(values[x] != values[x ^ (1 << local_i)]
                for x in range(len(values)))
    return Fraction(flips, len(values))


def should_stop(policy, depth, pathcode, remaining):
    if not remaining:
        return True
    if policy == 0:
        return False
    if policy == 1:
        return depth >= max(1, len(remaining))
    if policy == 2:
        return depth >= 1 and ((pathcode + depth) & 1) == 0
    if policy == 4:
        return depth >= 1
    return depth >= 2 and ((3 * pathcode + depth) % 3) == 0


def walk(values, remaining, policy, depth=0, pathcode=0, weight=Fraction(1)):
    if should_stop(policy, depth, pathcode, remaining):
        return weight * upper_u(values), Fraction(), {}, 1, 0
    pos = (policy + pathcode + 2 * depth) % len(remaining)
    original_i = remaining[pos]
    u = upper_u(values)
    kids = [restrict(values, pos, bit) for bit in (0, 1)]
    child_u = [upper_u(x) for x in kids]
    delta = u - sum(child_u, Fraction()) / 2
    q = influence(values, pos)
    assert delta <= 3 * q
    new_remaining = remaining[:pos] + remaining[pos + 1:]
    terminal = Fraction()
    charge = weight * delta
    owned = {original_i: weight * q}
    leaves = 0
    nodes = 1
    for bit in (0, 1):
        t, c, by_i, ll, nn = walk(
            kids[bit], new_remaining, policy, depth + 1,
            pathcode | (bit << depth), weight / 2,
        )
        terminal += t
        charge += c
        leaves += ll
        nodes += nn
        for i, z in by_i.items():
            owned[i] = owned.get(i, Fraction()) + z
    return terminal, charge, owned, leaves, nodes


def main():
    cases = trees = nodes = leaves = 0
    max_ratio = Fraction(-1)
    strict_ownership = 0
    for n in range(1, 5):
        edge_count = n * (n - 1) // 2
        for edges in range(1 << edge_count):
            for linear in range(1 << n):
                values = quadratic_truth(n, edges, linear)
                root_u = upper_u(values)
                root_infs = [influence(values, i) for i in range(n)]
                cases += 1
                for policy in range(5):
                    terminal, charge, owned, ll, nn = walk(
                        values, tuple(range(n)), policy
                    )
                    assert charge == root_u - terminal
                    query_i = sum(owned.values(), Fraction())
                    assert charge <= 3 * query_i
                    for i, z in owned.items():
                        assert z <= root_infs[i]
                    assert query_i <= sum(root_infs, Fraction())
                    if query_i < sum(root_infs, Fraction()):
                        strict_ownership += 1
                    if query_i:
                        max_ratio = max(max_ratio, charge / query_i)
                    trees += 1
                    nodes += nn
                    leaves += ll
    print(f"quadratic_phases={cases}")
    print(f"adaptive_trees={trees}")
    print(f"internal_nodes={nodes}")
    print(f"terminal_leaves={leaves}")
    print(f"strict_query_ownership_cases={strict_ownership}")
    print(f"maximum_retained_charge_over_query_influence={max_ratio}")
    print("arithmetic=integer_Walsh_and_exact_Fraction")
    print("scope=all quadratic coefficient choices through n=4; five deterministic adaptive/pruned policies")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
