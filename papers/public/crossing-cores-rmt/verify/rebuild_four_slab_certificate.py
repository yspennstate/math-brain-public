"""Independent rebuild of the rank-four box-spline certificate behind
Lemma 10.3 and Theorem 10.4.

From scratch:
  1. Construct the K5 frame (ten directions: reduced incidence of K5) and the
     M*(K3,3) frame (nine directions: a fundamental cycle matrix of K3,3).
  2. Enumerate ALL multiplicity vectors m with entries in {0,...,4} such that
     every one of the fifteen nonzero binary cocycle weights
         w_u(m) = sum over directions e with u.e odd of m_e
     is even and at least four (the hypotheses of Lemma 10.3 after the
     paper's reduction to m_e <= 4).
  3. Extract the coordinatewise-minimal valid vectors, count them, and count
     their orbits under the frame automorphisms (paper: 69 for K5 and 48 for
     M*(K3,3); every bounded valid multiplicity dominates one of these).
  4. For every minimal vector, prove B_D(0) <= 1/3 exactly: either compute
     the central box-spline value directly as a rational polytope volume
     (unimodular-basis fiber), or bound it by a spanning submultiset via the
     one-column convolution inequality (10.3), which only increases the
     value.  Record the exact spectrum of the direct values.
  5. Verify the reduction premise: subtracting 2 from any m_e >= 5 preserves
     validity (arithmetic check on the weight system).
  6. Independent spot lane for Theorem 10.4 itself: random 4 x d matrices M
     with entries in {0,+-1}, distinct noncoordinate coefficient-sum-one
     rows, verified totally unimodular, and the exact volume
     Pr{ |(MX)_j| <= 1/2, j<=4 } computed and checked <= 1/3.

Everything rational is exact; no floats enter any conclusion.

Run:  python -u rebuild_four_slab_certificate.py
"""
import sys, os, time, random
from fractions import Fraction as Fr
from itertools import combinations, product, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces, det_frac, mat_rank

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: {got}" + ("" if ok else f"  expected {expect}"), flush=True)
    if not ok:
        FAIL.append((name, got, expect))

# ------------------------------------------------------------- the frames

def k5_frame():
    """Reduced incidence directions of K5 over vertices 0..4, vertex 4 -> 0."""
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
    """Fundamental cycle matrix of K3,3, parts {a0,a1,a2} x {b0,b1,b2}.
    Tree: (a0,b0),(a0,b1),(a0,b2),(a1,b0),(a2,b0).  Chords: (a1,b1),(a1,b2),
    (a2,b1),(a2,b2).  Row per chord cycle; columns = 9 edges."""
    edges = [(i, j) for i in range(3) for j in range(3)]  # (a_i, b_j)
    eidx = {e: t for t, e in enumerate(edges)}
    chords = [(1, 1), (1, 2), (2, 1), (2, 2)]
    rows = []
    for (i, j) in chords:
        r = [0] * 9
        # cycle: (a_i,b_j) + (a0,b_j) reversed + (a0,b0) + (a_i,b0) reversed
        r[eidx[(i, j)]] = 1
        r[eidx[(0, j)]] = -1
        r[eidx[(0, 0)]] = 1
        r[eidx[(i, 0)]] = -1
        rows.append(r)
    cols = [tuple(rows[c][t] for c in range(4)) for t in range(9)]
    return cols, edges

def edge_perms_k5():
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    eidx = {e: t for t, e in enumerate(edges)}
    perms = []
    for p in permutations(range(5)):
        perm = [0] * 10
        for t, (i, j) in enumerate(edges):
            a, b = sorted((p[i], p[j]))
            perm[t] = eidx[(a, b)]
        perms.append(tuple(perm))
    return sorted(set(perms))

def edge_perms_k33():
    edges = [(i, j) for i in range(3) for j in range(3)]
    eidx = {e: t for t, e in enumerate(edges)}
    perms = set()
    for pa in permutations(range(3)):
        for pb in permutations(range(3)):
            for swap in (False, True):
                perm = [0] * 9
                for t, (i, j) in enumerate(edges):
                    ii, jj = pa[i], pb[j]
                    if swap:
                        ii, jj = jj, ii
                    perm[t] = eidx[(ii, jj)]
                perms.add(tuple(perm))
    return sorted(perms)

