#!/usr/bin/env python3
"""Exact finite audit of the all-dimensional rectangle-payment identities.

The proof in the report is analytic.  This program checks every Boolean sign
table through four variables, every nontrivial cut (up to complement), every
singleton identity, and the deterministic complete restriction-tree budget.
Only integer arithmetic is used.
"""

from itertools import combinations


def bit_at(table: int, x: int) -> int:
    return (table >> x) & 1


def pivotal_count(table: int, n: int, i: int) -> int:
    return sum(bit_at(table, x) != bit_at(table, x ^ (1 << i))
               for x in range(1 << n))


def block_rho_numerator(table: int, n: int, A: tuple[int, ...]) -> int:
    """Numerator of rho_A with denominator 2^(2n)."""
    B = tuple(i for i in range(n) if i not in A)
    mA = 1 << len(A)
    mB = 1 << len(B)

    def combine(a: int, b: int) -> int:
        x = 0
        for k, i in enumerate(A):
            x |= ((a >> k) & 1) << i
        for k, i in enumerate(B):
            x |= ((b >> k) & 1) << i
        return x

    # For fixed (y,y'), r(x)=f(x,y)f(x,y').  If r is negative at q of
    # the mA points, exactly 2*q*(mA-q) ordered (x,x') pairs disagree.
    bad = 0
    for y in range(mB):
        for yp in range(mB):
            q = 0
            for x in range(mA):
                q += bit_at(table, combine(x, y)) != bit_at(table, combine(x, yp))
            bad += 2 * q * (mA - q)
    return bad


def restrict_table(table: int, n: int, i: int, value: int) -> int:
    """Delete coordinate i after fixing it to value in {0,1}."""
    out = 0
    for z in range(1 << (n - 1)):
        lo = z & ((1 << i) - 1)
        hi = z >> i
        x = lo | (value << i) | (hi << (i + 1))
        out |= bit_at(table, x) << z
    return out


def total_influence_numerator(table: int, n: int) -> int:
    return sum(pivotal_count(table, n, i) for i in range(n))


def tree_budget_scaled(table: int, n: int) -> tuple[int, int, int]:
    """All three quantities scaled by 2^(2n)."""
    nodes = [(table, n, 0)]  # local table, remaining dimension, depth
    sum_rho = 0
    sum_query = 0
    while nodes:
        g, m, depth = nodes.pop()
        if m == 0:
            continue
        pnum = pivotal_count(g, m, 0)
        # node weight 2^-depth, local p=pnum/2^m
        sum_query += pnum * (1 << (2 * n - depth - m))
        # node weight times p(1-p)
        sum_rho += pnum * ((1 << m) - pnum) * (1 << (2 * n - depth - 2 * m))
        nodes.append((restrict_table(g, m, 0, 0), m - 1, depth + 1))
        nodes.append((restrict_table(g, m, 0, 1), m - 1, depth + 1))
    root_i = total_influence_numerator(table, n) * (1 << n)
    return sum_rho, sum_query, root_i


def main() -> None:
    block_checks = 0
    singleton_checks = 0
    tree_checks = 0
    tables = 0
    for n in range(1, 5):
        # Representatives A containing coordinate 0 avoid duplicate A|B cuts.
        cuts = []
        for a in range(1, n):
            for A in combinations(range(n), a):
                if 0 in A:
                    cuts.append(A)
        for table in range(1 << (1 << n)):
            tables += 1
            den = 1 << n
            piv = [pivotal_count(table, n, i) for i in range(n)]
            for A in cuts:
                rho_num = block_rho_numerator(table, n, A)
                pA = sum(piv[i] for i in A)
                pB = sum(piv[i] for i in range(n) if i not in A)
                assert rho_num <= pA * den
                assert rho_num <= pB * den
                block_checks += 2
            for i in range(n):
                rho_num = block_rho_numerator(table, n, (i,))
                assert rho_num == piv[i] * (den - piv[i])
                singleton_checks += 1
            srho, squery, root_i = tree_budget_scaled(table, n)
            assert srho <= squery
            assert squery == root_i
            tree_checks += 2

    print("EXACT AUDIT PASSED")
    print(f"boolean_tables={tables}")
    print(f"block_payment_assertions={block_checks}")
    print(f"singleton_identity_assertions={singleton_checks}")
    print(f"tree_budget_assertions={tree_checks}")
    print(f"total_assertions={block_checks + singleton_checks + tree_checks}")
    print("scope=all Boolean sign tables for 1<=n<=4; all nontrivial cuts up to complement")
    print("arithmetic=integers only; no floating point")


if __name__ == "__main__":
    main()
