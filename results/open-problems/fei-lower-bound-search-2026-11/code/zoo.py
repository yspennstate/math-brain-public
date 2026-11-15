"""zoo.py - structured monotone gates (graph properties, games, designs) scored as tower gates at every bias.

For each gate F and each bias p on a grid the script computes the Bellman value B_F(p) = (G_p(F) + W(p')) / J_p(F),
p' = Pr_p[F = -1], against a table W written by tower_vi.py --dump, and prints the largest excess B_F(p) - W(p), the
value at p = 1/2 and (when F is balanced) its H/(I-1).  A positive excess means F improves the tower at that bias.
usage: python zoo.py W_table.txt [OUT_lib.txt]     (OUT_lib gets "n hex" lines for every gate, for --libfile)
Convention: bit e of x set <=> element e present; x in U <=> F(x) = -1 <=> the property holds.
"""
import itertools
import sys

import numpy as np

from tower_vi import stats_grid


def allx(n):
    return np.arange(1 << n, dtype=np.int64)


def contains_any(n, masks):
    X = allx(n)
    U = np.zeros(1 << n, dtype=bool)
    for m in masks:
        U |= (X & m) == m
    return U


def reach_from(n, edges_vars, nv, sources, X=None):
    """edges_vars: list of (u, v, var) for bond models; returns reach bitmask array after closure from `sources`."""
    X = allx(n) if X is None else X
    reach = np.full(1 << n, sum(1 << s for s in sources), dtype=np.int64)
    for _ in range(nv):
        old = reach.copy()
        for u, v, e in edges_vars:
            has = (X >> e) & 1
            reach |= ((has & (reach >> u)) & 1) << v
            reach |= ((has & (reach >> v)) & 1) << u
        if (old == reach).all():
            break
    return reach


def site_reach(n, adj, sources_mask_cells, X=None):
    """site model: cells are the variables; reach = set of present cells connected to a present source cell."""
    X = allx(n) if X is None else X
    reach = X & sources_mask_cells
    for _ in range(n):
        old = reach.copy()
        for u in range(n):
            ru = (reach >> u) & 1
            for v in adj[u]:
                reach |= (ru & (X >> v) & 1) << v
        if (old == reach).all():
            break
    return reach


def edges_complete(nv):
    return [(u, v) for u in range(nv) for v in range(u + 1, nv)]


