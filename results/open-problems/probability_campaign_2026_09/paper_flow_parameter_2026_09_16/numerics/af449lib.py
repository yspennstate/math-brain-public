"""
Aldous-Fill flow parameter  F(G) = inf_f psi(f)  for simple random walk on a finite
connected simple graph, computed exactly-in-principle by LP (HiGHS via scipy) plus
exact rational dual certificates.

Book definitions (Aldous-Fill, Ch. 3 (3.98) and Ch. 4 Lemma 4.21):
  a unit flow from a to pi:   f antisymmetric on arcs, f_(i) = sum_j f_ij = 1_(i=a) - pi_i
  psi(f) = max_{arcs (i,j)} sum_a pi_a |f^(a)_ij| / (pi_i p_ij)
For SRW on a graph, pi_i p_ij = 1/(2m) for every arc, so
  psi(f) = 2m * max_e sum_a pi_a |f^(a)_e| = max_e sum_a deg(a) |f^(a)_e|.
"""
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from collections import deque
import heapq


# ---------------------------------------------------------------- graphs
def cone(adjH):
    """Cone K_1 v H. Hub is the LAST vertex (index n)."""
    n = len(adjH)
    adj = [list(a) + [n] for a in adjH] + [list(range(n))]
    return adj


def edges_of(adj):
    return [(u, v) for u in range(len(adj)) for v in adj[u] if u < v]


def bfs_dist(adj, src):
    n = len(adj)
    dist = [-1] * n
    dist[src] = 0
    dq = deque([src])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if dist[w] < 0:
                dist[w] = dist[u] + 1
                dq.append(w)
    return dist


def all_pairs_bfs(adj):
    return [bfs_dist(adj, s) for s in range(len(adj))]


def distance_distribution(adj):
    """counts[t] = number of ORDERED pairs (u,v) at distance t (u != v)."""
    n = len(adj)
    counts = {}
    for s in range(n):
        for t in bfs_dist(adj, s):
            if t > 0:
                counts[t] = counts.get(t, 0) + 1
    return counts


def is_connected(adj):
    return all(t >= 0 for t in bfs_dist(adj, 0))


# ---------------------------------------------------------------- finite fields and PG(2,q)
class GF:
    """GF(p^k) with elements 0..q-1 encoded as base-p digit vectors of polynomial coefficients."""
    def __init__(self, p, k=1, irreducible=None):
        self.p, self.k, self.q = p, k, p ** k
        if k == 1:
            self.add = lambda a, b: (a + b) % p
            self.mul = lambda a, b: (a * b) % p
            self.neg = lambda a: (-a) % p
            return
        # irreducible monic polynomial of degree k, coefficients low->high, without the leading 1
        irr = {(2, 2): [1, 1], (2, 3): [1, 1, 0], (3, 2): [1, 0], (2, 4): [1, 1, 0, 0]}[(p, k)] if irreducible is None else irreducible
        self.irr = irr
        q = self.q

        def to_vec(a):
            v = []
            for _ in range(k):
                v.append(a % p); a //= p
            return v

        def to_int(v):
            a = 0
            for c in reversed(v):
                a = a * p + c
            return a

        add_t = [[to_int([(x + y) % p for x, y in zip(to_vec(a), to_vec(b))]) for b in range(q)] for a in range(q)]

        def polymul(a, b):
            va, vb = to_vec(a), to_vec(b)
            prod = [0] * (2 * k - 1)
            for i, x in enumerate(va):
                for j, y in enumerate(vb):
                    prod[i + j] = (prod[i + j] + x * y) % p
            # reduce modulo x^k + irr(x)  (x^k = -irr(x))
            for deg in range(2 * k - 2, k - 1, -1):
                c = prod[deg]
                if c:
                    prod[deg] = 0
                    for i, r in enumerate(irr):
                        prod[deg - k + i] = (prod[deg - k + i] - c * r) % p
            return to_int(prod[:k])

        mul_t = [[polymul(a, b) for b in range(q)] for a in range(q)]
        self.add = lambda a, b: add_t[a][b]
        self.mul = lambda a, b: mul_t[a][b]
        self.neg = lambda a: to_int([(-x) % p for x in to_vec(a)])


