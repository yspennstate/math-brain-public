"""The linear-algebra proof of the cycle double cover theorem (as written out in arXiv 2607.15399, Geelen), tested.

For a cubic graph G and a nowhere-zero flow f : E -> F_2^3, the proof claims that the linear system over F_2

    p_u + p_v + z_e f_e = alpha_{u,e} + alpha_{v,e}          for every edge e = uv              (2)

in the unknowns p : V -> F_2^3 and z : E -> F_2 always has a solution, where at a vertex v with edges a, b, c
alpha_{v,a} = f_b, alpha_{v,b} = f_c, alpha_{v,c} = f_a.  A solution gives every edge e = uv the pair of colours
{p_v + alpha_{v,e}, p_v + alpha_{v,e} + f_e}, the same from either end, and the colour classes are a cycle
double cover.

This script does not use the proof.  For each graph and each flow it solves (2) by elimination, asserts that a
solution exists, builds the colour classes and asserts directly that every class is 2-regular or empty at
every vertex and every edge lies in exactly two classes.
Flows: all nowhere-zero F_2^3-flows for the small graphs (the Petersen graph has 28560, the value at 8 of its
flow polynomial (k-1)(k-2)(k-3)(k-4)(k^2-5k+10)); random ones for the larger graphs.
Control: the same system with f replaced by random nonzero labels that are not a flow.
"""
import random
import sys

import networkx as nx


def prepare(G):
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    edges = [tuple(sorted(e)) for e in G.edges()]
    assert all(d == 3 for _, d in G.degree()), "not cubic"
    assert not nx.has_bridges(G), "has a bridge"
    inc = [[] for _ in range(n)]
    for k, (u, v) in enumerate(edges):
        inc[u].append(k)
        inc[v].append(k)
    # fundamental cycles of a BFS tree, as edge bitmasks
    T = nx.bfs_tree(G, 0)
    parent = {v: u for u, v in T.edges()}
    eidx = {e: k for k, e in enumerate(edges)}
    tree_edges = {tuple(sorted(e)) for e in T.edges()}

    def path_to_root(v):
        m = 0
        while v in parent:
            m ^= 1 << eidx[tuple(sorted((v, parent[v])))]
            v = parent[v]
        return m

    basis = []
    for e in edges:
        if e not in tree_edges:
            basis.append(path_to_root(e[0]) ^ path_to_root(e[1]) ^ (1 << eidx[e]))
    assert len(basis) == len(edges) - n + 1
    return n, edges, inc, basis


def span(basis):
    out = [0]
    for b in basis:
        out += [x ^ b for x in out]
    return out


def flow_values(c1, c2, c3, m):
    return [(c1 >> k & 1) | (c2 >> k & 1) << 1 | (c3 >> k & 1) << 2 for k in range(m)]


def solve(n, edges, inc, f):
    """Solve (2).  Returns (p, z) or None."""
    m = len(edges)
    nv = 3 * n + m
    alpha = {}
    for v in range(n):
        a, b, c = inc[v]
        alpha[(v, a)], alpha[(v, b)], alpha[(v, c)] = f[b], f[c], f[a]
    rows = []
    for k, (u, v) in enumerate(edges):
        rhs = alpha[(u, k)] ^ alpha[(v, k)]
        for i in range(3):
            r = (1 << (3 * u + i)) ^ (1 << (3 * v + i))
            if f[k] >> i & 1:
                r |= 1 << (3 * n + k)
            if rhs >> i & 1:
                r |= 1 << nv
            rows.append(r)
    piv = {}
    for r in rows:
        while r & ((1 << nv) - 1):
            low = (r & -r).bit_length() - 1
            if low >= nv:
                break
            if low in piv:
                r ^= piv[low]
            else:
                piv[low] = r
                break
        else:
            if r:            # only the right-hand bit is left: 0 = 1
                return None
    # back substitution, free variables = 0
    x = 0
    for col in sorted(piv, reverse=True):
        r = piv[col]
        val = r >> nv & 1
        rest = (r & ((1 << nv) - 1)) ^ (1 << col)
        val ^= bin(rest & x).count("1") & 1
        if val:
            x |= 1 << col
    p = [(x >> (3 * v)) & 7 for v in range(n)]
    z = [(x >> (3 * n + k)) & 1 for k in range(m)]
    return p, z, alpha


def check_cover(n, edges, inc, f, sol):
    p, z, alpha = sol
    classes = [[] for _ in range(8)]
    for k, (u, v) in enumerate(edges):
        pu = {p[u] ^ alpha[(u, k)], p[u] ^ alpha[(u, k)] ^ f[k]}
        pv = {p[v] ^ alpha[(v, k)], p[v] ^ alpha[(v, k)] ^ f[k]}
        if pu != pv or len(pu) != 2:
            return None
        for col in pu:
            classes[col].append(k)
    cover = [0] * len(edges)
    ncyc = 0
    for col in range(8):
        deg = [0] * n
        for k in classes[col]:
            deg[edges[k][0]] += 1
            deg[edges[k][1]] += 1
            cover[k] += 1
        if any(d not in (0, 2) for d in deg):
            return None
        if classes[col]:
            H = nx.Graph([edges[k] for k in classes[col]])
            ncyc += nx.number_connected_components(H)
    if any(c != 2 for c in cover):
        return None
    return sum(1 for c in classes if c), ncyc


