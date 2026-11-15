"""Filtration witness on structured functions with up to 21 variables (FLOW section 12(j)(4)).

Functions with a transitive symmetry group are tested at coordinate 0 only; the others at every coordinate.
For each function: Inf_i, E_i/Inf_i, the minimum over orderings of L^pi_i/Inf_i (shortest path of filt_cs.py),
and M of the best ordering.

usage:
  python filt_big.py LIST            LIST = comma separated names, or a group: graph5 graph6 graph7 plane cyclic misc
  python filt_big.py names           print the names
"""
import sys
import time
import itertools
import numpy as np
from local_cs import wht, phi
from filt_cs import best_order, zeta


def tt_from_bool(true_mask):
    return np.where(true_mask, -1.0, 1.0)


# ---------------------------------------------------------------- graph properties
def graph_ctx(v):
    edges = list(itertools.combinations(range(v), 2))
    E = len(edges)
    idx = np.arange(1 << E, dtype=np.int64)
    bit = [((idx >> e) & 1).astype(np.uint8) for e in range(E)]
    deg = [np.zeros(1 << E, dtype=np.uint8) for _ in range(v)]
    for e, (a, b) in enumerate(edges):
        deg[a] += bit[e]
        deg[b] += bit[e]
    eid = {p: e for e, p in enumerate(edges)}
    return dict(v=v, edges=edges, E=E, idx=idx, bit=bit, deg=deg, eid=eid)


def reach_from(c, s):
    v = c["v"]
    reach = np.full(1 << c["E"], 1 << s, dtype=np.uint16)
    for _ in range(v - 1):
        for e, (a, b) in enumerate(c["edges"]):
            has = c["bit"][e].astype(np.uint16)
            ra = (reach >> a) & 1
            rb = (reach >> b) & 1
            reach |= ((has & ra) << b) | ((has & rb) << a)
    return reach


def graph_props(v):
    c = graph_ctx(v)
    E, idx, bit, deg, eid = c["E"], c["idx"], c["bit"], c["deg"], c["eid"]
    out = {}

    def lazy(name, fn):
        out["K%d_%s" % (v, name)] = (E, fn, True)

    lazy("connected", lambda: tt_from_bool(reach_from(c, 0) == (1 << v) - 1))

    def clique(k):
        acc = np.zeros(1 << E, dtype=bool)
        for S in itertools.combinations(range(v), k):
            m = 0
            for p in itertools.combinations(S, 2):
                m |= 1 << eid[p]
            acc |= (idx & m) == m
        return tt_from_bool(acc)
    lazy("triangle", lambda: clique(3))
    lazy("K4", lambda: clique(4))
    lazy("dominating", lambda: tt_from_bool(np.any([d == v - 1 for d in deg], axis=0)))
    lazy("no_isolated", lambda: tt_from_bool(np.all([d >= 1 for d in deg], axis=0)))
    lazy("mindeg2", lambda: tt_from_bool(np.all([d >= 2 for d in deg], axis=0)))
    for k in range(2, v - 1):
        lazy("maxdeg%d" % k, (lambda k: lambda: tt_from_bool(np.any([d >= k for d in deg], axis=0)))(k))

    def bipartite():
        acc = np.zeros(1 << E, dtype=bool)
        for side in range(1 << (v - 1)):
            m = 0
            for (a, b), e in eid.items():
                if ((side >> a) & 1) == ((side >> b) & 1):
                    m |= 1 << e
            acc |= (idx & m) == 0
        return tt_from_bool(acc)
    lazy("bipartite", bipartite)

    def forest():
        comp = np.zeros(1 << E, dtype=np.uint8)
        for s in range(v):
            r = reach_from(c, s)
            comp += ((r & ((1 << s) - 1)) == 0).astype(np.uint8)
        ne = np.zeros(1 << E, dtype=np.uint8)
        for b in bit:
            ne += b
        return tt_from_bool(ne + comp == v)
    lazy("forest", forest)

    def ham_cycle():
        acc = np.zeros(1 << E, dtype=bool)
        for perm in itertools.permutations(range(1, v)):
            if perm[0] > perm[-1]:
                continue
            cyc = (0,) + perm
            m = 0
            for t in range(v):
                a, b = cyc[t], cyc[(t + 1) % v]
                m |= 1 << eid[(min(a, b), max(a, b))]
            acc |= (idx & m) == m
        return tt_from_bool(acc)
    lazy("hamcycle", ham_cycle)

    if v % 2 == 0:
        def pm():
            acc = np.zeros(1 << E, dtype=bool)

            def rec(rest, m):
                nonlocal acc
                if not rest:
                    acc |= (idx & m) == m
                    return
                a = rest[0]
                for b in rest[1:]:
                    rec([x for x in rest if x not in (a, b)], m | (1 << eid[(a, b)]))
            rec(list(range(v)), 0)
            return tt_from_bool(acc)
        lazy("perfmatch", pm)
    return out