def pg2_incidence_graph(p, k=1):
    """Point-line incidence graph of PG(2,q), q=p^k. Returns (adj, npoints)."""
    F = GF(p, k)
    q = F.q
    # canonical representatives of projective points: first nonzero coordinate = 1
    pts = []
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if (x, y, z) == (0, 0, 0):
                    continue
                first = next(c for c in (x, y, z) if c != 0)
                if first == 1:
                    pts.append((x, y, z))
    assert len(pts) == q * q + q + 1
    N = len(pts)
    adj = [[] for _ in range(2 * N)]
    for i, (a, b, c) in enumerate(pts):       # lines indexed like points (dual)
        for j, (x, y, z) in enumerate(pts):
            s = F.add(F.add(F.mul(a, x), F.mul(b, y)), F.mul(c, z))
            if s == 0:
                adj[j].append(N + i)
                adj[N + i].append(j)
    for v in adj:
        assert len(v) == q + 1
    return adj, N


# ---------------------------------------------------------------- the LP
def flow_parameter_lp(adj, verbose=False, return_duals=False):
    """
    Minimise lambda subject to
       for each source a and vertex x:  sum_out f^a - sum_in f^a = 1_(x=a) - pi_x
       for each edge e:                  sum_a deg(a) (f^a_{e+} + f^a_{e-}) <= lambda
       f >= 0.
    Optimal lambda = F(G) = inf_f psi(f).
    """
    N = len(adj)
    E = edges_of(adj)
    M = len(E)
    deg = np.array([len(a) for a in adj], dtype=float)
    twom = deg.sum()
    pi = deg / twom
    nv = N * 2 * M + 1          # variables: x[a, k], k<M forward (u->v), k>=M backward (v->u); last = lambda
    lam = nv - 1

    # equality constraints: rows (a, x)
    heads = np.array([v for (u, v) in E] + [u for (u, v) in E])   # arc k goes tail->head
    tails = np.array([u for (u, v) in E] + [v for (u, v) in E])
    rows, cols, vals = [], [], []
    arcs = np.arange(2 * M)
    for a in range(N):
        base = a * 2 * M
        # out of tail: +1 ; into head: -1
        rows.append(a * N + tails); cols.append(base + arcs); vals.append(np.ones(2 * M))
        rows.append(a * N + heads); cols.append(base + arcs); vals.append(-np.ones(2 * M))
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    A_eq = sp.csr_matrix((vals, (rows, cols)), shape=(N * N, nv))
    b_eq = np.zeros(N * N)
    for a in range(N):
        b_eq[a * N: (a + 1) * N] = -pi
        b_eq[a * N + a] += 1.0

    # inequality constraints: rows e
    rows, cols, vals = [], [], []
    for a in range(N):
        base = a * 2 * M
        rows.append(np.arange(M)); cols.append(base + np.arange(M)); vals.append(np.full(M, deg[a]))
        rows.append(np.arange(M)); cols.append(base + M + np.arange(M)); vals.append(np.full(M, deg[a]))
    rows.append(np.arange(M)); cols.append(np.full(M, lam)); vals.append(-np.ones(M))
    rows = np.concatenate(rows); cols = np.concatenate(cols); vals = np.concatenate(vals)
    A_ub = sp.csr_matrix((vals, (rows, cols)), shape=(M, nv))
    b_ub = np.zeros(M)

    c = np.zeros(nv); c[lam] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(0, None),
                  method="highs", options={"disp": verbose})
    if res.status != 0:
        raise RuntimeError(res.message)
    if return_duals:
        lengths = -np.asarray(res.ineqlin.marginals)   # >= 0, sum = 1
        return res.fun, lengths, res
    return res.fun


