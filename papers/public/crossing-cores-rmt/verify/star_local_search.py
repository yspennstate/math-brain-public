"""Is the star a local maximum?  An exact neighbourhood search.

Random tuples land far from the extremum, so their maxima say little.
The informative test is local: start at the star system, which attains
2/(j+2), and replace one of its forms by EVERY other admissible slot
form in the ambient dimension, computing each resulting probability
exactly.  If any single-form replacement beats 2/(j+2), the slab
hierarchy is false and the witness is produced; if none does, the star
is an exact local maximum under single-form moves.

Also searched: the star embedded in one extra dimension, where the
replacing form may use a coordinate the star does not touch.

Run:  python -u star_local_search.py [jmax]
"""
import sys, os, time
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

def forms(d):
    out = []
    for supp in range(3, d + 1, 2):
        nminus = (supp - 1) // 2
        for positions in combinations(range(d), supp):
            for minus in combinations(positions, nminus):
                v = [0] * d
                for pnt in positions:
                    v[pnt] = 1
                for m in minus:
                    v[m] = -1
                out.append(tuple(v))
    return sorted(set(out))

def vol(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def star(j, d):
    rows = []
    for i in range(j):
        v = [0] * d
        v[0], v[1], v[2 + i] = 1, -1, 1
        rows.append(tuple(v))
    return rows

def main():
    jmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    for j in range(3, jmax + 1):
        bound = Fr(2, j + 2)
        for extra in (0, 1):
            d = j + 2 + extra
            base = star(j, d)
            v0 = vol(base, d)
            assert v0 == bound, (v0, bound)
            F = [f for f in forms(d) if f not in base]
            coords = {tuple(1 if i == k else 0 for i in range(d))
                      for k in range(d)}
            F = [f for f in F if f not in coords]
            best = Fr(0)
            arg = None
            t0 = time.time()
            n = 0
            for i in range(j):
                for g in F:
                    rows = list(base)
                    rows[i] = g
                    if len(set(rows)) < j:
                        continue
                    v = vol(rows, d)
                    n += 1
                    if v > best:
                        best, arg = v, (i, g)
            over = best > bound
            print(f"j={j} d={d} (+{extra} spare coordinate): star = {v0}, "
                  f"{n} single-form replacements, best {best} = "
                  f"{float(best):.6f}", flush=True)
            print(f"      bound {bound} = {float(bound):.6f}  ->  "
                  f"{'*** STAR IS NOT MAXIMAL ***' if over else 'star is a local maximum'}"
                  f"   ({time.time()-t0:.0f}s)", flush=True)
            if over:
                print(f"      witness: replace form {arg[0]} by {arg[1]}",
                      flush=True)

if __name__ == "__main__":
    main()
