# Exact spectral entropy, total influence and restriction-step constant for monotone graph properties on n <= 7
# vertices (N = n(n-1)/2 edge variables, uniform measure p = 1/2).  All edges are equivalent under S_n, so the
# restriction-step constant rho_0 = Delta_e / Inf_e is the same for every edge.  Properties are evaluated on all 2^N
# graphs at once: a graph is an integer whose bit e says whether edge e is present.
import sys, itertools, time, numpy as np
from mono_enum import phi

def edges(n):
    return list(itertools.combinations(range(n), 2))

def masks_of(n, subgraphs):
    idx = {e: k for k, e in enumerate(edges(n))}
    out = []
    for sg in subgraphs:
        m = 0
        for (a, b) in sg:
            m |= 1 << idx[(min(a, b), max(a, b))]
        out.append(m)
    return sorted(set(out))

def contains_any(G, ms):
    res = np.zeros(G.shape, dtype=bool)
    for m in ms:
        res |= (G & m) == m
    return res

def cycles(n, L):
    out = []
    for vs in itertools.combinations(range(n), L):
        first = vs[0]
        for perm in itertools.permutations(vs[1:]):
            if perm[0] > perm[-1]:
                continue                                  # each cycle once (fix start, fix direction)
            seq = (first,) + perm
            out.append([(seq[t], seq[(t + 1) % L]) for t in range(L)])
    return out

def matchings(n, size):
    out = []
    E = edges(n)
    for es in itertools.combinations(E, size):
        vs = [v for e in es for v in e]
        if len(set(vs)) == 2 * size:
            out.append(list(es))
    return out

def adjacency(G, n):
    idx = {e: k for k, e in enumerate(edges(n))}
    adj = []
    for v in range(n):
        a = np.zeros(G.shape, dtype=np.uint16)
        for u in range(n):
            if u != v:
                k = idx[(min(u, v), max(u, v))]
                a |= (((G >> k) & 1).astype(np.uint16) << u)
        adj.append(a)
    return adj

def connected(G, n):
    adj = adjacency(G, n)
    reach = np.ones(G.shape, dtype=np.uint16)            # vertex 0
    for _ in range(n):
        new = reach.copy()
        for v in range(n):
            new |= np.where((reach >> v) & 1, adj[v], 0).astype(np.uint16)
        reach = new
    return reach == (1 << n) - 1

def degrees(G, n):
    adj = adjacency(G, n)
    return [np.bitwise_count(a) for a in adj]

def wht(vec):
    G = vec.astype(np.float64).copy()
    N = len(G); h = 1
    while h < N:
        G = G.reshape(N // (2 * h), 2, h)
        a = G[:, 0, :].copy(); b = G[:, 1, :]
        G[:, 0, :] = a + b; G[:, 1, :] = a - b
        G = G.reshape(N); h *= 2
    return G / N

def analyse(f, N):
    g = 1.0 - 2.0 * f
    c = wht(g); P = c * c
    sizes = np.bitwise_count(np.arange(1 << N, dtype=np.uint32)).astype(np.float64)
    H = float(phi(P).sum()); I = float((P * sizes).sum())
    e = 0                                                 # every edge is equivalent
    idx0 = np.arange(1 << N, dtype=np.uint32)
    idx0 = idx0[(idx0 & 1) == 0]
    a = c[idx0]; b = c[idx0 | 1]
    inf = float((b * b).sum())
    delta = H - 0.5 * float((phi((a + b) ** 2) + phi((a - b) ** 2)).sum())
    mean = float(f.mean())
    return dict(mean=mean, var=4 * mean * (1 - mean), H=H, I=I, ratio=H / I if I > 0 else float('nan'),
                inf=inf, rho0=delta / inf if inf > 0 else float('nan'), EI=float(I / max(1e-300, 4 * mean * (1 - mean))))

if __name__ == '__main__':
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    for n in [int(v) for v in sys.argv[1].split(',')]:
        N = n * (n - 1) // 2
        t0 = time.time()
        G = np.arange(1 << N, dtype=np.uint32)
        deg = degrees(G, n)
        props = {}
        props['connected'] = connected(G, n)
        props['triangle'] = contains_any(G, masks_of(n, cycles(n, 3)))
        props['cycle (not a forest)'] = contains_any(G, masks_of(n, [c for L in range(3, n + 1) for c in cycles(n, L)]))
        props['odd cycle (not bipartite)'] = contains_any(G, masks_of(n, [c for L in range(3, n + 1, 2) for c in cycles(n, L)]))
        props['Hamiltonian cycle'] = contains_any(G, masks_of(n, cycles(n, n)))
        props['matching of size floor(n/2)'] = contains_any(G, masks_of(n, matchings(n, n // 2)))
        if n >= 4:
            props['K4'] = contains_any(G, masks_of(n, [list(itertools.combinations(q, 2)) for q in itertools.combinations(range(n), 4)]))
        props['no isolated vertex'] = np.logical_and.reduce([d >= 1 for d in deg])
        props['max degree >= 3'] = np.logical_or.reduce([d >= 3 for d in deg])
        props['min degree >= 2'] = np.logical_and.reduce([d >= 2 for d in deg])
        props['at least N/2 edges (symmetric control)'] = np.bitwise_count(G) >= (N + 1) // 2
        print('n = %d vertices, N = %d edges, 2^N = %d graphs (%.1f s to evaluate)' % (n, N, 1 << N, time.time() - t0), flush=True)
        for name, f in props.items():
            r = analyse(f.astype(np.float64), N)
            print('  %-40s mean %.4f  Var %.4f  H %8.4f  I %7.4f  H/I %.4f  rho_0 %.4f' % (name, r['mean'], r['var'], r['H'], r['I'], r['ratio'], r['rho0']), flush=True)
