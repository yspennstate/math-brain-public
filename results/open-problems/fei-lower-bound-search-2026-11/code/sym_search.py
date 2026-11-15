"""sym_search.py - search over ALL Boolean functions invariant under a permutation group of the inputs.

A function invariant under a group Gamma acting on the m inputs is a sign per orbit of points (K orbits), and its
Fourier coefficients are constant on orbits of index sets, so one evaluation costs K, not 2^m.  The 18-input record
(matchings of K33 plus one coin per edge) is invariant under Aut(K33) acting on edges and coins together; the coin
search fei_coin.c only reaches functions affine in the coins, this one reaches every invariant function.

Score on uniform inputs against a Bellman table W (file: log-odds, W):
    G = entropy of the normalised non-constant weights, J = I / Var, p' = Pr[f = -1],
    slack = G - c J + W(p'),  c = W(1/2).      slack > 0 would be a new lower bound.
Every reported state is expanded to its explicit truth table and re-scored by a full transform (second path).

K <= 34: every invariant function is scored (exhaustive).  Larger K: seeds (matching, Hamilton-cycle and triangle
properties of the graph, and with one coin per edge the record's coin rule), their single and pair flips, then
annealing from seeds, perturbed seeds and random starts.

usage: python3 sym_search.py STRUCT WFILE OUT [--secs 3000] [--seed 1] [--T0 0.3] [--T1 0.002] [--batch 64]
                                             [--anneal] [--pairs]
STRUCT: k33c k33v k33 k4c k4 k5 k6 k34 k44 pet q3e octa agl11 agl13 agl17 pgl11 pgl13 pgl17 dih12 dih14 dih16 k5c
        c6c c7c c8c k23c k24c k33mc w4c diac k113c (a small graph with one coin per edge)
        k33cx1 k33cx2 (k33c with 1 or 2 further inputs that the group of K33 leaves in place)
        k33k33 (two 3x3 grids and their swap), q4v (vertices of the 4-cube), ag24 pg24 (planes over GF(4))
"""
import itertools
import sys
import time

import numpy as np


EXTRA_INPUTS = [0]                          # set by struct() for k33cx1 / k33cx2


