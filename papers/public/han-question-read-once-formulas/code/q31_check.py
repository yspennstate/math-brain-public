"""Exact check of Q_k(f) = sum_{S not containing k} |f^(S) f^(S u {k})| / I_k(f) on tribes and read-once NOR trees.

f : {0,1}^n -> {-1,1}, uniform measure, f^(S) = E[f(x) chi_S(x)], I_k = Pr[f(x) != f(x^k)] = sum_{S containing k} f^(S)^2.
With F = 2^n f^ (integer Walsh-Hadamard transform), Q_k = sum |F(S) F(S+k)| / sum_{S containing k} F(S)^2, an exact rational.
"""
import sys
from fractions import Fraction
import numpy as np


def wht(a):
    a = a.astype(np.int64).copy()
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        x, y = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :], a[:, 1, :] = x + y, x - y
        a = a.reshape(-1)
        h *= 2
    return a


def q_all(table, n):
    F = wht(1 - 2 * table)
    idx = np.arange(1 << n)
    out = []
    ks = range(n) if n <= 14 else (0, n - 1)  # every coordinate on small n; first and last above (the families are symmetric under their block structure)
    for k in ks:
        m = (idx >> k) & 1 == 0
        S = idx[m]
        num = int(np.abs(F[S] * F[S | (1 << k)]).sum())
        den = int((F[S | (1 << k)] ** 2).sum())
        out.append(Fraction(num, den))
    return out


def bits(n):
    idx = np.arange(1 << n)
    return [((idx >> i) & 1).astype(np.int64) for i in range(n)]


def tribes(s, w):
    n = s * w
    x = bits(n)
    val = np.zeros(1 << n, dtype=np.int64)
    for j in range(s):
        a = np.ones(1 << n, dtype=np.int64)
        for i in range(w):
            a &= x[j * w + i]
        val |= a
    return val, n


def tribes_formula(s, w):
    al = 1 - Fraction(1, 2 ** w)
    t = al ** s
    return 2 - Fraction(4, 2 ** w) if t >= Fraction(1, 2) else 4 - Fraction(4, 2 ** w) - 4 * t


def nor_tree(fans):
    n = 1
    for s in fans:
        n *= s
    x = bits(n)
    layer = x
    for s in fans:  # level 1 gates read the inputs
        nxt = []
        for g in range(len(layer) // s):
            o = np.zeros(1 << n, dtype=np.int64)
            for i in range(s):
                o |= layer[g * s + i]
            nxt.append(1 - o)  # NOR: true iff all inputs false
        layer = nxt
    assert len(layer) == 1
    return layer[0], n


def tree_formula(fans):
    p = [Fraction(1, 2)]
    for s in fans:
        p.append((1 - p[-1]) ** s)
    L = len(fans)
    pL = p[L]
    return 2 * L - 1 - 4 * sum(p[1:L], Fraction(0)) - 2 * pL + abs(1 - 2 * pL)


def main():
    bad = 0
    print("AND_n: Q_k vs 2 - 2^(2-n)")
    for n in range(1, 9):
        val = np.ones(1 << n, dtype=np.int64)
        for b in bits(n):
            val &= b
        q = q_all(val, n)
        ok = all(v == 2 - Fraction(4, 2 ** n) for v in q)
        bad += not ok
        print("  n=%d Q=%s %s" % (n, q[0], "ok" if ok else "MISMATCH"))
    print("tribes T_{s,w}: every coordinate vs formula")
    for s in range(1, 9):
        for w in range(1, 6):
            if s * w > 20 or s * w < 2:
                continue
            val, n = tribes(s, w)
            q = q_all(val, n)
            f = tribes_formula(s, w)
            ok = all(v == f for v in q)
            bad += not ok
            print("  s=%d w=%d n=%2d Q=%.6f formula=%.6f %s" % (s, w, n, float(q[0]), float(f), "ok" if ok else "MISMATCH"))
    print("read-once NOR trees: every coordinate vs closed form")
    for fans in [(2,), (3,), (2, 2), (3, 2), (2, 3), (4, 2), (2, 4), (3, 3), (5, 3), (3, 5), (2, 2, 2), (2, 2, 3),
                 (3, 2, 2), (2, 3, 2), (2, 2, 4), (4, 2, 2), (4, 4), (2, 8), (8, 2), (2, 2, 2, 2), (2, 2, 5), (4, 5)]:
        val, n = nor_tree(fans)
        q = q_all(val, n)
        f = tree_formula(fans)
        ok = all(v == f for v in q)
        bad += not ok
        print("  fans=%-14s n=%2d Q=%.6f closed=%.6f %s" % (fans, n, float(q[0]), float(f), "ok" if ok else "MISMATCH"))
    print("closed form on deep trees (fan-in least with p_l <= 1/4):")
    for L in (1, 2, 5):  # deeper trees: deep_trees.py (floats)
        p, fans = Fraction(1, 2), []
        for _ in range(L):
            s = 1
            while (1 - p) ** s > Fraction(1, 4):
                s += 1
            fans.append(s)
            p = (1 - p) ** s
        import math
        logn = sum(math.log2(s) for s in fans)
        print("  L=%2d max fan-in %d log2 n=%.1f Q=%.4f" % (L, max(fans), logn, float(tree_formula(fans))))
    print("TOTAL MISMATCHES", bad)
    return bad


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
