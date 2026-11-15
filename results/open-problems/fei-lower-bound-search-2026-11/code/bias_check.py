"""bias_check.py - independent recomputation for fei_bias output, and a numerical test of the composition law.

usage: python bias_check.py FILE [FILE ...] [--top K]     recompute the leaders of fei_bias output files
       python bias_check.py --law                          test the composition law on random functions

Biased quantities are computed with exact rationals where it matters (the mass) and with an axis-by-axis tensor
transform in numpy, written separately from the C code.  The composed function F o AND_b is built as an explicit
truth table on k*b uniform bits and its H and I are taken from an ordinary Walsh-Hadamard transform.
"""
import sys
from fractions import Fraction

import numpy as np


def table_bits(tab, k):
    return np.array([(tab >> x) & 1 for x in range(1 << k)], dtype=np.float64)


def biased(tab, k, p):
    """mean, var, G, J, Hp, Ip of F = 1 - 2*[x in U] under Pr[y_j = 1] = p."""
    f = (1.0 - 2.0 * table_bits(tab, k)).reshape((2,) * k)
    s = np.sqrt(p * (1 - p))
    M = np.array([[1 - p, p], [-s, s]])
    for ax in range(k):
        f = np.moveaxis(np.tensordot(M, f, axes=([1], [ax])), 0, ax)
    w = (f ** 2).reshape(-1)          # index = sum_j t_j 2^(k-1-j); only |T| is needed below
    size = np.array([bin(t).count("1") for t in range(1 << k)])
    mean = f.reshape(-1)[0]
    var = 1 - mean ** 2
    nz = w[1:][w[1:] > 1e-300]
    G = float(-(nz / var * np.log2(nz / var)).sum())
    J = float((size * w).sum() / var)
    allw = w[w > 1e-300]
    Hp = float(-(allw * np.log2(allw)).sum())
    Ip = float((size * w).sum())
    return float(mean), float(var), G, J, Hp, Ip


def mass(tab, k, a, b):
    tot = Fraction(0)
    p = Fraction(a, 1 << b)
    for x in range(1 << k):
        if (tab >> x) & 1:
            j = bin(x).count("1")
            tot += p ** j * (1 - p) ** (k - j)
    return tot


def uniform_HI(vals):
    """H, I, mean of a +-1 table on uniform bits (plain Walsh-Hadamard)."""
    f = vals.astype(np.float64).copy()
    n = f.size.bit_length() - 1
    h = 1
    while h < f.size:
        f = f.reshape(-1, 2, h)
        f = np.stack([f[:, 0, :] + f[:, 1, :], f[:, 0, :] - f[:, 1, :]], axis=1).reshape(-1)
        h *= 2
    f /= f.size
    w = f ** 2
    size = np.array([bin(t).count("1") for t in range(f.size)])
    nz = w[w > 1e-300]
    return float(-(nz * np.log2(nz)).sum()), float((size * w).sum()), float(f[0])


def compose_and(tab, k, b):
    """truth table (+-1) of F(AND_b(block_1), ..., AND_b(block_k)) on k*b bits; a block is 'true' when all b bits are 1."""
    n = k * b
    out = np.empty(1 << n)
    full = (1 << b) - 1
    for x in range(1 << n):
        y = 0
        for j in range(k):
            if (x >> (j * b)) & full == full:
                y |= 1 << j
        out[x] = 1.0 - 2.0 * ((tab >> y) & 1)
    return out


def seed_and(b):
    """G and J of AND_b on uniform bits."""
    m = (1 << b) - 1
    var = 4.0 * m / 4 ** b
    return float(np.log2(m)), (2.0 * b / 2 ** b) / var


def law_test():
    rng = np.random.default_rng(7)
    worst = 0.0
    for k, b in [(3, 2), (4, 2), (5, 2), (6, 2), (3, 3), (4, 3), (5, 3)]:
        for _ in range(6):
            tab = int(rng.integers(1, (1 << (1 << k)) - 1, dtype=np.uint64)) if k < 6 else \
                int(rng.integers(1, 2 ** 63, dtype=np.uint64)) | (int(rng.integers(0, 2 ** 63, dtype=np.uint64)) << 63)
            tab &= (1 << (1 << k)) - 1
            if tab == 0 or tab == (1 << (1 << k)) - 1:
                continue
            p = 1.0 / (1 << b)
            mean, var, G, J, Hp, Ip = biased(tab, k, p)
            if var < 1e-12:
                continue
            G0, J0 = seed_and(b)
            H, I, m = uniform_HI(compose_and(tab, k, b))
            e1 = abs(H - (Hp + Ip * G0))
            e2 = abs(I - Ip * J0)
            e3 = abs(m - mean)
            # the normalised form
            Gf = (H - (m * m * np.log2(1 / (m * m)) if m != 0 else 0.0)) / (1 - m * m) - np.log2(1 / (1 - m * m))
            e4 = abs(Gf - (G + J * G0))
            e5 = abs(I / (1 - m * m) - J * J0)
            worst = max(worst, e1, e2, e3, e4, e5)
            print("k=%d b=%d H=%.9f law=%.9f I=%.9f law=%.9f  errs %.1e %.1e %.1e %.1e %.1e"
                  % (k, b, H, Hp + Ip * G0, I, Ip * J0, e1, e2, e3, e4, e5))
    print("worst error", worst)


def main():
    args = sys.argv[1:]
    if "--law" in args:
        law_test()
        return
    top = 2
    if "--top" in args:
        i = args.index("--top")
        top = int(args[i + 1])
        del args[i:i + 2]
    for fn in args:
        rows = []
        kv = None
        with open(fn, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("# fei_bias"):
                    kv = dict(t.split("=") for t in line.split()[2:])
                    continue
                if line.startswith("#") or "|" not in line:
                    continue
                a_, b_, c_ = line.split("|")
                rows.append((float(a_.split()[2]), c_.strip()))
        if not rows or kv is None:
            print(fn, "no exact-mass runs yet")
            continue
        k, a, b, c, d = (int(kv[t]) for t in ("k", "a", "b", "c", "d"))
        al, be, ga, de = (float(kv[t]) for t in ("al", "be", "ga", "de"))
        best = {}
        for v, h in rows:
            best[h] = v
        lst = sorted(best.items(), key=lambda t: -t[1])
        vals = sorted((v for v, _ in rows), reverse=True)
        print("== %s k=%d p=%d/%d target=%d/%d runs=%d best=%.12f median=%.12f distinct=%d"
              % (fn, k, a, 1 << b, c, 1 << d, len(rows), vals[0], vals[len(vals) // 2], len(lst)))
        p = a / (1 << b)
        for h, v in lst[:top]:
            tab = int(h, 16)
            mean, var, G, J, Hp, Ip = biased(tab, k, p)
            S = (G + al * J + be) / (ga * J - de)
            ms = mass(tab, k, a, b)
            mono = all(((tab >> (x | (1 << i))) & 1) for x in range(1 << k) if (tab >> x) & 1 for i in range(k))
            line = "  %.12f recomputed %.12f diff=%.1e G=%.9f J=%.9f mass=%s exact=%s monotone=%s" % (
                v, S, abs(S - v), G, J, ms, ms == Fraction(c, 1 << d), mono)
            if a == 1 and c == 1 and d == b:
                G0, J0 = seed_and(b)
                line += "  tower bound with seed AND_%d: %.9f" % (b, (S + G0) / J0)
            print(line)
            print("     table", h)


if __name__ == "__main__":
    main()