def gates():
    out = []

    def add(name, n, U):
        U = np.asarray(U, dtype=bool)
        if U.all() or not U.any():
            return
        out.append((name, n, U))

    # bipartite matchings saturating the left side
    for a, b in ((2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 3), (3, 4), (3, 5), (4, 4)):
        n = a * b
        masks = set()
        for inj in itertools.permutations(range(b), a):
            masks.add(sum(1 << (i * b + j) for i, j in enumerate(inj)))
        add("match_K%d,%d" % (a, b), n, contains_any(n, masks))
    # perfect matchings / hamiltonian cycles / triangles / connectivity of complete graphs
    for nv in (4, 5, 6):
        E = edges_complete(nv)
        n = len(E)
        idx = {e: i for i, e in enumerate(E)}
        tri = [sum(1 << idx[e] for e in itertools.combinations(t, 2)) for t in itertools.combinations(range(nv), 3)]
        add("triangle_K%d" % nv, n, contains_any(n, tri))
        ham = set()
        for perm in itertools.permutations(range(1, nv)):
            cyc = (0,) + perm
            ham.add(sum(1 << idx[tuple(sorted((cyc[i], cyc[(i + 1) % nv])))] for i in range(nv)))
        add("hamcycle_K%d" % nv, n, contains_any(n, ham))
        hp = set()
        for perm in itertools.permutations(range(nv)):
            hp.add(sum(1 << idx[tuple(sorted((perm[i], perm[i + 1])))] for i in range(nv - 1)))
        add("hampath_K%d" % nv, n, contains_any(n, hp))
        ev = [(u, v, idx[(u, v)]) for u, v in E]
        r = reach_from(n, ev, nv, [0])
        add("connected_K%d" % nv, n, r == (1 << nv) - 1)
        add("st_conn_K%d" % nv, n, (r >> 1) & 1 == 1)
        X = allx(n)
        deg_ok = np.ones(1 << n, dtype=bool)
        for v in range(nv):
            m = sum(1 << idx[e] for e in E if v in e)
            deg_ok &= (X & m) != 0
        add("no_isolated_K%d" % nv, n, deg_ok)
        if nv % 2 == 0:
            def pms(vs):
                if not vs:
                    yield 0
                    return
                a = vs[0]
                for b in vs[1:]:
                    rest = [x for x in vs if x not in (a, b)]
                    for m in pms(rest):
                        yield m | (1 << idx[(a, b)])
            add("pm_K%d" % nv, n, contains_any(n, list(pms(list(range(nv))))))
    # bipartite connectivity and 4-cycles
    for a, b in ((2, 3), (2, 4), (3, 3), (3, 4), (4, 4), (2, 5), (3, 5)):
        n = a * b
        ev = [(i, a + j, i * b + j) for i in range(a) for j in range(b)]
        r = reach_from(n, ev, a + b, [0])
        add("connected_K%d,%d" % (a, b), n, r == (1 << (a + b)) - 1)
        c4 = [sum(1 << (i * b + j) for i in ii for j in jj) for ii in itertools.combinations(range(a), 2) for jj in itertools.combinations(range(b), 2)]
        add("c4_K%d,%d" % (a, b), n, contains_any(n, c4))
    # cube, octahedron, Petersen: perfect matching and connectivity
    cube = [(u, u ^ (1 << i)) for u in range(8) for i in range(3) if u < u ^ (1 << i)]
    octa = [(u, v) for u in range(6) for v in range(u + 1, 6) if u + v != 5]
    pet = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    prism = [(i, (i + 1) % 3) for i in range(3)] + [(3 + i, 3 + (i + 1) % 3) for i in range(3)] + [(i, i + 3) for i in range(3)]
    wheel5 = [(0, i) for i in range(1, 6)] + [(i, i % 5 + 1) for i in range(1, 6)]
    for name, E, nv in (("cube", cube, 8), ("octa", octa, 6), ("petersen", pet, 10), ("prism", prism, 6), ("wheel5", wheel5, 6)):
        E = [tuple(sorted(e)) for e in E]
        n = len(E)
        idx = {e: i for i, e in enumerate(E)}
        ev = [(u, v, idx[(u, v)]) for u, v in E]
        r = reach_from(n, ev, nv, [0])
        add("connected_" + name, n, r == (1 << nv) - 1)

        def pms(vs):
            if not vs:
                yield 0
                return
            a = vs[0]
            for b in vs[1:]:
                e = tuple(sorted((a, b)))
                if e in idx:
                    rest = [x for x in vs if x not in (a, b)]
                    for m in pms(rest):
                        yield m | (1 << idx[e])
        if nv % 2 == 0:
            add("pm_" + name, n, contains_any(n, list(pms(list(range(nv))))))
    # self-dual bond crossing of the (m+1) x m lattice (m = 2 is the bridge)
    for m in (2, 3):
        vid = lambda i, j: i * m + j
        ev = []
        e = 0
        for j in range(m):
            for i in range(m):
                ev.append((vid(i, j), vid(i + 1, j), e)); e += 1
        for i in range(1, m):
            for j in range(m - 1):
                ev.append((vid(i, j), vid(i, j + 1), e)); e += 1
        n = e
        r = reach_from(n, ev, (m + 1) * m, [vid(0, j) for j in range(m)])
        right = sum(1 << vid(m, j) for j in range(m))
        add("bondcross_%d" % m, n, (r & right) != 0)
    # Hex boards (site crossing left-right on an a x b rhombus)
    for a, b in ((2, 2), (3, 3), (3, 4), (4, 3), (4, 4), (2, 5), (3, 5), (5, 3), (2, 7), (2, 8)):
        n = a * b
        cid = lambda r, c: r * b + c
        adj = [[] for _ in range(n)]
        for r in range(a):
            for c in range(b):
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)):
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < a and 0 <= cc < b:
                        adj[cid(r, c)].append(cid(rr, cc))
        left = sum(1 << cid(r, 0) for r in range(a))
        right = sum(1 << cid(r, b - 1) for r in range(a))
        rch = site_reach(n, adj, left)
        add("hex_%dx%d" % (a, b), n, (rch & right) != 0)
    # the game of Y on a triangle of side s (self-dual)
    for s in (3, 4, 5):
        cells = [(r, c) for r in range(s) for c in range(r + 1)]
        n = len(cells)
        cidx = {rc: i for i, rc in enumerate(cells)}
        adj = [[] for _ in range(n)]
        for (r, c), i in cidx.items():
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)):
                if (r + dr, c + dc) in cidx:
                    adj[i].append(cidx[(r + dr, c + dc)])
        sideA = sum(1 << i for (r, c), i in cidx.items() if c == 0)
        sideB = sum(1 << i for (r, c), i in cidx.items() if c == r)
        sideC = sum(1 << i for (r, c), i in cidx.items() if r == s - 1)
        X = allx(n)
        win = np.zeros(1 << n, dtype=bool)
        for (r, c), i in cidx.items():
            if c == 0:
                rch = site_reach(n, adj, 1 << i)
                win |= ((rch & sideB) != 0) & ((rch & sideC) != 0)
        add("Y_%d" % s, n, win)
    # designs: contains a block
    fano = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]
    add("fano_line", 7, contains_any(7, [sum(1 << i for i in L) for L in fano]))
    ag = []
    for a_, b_ in ((1, 0), (0, 1), (1, 1), (1, 2)):
        for c_ in range(3):
            ag.append(tuple(x * 3 + y for x in range(3) for y in range(3) if (a_ * x + b_ * y) % 3 == c_))
    add("ag23_line", 9, contains_any(9, [sum(1 << i for i in L) for L in ag]))
    ttt = [L for L in ag if True][:0] + [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    add("tictactoe_line", 9, contains_any(9, [sum(1 << i for i in L) for L in ttt]))
    pg3 = [tuple(sorted((d + s_) % 13 for d in (0, 1, 3, 9))) for s_ in range(13)]
    add("pg23_line", 13, contains_any(13, [sum(1 << i for i in L) for L in pg3]))
    # 2-fold cover type: contains two disjoint blocks of the Fano complement etc. are left to composition
    # thresholds
    for n in range(7, 16):
        pc = np.array([bin(x).count("1") for x in range(1 << n)])
        for k in range(2, n):
            add("thr_%d_of_%d" % (k, n), n, pc >= k)
    return out


def main():
    wt = np.loadtxt(sys.argv[1], comments="#")
    t, W = wt[:, 0], wt[:, 1]
    ps = np.concatenate([np.linspace(0.02, 0.98, 97), [0.34375, 0.381966011250105, 0.618033988749895, 0.65625]])
    ps = np.unique(ps)
    half = int(np.argmin(np.abs(ps - 0.5)))
    tq = np.log2(ps / (1 - ps))
    Wp = np.interp(tq, t, W)
    lib = open(sys.argv[2], "w", encoding="utf-8") if len(sys.argv) > 2 else None
    rows = []
    for name, n, U in gates():
        G, J, P = stats_grid(U[None, :].astype(np.uint8), n, ps)
        G, J, P = G[0], J[0], P[0]
        Pc = np.clip(P, 1e-12, 1 - 1e-12)
        cont = np.interp(np.clip(np.log2(Pc / (1 - Pc)), t[0], t[-1]), t, W)
        ok = np.isfinite(J) & (J > 1 + 1e-9)
        B = np.where(ok, (G + cont) / np.where(ok, J, 1.0), -1.0)
        ex = B - Wp
        j = int(np.argmax(ex))
        bal = ""
        if abs(P[half] - 0.5) < 1e-12 and J[half] > 1:
            bal = " bal H/(I-1)=%.6f" % (G[half] / (J[half] - 1))
        rows.append((ex[j], "%-18s n=%2d  best excess %+.5f at p=%.4f (p'=%.4f G=%.4f J=%.4f)  at 1/2: B=%.5f p'=%.4f%s"
                     % (name, n, ex[j], ps[j], P[j], G[j], J[j], B[half], P[half], bal)))
        if lib:
            tab = 0
            for x in np.nonzero(U)[0]:
                tab |= 1 << int(x)
            lib.write("%d %x\n" % (n, tab))
    rows.sort(key=lambda r: -r[0])
    print("W(1/2) in the table: %.6f;  %d gates" % (np.interp(0.0, t, W), len(rows)))
    for _, line in rows:
        print(line)


if __name__ == "__main__":
    main()