def opt(name, default, typ=float):
    return typ(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


# ---------- structures: m and generators (permutations of range(m)) ----------
def edge_perm(edges, vp):
    idx = {frozenset(e): i for i, e in enumerate(edges)}
    return [idx[frozenset((vp[u], vp[v]))] for (u, v) in edges]


def sym_gens(n, off=0, total=None):
    total = total if total is not None else n
    a = list(range(total)); b = list(range(total))
    if n >= 2:
        a[off], a[off + 1] = off + 1, off
        for i in range(n):
            b[off + i] = off + (i + 1) % n
    return [a, b]


def with_coins(perms, E):
    return [p + [E + q for q in p] for p in perms]


def block_aut(nv, blocks):
    """generators of the automorphism group of a set system on nv <= 9 points (brute force)"""
    bs = {frozenset(b) for b in blocks}
    idt = tuple(range(nv)); grp = {idt}; vgens = []
    for vp in itertools.permutations(range(nv)):
        if vp in grp or not all(frozenset(vp[u] for u in b) in bs for b in blocks):
            continue
        vgens.append(list(vp)); stack = list(grp)
        while stack:
            a = stack.pop()
            for g in vgens:
                b = tuple(g[a[i]] for i in range(nv))
                if b not in grp:
                    grp.add(b); stack.append(b)
    return vgens


def point_struct(name):
    """points with r coins each: fanoc fanoc2 ag23c q3vc w33c s<n>c, and the bare projective plane pg23"""
    r = 1
    if name.startswith("fano"):
        n = 7; r = 2 if name.endswith("2") else 1
        vg = block_aut(7, [(i, (i + 1) % 7, (i + 3) % 7) for i in range(7)])
    elif name == "ag23c":
        n = 9; lines = set()
        for x in range(3):
            for y in range(3):
                for dx, dy in ((1, 0), (0, 1), (1, 1), (1, 2)):
                    lines.add(tuple(sorted(3 * ((x + k * dx) % 3) + (y + k * dy) % 3 for k in range(3))))
        vg = block_aut(9, sorted(lines))
    elif name == "q3vc":
        n = 8
        vg = [[u ^ 1 for u in range(8)],
              [((u & 1) << 1) | ((u >> 1) & 1) | (u & 4) for u in range(8)],
              [((u & 1) << 1) | ((u & 2) << 1) | ((u >> 2) & 1) for u in range(8)]]
    elif name == "w33c":
        n = 9
        vg = sym_gens(3, 0, 9) + [[(i + 3) % 9 for i in range(9)],
                                  [i + 3 if i < 3 else i - 3 if i < 6 else i for i in range(9)]]
    elif name == "pg23":
        vecs = [v for v in itertools.product(range(3), repeat=3) if any(v) and next(x for x in v if x) == 1]
        vid = {v: k for k, v in enumerate(vecs)}
        mats = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    M = [[int(a == b) for b in range(3)] for a in range(3)]; M[i][j] = 1; mats.append(M)
        mats.append([[2, 0, 0], [0, 1, 0], [0, 0, 1]])
        gens = []
        for M in mats:
            g = []
            for v in vecs:
                w = [sum(M[i][j] * v[j] for j in range(3)) % 3 for i in range(3)]
                lead = next(x for x in w if x)                 # 1 or 2, its own inverse mod 3
                g.append(vid[tuple((x * lead) % 3 for x in w)])
            gens.append(g)
        return 13, gens, None
    else:
        n = int(name[1:-1]); vg = sym_gens(n)
    m = n * (1 + r)
    gens = [list(p) + [n * (1 + l) + q for l in range(r) for q in p] for p in vg]
    if r == 2:
        t = list(range(m)); t[n], t[2 * n] = 2 * n, n          # the two coins of a point are interchangeable
        gens.append(t)
    return m, gens, None


LCF = {"heawood": (14, [5, -5]), "mobkan": (16, [5, -5]), "pappus": (18, [5, 7, -7, 7, -7, -5]),
       "desarg": (20, [5, -5, 9, -9]), "dodec": (20, [10, 7, 4, -4, -7, 10, -4, 7, -7, 4])}


def named_graph(name):
    # adjacency sets of a small vertex-transitive graph: cubic ones by LCF code, Clebsch, Shrikhande
    if name in LCF:
        n, code = LCF[name]
        adj = [set() for _ in range(n)]
        for i in range(n):
            for j in ((i + 1) % n, (i + code[i % len(code)]) % n):
                adj[i].add(j); adj[j].add(i)
        return adj
    if name == "clebsch":
        return [{v for v in range(16) if bin(u ^ v).count("1") == 1 or u ^ v == 15} for u in range(16)]
    if name == "shrik":
        d = [(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)]
        return [{4 * ((u // 4 + a) % 4) + (u % 4 + b) % 4 for a, b in d} for u in range(16)]
    raise SystemExit("unknown graph " + name)


def graph_auts(adj):
    # all automorphisms, by backtracking in vertex order
    n = len(adj)
    out, img, used = [], [], set()

    def rec():
        v = len(img)
        if v == n:
            out.append(list(img))
            return
        for w in range(n):
            if w in used or len(adj[w]) != len(adj[v]):
                continue
            if all((u in adj[v]) == (img[u] in adj[w]) for u in range(v)):
                img.append(w); used.add(w)
                rec()
                img.pop(); used.discard(w)
    rec()
    return out


def few_gens(auts):
    # a short generating list: take an automorphism whenever it lies outside the group generated so far
    n = len(auts[0])
    G, gens = {tuple(range(n))}, []
    for a in auts:
        if tuple(a) in G:
            continue
        gens.append(list(a))
        front = list(G)
        while front:
            new = []
            for g in front:
                for h in gens:
                    k = tuple(h[x] for x in g)
                    if k not in G:
                        G.add(k); new.append(k)
            front = new
    assert len(G) == len(auts)
    return gens


GF_POLY = {4: (2, [1, 1, 1]), 8: (2, [1, 1, 0, 1]), 9: (3, [1, 0, 1]), 16: (2, [1, 1, 0, 0, 1])}   # monic, low degree first


def gf_tables(q):
    """p, k and the addition and multiplication tables of GF(q), q prime or in GF_POLY; an element is the integer
    whose base-p digits are its coefficients"""
    p, poly = GF_POLY[q] if q in GF_POLY else (q, [0, 1])
    k = len(poly) - 1
    dig = lambda x: [(x // p ** i) % p for i in range(k)]
    num = lambda d: sum(c * p ** i for i, c in enumerate(d))
    add = [[num([(a + b) % p for a, b in zip(dig(x), dig(y))]) for y in range(q)] for x in range(q)]

    def mulx(x, y):
        a = dig(x); b = dig(y); c = [0] * (2 * k - 1)
        for i in range(k):
            for j in range(k):
                c[i + j] = (c[i + j] + a[i] * b[j]) % p
        for d in range(2 * k - 2, k - 1, -1):
            t = c[d]; c[d] = 0
            for i in range(k):
                c[d - k + i] = (c[d - k + i] - t * poly[i]) % p
        return num(c[:k])
    return p, k, add, [[mulx(x, y) for y in range(q)] for x in range(q)]


def struct(name):
    if name == "k33ce":
        # k33c under the third index-2 subgroup of its group of order 72: the vertex permutations whose two sides
        # carry the same sign, with or without the swap of the sides (order 36).  The other two are k33cs and ap_9ck.
        edges = [(i, 3 + j) for i in range(3) for j in range(3)]
        vps = [[1, 2, 0, 3, 4, 5], [0, 1, 2, 4, 5, 3], [1, 0, 2, 4, 3, 5], [3, 4, 5, 0, 1, 2]]
        return 18, with_coins([edge_perm(edges, vp) for vp in vps], 9), edges
    if name == "ap_9ck":
        # ap_9c with the edge list of K_{3,3} attached, so that the k33c seeds (the record among them) start the search.
        # In the script's own labelling of GF(9) the ap_9c group is an index-2 subgroup of the k33c group
        # (ap9_in_k33.py), different from the k33cs one; edge 3i+j is point 3i+j.
        m, gens, _ = struct("ap_9c")
        return m, gens, [(i, 3 + j) for i in range(3) for j in range(3)]
    if name.startswith(("psl_", "ap_")):
        # psl_q: the q + 1 points of the projective line over GF(q) under PSL(2,q); ap_q: the q points of GF(q) under
        # the maps x -> s x + b with s a nonzero square.  Meant for odd q.  A trailing c adds one coin per point.
        fam, tail = name.split("_")[:2]
        q = int(tail.rstrip("c"))
        p, k, add, mul = gf_tables(q)
        g = next(r for r in range(2, q)
                 if len(set(itertools.accumulate([r] * (q - 1), lambda a, b: mul[a][b]))) == q - 1)
        tr = [[add[x][p ** i] for x in range(q)] for i in range(k)]
        sq = [mul[mul[g][g]][x] for x in range(q)]
        if fam == "ap":
            n = q
            perms = tr + [sq]
        else:
            n = q + 1
            neg = [next(y for y in range(q) if add[x][y] == 0) for x in range(q)]
            inv = [0] + [next(y for y in range(q) if mul[x][y] == 1) for x in range(1, q)]
            perms = [t + [q] for t in tr] + [sq + [q]] + [[q] + [neg[inv[x]] for x in range(1, q)] + [0]]
        return (2 * n, with_coins(perms, n), None) if tail.endswith("c") else (n, perms, None)
    if name.startswith("gl_"):
        # gl_n: the 2^n - 1 nonzero vectors over GF(2) under GL(n,2); a trailing c adds one coin per point
        tail = name.split("_")[1]
        n = int(tail.rstrip("c")); N = (1 << n) - 1
        full = [[sum(((x >> i) & 1) << vp[i] for i in range(n)) for x in range(N + 1)] for vp in sym_gens(n)]
        full.append([x ^ ((x >> 1) & 1) for x in range(N + 1)])
        perms = [[f[x] - 1 for x in range(1, N + 1)] for f in full]
        return (2 * N, with_coins(perms, N), None) if tail.endswith("c") else (N, perms, None)
    if name.startswith(("ev_", "ec_", "eh_")):
        # ev_<g>: the edges of a graph and one further input per vertex; ec_<g>: the edges and one coin per edge;
        # eh_k<a>x<b>: the edges of K_{a,b} and one further input per vertex of the a side (the sides are not exchanged).
        # <g> is k<n> (complete graph), k<a>x<b> (complete bipartite graph) or octa.  ev_k3x3 is k33v, ec_k3x3 is k33c.
        fam, g = name.split("_")[:2]
        a = None
        if g == "octa":
            nv = 6
            edges = [(i, j) for i in range(6) for j in range(i + 1, 6) if j != i + 3]
            vps = [[3, 1, 2, 0, 4, 5], [1, 2, 0, 4, 5, 3], [1, 0, 2, 4, 3, 5]]
        elif "x" in g:
            a, b = (int(t) for t in g[1:].split("x"))
            nv = a + b
            edges = [(i, a + j) for i in range(a) for j in range(b)]
            vps = (sym_gens(a, 0, nv) if a >= 2 else []) + (sym_gens(b, a, nv) if b >= 2 else [])
            if a == b and fam != "eh":
                vps.append([a + i for i in range(a)] + [i for i in range(a)])
        else:
            nv = int(g[1:])
            edges = [(i, j) for i in range(nv) for j in range(i + 1, nv)]
            vps = sym_gens(nv)
        eps = [edge_perm(edges, vp) for vp in vps]
        E = len(edges)
        if fam == "ec":
            return 2 * E, with_coins(eps, E), edges
        if fam == "eh" and a is None:
            raise SystemExit("eh_ needs a complete bipartite graph: " + name)
        nx = nv if fam == "ev" else a
        return E + nx, [ep + [E + v for v in vp[:nx]] for ep, vp in zip(eps, vps)], edges
    if name == "m11t":
        # 12 points under the Mathieu group M11 in its 3-transitive action (order 7920), a subgroup of the m12 group
        return 12, [[9, 1, 0, 7, 2, 4, 5, 11, 10, 6, 8, 3], [2, 11, 4, 0, 6, 1, 10, 9, 8, 5, 7, 3]], None
    if name in ("m11", "m11c"):
        # 11 points under the Mathieu group M11 (order 7920), generated by an 11-cycle and (2 6 10 7)(3 9 4 5);
        # m11c adds one coin per point
        a = [(x + 1) % 11 for x in range(11)]
        b = list(range(11))
        for cyc in ((2, 6, 10, 7), (3, 9, 4, 5)):
            for i, x in enumerate(cyc):
                b[x] = cyc[(i + 1) % 4]
        return (22, with_coins([a, b], 11), None) if name == "m11c" else (11, [a, b], None)
    if name.startswith(("pl_", "plf_", "al_", "alf_")):
        # pl_q / plf_q: the q + 1 points of the projective line over GF(q) under PGL(2,q) / PGammaL(2,q);
        # al_q / alf_q: the q points of GF(q) under AGL(1,q) / AGammaL(1,q).  A trailing c adds one coin per point.
        fam, tail = name.split("_")[:2]
        q = int(tail.rstrip("c"))
        p, k, add, mul = gf_tables(q)
        g = next(r for r in range(2, q)
                 if len(set(itertools.accumulate([r] * (q - 1), lambda a, b: mul[a][b]))) == q - 1)
        tr = [[add[x][p ** i] for x in range(q)] for i in range(k)]
        ml = [mul[g][x] for x in range(q)]
        fr = list(range(q))
        for _ in range(p - 1):
            fr = [mul[fr[x]][x] for x in range(q)]                      # x -> x^p
        if fam in ("al", "alf"):
            n = q
            perms = tr + [ml] + ([fr] if fam == "alf" and k > 1 else [])
        else:
            n = q + 1
            neg = [next(y for y in range(q) if add[x][y] == 0) for x in range(q)]
            inv = [0] + [next(y for y in range(q) if mul[x][y] == 1) for x in range(1, q)]
            perms = [t + [q] for t in tr] + [ml + [q]] + [[q] + [neg[inv[x]] for x in range(1, q)] + [0]]
            if fam == "plf" and k > 1:
                perms.append(fr + [q])
        return (2 * n, with_coins(perms, n), None) if tail.endswith("c") else (n, perms, None)
    if name.startswith("af_"):
        # af_n: the 2^n points of the affine space over GF(2) under AGL(n,2); a trailing c adds one coin per point
        tail = name.split("_")[1]
        n = int(tail.rstrip("c")); N = 1 << n
        perms = [[sum(((x >> i) & 1) << vp[i] for i in range(n)) for x in range(N)] for vp in sym_gens(n)]
        perms += [[x ^ ((x >> 1) & 1) for x in range(N)], [x ^ 1 for x in range(N)]]
        return (2 * N, with_coins(perms, N), None) if tail.endswith("c") else (N, perms, None)
    if name == "m12":
        # the 12 points of the projective line over GF(11) under the Mathieu group M12 (order 95040)
        P = 11
        return 12, [[(x + 1) % P for x in range(P)] + [P], [(3 * x) % P for x in range(P)] + [P],
                    [P] + [(-pow(x, P - 2, P)) % P for x in range(1, P)] + [0],
                    [(4 * x * x - 3 * pow(x, 7, P)) % P for x in range(P)] + [P]], None
    if name.startswith("gv_"):
        # the vertices of a named graph as inputs, under its full automorphism group
        auts = graph_auts(named_graph(name[3:]))
        return len(auts[0]), few_gens(auts), None
    if name.startswith("wr_"):
        # wr_a_b: b blocks of a inputs under S_a wr S_b (any permutation inside a block, any permutation of the blocks)
        a, b = (int(t) for t in name.split("_")[1:3])
        m = a * b
        gens = sym_gens(a, 0, m) if a >= 2 else []
        if b >= 2:
            gens.append(list(range(a, 2 * a)) + list(range(a)) + list(range(2 * a, m)))
            gens.append([(x + a) % m for x in range(m)])
        return m, gens, None
    if name.startswith("pr_"):
        # pr_a_b_c: consecutive blocks of a, b, c, ... inputs, any permutation inside a block, none between blocks
        sizes = [int(t) for t in name.split("_")[1:]]
        m = sum(sizes)
        gens, off = [], 0
        for a in sizes:
            if a >= 2:
                gens += sym_gens(a, off, m)
            off += a
        return m, gens, None
    if name.startswith("wn_"):
        # wn_a_b_c: nested blocks, innermost first (blocks of a inputs, b of those form a larger block, c of those, ...),
        # every level under its full symmetric group; wn_a_b is wr_a_b
        sizes = [int(t) for t in name.split("_")[1:]]
        m = 1
        for a in sizes:
            m *= a
        gens, blk = [], 1
        for a in sizes:
            if a >= 2:
                g = list(range(m))
                for x in range(blk):
                    g[x], g[x + blk] = x + blk, x
                gens.append(g)
                g = list(range(m))
                for x in range(blk * a):
                    g[x] = (x + blk) % (blk * a)
                gens.append(g)
            blk *= a
        return m, gens, None
    if name.startswith("gr_"):
        # gr_a_b: the a*b cells of a grid (edges of K_{a,b}); any permutation of the rows and any of the columns,
        # and the transpose when a == b. No seeds: these anneal from random starts.
        a, b = [int(t) for t in name.split("_")[1:3]]
        edges = [(i, a + j) for i in range(a) for j in range(b)]
        vps = sym_gens(a, 0, a + b) + sym_gens(b, a, a + b)
        if a == b:
            vps.append([a + i for i in range(a)] + [i for i in range(a)])
        return a * b, [edge_perm(edges, vp) for vp in vps], None
    if name.startswith("sub_"):
        # sub_n_k: the k-subsets of an n-set as inputs, under S_n (sub_n_2 is the edge set of K_n). No seeds.
        n, k = [int(t) for t in name.split("_")[1:3]]
        pts = [frozenset(c) for c in itertools.combinations(range(n), k)]
        idx = {s: i for i, s in enumerate(pts)}
        return len(pts), [[idx[frozenset(vp[u] for u in s)] for s in pts] for vp in sym_gens(n)], None
    if name.startswith("dg_"):
        # dg_n: the ordered pairs (u, v), u != v, of an n-set as inputs (the arcs of the complete digraph), under S_n
        n = int(name.split("_")[1])
        pts = [(u, v) for u in range(n) for v in range(n) if u != v]
        idx = {s: i for i, s in enumerate(pts)}
        return len(pts), [[idx[(vp[u], vp[v])] for (u, v) in pts] for vp in sym_gens(n)], None
    if name.startswith("g3_"):
        # g3_a_b_c: the cells of an a x b x c box, any permutation of each of the three axes (no exchange of axes)
        dims = [int(t) for t in name.split("_")[1:4]]
        pts = list(itertools.product(*[range(d) for d in dims]))
        idx = {s: i for i, s in enumerate(pts)}
        gens = []
        for ax, n in enumerate(dims):
            for vp in (sym_gens(n) if n >= 2 else []):
                gens.append([idx[tuple(vp[t[d]] if d == ax else t[d] for d in range(3))] for t in pts])
        return len(pts), gens, None
    if name.startswith("bs_"):
        # bs_n: the 2^n subsets of an n-set as inputs (the points of the cube), under S_n permuting the coordinates
        n = int(name.split("_")[1])
        return 1 << n, [[sum(((x >> i) & 1) << vp[i] for i in range(n)) for x in range(1 << n)]
                        for vp in sym_gens(n)], None
    if name in ("fanoc", "fanoc2", "ag23c", "q3vc", "w33c", "pg23") or \
            (name[0] == "s" and name.endswith("c") and name[1:-1].isdigit()):
        return point_struct(name)
    if name in ("k33cx1", "k33cx2"):
        # k33c plus 1 or 2 further inputs fixed by the group of K33 (order 72); two further inputs may be swapped
        r = int(name[-1])
        edges = [(i, 3 + j) for i in range(3) for j in range(3)]
        vps = sym_gens(3, 0, 6) + sym_gens(3, 3, 6) + [[3, 4, 5, 0, 1, 2]]
        gens = [p + list(range(18, 18 + r)) for p in with_coins([edge_perm(edges, vp) for vp in vps], 9)]
        if r == 2:
            gens.append(list(range(18)) + [19, 18])
        EXTRA_INPUTS[0] = r
        return 18 + r, gens, edges
    if name == "k33k33":
        # two 3x3 grids, each under the group of K33, and the swap of the two grids: order 2 * 72^2
        edges = [(i, 3 + j) for i in range(3) for j in range(3)]
        vps = sym_gens(3, 0, 6) + sym_gens(3, 3, 6) + [[3, 4, 5, 0, 1, 2]]
        gens = [edge_perm(edges, vp) + list(range(9, 18)) for vp in vps]
        return 18, gens + [list(range(9, 18)) + list(range(9))], None
    if name == "q4v":
        # the 16 vertices of the 4-cube under its full group of order 384
        return 16, [[u ^ 1 for u in range(16)],
                    [(u & 12) | ((u & 1) << 1) | ((u >> 1) & 1) for u in range(16)],
                    [((u << 1) & 15) | (u >> 3) for u in range(16)]], None
    if name in ("ag24", "pg24"):
        mul = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]          # GF(4), addition is xor
        if name == "ag24":
            # the 16 points of the affine plane over GF(4) under AGL(2,4), order 2880
            maps = [lambda x, y: (x ^ 1, y), lambda x, y: (x ^ y, y), lambda x, y: (y, x), lambda x, y: (mul[2][x], y)]
            return 16, [[4 * f(x, y)[0] + f(x, y)[1] for x in range(4) for y in range(4)] for f in maps], None
        # the 21 points of the projective plane over GF(4) under PGL(3,4), order 60480
        vecs = [v for v in itertools.product(range(4), repeat=3) if any(v) and next(x for x in v if x) == 1]
        vid = {v: k for k, v in enumerate(vecs)}
        inv = [0, 1, 3, 2]
        mats = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    M = [[int(a == b) for b in range(3)] for a in range(3)]; M[i][j] = 1; mats.append(M)
        mats.append([[2, 0, 0], [0, 1, 0], [0, 0, 1]])
        gens = []
        for M in mats:
            g = []
            for v in vecs:
                w = [mul[M[i][0]][v[0]] ^ mul[M[i][1]][v[1]] ^ mul[M[i][2]][v[2]] for i in range(3)]
                s = inv[next(x for x in w if x)]
                g.append(vid[tuple(mul[s][x] for x in w)])
            gens.append(g)
        return 21, gens, None
    if name == "k33cs":
        # k33c without the swap of the two sides: group S3 x S3 of order 36, a larger space around the record
        edges = [(i, 3 + j) for i in range(3) for j in range(3)]
        vps = sym_gens(3, 0, 6) + sym_gens(3, 3, 6)
        return 18, with_coins([edge_perm(edges, vp) for vp in vps], 9), edges
    if name in ("k33", "k33c", "k33v", "k34", "k44"):
        a, b = {"k33": (3, 3), "k33c": (3, 3), "k33v": (3, 3), "k34": (3, 4), "k44": (4, 4)}[name]
        edges = [(i, a + j) for i in range(a) for j in range(b)]
        vps = sym_gens(a, 0, a + b) + sym_gens(b, a, a + b)
        if a == b:
            vps.append([a + i for i in range(a)] + [i for i in range(a)])
        eps = [edge_perm(edges, vp) for vp in vps]
        E = len(edges)
        if name == "k33c":
            return 2 * E, with_coins(eps, E), edges
        if name == "k33v":
            return E + a + b, [ep + [E + v for v in vp] for ep, vp in zip(eps, vps)], edges
        return E, eps, edges
    if len(name) >= 4 and name[0] == "k" and name[1] in "34" and name[2] == "c" and name[3:].isdigit():
        # K_n with r coins per edge; the r coins of an edge are interchangeable (k4c2: 18 inputs, k3c5: 18 inputs)
        n = int(name[1]); r = int(name[3:])
        edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        E = len(edges); m = E * (1 + r)
        gens = []
        for vp in sym_gens(n):
            ep = edge_perm(edges, vp)
            gens.append(ep + [E * (1 + l) + q for l in range(r) for q in ep])
        if r >= 2:
            t = list(range(m)); t[E], t[2 * E] = 2 * E, E
            gens.append(t)
            cyc = list(range(m))
            for l in range(r):
                cyc[E * (1 + l)] = E * (1 + (l + 1) % r)
            gens.append(cyc)
        return m, gens, edges
    if name in ("k4", "k4c", "k5", "k5c", "k6"):
        n = int(name[1])
        edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
        eps = [edge_perm(edges, vp) for vp in sym_gens(n)]
        E = len(edges)
        return (2 * E, with_coins(eps, E), edges) if name.endswith("c") else (E, eps, edges)
    small = {"c6c": (6, [(i, (i + 1) % 6) for i in range(6)]),
             "c7c": (7, [(i, (i + 1) % 7) for i in range(7)]),
             "c8c": (8, [(i, (i + 1) % 8) for i in range(8)]),
             "k23c": (5, [(i, 2 + j) for i in range(2) for j in range(3)]),
             "k24c": (6, [(i, 2 + j) for i in range(2) for j in range(4)]),
             "k33mc": (6, [(i, 3 + j) for i in range(3) for j in range(3) if (i, j) != (0, 0)]),
             "w4c": (5, [(0, i) for i in range(1, 5)] + [(i, 1 + i % 4) for i in range(1, 5)]),
             "diac": (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]),
             "k113c": (5, [(0, 1)] + [(i, j) for i in range(2) for j in range(2, 5)])}
    if name in small:
        # a small graph with one coin per edge; the group is the whole automorphism group, found by brute force
        nv, edges = small[name]
        es = {frozenset(e) for e in edges}
        idt = tuple(range(nv)); grp = {idt}; vgens = []
        for vp in itertools.permutations(range(nv)):
            if vp in grp or not all(frozenset((vp[u], vp[v])) in es for u, v in edges):
                continue
            vgens.append(list(vp)); stack = list(grp)
            while stack:
                a = stack.pop()
                for g in vgens:
                    b = tuple(g[a[i]] for i in range(nv))
                    if b not in grp:
                        grp.add(b); stack.append(b)
        E = len(edges)
        return 2 * E, with_coins([edge_perm(edges, vp) for vp in vgens], E), edges
    if name == "pet":
        verts = [(i, j) for i in range(5) for j in range(i + 1, 5)]
        vid = {v: k for k, v in enumerate(verts)}
        edges = [(vid[u], vid[v]) for u in verts for v in verts if u < v and not set(u) & set(v)]
        eps = []
        for sp in sym_gens(5):
            vp = [vid[tuple(sorted((sp[u[0]], sp[u[1]])))] for u in verts]
            eps.append(edge_perm(edges, vp))
        return len(edges), eps, edges
    if name == "q3e":
        edges = [(u, u ^ (1 << i)) for u in range(8) for i in range(3) if not u >> i & 1]
        vps = [[u ^ 1 for u in range(8)],
               [((u & 1) << 1) | ((u >> 1) & 1) | (u & 4) for u in range(8)],
               [((u & 1) << 1) | ((u & 2) << 1) | ((u >> 2) & 1) for u in range(8)]]
        return len(edges), [edge_perm(edges, vp) for vp in vps], edges
    if name == "octa":
        edges = [(i, j) for i in range(6) for j in range(i + 1, 6) if j != i + 3]
        vps = [[3, 1, 2, 0, 4, 5], [1, 2, 0, 4, 5, 3], [1, 0, 2, 4, 3, 5]]
        return len(edges), [edge_perm(edges, vp) for vp in vps], edges
    if name.startswith("agl") or name.startswith("pgl"):
        p = int(name[3:])
        g = next(r for r in range(2, p) if len({pow(r, k, p) for k in range(p - 1)}) == p - 1)
        if name.startswith("agl"):
            return p, [[(x + 1) % p for x in range(p)], [(g * x) % p for x in range(p)]], None
        inv = [p] + [(-pow(x, p - 2, p)) % p for x in range(1, p)] + [0]          # x -> -1/x, 0 <-> infinity (= p)
        return p + 1, [[(x + 1) % p for x in range(p)] + [p], [(g * x) % p for x in range(p)] + [p], inv], None
    if name.startswith("dih"):
        n = int(name[3:])
        return n, [[(x + 1) % n for x in range(n)], [(-x) % n for x in range(n)]], None
    raise SystemExit("unknown structure " + name)


# ---------- orbits of points and the class-level transform ----------
def orbits(m, gens):
    N = 1 << m
    x = np.arange(N, dtype=np.uint32)
    imgs = []
    for g in gens:
        assert sorted(g) == list(range(m)), "not a permutation"
        y = np.zeros(N, dtype=np.uint32)
        for i in range(m):
            y |= ((x >> np.uint32(i)) & np.uint32(1)) << np.uint32(g[i])
        imgs.append(y)
        inv = np.empty(N, dtype=np.uint32); inv[y] = x
        imgs.append(inv)
    lab = x.copy()
    while True:
        old = lab.copy()
        for y in imgs:
            np.minimum(lab, lab[y], out=lab)
        if np.array_equal(old, lab):
            break
    reps, cls, sizes = np.unique(lab, return_inverse=True, return_counts=True)
    return reps.astype(np.int64), cls.astype(np.int32), sizes.astype(np.float64)


def fwht_rows(a):
    B, N = a.shape
    h = 1
    while h < N:
        v = a.reshape(B, N // (2 * h), 2, h)
        t = v[:, :, 0, :].copy()
        v[:, :, 0, :] += v[:, :, 1, :]
        v[:, :, 1, :] = t - v[:, :, 1, :]
        h *= 2


def class_transform(m, reps, cls, batch):
    """A[d, c] = 2^-m sum_{x in class c} chi_{rep_d}(x)."""
    N = 1 << m; K = len(reps)
    A = np.empty((K, K))
    for c0 in range(0, K, batch):
        c1 = min(K, c0 + batch)
        ind = np.zeros((c1 - c0, N))
        sel = (cls >= c0) & (cls < c1)
        ind[cls[sel] - c0, np.nonzero(sel)[0]] = 1.0
        fwht_rows(ind)
        A[:, c0:c1] = ind[:, reps].T / N
    return A


def popcounts(N):
    x = np.arange(N, dtype=np.uint32); r = np.zeros(N, dtype=np.int64)
    while x.any():
        r += (x & 1); x >>= 1
    return r


def explicit(tt, wfun, c):
    """Second path: full transform of the +-1 truth table."""
    N = len(tt)
    a = tt.astype(np.float64).reshape(1, N).copy()
    fwht_rows(a)
    a = a[0] / N
    w = a * a; mean = a[0]; w[0] = 0.0
    V = w.sum()
    pi = w[w > 0] / V
    G = float(-(pi * np.log2(pi)).sum()); J = float((popcounts(N) * w).sum() / V); pp = 0.5 * (1 - mean)
    return G, J, pp, G - c * J + wfun(pp)


def graph_seeds(m, edges, N):
    out = []
    if edges is None:
        return out
    m -= EXTRA_INPUTS[0]                    # k33cx<r>: the r further inputs sit after the coins and the seeds ignore them
    E = len(edges); nv = 1 + max(max(e) for e in edges)
    eid = {frozenset(e): i for i, e in enumerate(edges)}
    fams = {}
    if nv % 2 == 0:
        pm = set()
        for perm in itertools.permutations(range(nv)):
            prs = [frozenset((perm[2 * i], perm[2 * i + 1])) for i in range(nv // 2)]
            if all(p in eid for p in prs):
                pm.add(sum(1 << eid[p] for p in prs))
        fams["pm"] = sorted(pm)
    hc = set()
    for perm in itertools.permutations(range(1, nv)):
        cyc = (0,) + perm
        prs = [frozenset((cyc[i], cyc[(i + 1) % nv])) for i in range(nv)]
        if all(p in eid for p in prs):
            hc.add(sum(1 << eid[p] for p in prs))
    if hc:
        fams["ham"] = sorted(hc)
    tri = []
    for a, b, cc in itertools.combinations(range(nv), 3):
        t = [frozenset((a, b)), frozenset((a, cc)), frozenset((b, cc))]
        if all(p in eid for p in t):
            tri.append(sum(1 << eid[p] for p in t))
    if tri:
        fams["tri"] = tri
    x = np.arange(N, dtype=np.int64); xe = x & ((1 << E) - 1)
    for nm, masks in fams.items():
        f = np.ones(N)
        for mk in masks:
            f[(xe & mk) == mk] = -1.0
        out.append((nm, f.copy()))
        if m == 2 * E:                                         # one coin per edge: the record's rule
            g = f.copy(); used = 0
            for e, (u, v) in enumerate(edges):
                nb = sum(1 << i for i, (a, b) in enumerate(edges) if i != e and {a, b} & {u, v})
                hit = ((xe & ~(1 << e)) == nb) & (f > 0)
                used += int(hit.sum())
                g[hit] = np.where((x[hit] >> (E + e)) & 1, -1.0, 1.0)
            if used:
                out.append((nm + "+coins", g))
    if E == 9 and edges == [(i, 3 + j) for i in range(3) for j in range(3)]:
        # K33 only: the edge bits as a 3x3 matrix; determinant mod 2 and over the reals, bare and with the record's coin rule
        b = [(xe >> i) & 1 for i in range(9)]
        det = b[0] * (b[4] * b[8] - b[5] * b[7]) - b[1] * (b[3] * b[8] - b[5] * b[6]) + b[2] * (b[3] * b[7] - b[4] * b[6])
        for nm, hit0 in (("det2", (det & 1) == 1), ("detR", det != 0)):
            f = np.where(hit0, -1.0, 1.0)
            out.append((nm, f.copy()))
            if m == 2 * E:
                g = f.copy(); used = 0
                for e, (u, v) in enumerate(edges):
                    nb = sum(1 << i for i, (a, b2) in enumerate(edges) if i != e and {a, b2} & {u, v})
                    hit = ((xe & ~(1 << e)) == nb) & (f > 0)
                    used += int(hit.sum())
                    g[hit] = np.where((x[hit] >> (E + e)) & 1, -1.0, 1.0)
                if used:
                    out.append((nm + "+coin", g))      # not "+coins": the full pair scan stays on the record seeds
    return out


def main():
    name, wfile, out = sys.argv[1], sys.argv[2], sys.argv[3]
    secs = opt("--secs", 3000.0); seed = opt("--seed", 1, int); T0 = opt("--T0", 0.3); T1 = opt("--T1", 0.002)
    batch = opt("--batch", 64, int)
    jmin = opt("--jmin", 0.0)                    # anneal and flip scans refuse a gate with J below this (0 = no floor)
    rng = np.random.default_rng(seed)
    tab = np.loadtxt(wfile); wt, ww = tab[:, 0], tab[:, -1]

    def wfun(p):
        p = min(max(p, 1e-15), 1 - 1e-15)
        return float(np.interp(np.log2(p / (1 - p)), wt, ww))
    c = wfun(0.5)
    t0 = time.time()
    m, gens, edges = struct(name)
    reps, cls, sizes = orbits(m, gens)
    K = len(reps); N = 1 << m
    A = class_transform(m, reps, cls, batch)
    At = np.ascontiguousarray(A.T)
    lvl = np.array([bin(int(r)).count("1") for r in reps], dtype=np.float64)
    d0 = int(np.nonzero(reps == 0)[0][0])
    assert d0 == 0
    nl = sizes * lvl
    fo = open(out, "a")

    def say(s):
        print(s, flush=True); fo.write(s + "\n"); fo.flush()
    say("# %s m=%d classes=%d c=%.12f table=%s seed=%d setup %.0f s" % (name, m, K, c, wfile, seed, time.time() - t0))

    def score(fh):
        mean = fh[d0]
        w = fh * fh; w[d0] = 0.0
        V = float(sizes @ w)
        if V < 1e-12:
            return -1e9, 0.0, 0.0, 0.5
        pi = w / V
        lg = np.zeros(K); nz = pi > 0
        lg[nz] = np.log2(pi[nz])
        G = float(-(sizes * pi) @ lg); J = float(nl @ pi); pp = 0.5 * (1 - mean)
        if J < jmin:
            return -1e9, G, J, pp
        return G - c * J + wfun(pp), G, J, pp

    def report(tag, s):
        sl, G, J, pp = score(A @ s)
        G2, J2, pp2, sl2 = explicit(s[cls], wfun, c)
        say("%s slack %+.9f G %.9f J %.9f p' %.9f | explicit: slack %+.9f G %.9f J %.9f | signs %s" %
            (tag, sl, G, J, pp, sl2, G2, J2, "".join("1" if v < 0 else "0" for v in s) if K <= 400 else "(%d classes)" % K))
        if (sl > 1e-7 or sl2 > 1e-7) and J > 1 + 1e-9:
            say("!!! POSITIVE SLACK %s: check before a word is said" % tag)
            np.save(out + "." + tag.replace(" ", "_") + ".npy", s.astype(np.int8))
        return sl

    def decode(r):
        r = int(r)
        if edges is None:
            return "{%s}" % ",".join(str(i) for i in range(m) if r >> i & 1)
        E = len(edges)
        return "e%s c%s" % ([i for i in range(E) if r >> i & 1], [i - E for i in range(E, m) if r >> i & 1])

    def flips(tag, s, top=8, allpairs=False):
        fh = A @ s
        v = np.array([score(fh - (2.0 * s[k]) * At[k])[0] for k in range(K)])
        order = np.argsort(-v)
        for k in order[:top]:
            say("  flip1 %s class %d size %d rep %s -> slack %+.9f" % (tag, k, int(sizes[k]), decode(reps[k]), v[k]))
        cand = order if allpairs else order[:min(K, 150)]
        bp = (-1e9, 0, 0)
        for i, k in enumerate(cand):
            f1 = fh - (2.0 * s[k]) * At[k]
            for l in cand[i + 1:]:
                u = score(f1 - (2.0 * s[l]) * At[l])[0]
                if u > bp[0]:
                    bp = (u, int(k), int(l))
            if allpairs and i % 500 == 0:
                say("  flip2 %s progress %d/%d best so far %+.9f (%d,%d)" % (tag, i, len(cand), bp[0], bp[1], bp[2]))
        say("  flip2 %s best pair among %d: classes %d %d (reps %s | %s) -> slack %+.9f" %
            (tag, len(cand), bp[1], bp[2], decode(reps[bp[1]]), decode(reps[bp[2]]), bp[0]))

    def exhaustive():
        L = min(K - 1, 14); Hn = K - 1 - L
        low = np.arange(1 << L)
        S = np.where((low[None, :] >> np.arange(L)[:, None]) & 1, -1.0, 1.0)
        P = A[:, 1:1 + L] @ S
        szc = sizes[:, None]; nlc = nl[:, None]
        tops = []
        for hi in range(1 << Hn):
            sh = np.where((hi >> np.arange(Hn)) & 1, -1.0, 1.0)
            base = A[:, 0] + (A[:, 1 + L:] @ sh if Hn else 0.0)
            F = P + base[:, None]
            mean = F[0].copy()
            w = F * F; w[0] = 0.0
            V = (szc * w).sum(axis=0)
            ok = V > 1e-12
            pi = w / np.where(ok, V, 1.0)
            G = -(szc * pi * np.log2(np.where(pi > 0, pi, 1.0))).sum(axis=0)
            J = (nlc * pi).sum(axis=0)
            pp = np.clip(0.5 * (1 - mean), 1e-15, 1 - 1e-15)
            sl = np.where(ok & (J > 1 + 1e-9), G - c * J + np.interp(np.log2(pp / (1 - pp)), wt, ww), -1e9)
            for j in np.argpartition(-sl, 4)[:4]:
                tops.append((float(sl[j]), hi, int(j)))
            if len(tops) > 4000:
                tops.sort(reverse=True); del tops[40:]
            if hi and hi % 20000 == 0:
                say("# exhaustive %d/%d best so far %+.9f, %.0f s" % (hi, 1 << Hn, max(tops)[0], time.time() - t0))
        tops.sort(reverse=True)
        say("# exhaustive over 2^%d functions done, %.0f s" % (K - 1, time.time() - t0))
        for i, (sl, hi, j) in enumerate(tops[:12]):
            s = np.ones(K)
            s[1:1 + L] = S[:, j]
            if Hn:
                s[1 + L:] = np.where((hi >> np.arange(Hn)) & 1, -1.0, 1.0)
            report("exh%d" % i, s)

    seeds = []
    for nm, f in graph_seeds(m, edges, N):
        s = f[reps]
        if not np.array_equal(s[cls], f):
            say("seed %s is not invariant, skipped" % nm); continue
        report("seed " + nm, s)
        seeds.append((nm, s))
    if K <= 34 and "--anneal" not in sys.argv:
        exhaustive(); fo.close(); return
    for nm, s in seeds:
        flips(nm, s, allpairs=("--pairs" in sys.argv and nm.endswith("+coins")))

    def climb(s, fh, cur):
        improved = True
        while improved:
            improved = False
            for k in rng.permutation(K):
                nf = fh - (2.0 * s[k]) * At[k]
                v = score(nf)[0]
                if v > cur + 1e-12:
                    fh = nf; s[k] = -s[k]; cur = v; improved = True
        return s, cur

    best = (-1e9, None)
    run = 0
    rt = min(300.0, max(5.0, 0.02 * K))
    while time.time() - t0 < secs:
        if run < len(seeds):
            tag, s, temp0 = seeds[run][0], seeds[run][1].copy(), 0.02
        elif seeds and run % 3 == 0:
            j = int(rng.integers(0, len(seeds)))
            tag, s, temp0 = "pert-" + seeds[j][0], seeds[j][1].copy(), 0.05
            for k in rng.integers(0, K, size=max(2, K // 100)):
                s[k] = -s[k]
        else:
            tag, s, temp0 = "rand", rng.choice([-1.0, 1.0], size=K), T0
        fh = A @ s
        cur = score(fh)[0]
        tstart = time.time(); tend = min(t0 + secs, tstart + rt)
        rb, rs = cur, s.copy(); it = 0
        while time.time() < tend:
            T = temp0 * (T1 / temp0) ** ((time.time() - tstart) / max(1e-9, tend - tstart))
            for k, u in zip(rng.integers(0, K, size=1000), rng.random(1000)):
                nf = fh - (2.0 * s[k]) * At[k]
                v = score(nf)[0]
                if v >= cur or u < np.exp((v - cur) / T):
                    fh = nf; s[k] = -s[k]; cur = v
                    if cur > rb:
                        rb, rs = cur, s.copy()
            it += 1000
        s, cur = climb(rs.copy(), A @ rs, rb)
        if cur > best[0] + 1e-9 or run < len(seeds) or run % 20 == 0:
            report("run%d %s moves %d" % (run, tag, it), s)
        if cur > best[0]:
            best = (cur, s.copy())
        run += 1
    if best[1] is not None:
        report("BEST of %d runs" % run, best[1])
        np.save(out + ".best.npy", best[1].astype(np.int8))
    fo.close()


if __name__ == "__main__":
    main()