# ---------------------------------------------------------------- DNFs from set systems
def dnf(n, terms):
    idx = np.arange(1 << n, dtype=np.int64)
    acc = np.zeros(1 << n, dtype=bool)
    for T in terms:
        m = 0
        for j in T:
            m |= 1 << j
        acc |= (idx & m) == m
    return tt_from_bool(acc)


def gf4_plane():
    mul = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    pts = []
    for vec in itertools.product(range(4), repeat=3):
        if vec == (0, 0, 0):
            continue
        lead = next(x for x in vec if x)
        if lead == 1:
            pts.append(vec)
    assert len(pts) == 21
    lines = []
    for L in pts:
        on = [k for k, P in enumerate(pts)
              if (mul[L[0]][P[0]] ^ mul[L[1]][P[1]] ^ mul[L[2]][P[2]]) == 0]
        assert len(on) == 5
        lines.append(on)
    return lines


def gfp_plane(p):
    pts = []
    for vec in itertools.product(range(p), repeat=3):
        if vec == (0, 0, 0):
            continue
        lead = next(x for x in vec if x)
        if lead == 1:
            pts.append(vec)
    lines = []
    for L in pts:
        lines.append([k for k, P in enumerate(pts) if sum(a * b for a, b in zip(L, P)) % p == 0])
    return len(pts), lines


def plane_fns():
    out = {}
    n7, l7 = gfp_plane(2)
    out["FANO_dnf"] = (n7, lambda: dnf(n7, l7), True)
    n13, l13 = gfp_plane(3)
    out["PG23_dnf"] = (n13, lambda: dnf(n13, l13), True)
    out["PG24_dnf"] = (21, lambda: dnf(21, gf4_plane()), True)
    # affine planes: points of F_p^2, lines of p points
    for p in (3, 4):
        if p == 3:
            pts = list(itertools.product(range(3), repeat=2))
            lines = []
            for a, b, c in [(1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 2, 0)]:
                for cc in range(3):
                    lines.append([k for k, (x, y) in enumerate(pts) if (a * x + b * y) % 3 == cc])
            out["AG23_dnf"] = (9, (lambda L: lambda: dnf(9, L))(lines), True)
        else:
            full = gf4_plane()
            drop = set(full[0])
            keep = [k for k in range(21) if k not in drop]
            ren = {k: t for t, k in enumerate(keep)}
            lines = [[ren[k] for k in L if k in ren] for L in full[1:]]
            out["AG24_dnf"] = (16, (lambda L: lambda: dnf(16, L))(lines), True)
    return out


def cyclic_fns():
    out = {}
    for n, w in [(8, 3), (10, 3), (12, 3), (12, 4), (14, 4), (16, 4), (18, 4), (20, 4), (16, 5), (20, 5), (21, 5),
                 (20, 2), (16, 2), (12, 2)]:
        terms = [[(j + t) % n for t in range(w)] for j in range(n)]
        out["CYC_n%d_w%d" % (n, w)] = (n, (lambda n, T: lambda: dnf(n, T))(n, terms), True)
    # spread cyclic terms {j, j+1, j+3} (perfect difference set type) and {j, j+1, j+3, j+9} mod 13
    for n, D in [(7, (0, 1, 3)), (13, (0, 1, 3, 9)), (21, (0, 1, 4, 14, 16)), (15, (0, 1, 3)), (20, (0, 1, 3)),
                 (20, (0, 1, 4, 6)), (21, (0, 1, 3, 7))]:
        terms = [[(j + d) % n for d in D] for j in range(n)]
        out["DIFF_n%d_%s" % (n, "".join("%x" % d for d in D))] = (n, (lambda n, T: lambda: dnf(n, T))(n, terms), True)
    return out


