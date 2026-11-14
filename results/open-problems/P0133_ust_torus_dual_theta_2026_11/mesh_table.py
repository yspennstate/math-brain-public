"""Superbase law by mesh for samples from ust_torus_shear.py or ust_metal (plain or .gz tsv).

Groups files by modulus tau = (s + i n2) / n1 and prints, per superbase (classes in that tau), P and its standard
error on each mesh, finest last, plus Q = sum |v|^2 / Im tau and the triangle's angles in degrees.
Usage: python mesh_table.py [--top K] files..."""
import cmath
import gzip
import math
import sys
from collections import Counter, defaultdict


def key(cls):
    out = []
    for a, b in cls:
        if a < 0 or (a == 0 and b < 0):
            a, b = -a, -b
        out.append((a, b))
    return tuple(sorted(out))


def load(fn):
    op = gzip.open if fn.endswith(".gz") else open
    cnt, tot, meta = Counter(), 0, None
    with op(fn, "rt", encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            n1, n2, s, m = int(p[0]), int(p[1]), int(p[2]), int(p[3])
            meta = (n1, n2, s)
            tot += 1
            if m != 3:
                cnt["fig8"] += 1
                continue
            cnt[key(tuple(map(int, x.split(","))) for x in p[4].split(";"))] += 1
    return meta, cnt, tot


def angles(k, tau):
    z = [a + b * tau for a, b in k]
    L = sorted(abs(w) for w in z)
    A = [math.degrees(math.acos((L[(i + 1) % 3] ** 2 + L[(i + 2) % 3] ** 2 - L[i] ** 2) / (2 * L[(i + 1) % 3] * L[(i + 2) % 3])))
         for i in range(3)]
    return sorted(A)


def main():
    args = sys.argv[1:]
    top = 8
    if args and args[0] == "--top":
        top, args = int(args[1]), args[2:]
    pooled = {}
    for fn in args:
        meta, cnt, tot = load(fn)
        if meta in pooled:
            pooled[meta][0].update(cnt)
            pooled[meta][1] += tot
        else:
            pooled[meta] = [cnt, tot]
    groups = defaultdict(list)
    for meta, (cnt, tot) in pooled.items():
        n1, n2, s = meta
        tau = complex(s, n2) / n1
        groups[(round(tau.real, 6), round(tau.imag, 6))].append((n1 * n2, meta, cnt, tot))
    for (tr, ti), runs in sorted(groups.items()):
        tau = complex(tr, ti)
        runs.sort()
        print(f"\ntau = {tr:.4f} + {ti:.4f} i   meshes: " + ", ".join(f"{m[0]}x{m[1]} s{m[2]} ({t})" for _, m, _, t in runs))
        print("  fig8: " + "  ".join(f"{c['fig8'] / t:.5f}" for _, _, c, t in runs))
        fin = runs[-1][2]
        keys = [k for k, _ in fin.most_common() if k != "fig8"][:top]
        for k in keys:
            Q = sum(abs(a + b * tau) ** 2 for a, b in k) / tau.imag
            cells = []
            for _, _, c, t in runs:
                p = c[k] / t
                cells.append(f"{p:.5f}({math.sqrt(p * (1 - p) / t):.5f})")
            ang = angles(k, tau)
            print(f"  Q {Q:7.3f}  angles {ang[0]:5.1f} {ang[1]:5.1f} {ang[2]:5.1f}  " + "  ".join(cells) + f"  {k}")


if __name__ == "__main__":
    main()
