"""Write the extreme rays of the split cones R1, R2 for the C program split_dense.c (an agent, 11 Nov 2026).

R1 = {x sorted decreasing, sum 0, x_1 + x_n >= 0, x_2 + x_(n-1) >= 0},  R2 the same with x_2 + x_(n-1) <= 0.
Vertex enumeration with exact rationals: a ray is the null line of n-2 tight inequalities together with sum = 0,
kept if it satisfies all n+1 inequalities.  Uses only rays_enum.null_line / primitive.

Usage: split_rays.py nmin nmax outdir
"""
import sys
from itertools import combinations
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


def main():
    nmin, nmax, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    for n in range(nmin, nmax + 1):
        for which in ("R1", "R2"):
            R = cone_rays(n, which)
            with open(f"{out}/rays_{which}_n{n}.txt", "w", newline="\n") as f:
                f.write(f"{n} {len(R)}\n")
                for v in R:
                    f.write(" ".join(str(int(c)) for c in v) + "\n")
            print(f"n={n} {which}: {len(R)} rays", flush=True)


if __name__ == "__main__":
    main()
