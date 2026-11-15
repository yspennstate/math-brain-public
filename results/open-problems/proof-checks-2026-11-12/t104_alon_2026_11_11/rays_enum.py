"""Extreme rays of C = {sum x = 0, x_1 >= ... >= x_n, x_1 + x_n >= 0} by brute-force vertex enumeration
(an agent, 11 Nov 2026). Independent of the closed formula in cone_recheck.rays: C lies in the hyperplane
sum x = 0 (dimension n-1) and is cut out by n inequalities; an extreme ray is a line on which n-2 linearly
independent inequalities are tight and the others hold. Every (n-2)-subset is tried with exact rationals.

Usage: rays_enum.py n [outfile]    prints the count and, if cone_recheck is importable, whether the two lists agree.
"""
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import reduce


def constraints(n):
    rows = []
    for i in range(n - 1):
        r = [0] * n
        r[i], r[i + 1] = 1, -1
        rows.append(r)
    r = [0] * n
    r[0], r[n - 1] = 1, 1
    rows.append(r)
    return rows


def null_line(rows, n):
    """Return a spanning vector of the null space of rows if it is one-dimensional, else None."""
    m = [[Fraction(v) for v in r] for r in rows]
    piv = []
    rr = 0
    for c in range(n):
        p = next((i for i in range(rr, len(m)) if m[i][c] != 0), None)
        if p is None:
            continue
        m[rr], m[p] = m[p], m[rr]
        d = m[rr][c]
        m[rr] = [v / d for v in m[rr]]
        for i in range(len(m)):
            if i != rr and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[rr])]
        piv.append(c)
        rr += 1
        if rr == len(m):
            break
    free = [c for c in range(n) if c not in piv]
    if len(free) != 1:
        return None
    f = free[0]
    v = [Fraction(0)] * n
    v[f] = Fraction(1)
    for i, c in enumerate(piv):
        v[c] = -m[i][f]
    return v


def primitive(v):
    den = reduce(lambda a, b: a * b // gcd(a, b), [x.denominator for x in v], 1)
    w = [int(x * den) for x in v]
    g = reduce(gcd, [abs(x) for x in w], 0)
    return tuple(x // g for x in w)


def extreme_rays(n):
    G = constraints(n)
    found = set()
    for S in combinations(range(n), n - 2):
        v = null_line([[1] * n] + [G[i] for i in S], n)
        if v is None:
            continue
        vals = [sum(a * b for a, b in zip(G[i], v)) for i in range(n)]
        if all(x >= 0 for x in vals):
            pass
        elif all(x <= 0 for x in vals):
            v = [-x for x in v]
        else:
            continue
        found.add(primitive(v))
    return sorted(found, reverse=True)


def main():
    n = int(sys.argv[1])
    R = extreme_rays(n)
    for r in R:
        assert sum(r) == 0 and all(r[c] >= r[c + 1] for c in range(n - 1)) and r[0] + r[-1] >= 0
    msg = f"n={n} extreme_rays={len(R)}"
    try:
        from cone_recheck import rays
        F, _ = rays(n)
        Fp = sorted({primitive([Fraction(x) for x in r]) for r in F}, reverse=True)
        msg += f" formula_rays={len(F)} same_set={Fp == R}"
    except ImportError:
        msg += " (cone_recheck not importable, no comparison)"
    print(msg)
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", newline="\n") as f:
            f.write(f"{n} {len(R)}\n")
            for r in R:
                f.write(" ".join(str(x) for x in r) + "\n")


if __name__ == "__main__":
    main()
