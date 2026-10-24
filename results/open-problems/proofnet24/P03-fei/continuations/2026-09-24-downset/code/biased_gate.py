# Biased strengthened inequality (O'Donnell-Tan) for small monotone 2-DNF gates under product measures:
#   L_mu(G) = sum_{A nonempty} P_mu(A) log2(sigma_A^2 / P_mu(A)),  ratio = L_mu / (I_mu - Var_mu),
# with q_j = mu(y_j = 1), nu_j = 2 q_j - 1, sigma_j^2 = 1 - nu_j^2, phi_j = (2 y_j - 1 - nu_j)/sigma_j, and
# 1 - 2G = sum_A g~(A) phi_A (the conventions of the 2026-09-23 paper, eq. (biased)).
# Question: does the ratio stay bounded (near 2 + 4 log2 e = 7.771) as the biases go to 0 or 1, for gates that are
# not read-once (paths, cycles, stars, triangle, K4, K_{2,3}), or does it grow like log(1/q)?
import itertools, math, numpy as np

def biased_transform(vals, q):
    """vals: array over {0,1}^m (bit j of the index = y_j) of F = 1 - 2G; returns coefficients g~(A) indexed by mask."""
    m = len(q); a = vals.astype(np.float64).copy()
    for j in range(m):
        nu = 2 * q[j] - 1; s = math.sqrt(1 - nu * nu)
        ph1 = (1 - nu) / s; ph0 = (-1 - nu) / s
        a = a.reshape(-1, 2, 1 << j)
        x0 = a[:, 0, :].copy(); x1 = a[:, 1, :].copy()
        a[:, 0, :] = (1 - q[j]) * x0 + q[j] * x1                 # coefficient of 1
        a[:, 1, :] = (1 - q[j]) * ph0 * x0 + q[j] * ph1 * x1     # coefficient of phi_j
        a = a.reshape(-1)
    return a

def ratio(edges, m, q):
    N = 1 << m; x = np.arange(N)
    G = np.zeros(N, dtype=bool)
    for (u, v) in edges: G |= ((x >> u) & 1).astype(bool) & ((x >> v) & 1).astype(bool)
    c = biased_transform(np.where(G, -1.0, 1.0), q)
    P = c * c
    sig2 = np.array([1 - (2 * qq - 1) ** 2 for qq in q])
    logsig = np.zeros(N)
    pc = np.zeros(N)
    for j in range(m):
        has = ((x >> j) & 1).astype(bool)
        logsig[has] += math.log2(sig2[j]); pc[has] += 1
    nz = (np.arange(N) > 0) & (P > 1e-300)
    L = float((P[nz] * (logsig[nz] - np.log2(P[nz]))).sum())
    I = float((P * pc).sum()); Var = float(P[1:].sum())
    return L, I - Var, abs(P.sum() - 1)

if __name__ == '__main__':
    gates = {
        'edge': (2, [(0, 1)]),
        'matching2': (4, [(0, 1), (2, 3)]),
        'matching3': (6, [(0, 1), (2, 3), (4, 5)]),
        'path3': (3, [(0, 1), (1, 2)]),
        'path4': (4, [(0, 1), (1, 2), (2, 3)]),
        'path6': (6, [(i, i + 1) for i in range(5)]),
        'star3': (4, [(0, 1), (0, 2), (0, 3)]),
        'triangle': (3, [(0, 1), (1, 2), (0, 2)]),
        'cycle5': (5, [(i, (i + 1) % 5) for i in range(5)]),
        'K4': (4, list(itertools.combinations(range(4), 2))),
        'K23': (5, [(i, 2 + j) for i in range(2) for j in range(3)]),
    }
    worst = 0.0
    for name, (m, e) in gates.items():
        row = []
        for q0 in (0.5, 0.2, 0.05, 1e-2, 1e-3, 1e-4, 1e-6, 0.8, 0.95, 0.99, 0.999, 1 - 1e-6):
            L, D, perr = ratio(e, m, [q0] * m)
            r = L / D if D > 1e-300 else float('nan')
            worst = max(worst, r if r == r else 0)
            row.append('%g:%.3f' % (q0, r))
        # mixed biases: one tiny, others moderate, and random
        rng = np.random.default_rng(1)
        mx = 0.0
        for t in range(300):
            qs = list(np.exp(rng.uniform(np.log(1e-5), np.log(0.5), size=m)))
            qs = [qq if rng.random() < 0.5 else 1 - qq for qq in qs]
            L, D, perr = ratio(e, m, qs)
            if D > 1e-300: mx = max(mx, L / D)
        worst = max(worst, mx)
        print('%-10s equal q: %s | random biases max %.3f' % (name, ' '.join(row), mx), flush=True)
    print('largest ratio: %.4f (AND2/OR2 sharp constant 2 + 4 log2 e = %.4f)' % (worst, 2 + 4 / math.log(2)))