def misc_fns():
    out = {}

    def hwb(n):
        idx = np.arange(1 << n, dtype=np.int64)
        wt = np.zeros(1 << n, dtype=np.int64)
        for j in range(n):
            wt += (idx >> j) & 1
        val = np.where(wt > 0, (idx >> np.maximum(wt - 1, 0)) & 1, 0)
        return tt_from_bool(val == 1)
    for n in (8, 12, 16):
        out["HWB_%d" % n] = (n, (lambda n: lambda: hwb(n))(n), False)

    def tribes(w, s):
        return dnf(w * s, [[t * w + j for j in range(w)] for t in range(s)])
    for w, s in [(3, 5), (3, 6), (3, 7), (4, 4), (4, 5), (5, 4), (2, 9), (2, 10)]:
        out["TRIBES_%dx%d" % (w, s)] = (w * s, (lambda w, s: lambda: tribes(w, s))(w, s), False)

    def alt(depth, n):
        # read-once alternating AND/OR of fan-in 2, AND at the leaves
        idx = np.arange(1 << n, dtype=np.int64)
        vals = [((idx >> j) & 1).astype(bool) for j in range(n)]
        op_and = True
        while len(vals) > 1:
            vals = [(vals[2 * t] & vals[2 * t + 1]) if op_and else (vals[2 * t] | vals[2 * t + 1])
                    for t in range(len(vals) // 2)]
            op_and = not op_and
        return tt_from_bool(vals[0])
    out["ALT_16"] = (16, lambda: alt(4, 16), True)

    def maj_of_and(m, w):
        n = m * w
        idx = np.arange(1 << n, dtype=np.int64)
        cnt = np.zeros(1 << n, dtype=np.int64)
        for t in range(m):
            mask = sum(1 << (t * w + j) for j in range(w))
            cnt += (idx & mask) == mask
        return cnt
    out["MAJ5_AND2"] = (10, lambda: tt_from_bool(maj_of_and(5, 2) >= 3), True)
    out["MAJ5_AND3"] = (15, lambda: tt_from_bool(maj_of_and(5, 3) >= 3), True)
    out["MAJ7_AND2"] = (14, lambda: tt_from_bool(maj_of_and(7, 2) >= 4), True)
    out["TH2_AND3x6"] = (18, lambda: tt_from_bool(maj_of_and(6, 3) >= 2), True)
    out["TH2_AND4x5"] = (20, lambda: tt_from_bool(maj_of_and(5, 4) >= 2), True)
    out["TH2_AND2x8"] = (16, lambda: tt_from_bool(maj_of_and(8, 2) >= 2), True)
    out["TH3_AND2x9"] = (18, lambda: tt_from_bool(maj_of_and(9, 2) >= 3), True)

    def rand_mdnf(n, w, m, seed):
        rng = np.random.default_rng(seed)
        return dnf(n, [list(rng.choice(n, w, replace=False)) for _ in range(m)])
    for n, w, m, seed in [(16, 3, 6, 1), (16, 3, 10, 2), (16, 4, 12, 3), (18, 4, 14, 4), (18, 3, 8, 5),
                          (20, 4, 12, 6), (20, 5, 24, 7)]:
        out["RDNF_n%d_w%d_m%d" % (n, w, m)] = (n, (lambda a: lambda: rand_mdnf(*a))((n, w, m, seed)), False)
    return out


def bip_fns():
    """properties of bipartite graphs on K_{l,r}; variable (a, b) has index a * r + b; all are edge-transitive."""
    out = {}

    def ctx(l, r):
        n = l * r
        idx = np.arange(1 << n, dtype=np.int64)
        return n, idx

    def saturating(l, r):
        # a matching that covers the left side (l <= r)
        n, idx = ctx(l, r)
        acc = np.zeros(1 << n, dtype=bool)
        for perm in itertools.permutations(range(r), l):
            m = 0
            for a, b in enumerate(perm):
                m |= 1 << (a * r + b)
            acc |= (idx & m) == m
        return tt_from_bool(acc)

    def degs(l, r):
        n, idx = ctx(l, r)
        left = [np.zeros(1 << n, dtype=np.uint8) for _ in range(l)]
        right = [np.zeros(1 << n, dtype=np.uint8) for _ in range(r)]
        for a in range(l):
            for b in range(r):
                bit = ((idx >> (a * r + b)) & 1).astype(np.uint8)
                left[a] += bit
                right[b] += bit
        return left, right

    def no_isolated(l, r):
        left, right = degs(l, r)
        return tt_from_bool(np.all([d >= 1 for d in left + right], axis=0))

    def c4(l, r):
        n, idx = ctx(l, r)
        acc = np.zeros(1 << n, dtype=bool)
        for a1, a2 in itertools.combinations(range(l), 2):
            for b1, b2 in itertools.combinations(range(r), 2):
                m = (1 << (a1 * r + b1)) | (1 << (a1 * r + b2)) | (1 << (a2 * r + b1)) | (1 << (a2 * r + b2))
                acc |= (idx & m) == m
        return tt_from_bool(acc)

    for l, r in [(3, 3), (3, 4), (4, 4), (3, 5), (4, 5), (3, 6), (5, 5), (4, 6)]:
        out["PM_K%d%d" % (l, r)] = (l * r, (lambda l, r: lambda: saturating(l, r))(l, r), True)
    for l, r in [(3, 3), (4, 4), (4, 5), (5, 5)]:
        out["NOISO_K%d%d" % (l, r)] = (l * r, (lambda l, r: lambda: no_isolated(l, r))(l, r), l == r)
        out["C4_K%d%d" % (l, r)] = (l * r, (lambda l, r: lambda: c4(l, r))(l, r), True)
    return out


def catalogue():
    cat = {}
    groups = {}
    g = bip_fns()
    cat.update(g)
    groups["bip"] = list(g)
    for v in (5, 6, 7):
        g = graph_props(v)
        cat.update(g)
        groups["graph%d" % v] = list(g)
    for name, fn in [("plane", plane_fns), ("cyclic", cyclic_fns), ("misc", misc_fns)]:
        g = fn()
        cat.update(g)
        groups[name] = list(g)
    return cat, groups


def best_M(p, q, m):
    """min over orderings of max_{K>=1} A_{>=K} B_{<=K} / Inf_i^2 (bottleneck path in the subset lattice):
    the step R - j -> R costs (tot_a - a(R - j)) * b(R)."""
    a = zeta(p, m)
    b = zeta(q, m)
    size = 1 << m
    idx = np.arange(size)
    pc = np.zeros(size, dtype=np.int8)
    for j in range(m):
        pc += ((idx >> j) & 1).astype(np.int8)
    tot_a = float(a[size - 1])
    inf = float(b[size - 1])
    best = np.full(size, np.inf)
    best[0] = 0.0
    for layer in range(1, m + 1):
        R = idx[pc == layer]
        for j in range(m):
            sel = R[(R >> j) & 1 == 1]
            prev = sel ^ (1 << j)
            cand = np.maximum(best[prev], (tot_a - a[prev]) * b[sel])
            best[sel] = np.minimum(best[sel], cand)
    return float(best[size - 1]) / inf ** 2


def run(name, n, make, transitive):
    t0 = time.time()
    f = make()
    mean = float(f.mean())
    mu = wht(f, n) ** 2
    idx = np.arange(1 << n)
    rows = []
    for i in ([0] if transitive else range(n)):
        lo = idx[(idx >> i) & 1 == 0]
        p = mu[lo]
        q = mu[lo | (1 << i)]
        inf = float(q.sum())
        if inf < 1e-12:
            continue
        E = float(phi(p, q).sum())
        val, order, M = best_order(p, q, n - 1)
        rows.append((val / inf, E / inf, inf, M, i, best_M(p, q, n - 1)))
    if not rows:
        print("%-18s n=%2d constant or no relevant coordinate" % (name, n), flush=True)
        return
    F, E, inf, M, i, _ = min(rows)
    minE = min(r[1] for r in rows)
    minM = min(r[5] for r in rows)
    print("%-18s n=%2d mean=%+.4f Inf=%.5f minE=%.4f F=%.4f (i=%d, E_i=%.4f, M=%.3f) minM=%.3f %s  %.0fs"
          % (name, n, mean, inf, minE, F, i, E, M, minM, "transitive" if transitive else "all coords",
             time.time() - t0), flush=True)


def main():
    cat, groups = catalogue()
    arg = sys.argv[1]
    if arg == "names":
        for g, names in groups.items():
            print(g, ":", " ".join(names))
        return
    names = []
    for tok in arg.split(","):
        names += groups.get(tok, [tok])
    for name in names:
        n, make, transitive = cat[name]
        run(name, n, make, transitive)


if __name__ == "__main__":
    main()
