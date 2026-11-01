"""Exact three-slab scan: the missing step for a general-r proof of the 4/9
bound.

Theorem 9.1's proof of p_T <= 9/20 splits on the number e of exceptional
states.  For e = 2 the value is 9/20 (empty chain, k = 4) or 4/9 (nonempty
chain).  For e >= 3 the paper bounds by 9/20 (Lemma 8.1, two slabs) or 2/5
(Lemma 8.2, three critical slabs).  To get the global 4/9 bound for r >= 5
one needs: THREE distinct exceptional slabs always give at most 4/9.

By Lemma 2.5 every slot form has coefficients in {0, +-1} with odd support
of size at least three, so the scan is finite once the dimension is fixed.
This script enumerates, for d = 4, 5 (and 6 when asked), all admissible
pairs (M, N) of distinct such forms, neither equal to +-L nor a coordinate,
and computes

    Pr{ |L| <= 1/2, |M| <= 1/2, |N| <= 1/2 },   L = X1 + X2 - X3,

exactly as a rational polytope volume.  It reports the maximum and every
configuration attaining it.

Run:  python -u three_slab_scan.py [dmax]
"""
import sys, os, time
from fractions import Fraction as Fr
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

def forms(d):
    """All vectors in {0,+-1}^d with coefficient sum 1 and odd support >= 3."""
    out = []
    for supp_size in range(3, d + 1, 2):
        nminus = (supp_size - 1) // 2
        nplus = supp_size - nminus
        if nplus - nminus != 1:
            continue
        for positions in combinations(range(d), supp_size):
            for minus in combinations(positions, nminus):
                v = [0] * d
                for pnt in positions:
                    v[pnt] = 1
                for m in minus:
                    v[m] = -1
                out.append(tuple(v))
    return sorted(set(out))

def slab_volume(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def main():
    dmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    FOURNINTHS = Fr(4, 9)
    for d in range(4, dmax + 1):
        L = tuple([1, 1, -1] + [0] * (d - 3))
        coords = {tuple(1 if i == j else 0 for i in range(d)) for j in range(d)}
        F = [f for f in forms(d)
             if f != L and tuple(-x for x in L) != f and f not in coords]
        print(f"d={d}: {len(F)} admissible forms, "
              f"{len(F)*(len(F)-1)//2} distinct pairs", flush=True)
        best = Fr(0)
        arg = []
        t0 = time.time()
        n = 0
        for M, N in combinations(F, 2):
            v = slab_volume([L, M, N], d)
            n += 1
            if v > best:
                best, arg = v, [(M, N)]
            elif v == best:
                arg.append((M, N))
            if n % 200 == 0:
                print(f"   {n} pairs, running max {best} ({time.time()-t0:.0f}s)",
                      flush=True)
        print(f"d={d}: MAX over three distinct slabs = {best} = {float(best):.6f}",
              flush=True)
        print(f"       4/9 = {float(FOURNINTHS):.6f}   "
              f"{'MAX <= 4/9 (supports the bound)' if best <= FOURNINTHS else 'MAX EXCEEDS 4/9'}",
              flush=True)
        print(f"       attained by {len(arg)} pairs, e.g. M={arg[0][0]} N={arg[0][1]}",
              flush=True)

if __name__ == "__main__":
    main()