# ---------------------------------------------------------------- exact dual certificate
def dual_value_exact(adj, lengths):
    """
    lengths: dict edge (u,v) with u<v -> Fraction >= 0.
    Returns the exact value  2m * sum_{u,v ordered} pi_u pi_v d_l(u,v) / sum_e l_e ,
    which is a lower bound on F(G) (LP weak duality).
    """
    N = len(adj)
    E = edges_of(adj)
    deg = [len(a) for a in adj]
    twom = sum(deg)
    # integer scaling for exact Dijkstra
    den = 1
    for e in E:
        den = den * lengths[e].denominator // np.gcd(den, lengths[e].denominator)
    w = {}
    for (u, v) in E:
        L = int(lengths[(u, v)] * den)
        w[(u, v)] = L; w[(v, u)] = L
    total = Fraction(0)
    for s in range(N):
        dist = [None] * N
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for x in adj[u]:
                nd = d + w[(u, x)]
                if dist[x] is None or nd < dist[x]:
                    dist[x] = nd
                    heapq.heappush(pq, (nd, x))
        total += Fraction(deg[s]) * sum(Fraction(deg[t]) * dist[t] for t in range(N))
    total = total / (Fraction(twom) ** 2) / den
    suml = sum(lengths[e] for e in E)
    return Fraction(twom) * total / suml


def two_length_dual_cone(counts_H, n, d, r):
    """
    Exact value of the two-length dual certificate on the cone K_1 v H
    (H d-regular on n vertices with ordered-pair distance counts counts_H[t]):
      base length b = 2(d+2)/(r+d),  hub length L = (d+2) r/(r+d)   (so 2L/b = r, sum_e l_e = 2m).
    Value = 2 pi_h pi_B L + pi_v^2 sum_{u != v} min(b dist_H(u,v), 2L).
    """
    d2 = d + 2
    b = Fraction(2 * d2, r + d)
    L = Fraction(d2 * r, r + d)
    pi_h = Fraction(1, d2)
    pi_v = Fraction(d + 1, n * d2)
    pi_B = n * pi_v
    S = Fraction(0)
    for t, cnt in counts_H.items():
        S += cnt * min(b * t, 2 * L)
    return 2 * pi_h * pi_B * L + pi_v * pi_v * S


def best_two_length_dual_cone(counts_H, n, d):
    best = None
    for r in range(1, max(counts_H) + 1):
        v = two_length_dual_cone(counts_H, n, d, r)
        if best is None or v > best[0]:
            best = (v, r)
    return best


def hub_routing_upper_bound(n, d):
    """psi of the all-through-the-hub routing on K_1 v H (exact): 2(d+1)(1 - pi_v)."""
    pi_v = Fraction(d + 1, n * (d + 2))
    return 2 * (d + 1) * (1 - pi_v)


def ball_bound_lower(n, d, r):
    """Rigorous lower bound on the two-length certificate using only |B(v,r-1)| <= 1 + d((d-1)^(r-1)-1)/(d-2)."""
    d2 = d + 2
    L = Fraction(d2 * r, r + d)
    pi_h = Fraction(1, d2)
    pi_v = Fraction(d + 1, n * d2)
    pi_B = n * pi_v
    if d >= 3:
        S = d * ((d - 1) ** (r - 1) - 1) // (d - 2) if d > 2 else 2 * (r - 1)
    else:
        S = 2 * (r - 1)
    far = n * (n - 1) - n * S   # ordered pairs with dist >= r
    far = max(far, 0)
    return 2 * L * (pi_h * pi_B + pi_v * pi_v * far)


# ---------------------------------------------------------------- spectrum
def srw_eigs(adj):
    N = len(adj)
    A = np.zeros((N, N))
    for u in range(N):
        for v in adj[u]:
            A[u, v] = 1.0
    deg = A.sum(1)
    Dm = np.diag(deg ** -0.5)
    S = Dm @ A @ Dm
    return np.sort(np.linalg.eigvalsh(S))[::-1]


def tau2(adj):
    ev = srw_eigs(adj)
    return 1.0 / (1.0 - ev[1]), ev


def adjacency_eigs(adj):
    N = len(adj)
    A = np.zeros((N, N))
    for u in range(N):
        for v in adj[u]:
            A[u, v] = 1.0
    return np.sort(np.linalg.eigvalsh(A))[::-1]
