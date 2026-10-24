"""Graph-property test bed: exact spectral quantities of natural graph properties on K_m (m = 4..7),
evaluated through isomorphism classes (orbits of S_m on edge sets).

For each property: mean, H, I, H/I, orbit entropy H(O)/I, E log2|O| / I, H(|S|)/I,
E_sb log2(n/|S|) (size-biased), E[|S| log2(e n/|S|)]/I, and the vertex term E[v(S) log2(e m/v(S))]/I
where v(S) = number of non-isolated vertices of the spectral graph S.
"""
import sys, os, json, math, itertools, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tlib
import networkx as nx

tlib.setup_process()


def graph_of(mask, m, edges):
    G = nx.Graph()
    G.add_nodes_from(range(m))
    for e, (a, b) in enumerate(edges):
        if (mask >> e) & 1:
            G.add_edge(a, b)
    return G


def hamiltonian(G, m):
    if m < 3:
        return False
    for perm in itertools.permutations(range(1, m)):
        if perm[0] > perm[-1]:
            continue
        cyc = (0,) + perm
        if all(G.has_edge(cyc[i], cyc[(i + 1) % m]) for i in range(m)):
            return True
    return False


def properties(m):
    P = {}
    P['connected'] = lambda G: nx.is_connected(G)
    P['triangle'] = lambda G: any(nx.triangles(G).values())
    P['matching_max'] = lambda G: len(nx.max_weight_matching(G, maxcardinality=True)) >= m // 2
    P['bipartite'] = lambda G: nx.is_bipartite(G)
    P['forest'] = lambda G: nx.is_forest(G)
    P['no_isolated'] = lambda G: min(dict(G.degree()).values()) > 0
    P['hamiltonian'] = lambda G: hamiltonian(G, m)
    if m >= 5:
        P['planar'] = lambda G: nx.check_planarity(G)[0]
    if m >= 4:
        P['K4'] = lambda G: any(len(c) >= 4 for c in nx.find_cliques(G))
    return P


def run(m):
    gens, n, idx = tlib.graph_gens(m)
    edges = sorted(idx, key=lambda e: idx[e])
    t0 = time.time()
    V = tlib.InvariantSpace(gens, n, 'K%d' % m)
    reps = V.reps
    # per-orbit vertex counts of spectral graphs
    vcount = np.zeros(V.k)
    for o, r in enumerate(reps):
        verts = set()
        for e, (a, b) in enumerate(edges):
            if (r >> e) & 1:
                verts.add(a); verts.add(b)
        vcount[o] = len(verts)
    out = []
    Gs = [graph_of(int(r), m, edges) for r in reps]
    props = properties(m)
    # majority-type and degree / triangle-count thresholds chosen near balance
    ecount = np.array([G.number_of_edges() for G in Gs])
    tri = np.array([sum(nx.triangles(G).values()) // 3 for G in Gs])
    maxdeg = np.array([max(dict(G.degree()).values()) for G in Gs])
    w = V.osize.astype(float) / (1 << n)
    def near_median(vals):
        best = None
        for t in sorted(set(vals.tolist())):
            pr = w[vals >= t].sum()
            if best is None or abs(pr - 0.5) < abs(best[1] - 0.5):
                best = (t, pr)
        return best[0]
    t_tri = near_median(tri); t_deg = near_median(maxdeg)
    table = {}
    for name, fn in props.items():
        table[name] = np.array([-1.0 if fn(G) else 1.0 for G in Gs])
    table['edges>=n/2'] = np.where(ecount >= n / 2, -1.0, 1.0)
    table['triangles>=%d' % t_tri] = np.where(tri >= t_tri, -1.0, 1.0)
    table['maxdeg>=%d' % t_deg] = np.where(maxdeg >= t_deg, -1.0, 1.0)
    for name, F in table.items():
        st = V.orbit_stats(F)
        c = V.coeffs(F); p = c * c; wt = V.osize * p
        I = st['I']
        if I < 1e-12:
            continue
        lev = V.level.astype(float)
        with np.errstate(divide='ignore', invalid='ignore'):
            sb = np.where(lev > 0, lev * wt * np.log2(n / np.maximum(lev, 1)), 0).sum() / I
            vt = np.where(vcount > 0, wt * vcount * np.log2(np.e * m / np.maximum(vcount, 1)), 0).sum() / I
        row = dict(m=m, prop=name, mean=st['mean'], H=st['H'], I=I, HI=st['H'] / I, HorbI=st['Horb'] / I,
                   ElogI=st['Elog'] / I, HlevI=st['Hlev'] / I, sb_log=sb, naiveI=st['naive'] / I, vertI=vt)
        out.append(row)
        print("K%d %-16s mean=%+.4f H=%.4f I=%.4f H/I=%.3f Horb/I=%.3f Elog/I=%.3f Hlev/I=%.3f Esb log(n/|S|)=%.3f naive/I=%.3f vert/I=%.3f" % (
            m, name, st['mean'], st['H'], I, st['H'] / I, st['Horb'] / I, st['Elog'] / I, st['Hlev'] / I, sb, st['naive'] / I, vt), flush=True)
    print("K%d done in %.1fs, %d classes" % (m, time.time() - t0, V.k), flush=True)
    return out


if __name__ == '__main__':
    allrows = []
    for m in [int(a) for a in sys.argv[1:]]:
        allrows += run(m)
    with open(os.path.join(HERE, '..', 'logs', 'graph_testbed_%s.json' % '_'.join(sys.argv[1:])), 'w') as fh:
        json.dump(allrows, fh, indent=1)