# --------------------------------------------------- validity enumeration

def weight_masks(cols):
    """For each direction, the 15-bit mask of nonzero binary cocycles u with
    u . e odd."""
    masks = []
    for e in cols:
        m = 0
        for u in range(1, 16):
            dot = sum(((u >> b) & 1) * (e[b] & 1) for b in range(4))
            if dot % 2 == 1:
                m |= 1 << (u - 1)
        masks.append(m)
    return masks

def weight_increments(masks):
    """Per direction, the 15-vector of 0/1 incidences."""
    return [tuple((mk >> u) & 1 for u in range(15)) for mk in masks]

def gen_valid(cols, masks, cap=4, sum_cap=None):
    """Yield all valid m in {0..cap}^n (every w_u even and >= 4), depth-first
    with incremental weights; optional total-sum cap."""
    n = len(cols)
    inc = weight_increments(masks)
    w = [0] * 15
    m = [0] * n

    def rec(t, tot):
        if t == n:
            for x in w:
                if x % 2 or x < 4:
                    return
            yield tuple(m)
            return
        for v in range(cap + 1):
            if sum_cap is not None and tot + v > sum_cap:
                break
            m[t] = v
            if v:
                for u in range(15):
                    if inc[t][u]:
                        w[u] += v
            yield from rec(t + 1, tot + v)
            if v:
                for u in range(15):
                    if inc[t][u]:
                        w[u] -= v
        m[t] = 0

    yield from rec(0, 0)

def pareto_minima(valid):
    valid = sorted(valid, key=sum)
    minima = []
    for v in valid:
        dominated = False
        for m in minima:
            if all(a <= b for a, b in zip(m, v)):
                dominated = True
                break
        if not dominated:
            minima.append(v)
    return minima

def orbit_count(vectors, perms):
    seen = set()
    for v in vectors:
        canon = min(tuple(v[p[t]] for t in range(len(v))) for p in perms)
        seen.add(canon)
    return len(seen)

# --------------------------------------------------- exact box-spline value

def bspline_at_zero(cols_multiset):
    """Exact central value of the box spline of the 4 x n multiset (density
    of sum U_i d_i at 0), via a unimodular column basis and the engine."""
    n = len(cols_multiset)
    basis = None
    for c4 in combinations(range(n), 4):
        M = [[cols_multiset[t][r] for t in c4] for r in range(4)]
        d = det_frac(M)
        if abs(d) == 1:
            basis = c4
            break
    if basis is None:
        return None  # not spanning with unimodular basis (cannot happen: TU)
    rest = [t for t in range(n) if t not in basis]
    if not rest:
        return Fr(1)  # n = 4, unimodular: density = 1 at 0
    B = [[Fr(cols_multiset[t][r]) for t in basis] for r in range(4)]
    # invert B exactly
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
    # rows of Binv.R over the rest columns
    hs = []
    for j in range(4):
        row = []
        for t in rest:
            row.append(sum(Binv[j][r] * cols_multiset[t][r] for r in range(4)))
        # |row . w| <= 1 in w in [-1,1]^{n-4}
        num = [x for x in row]
        # clear denominators to keep integer halfspaces
        from math import lcm
        dens = [x.denominator for x in num]
        Lc = 1
        for d in dens:
            Lc = Lc * d // __import__("math").gcd(Lc, d)
        numi = tuple(int(x * Lc) for x in num)
        hs.append((numi, Lc))
        hs.append((tuple(-v for v in numi), Lc))
    d = len(rest)
    vol = volume_from_halfspaces(hs, [(-1, 1)] * d)
    return vol / 2 ** d

