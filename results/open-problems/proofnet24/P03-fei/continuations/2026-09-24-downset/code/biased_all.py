# Biased strengthened inequality over ALL monotone functions on n <= 5 variables: for many product measures (random
# log-uniform biases towards 0 and 1, plus equal biases), compute ratio = L_mu/(I_mu - Var_mu) for every function at once
# and keep the largest; then run a local search on the biases for the 30 best (function, measure) pairs.
import sys, math, random, numpy as np
from mono_enum import monotone_masks

def biased_transform_many(V, q):
    """V: (F, N) values of 1-2G; returns (F, N) coefficients in the biased basis."""
    Fn, N = V.shape; m = len(q); a = V.astype(np.float64).copy()
    for j in range(m):
        nu = 2 * q[j] - 1; s = math.sqrt(max(1 - nu * nu, 1e-300))
        ph1 = (1 - nu) / s; ph0 = (-1 - nu) / s
        a = a.reshape(Fn, -1, 2, 1 << j)
        x0 = a[:, :, 0, :].copy(); x1 = a[:, :, 1, :].copy()
        a[:, :, 0, :] = (1 - q[j]) * x0 + q[j] * x1
        a[:, :, 1, :] = (1 - q[j]) * ph0 * x0 + q[j] * ph1 * x1
        a = a.reshape(Fn, N)
    return a

def ratios(V, q, m):
    N = 1 << m; x = np.arange(N)
    c = biased_transform_many(V, q); P = c * c
    logsig = np.zeros(N); pc = np.zeros(N)
    for j in range(m):
        has = ((x >> j) & 1).astype(bool); logsig[has] += math.log2(1 - (2 * q[j] - 1) ** 2); pc[has] += 1
    Pn = P[:, 1:]
    with np.errstate(divide='ignore', invalid='ignore'):
        term = np.where(Pn > 1e-300, Pn * (logsig[None, 1:] - np.log2(np.where(Pn > 1e-300, Pn, 1.0))), 0.0)
    L = term.sum(1)
    D = (P * pc[None, :]).sum(1) - Pn.sum(1)
    return np.where(D > 1e-12, L / np.where(D > 1e-12, D, 1.0), 0.0), D

if __name__ == '__main__':
    rng = random.Random(7)
    for m in [int(t) for t in sys.argv[1].split(',')]:
        masks = monotone_masks(m); N = 1 << m
        bits = ((masks[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
        V = np.where(bits, -1.0, 1.0)
        best = []
        qs = [[0.5] * m] + [[e] * m for e in (1e-4, 1e-2, 0.1, 0.3, 0.7, 0.9, 0.99, 0.9999)]
        for t in range(int(sys.argv[2])):
            q = [math.exp(rng.uniform(math.log(1e-5), math.log(0.5))) for _ in range(m)]
            qs.append([qq if rng.random() < 0.5 else 1 - qq for qq in q])
        for q in qs:
            r, D = ratios(V, q, m)
            k = np.argsort(-r)[:5]
            for i in k: best.append((float(r[i]), int(i), list(q)))
        best.sort(key=lambda z: -z[0]); top = best[:30]
        print('m=%d: %d functions, %d measures; best before search %.5f' % (m, len(masks), len(qs), top[0][0]), flush=True)
        overall = top[0][0]; arg = top[0]
        for r0, i, q in top:
            q = list(q); r = r0
            for it in range(400):
                j = rng.randrange(m); old = q[j]
                if rng.random() < 0.5: new = old * math.exp(rng.gauss(0, 1.0))
                else: new = 1 - (1 - old) * math.exp(rng.gauss(0, 1.0))
                q[j] = min(1 - 1e-7, max(1e-7, new))
                r2 = float(ratios(V[i:i + 1], q, m)[0][0])
                if r2 >= r: r = r2
                else: q[j] = old
            if r > overall: overall = r; arg = (r, i, q)
        print('m=%d: largest ratio after local search %.6f (2 + 4 log2 e = %.6f), function mask %s, biases %s'
              % (m, overall, 2 + 4 / math.log(2), hex(int(masks[arg[1]])), [round(v, 7) for v in arg[2]]), flush=True)