def flower_snark(n):
    G = nx.Graph()
    for i in range(n):
        for x in "bcd":
            G.add_edge(("a", i), (x, i))
        G.add_edge(("b", i), ("b", (i + 1) % n))
        if i < n - 1:
            G.add_edge(("c", i), ("c", i + 1))
            G.add_edge(("d", i), ("d", i + 1))
    G.add_edge(("c", n - 1), ("d", 0))
    G.add_edge(("d", n - 1), ("c", 0))
    return G


def run(name, G, rng, limit_all=7, nrandom=300):
    n, edges, inc, basis = prepare(G)
    m = len(edges)
    full = (1 << m) - 1
    tested = 0
    colours = {}
    cyc = {}
    if len(basis) <= limit_all:
        S = span(basis)
        mode = "all"
        for c1 in S:
            for c2 in S:
                u12 = c1 | c2
                for c3 in S:
                    if u12 | c3 == full:
                        f = flow_values(c1, c2, c3, m)
                        sol = solve(n, edges, inc, f)
                        assert sol is not None, ("system (2) has no solution", name, f)
                        res = check_cover(n, edges, inc, f, sol)
                        assert res is not None, ("solution is not a cycle double cover", name, f)
                        tested += 1
                        colours[res[0]] = colours.get(res[0], 0) + 1
                        cyc[res[1]] = cyc.get(res[1], 0) + 1
    else:
        mode = "random"
        tries = 0
        while tested < nrandom:
            tries += 1
            cs = []
            for _ in range(3):
                c = 0
                for b in basis:
                    if rng.random() < 0.5:
                        c ^= b
                cs.append(c)
            if cs[0] | cs[1] | cs[2] != full:
                continue
            f = flow_values(cs[0], cs[1], cs[2], m)
            sol = solve(n, edges, inc, f)
            assert sol is not None, ("system (2) has no solution", name, f)
            res = check_cover(n, edges, inc, f, sol)
            assert res is not None, ("solution is not a cycle double cover", name, f)
            tested += 1
            colours[res[0]] = colours.get(res[0], 0) + 1
            cyc[res[1]] = cyc.get(res[1], 0) + 1
    print("%-22s %2d vertices %2d edges, cycle space dim %2d: %6d nowhere-zero flows (%s), system solvable and cover valid for every one; colours used %s" % (name, n, m, len(basis), tested, mode, dict(sorted(colours.items()))), flush=True)
    return n, edges, inc


def control(name, G, rng, trials=2000):
    n, edges, inc, basis = prepare(G)
    m = len(edges)
    unsolvable = invalid = valid = 0
    for _ in range(trials):
        f = [rng.randint(1, 7) for _ in range(m)]
        if all(f[inc[v][0]] ^ f[inc[v][1]] ^ f[inc[v][2]] == 0 for v in range(n)):
            continue
        sol = solve(n, edges, inc, f)
        if sol is None:
            unsolvable += 1
        elif check_cover(n, edges, inc, f, sol) is None:
            invalid += 1
        else:
            valid += 1
    print("control %-14s random nonzero labels that are not flows: system unsolvable %d, solvable but not a cover %d, a cover %d (of %d)" % (name, unsolvable, invalid, valid, unsolvable + invalid + valid), flush=True)


def main():
    rng = random.Random(8)
    run("K4", nx.complete_graph(4), rng)
    run("K33", nx.complete_bipartite_graph(3, 3), rng)
    run("prism", nx.circular_ladder_graph(3), rng)
    run("cube", nx.cubical_graph(), rng)
    run("Petersen", nx.petersen_graph(), rng)
    run("Heawood", nx.heawood_graph(), rng, nrandom=400)
    run("flower snark J3", flower_snark(3), rng, limit_all=0, nrandom=400)
    run("flower snark J5", flower_snark(5), rng, nrandom=400)
    run("flower snark J7", flower_snark(7), rng, nrandom=200)
    run("dodecahedron", nx.dodecahedral_graph(), rng, nrandom=300)
    run("Desargues", nx.desargues_graph(), rng, nrandom=300)
    run("Moebius-Kantor", nx.moebius_kantor_graph(), rng, nrandom=300)
    done = 0
    seed = 0
    while done < 40:
        seed += 1
        nn = rng.choice((8, 10, 12, 14, 16, 18, 20, 22, 24))
        G = nx.random_regular_graph(3, nn, seed=seed)
        if not nx.is_connected(G) or nx.has_bridges(G):
            continue
        run("random cubic #%d" % seed, G, rng, limit_all=5, nrandom=60)
        done += 1
    control("Petersen", nx.petersen_graph(), rng)
    control("cube", nx.cubical_graph(), rng)
    print("all assertions passed")


if __name__ == "__main__":
    main()
