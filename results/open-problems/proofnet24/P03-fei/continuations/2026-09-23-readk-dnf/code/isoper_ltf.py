# (*) for threshold functions at larger n, float64 without cancellation:
#   alpha = mu(f=1) summed directly, Var = 4 alpha (1-alpha), rho_i = mu(i pivotal) summed directly.
# r1 = (Var ln(1/Var) - sum_i Inf_i ln+(rho_i/Var)) / I,  Inf_i = sig_i^2 rho_i.
import numpy as np, math, random, sys
def run(w, th, q):
    n = len(w); N = 1 << n
    X = ((np.arange(N)[:, None] >> np.arange(n)) & 1).astype(np.int8)
    lw = np.where(X == 1, np.log(q), np.log1p(-q)).sum(axis=1)
    wt = np.exp(lw)
    s = X @ np.array(w)
    f = (s >= th)
    a = wt[f].sum(); b = wt[~f].sum()
    alpha = min(a, b)
    if alpha <= 0: return None
    Var = 4 * a * b / (a + b) ** 2
    sig2 = 4 * q * (1 - q)
    rho = np.zeros(n)
    for i in range(n):
        m0 = X[:, i] == 0
        s0 = s[m0]; w0 = wt[m0] / (1 - q[i])
        piv = (s0 < th) & (s0 + w[i] >= th)
        rho[i] = w0[piv].sum()
    Inf = sig2 * rho; I = Inf.sum()
    if I <= 0: return None
    cred = sum(Inf[i] * max(0.0, math.log(rho[i] / Var)) for i in range(n) if rho[i] > 0)
    return (Var * math.log(1 / Var) - cred) / I, Var, I
rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nlo, nhi = int(sys.argv[3]), int(sys.argv[4])
best = (-1e9, None)
for t in range(T):
    n = rng.randint(nlo, nhi)
    mode = rng.random()
    if mode < 0.3: w = [1.0] * n
    elif mode < 0.6: w = [float(rng.randint(1, 6)) for _ in range(n)]
    else: w = [rng.expovariate(1.0) for _ in range(n)]
    th = rng.uniform(0.01, sum(w))
    q = []
    for _ in range(n):
        u = rng.random()
        q.append(10 ** -rng.uniform(0, 12) if u < 0.4 else (1 - 10 ** -rng.uniform(0, 12) if u < 0.6 else rng.uniform(0.01, 0.99)))
    q = np.clip(np.array(q), 1e-13, 1 - 1e-13)
    r = run(w, th, q)
    if r and r[0] > best[0]:
        best = (r[0], (n, [round(x, 3) for x in w], round(th, 3), [float('%.3g' % x) for x in q], r[1], r[2]))
        print(t, 'best r1', round(r[0], 4), best[1], flush=True)
print('DONE', best[0])
