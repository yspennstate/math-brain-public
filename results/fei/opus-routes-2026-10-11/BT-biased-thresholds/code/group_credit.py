"""Credit inequality and alpha*TC/I for thresholds with exchangeable groups (G <= 3 groups),
large group sizes, via count distributions (float64, log-safe). Evidence only."""
import numpy as np, math, sys, time, json
from scipy.stats import binom
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
TLIM = float(sys.argv[2]) if len(sys.argv) > 2 else 300

def analyze(w, m, q, theta):
    G = len(w)
    pm = [binom.pmf(np.arange(m[g] + 1), m[g], q[g]) for g in range(G)]
    grids = np.meshgrid(*[np.arange(m[g] + 1) for g in range(G)], indexing='ij')
    W = sum(w[g] * grids[g] for g in range(G))
    P = pm[0].reshape([-1] + [1] * (G - 1))
    for g in range(1, G):
        P = P * pm[g].reshape([1] * g + [-1] + [1] * (G - 1 - g))
    Ain = W >= theta - 1e-12
    a1 = P[Ain].sum(); a0 = P[~Ain].sum()
    if a1 <= 1e-200 or a0 <= 1e-200: return None
    # minority side
    A = Ain if a1 <= a0 else ~Ain
    alpha = min(a1, a0)
    # TC of mu_A: H(Y) = H(counts|A) + E_A sum ln C(m_g, N_g); marginals per coordinate
    pc = np.where(A, P, 0.0) / alpha
    nz = pc > 0
    Hcounts = -np.sum(pc[nz] * np.log(pc[nz]))
    lnC = 0.0
    Hm = 0.0
    for g in range(G):
        lc = np.array([math.lgamma(m[g] + 1) - math.lgamma(k + 1) - math.lgamma(m[g] - k + 1) for k in range(m[g] + 1)])
        lnC += np.sum(pc * lc.reshape([1] * g + [-1] + [1] * (G - 1 - g)))
        EN = np.sum(pc * grids[g])
        b = EN / m[g]
        for x in (b, 1 - b):
            if x > 0: Hm -= m[g] * x * math.log(x)
    TC = Hm - (Hcounts + lnC)
    # pivotal probabilities rho_g for a coordinate of group g (increasing threshold on original side)
    I = 0.0; credit = 0.0
    V = 4 * alpha * (1 - alpha)
    for g in range(G):
        if m[g] == 0: continue
        pm2 = list(pm); pm2[g] = binom.pmf(np.arange(m[g]), m[g] - 1, q[g])
        grids2 = np.meshgrid(*[np.arange(len(pm2[h])) for h in range(G)], indexing='ij')
        W2 = sum(w[h] * grids2[h] for h in range(G))
        P2 = pm2[0].reshape([-1] + [1] * (G - 1))
        for h in range(1, G):
            P2 = P2 * pm2[h].reshape([1] * h + [-1] + [1] * (G - 1 - h))
        rho = P2[(W2 >= theta - w[g] - 1e-12) & (W2 < theta - 1e-12)].sum()
        s2 = 4 * q[g] * (1 - q[g])
        Ig = m[g] * s2 * rho
        I += Ig
        if rho > 0: credit += Ig * max(0.0, math.log(4 * rho / V))
    if I <= 0: return None
    return dict(alpha=alpha, TC=TC, I=I, aTC_I=alpha * TC / I, excess_I=(V * math.log(1 / V) - credit) / I)

t0 = time.time(); best = {'aTC_I': (0, None), 'excess_I': (0, None)}; cnt = 0
weight_sets = [(1, 2), (1, 3), (2, 3), (1, 1.5), (1, 10), (1, 2, 3), (1, 2, 4), (1, 3, 9), (2, 3, 5), (1, 1.1)]
qvals = [1e-4, 1e-3, 1e-2, 0.05, 0.2, 0.5, 0.8, 0.95, 0.99, 0.999]
while time.time() - t0 < TLIM:
    w = list(weight_sets[rng.integers(len(weight_sets))])
    G = len(w)
    m = [int(rng.choice([1, 2, 3, 5, 10, 30, 80])) for _ in range(G)]
    if G == 3: m = [min(x, 30) for x in m]
    q = [float(rng.choice(qvals)) for _ in range(G)]
    Wmax = sum(w[g] * m[g] for g in range(G))
    theta = rng.random() * Wmax
    r = analyze(w, m, q, theta)
    cnt += 1
    if r is None: continue
    for key in best:
        if r[key] > best[key][0]:
            best[key] = (r[key], dict(w=w, m=m, q=q, theta=theta, alpha=r['alpha'], TC=r['TC']))
print('configs', cnt)
for k, v in best.items(): print(k, v)
