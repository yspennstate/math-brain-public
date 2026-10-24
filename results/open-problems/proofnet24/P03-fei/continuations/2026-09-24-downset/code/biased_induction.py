# The biased strengthened inequality by induction on coordinates. For a gate G under the product measure mu with biases q,
#   L(G) = sum_{A nonempty} P(A) log2(sigma_A^2 / P(A)),   R(G) = I - Var,
# and restricting coordinate v to b (probabilities 1-q_v, q_v) gives G_b on the other coordinates with the same measure.
# The induction proves L <= C R on a restriction-closed class if every nonconstant member has a coordinate with
#   Lstep_v = L(G) - E_b L(G_b)  <=  C * Rstep_v,   Rstep_v = R(G) - E_b R(G_b).
# We compute rho(G, q) = min_v Lstep_v / Rstep_v exactly for small monotone 2-DNF gates over many bias vectors, and
# report the largest value found. Bounded (below 2 + 4 log2 e = 7.77) = the one-coordinate step can work for these gates.
import itertools, math, numpy as np
from biased_gate import biased_transform

def LR(F, q):
    """F: +-1 array over {0,1}^m (bit j of the index = y_j), q: biases. Returns (L, R)."""
    m = len(q); N = 1 << m
    c = biased_transform(F.astype(float), q); P = c * c
    sig2 = np.array([4 * qq * (1 - qq) for qq in q])
    x = np.arange(N)
    logsig = np.zeros(N); pc = np.zeros(N)
    for j in range(m):
        has = ((x >> j) & 1).astype(bool); logsig[has] += math.log2(sig2[j]); pc[has] += 1
    nz = (x > 0) & (P > 1e-300)
    L = float((P[nz] * (logsig[nz] - np.log2(P[nz]))).sum())
    R = float((P * pc).sum()) - float(P[1:].sum())
    return L, R

def restrict(F, m, v, b):
    x = np.arange(1 << m)
    keep = ((x >> v) & 1) == b
    return F[keep]            # remaining coordinates keep their relative order

def rho(F, q):
    m = len(q); L, R = LR(F, q); best = math.inf
    for v in range(m):
        qq = q[:v] + q[v + 1:]
        F0 = restrict(F, m, v, 0); F1 = restrict(F, m, v, 1)
        L0, R0 = LR(F0, qq) if m > 1 else (0.0, 0.0)
        L1, R1 = LR(F1, qq) if m > 1 else (0.0, 0.0)
        Ls = L - ((1 - q[v]) * L0 + q[v] * L1); Rs = R - ((1 - q[v]) * R0 + q[v] * R1)
        if Rs > 1e-15: best = min(best, Ls / Rs)
    return best

def gate(m, edges):
    x = np.arange(1 << m); G = np.zeros(1 << m, dtype=bool)
    for (u, w) in edges: G |= ((x >> u) & 1).astype(bool) & ((x >> w) & 1).astype(bool)
    return np.where(G, -1.0, 1.0)

rng = np.random.default_rng(17)
graphs = {'edge': (2, [(0, 1)]), 'path3': (3, [(0, 1), (1, 2)]), 'triangle': (3, [(0, 1), (1, 2), (0, 2)]),
          'matching2': (4, [(0, 1), (2, 3)]), 'path4': (4, [(0, 1), (1, 2), (2, 3)]), 'star3': (4, [(0, 1), (0, 2), (0, 3)]),
          'C4': (4, [(0, 1), (1, 2), (2, 3), (3, 0)]), 'K4': (4, list(itertools.combinations(range(4), 2))),
          'path5': (5, [(i, i + 1) for i in range(4)]), 'C5': (5, [(i, (i + 1) % 5) for i in range(5)]),
          'K23': (5, [(i, 2 + j) for i in range(2) for j in range(3)]), 'matching3': (6, [(0, 1), (2, 3), (4, 5)]),
          'path6': (6, [(i, i + 1) for i in range(5)]), 'K33': (6, [(i, 3 + j) for i in range(3) for j in range(3)])}
overall = 0.0
for name, (m, e) in graphs.items():
    F = gate(m, e); worst = (0.0, None)
    trials = [[q0] * m for q0 in (0.5, 0.3, 0.1, 0.03, 0.01, 1e-3, 0.7, 0.9, 0.97, 0.99, 0.999)]
    for t in range(250):
        qs = list(np.exp(rng.uniform(np.log(1e-4), np.log(0.5), size=m)))
        trials.append([qq if rng.random() < 0.5 else 1 - qq for qq in qs])
    for q in trials:
        r = rho(F, q)
        if r > worst[0]: worst = (r, q)
    overall = max(overall, worst[0])
    print('%-10s max over %d bias vectors of min_v Lstep/Rstep = %.4f  (at q = %s)'
          % (name, len(trials), worst[0], ', '.join('%.3g' % v for v in worst[1])), flush=True)
print('largest: %.4f   (2 + 4 log2 e = %.4f)' % (overall, 2 + 4 / math.log(2)))
