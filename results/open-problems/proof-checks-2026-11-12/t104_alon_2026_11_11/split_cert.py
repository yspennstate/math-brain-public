"""Exact coefficient test for the polyhedral split (an agent, 11 Nov 2026).

Cones (x sorted decreasing, sum x = 0, x_1 + x_n >= 0):
    R1: x_2 + x_(n-1) >= 0,  polynomial G_A = (n-4)(2Q-T^2)T - 2(n-3)P^2 + (n-1)((n^2-6n+6)T^2 + 2nQ) x_1 x_2
    R2: x_2 + x_(n-1) <= 0,  polynomial G_B, the same with x_n x_(n-1).
Extreme rays by vertex enumeration (every n-2 of the n+1 inequalities tight, exact rationals); then x = sum t_k r_k
and G is expanded in t; a negative coefficient is reported with its rays.

Usage: split_cert.py nmin nmax [R1|R2|both]
"""
import sys
import time
from fractions import Fraction
from itertools import combinations
from sympy import ZZ
from sympy.polys.rings import ring
from rays_enum import null_line, primitive


def cone_rays(n, which):
    G = []
    for i in range(n - 1):
        r = [0] * n
        r[i], r[i + 1] = 1, -1
        G.append(r)
    r = [0] * n
    r[0] += 1
    r[n - 1] += 1
    G.append(r)
    r = [0] * n
    sgn = 1 if which == "R1" else -1
    r[1] += sgn
    r[n - 2] += sgn
    G.append(r)
    found = set()
    for S in combinations(range(len(G)), n - 2):
        v = null_line([[1] * n] + [G[i] for i in S], n)
        if v is None:
            continue
        vals = [sum(a * b for a, b in zip(g, v)) for g in G]
        if all(x >= 0 for x in vals):
            pass
        elif all(x <= 0 for x in vals):
            v = [-x for x in v]
        else:
            continue
        found.add(primitive(v))
    return sorted(found, reverse=True)


def test(n, which):
    R = cone_rays(n, which)
    k = len(R)
    Rg, *t = ring(",".join(f"t{i}" for i in range(k)), ZZ)
    x = [sum((R[a][i] * t[a] for a in range(k) if R[a][i]), Rg(0)) for i in range(n)]
    sq = [v * v for v in x]
    T = sum(sq, Rg(0))
    P = sum((sq[i] * x[i] for i in range(n)), Rg(0))
    Q = sum((sq[i] * sq[i] for i in range(n)), Rg(0))
    M = x[0] * x[1] if which == "R1" else x[n - 1] * x[n - 2]
    G = (n - 4) * (2 * Q - T * T) * T - 2 * (n - 3) * P * P + (n - 1) * ((n * n - 6 * n + 6) * T * T + 2 * n * Q) * M
    neg = [(mon, c) for mon, c in G.terms() if c < 0]
    return R, len(G.terms()), neg


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    sel = sys.argv[3] if len(sys.argv) > 3 else "both"
    for n in range(nmin, nmax + 1):
        for which in ("R1", "R2"):
            if sel not in ("both", which):
                continue
            t0 = time.time()
            R, nt, neg = test(n, which)
            print(f"n={n} {which}: rays {len(R)}, nonzero monomials {nt}, negative {len(neg)}  [{time.time() - t0:.1f} s]", flush=True)
            if neg:
                used = sorted({i for mon, c in neg for i, e in enumerate(mon) if e})
                print("   rays in negative monomials:", [(i, R[i]) for i in used][:12])
                for mon, c in sorted(neg, key=lambda z: z[1])[:5]:
                    print("   ", c, {i: e for i, e in enumerate(mon) if e})
            if n <= 7:
                print("   rays:", R)


if __name__ == "__main__":
    main()
