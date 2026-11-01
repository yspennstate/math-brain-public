#!/usr/bin/env python3
"""Exact exhaustive checksum for P0169 on n <= 4.

Encoding: a point p in {0,...,2^n-1} has x_i=(-1)^bit_i(p).
A truth table is encoded by an integer T; output is +1 where bit_p(T)=1
and -1 otherwise. The Walsh transform therefore has integer numerators
W[S] = sum_x f(x) chi_S(x), and \hat f(S)=W[S]/2^n exactly.

This is finite evidence only. It is not used as a proof for arbitrary n.
"""
from collections import Counter
from fractions import Fraction


def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def exact_degree(w):
    return max((mask.bit_count() for mask, num in enumerate(w) if num), default=0)


def main():
    for n in range(1, 5):
        N = 1 << n
        max_num = {d: None for d in range(1, n+1)}
        witness = {}
        cap_count = Counter()
        exact_count = Counter()

        for table in range(1 << N):
            vals = [1 if ((table >> p) & 1) else -1 for p in range(N)]
            w = fwht(vals)
            deg = exact_degree(w)
            exact_count[deg] += 1
            linear_num = sum(w[1 << i] for i in range(n))

            for d in range(1, n+1):
                if deg <= d:
                    cap_count[d] += 1
                    if max_num[d] is None or linear_num > max_num[d]:
                        max_num[d] = linear_num
                        witness[d] = (table, deg)

        print(f"n={n}")
        print("  exact_degree_counts=" + repr(dict(sorted(exact_count.items()))))
        for d in range(1, n+1):
            t, deg = witness[d]
            print(
                f"  degree_cap={d} functions={cap_count[d]} "
                f"max_linear_sum={Fraction(max_num[d], N)} "
                f"witness_table={hex(t)} witness_exact_degree={deg}"
            )


if __name__ == "__main__":
    main()
