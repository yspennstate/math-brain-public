# Biased down-set identities and bounds for monotone G under a product measure mu (biases q_j), coordinate v, q = q_v:
#   D = {G = 0}, mu' = mu on the other coordinates, B = blocked y (y in D, y+v not in D) = pivotal, Fr = free y (y+v in D),
#   alpha(T) = E_{mu_D}[chi_T 1_B],  beta(T) = E_{mu_D}[chi_T 1_Fr]   (chi = the mu-orthonormal characters),
#   claims: Ft(T+v) = -2 mu(D) tau alpha(T), Ft(T) = 2 mu(D)(alpha + beta)(T) for T nonempty, tau = sqrt(q/(1-q));
#           sum alpha^2 = (1-q)^2 mu'(B)/mu(D)^2, sum beta^2 = mu'(Fr)/mu(D)^2;  Inf~_v = 4q(1-q) mu'(B).
#   erasure bound: sum_{T nonempty} E(Ft(T)^2, Ft(T+v)^2) <= Inf~_v log2(e(1 + 2(1-q)/q + 2 mu'(Fr)/(q(1-q) mu'(B)))).
#   minterm lemma: a minterm of size k with all its biases in [eps, 1-eps] has a v with mu_D(v blocked) >= eps^(k-1)(1-eps).
import math, itertools, numpy as np
from biased_gate import biased_transform
rng = np.random.default_rng(41)
def phi(p): return np.where(p > 1e-300, -p * np.log2(np.where(p > 1e-300, p, 1)), 0.0)
worst_id = 0.0; worst_er = 0.0; worst_mt = 9.0; n_cases = 0
for trial in range(300):
    m = int(rng.integers(3, 8)); N = 1 << m; x = np.arange(N); G = np.zeros(N, dtype=bool); terms = []
    for _ in range(int(rng.integers(1, 2 * m))):
        w = int(rng.integers(1, 4)); S = sorted(int(u) for u in rng.choice(m, size=w, replace=False)); terms.append(S)
        mask = sum(1 << u for u in S); G |= (x & mask) == mask
    if G.all() or not G.any(): continue
    eps = float(rng.choice([0.05, 0.1, 0.2, 0.3, 0.45]))
    q = list(rng.uniform(eps, 1 - eps, size=m))
    Ft = biased_transform(np.where(G, -1.0, 1.0), q)
    wts = np.ones(N)
    for j in range(m): wts *= np.where((x >> j) & 1, q[j], 1 - q[j])
    muD = float(wts[~G].sum())
    for v in range(m):
        qv = q[v]; tau = math.sqrt(qv / (1 - qv))
        lo = x[((x >> v) & 1) == 0]; hi = lo | (1 << v)
        wp = wts[lo] / (1 - qv)                       # mu' weight of y
        B = (~G[lo]) & G[hi]; Fr = (~G[hi])
        muB = float(wp[B].sum()); muF = float(wp[Fr].sum())
        # identities via the Fourier side
        a2 = float((Ft[hi] ** 2).sum()) / (4 * muD * muD * tau * tau)
        worst_id = max(worst_id, abs(a2 - (1 - qv) ** 2 * muB / muD ** 2))
        inf = float((Ft[hi] ** 2).sum())
        worst_id = max(worst_id, abs(inf - 4 * qv * (1 - qv) * muB))
        if muB <= 1e-15: continue
        nz = lo > 0
        E = float((phi(Ft[lo][nz] ** 2) + phi(Ft[hi][nz] ** 2) - phi(Ft[lo][nz] ** 2 + Ft[hi][nz] ** 2)).sum())
        bound = inf * math.log2(math.e * (1 + 2 * (1 - qv) / qv + 2 * muF / (qv * (1 - qv) * muB)))
        worst_er = max(worst_er, E / bound)
        n_cases += 1
    # minterm lemma on the smallest term (a minterm contains it; use the true minterms)
    ones = [xx for xx in range(N) if G[xx]]
    minterms = [xx for xx in ones if all(not G[xx & ~(1 << u)] for u in range(m) if (xx >> u) & 1)]
    for M in minterms:
        vs = [u for u in range(m) if (M >> u) & 1]; k = len(vs)
        if k < 2: continue
        best = 0.0
        for v in vs:
            lo = x[((x >> v) & 1) == 0]; hi = lo | (1 << v)
            wb = (wts[lo])[(~G[lo]) & G[hi]].sum()          # mu(y blocked, x_v = 0)
            best = max(best, float(wb) / muD)
        worst_mt = min(worst_mt, best / (eps ** (k - 1) * (1 - eps)))
print('identities: max abs error %.2e' % worst_id)
print('erasure bound: %d (gate, coordinate) cases, max ratio to the bound %.4f (claim <= 1)' % (n_cases, worst_er))
print('minterm lemma: min over minterms of max_v mu_D(v blocked) / (eps^(k-1)(1-eps)) = %.4f (claim >= 1)' % worst_mt)
