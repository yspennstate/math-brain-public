"""Close the remaining four-slab certificate minima with deterministic
witness searches.

For each minimal multiplicity vector whose central box-spline value was not
directly evaluated (support too large), find a SPANNING submultiset W with
B_W(0) <= 1/3; by the one-column convolution inequality this bounds the full
vector's value.  Search order (all exact):
  1. every single-copy subset of 8 distinct support directions (C(s,8))
  2. every doubled 4-subset (two copies each of 4 independent directions)
  3. every mixed 2+2+2+1+1 pattern over 5 directions
  4. escalate: exact direct evaluation up to dimension 12
Writes fourslab_witnesses.json with the winning witness per vector.

Run:  python -u close_witnesses.py
"""
import sys, os, json, time
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces, det_frac, mat_rank

from itertools import product, permutations

def k5_frame():
    def col(i, j):
        v = [0, 0, 0, 0]
        if i < 4:
            v[i] += 1
        if j < 4:
            v[j] -= 1
        return tuple(v)
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    return [col(i, j) for (i, j) in edges], edges

def k33_frame():
    edges = [(i, j) for i in range(3) for j in range(3)]
    eidx = {e: t for t, e in enumerate(edges)}
    chords = [(1, 1), (1, 2), (2, 1), (2, 2)]
    rows = []
    for (i, j) in chords:
        r = [0] * 9
        r[eidx[(i, j)]] = 1
        r[eidx[(0, j)]] = -1
        r[eidx[(0, 0)]] = 1
        r[eidx[(i, 0)]] = -1
        rows.append(r)
    cols = [tuple(rows[c][t] for c in range(4)) for t in range(9)]
    return cols, edges

def multiset_cols(cols, m):
    out = []
    for t, mult in enumerate(m):
        out.extend([cols[t]] * mult)
    return out

def bspline_at_zero(cols_multiset):
    from itertools import combinations as combs
    n = len(cols_multiset)
    basis = None
    for c4 in combs(range(n), 4):
        M = [[cols_multiset[t][r] for t in c4] for r in range(4)]
        d = det_frac(M)
        if abs(d) == 1:
            basis = c4
            break
    if basis is None:
        return None
    rest = [t for t in range(n) if t not in basis]
    if not rest:
        return Fr(1)
    B = [[Fr(cols_multiset[t][r]) for t in basis] for r in range(4)]
    aug = [row[:] + [Fr(1) if i == r else Fr(0) for i in range(4)]
           for r, row in enumerate(B)]
    for c in range(4):
        piv = next(r for r in range(c, 4) if aug[r][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(4):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [a - f * b for a, b in zip(aug[r], aug[c])]
    Binv = [row[4:] for row in aug]
    import math
    hs = []
    for j in range(4):
        row = []
        for t in rest:
            row.append(sum(Binv[j][r] * cols_multiset[t][r] for r in range(4)))
        Lc = 1
        for x in row:
            Lc = Lc * x.denominator // math.gcd(Lc, x.denominator)
        numi = tuple(int(x * Lc) for x in row)
        hs.append((numi, Lc))
        hs.append((tuple(-v for v in numi), Lc))
    d = len(rest)
    vol = volume_from_halfspaces(hs, [(-1, 1)] * d)
    return vol / 2 ** d

THIRD = Fr(1, 3)

def spanning(cols):
    return mat_rank(cols) == 4

def close_vector(cols, v):
    """Return (bound, witness_desc) with bound <= 1/3, or (best, None)."""
    support = [t for t, m in enumerate(v) if m > 0]
    best = None
    # pattern 1: 8 distinct singles
    if len(support) >= 8:
        for sub in combinations(support, 8):
            W = [cols[t] for t in sub]
            if not spanning(W):
                continue
            val = bspline_at_zero(W)
            if val is None:
                continue
            if best is None or val < best[0]:
                best = (val, ("singles8", sub))
            if val <= THIRD:
                return best
    # pattern 2: doubled 4-subsets (need m_t >= 2)
    doubles = [t for t in support if v[t] >= 2]
    for sub in combinations(doubles, 4):
        W = []
        for t in sub:
            W.extend([cols[t]] * 2)
        if not spanning([cols[t] for t in sub]):
            continue
        val = bspline_at_zero(W)
        if val is None:
            continue
        if best is None or val < best[0]:
            best = (val, ("doubles4", sub))
        if val <= THIRD:
            return best
    # pattern 3: 2+2+2+1+1 over five directions
    if len(support) >= 5:
        for five in combinations(support, 5):
            if not spanning([cols[t] for t in five]):
                continue
            for trip in combinations([t for t in five if v[t] >= 2], 3):
                singles = [t for t in five if t not in trip]
                W = []
                for t in trip:
                    W.extend([cols[t]] * 2)
                for t in singles:
                    W.append(cols[t])
                val = bspline_at_zero(W)
                if val is None:
                    continue
                if best is None or val < best[0]:
                    best = (val, ("mixed222_11", trip + tuple(singles)))
                if val <= THIRD:
                    return best
    # pattern 4: direct evaluation if dimension allows
    D = multiset_cols(cols, v)
    if len(D) - 4 <= 12:
        val = bspline_at_zero(D)
        if val is not None:
            return (val, ("direct", None)) if val <= THIRD else ((val, None))
    return best if best else (None, None)

def main():
    out = {}
    for name, frame in (("K5", k5_frame()[0]), ("MsK33", k33_frame()[0])):
        vals_file = os.path.join(HERE, f"fourslab_values_{name}.json")
        done_vals = {}
        if os.path.exists(vals_file):
            with open(vals_file, encoding="utf-8") as f:
                done_vals = {tuple(json.loads(k)): Fr(s)
                             for k, s in json.load(f).items()}
        unclosed = [v for v, val in done_vals.items() if val > THIRD]
        print(f"{name}: {len(done_vals)} valued orbit reps, "
              f"{len(unclosed)} above 1/3 needing witnesses", flush=True)
        res = {}
        t0 = time.time()
        for i, v in enumerate(unclosed):
            bound, wit = close_vector(frame, list(v))
            key = json.dumps(list(v))
            if bound is not None and bound <= THIRD and wit:
                res[key] = {"bound": str(bound), "witness": [wit[0], list(wit[1]) if wit[1] else None]}
                print(f"  closed {i+1}/{len(unclosed)}: bound {bound} via {wit[0]} "
                      f"({time.time()-t0:.0f}s)", flush=True)
            else:
                res[key] = {"bound": str(bound[0]) if isinstance(bound, tuple) and bound[0] is not None else (str(bound) if bound else "none"),
                            "witness": None}
                print(f"  UNCLOSED {i+1}/{len(unclosed)}: best {bound}", flush=True)
        out[name] = res
        with open(os.path.join(HERE, "fourslab_witnesses.json"), "w",
                  encoding="utf-8") as f:
            json.dump(out, f, indent=1)
    nc = sum(1 for fr in out.values() for r in fr.values() if r["witness"] is None)
    print(f"\nWITNESS CLOSURE {'COMPLETE - ALL <= 1/3' if nc == 0 else f'INCOMPLETE: {nc} vectors remain'}", flush=True)

if __name__ == "__main__":
    main()
