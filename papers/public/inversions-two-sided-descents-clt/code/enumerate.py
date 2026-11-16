"""Exact moments of inversions and descents over all permutations of n elements, n = 2..8.

Checks, with exact rational arithmetic:
  Var I          = n(n-1)(2n+5)/72
  Var D          = (n+1)/12
  Cov(D, D')     = (n-1)/(2n)        D' = descents of the inverse
  Cov(I, D)      = Cov(I, D') = (n-1)/4
  Cov(I, T)      = (n-1)/2           T = D + D'
  Var T          = (n+7)/6 - 1/n
Run: python enumerate.py   (about a minute for n = 8)
"""
from fractions import Fraction as Fr
from itertools import permutations


def stats(p):
    n = len(p)
    q = [0] * n
    for i, v in enumerate(p):
        q[v] = i
    inv = sum(1 for a in range(n) for b in range(a + 1, n) if p[a] > p[b])
    d = sum(p[i] > p[i + 1] for i in range(n - 1))
    e = sum(q[i] > q[i + 1] for i in range(n - 1))
    return inv, d, e


def main():
    ok = True
    for n in range(2, 9):
        rows = [stats(p) for p in permutations(range(n))]
        N = len(rows)

        def mean(f):
            return Fr(sum(f(r) for r in rows), N)

        def cov(f, g):
            return mean(lambda r: f(r) * g(r)) - mean(f) * mean(g)

        I = lambda r: r[0]
        D = lambda r: r[1]
        E = lambda r: r[2]
        T = lambda r: r[1] + r[2]
        checks = [
            ("Var I", cov(I, I), Fr(n * (n - 1) * (2 * n + 5), 72)),
            ("Var D", cov(D, D), Fr(n + 1, 12)),
            ("Cov(D,D')", cov(D, E), Fr(n - 1, 2 * n)),
            ("Cov(I,D)", cov(I, D), Fr(n - 1, 4)),
            ("Cov(I,D')", cov(I, E), Fr(n - 1, 4)),
            ("Cov(I,T)", cov(I, T), Fr(n - 1, 2)),
            ("Var T", cov(T, T), Fr(n + 7, 6) - Fr(1, n)),
        ]
        line = []
        for name, got, want in checks:
            ok &= got == want
            line.append(f"{name}={got}" + ("" if got == want else f" (formula {want})"))
        print(f"n={n}: " + ", ".join(line))
    print("all formulas hold" if ok else "MISMATCH")


if __name__ == "__main__":
    main()