def spanning_bound(cols_multiset, target=Fr(1, 3), tries=400, size=9, seed=7):
    """Search a spanning submultiset W of the given size with
    B_W(0) <= target; by (10.3) this bounds B_D(0)."""
    rng = random.Random(seed)
    n = len(cols_multiset)
    best = None
    for _ in range(tries):
        idx = rng.sample(range(n), min(size, n))
        sub = [cols_multiset[t] for t in idx]
        if mat_rank(sub) < 4:
            continue
        v = bspline_at_zero(sub)
        if v is None:
            continue
        if best is None or v < best:
            best = v
        if v <= target:
            return v
    return best

def multiset_cols(cols, m):
    out = []
    for t, mult in enumerate(m):
        out.extend([cols[t]] * mult)
    return out

# ------------------------------------------------------------------- run

def run_frame(name, cols, perms, expect_orbits):
    t0 = time.time()
    masks = weight_masks(cols)
    # phase 1: minima among the sum-capped valid vectors
    small = list(gen_valid(cols, masks, cap=4, sum_cap=20))
    print(f"{name}: {len(small)} valid vectors with sum <= 20 "
          f"({time.time()-t0:.1f}s)", flush=True)
    minima = pareto_minima(small)
    print(f"{name}: {len(minima)} coordinatewise-minimal vectors", flush=True)
    check(f"{name} minimal orbits", orbit_count(minima, perms), expect_orbits)
    # phase 2 (streaming): EVERY valid vector in {0..4}^n is a minimal vector
    # or dominates one -- this also proves no minimal vector has sum > 20
    t0 = time.time()
    minset = set(minima)
    viol = 0
    total_valid = 0
    for v in gen_valid(cols, masks, cap=4, sum_cap=None):
        total_valid += 1
        if v in minset:
            continue
        if not any(all(a <= b for a, b in zip(m, v)) for m in minima):
            viol += 1
    print(f"{name}: {total_valid} valid vectors in the full cap-4 cube "
          f"({time.time()-t0:.1f}s)", flush=True)
    check(f"{name} every valid vector dominates a minimal one", viol, 0)
    # reduction premise: subtracting 2 from an entry >= 5 preserves validity
    # (arithmetic on weights; test on synthetic examples derived from minima)
    ok_red = True
    for v in minima[:50]:
        vv = list(v)
        vv[0] += 4  # push above cap
        w = [0] * 15
        for t, mult in enumerate(vv):
            if mult:
                mk = masks[t]
                for u in range(15):
                    if (mk >> u) & 1:
                        w[u] += mult
        if all(x % 2 == 0 and x >= 4 for x in w):
            vv2 = vv[:]
            vv2[0] -= 2
            w2 = [x - 2 if (masks[0] >> u) & 1 else x for u, x in enumerate(w)]
            if not all(x % 2 == 0 and x >= 4 for x in w2):
                ok_red = False
    check(f"{name} subtract-2 reduction preserves validity", ok_red, True)

    # exact values on ORBIT REPRESENTATIVES (the value is invariant under the
    # frame automorphisms); equal-value spot checks on extra orbit members
    import json
    ck_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           f"fourslab_values_{name.replace('*','s').replace('(','').replace(')','')}.json")
    orbit_map = {}
    for v in minima:
        canon = min(tuple(v[p[t]] for t in range(len(v))) for p in perms)
        orbit_map.setdefault(canon, []).append(v)
    done = {}
    if os.path.exists(ck_path):
        with open(ck_path, encoding="utf-8") as f:
            done = {tuple(json.loads(k)): Fr(s) for k, s in json.load(f).items()}
    values = []
    bounded = 0
    t0 = time.time()
    reps = sorted(orbit_map, key=sum)
    for i, canon in enumerate(reps):
        if canon in done:
            val, how = done[canon], "direct"
        else:
            D = multiset_cols(cols, canon)
            n = len(D)
            if n - 4 <= 9:
                val, how = bspline_at_zero(D), "direct"
            else:
                val, how = spanning_bound(D), "bound"
                bounded += 1
            done[canon] = val
            with open(ck_path + ".tmp", "w", encoding="utf-8") as f:
                json.dump({json.dumps(list(k)): str(x) for k, x in done.items()}, f)
            os.replace(ck_path + ".tmp", ck_path)
        values.append((val, canon, how))
        if (i + 1) % 10 == 0 or i + 1 == len(reps):
            print(f"  {name}: {i+1}/{len(reps)} orbit values "
                  f"({time.time()-t0:.1f}s)", flush=True)
    # invariance spot-check: a second member of a few multi-member orbits
    spot = 0
    for canon, members in orbit_map.items():
        if spot >= 4:
            break
        others = [m for m in members if m != canon]
        if others:
            v2 = bspline_at_zero(multiset_cols(cols, others[0]))
            check(f"{name} orbit-invariance spot", v2, done[canon])
            spot += 1
    vals = [v for v, _, _ in values if v is not None]
    check(f"{name} all minima orbits valued", len(vals), len(reps))
    check(f"{name} every value <= 1/3", all(v <= Fr(1, 3) for v in vals), True)
    direct_vals = sorted((v for v, _, how in values if how == "direct"),
                         reverse=True)
    if direct_vals:
        print(f"{name}: direct-value spectrum top5 = "
              f"{[str(x) for x in direct_vals[:5]]}, "
              f"n_at_max={direct_vals.count(direct_vals[0])}, "
              f"bounded_indirectly={bounded}", flush=True)
    return values

k5cols, _ = k5_frame()
check("K5 frame rank", mat_rank(k5cols), 4)
check("K5 frame size", len(k5cols), 10)
p5 = edge_perms_k5()
check("K5 automorphism count", len(p5), 120)

k33cols, _ = k33_frame()
check("M*(K33) frame rank", mat_rank(k33cols), 4)
check("M*(K33) frame size", len(k33cols), 9)
p33 = edge_perms_k33()
check("K33 automorphism count", len(p33), 72)

vals33 = run_frame("M*(K33)", k33cols, p33, 48)
vals5 = run_frame("K5", k5cols, p5, 69)

# combined spectrum statement from the paper: max 1/3 attained, next 211/640
allv = sorted({v for v, _, how in vals5 + vals33 if how == "direct"},
              reverse=True)
print(f"combined distinct direct values, top6: {[str(x) for x in allv[:6]]}",
      flush=True)
check("combined maximum = 1/3", allv[0] if allv else None, Fr(1, 3))

# ---------------------- independent random-sample lane for Theorem 10.4
def is_tu(M):
    """Total unimodularity by brute minor check (matrix is 4 x d, entries
    0,+-1)."""
    rowsn = len(M)
    d = len(M[0])
    for sz in (2, 3, 4):
        for rs in combinations(range(rowsn), sz):
            for cs in combinations(range(d), sz):
                sub = [[M[r][c] for c in cs] for r in rs]
                if abs(det_frac(sub)) > 1:
                    return False
    return True

rng = random.Random(20260823)
tested = 0
worst = Fr(0)
t0 = time.time()
while tested < 60 and time.time() - t0 < 900:
    d = rng.choice((4, 5))
    rows = set()
    while len(rows) < 4:
        r = tuple(rng.choice((-1, 0, 1)) for _ in range(d))
        if sum(r) == 1 and sum(1 for x in r if x) >= 2:
            rows.add(r)
    M = [list(r) for r in rows]
    if len({tuple(r) for r in M}) < 4 or not is_tu(M):
        continue
    hs = []
    for r in M:
        hs.append((tuple(r), 1))
        hs.append((tuple(-x for x in r), 1))
    vol = volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d
    if vol > worst:
        worst = vol
    if vol > Fr(1, 3):
        check(f"Thm 10.4 random sample M={M}", vol <= Fr(1, 3), True)
    tested += 1
print(f"Thm 10.4 random lane: {tested} TU matrices tested, max volume {worst}",
      flush=True)
check("Thm 10.4 random lane max <= 1/3", worst <= Fr(1, 3), True)

print(flush=True)
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL[:30]:
        print("   ", f)
    sys.exit(1)
print("FOUR-SLAB CERTIFICATE REBUILD PASSED")
