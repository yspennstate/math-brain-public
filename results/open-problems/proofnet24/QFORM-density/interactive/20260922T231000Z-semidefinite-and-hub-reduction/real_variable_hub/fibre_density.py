try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Exact, unbiased (bin-free) density estimator for Q = X^T A X + b^T X, X independent with given densities.
# Fibre identity with the partition of unity (d_i Q)^2/|grad Q|^2:
#   p(s) = sum_i E[ sum_{roots r of Q(.,X_{-i}) = s} f_i(r) |d_i Q| / |grad Q|^2 ]   (COUNTEREXAMPLE_SEARCH.md, item 1)
import numpy as np, sys, time

class Law:
    """density f and sampler for one coordinate"""
    def __init__(self, kind, rng, M=1, N=1, spread=7.3):
        self.kind = kind
        if kind == 'unif':                      # uniform on [-1/2, 1/2]
            pass
        elif kind == 'multi':                   # uniform on M intervals of length 1/M at spread positions
            self.M = M; self.len = 1.0 / M
            self.pos = spread * np.arange(M) - spread * (M - 1) / 2 + rng.uniform(-0.3, 0.3, M)
        elif kind == 'bumpy':                   # N Gaussian bumps of height 1, mass 1/N, sd 1/(N sqrt(2 pi)), spread positions
            self.N = N; self.sd = 1.0 / (N * np.sqrt(2 * np.pi))
            self.pos = spread * np.arange(N) - spread * (N - 1) / 2 + rng.uniform(-0.3, 0.3, N)
        self.rng = rng
    def sample(self, n):
        r = self.rng
        if self.kind == 'unif':
            return r.uniform(-0.5, 0.5, n)
        if self.kind == 'multi':
            k = r.integers(0, self.M, n); return self.pos[k] + r.uniform(0, self.len, n)
        k = r.integers(0, self.N, n); return self.pos[k] + self.sd * r.normal(size=n)
    def f(self, x):
        if self.kind == 'unif':
            return ((x >= -0.5) & (x < 0.5)).astype(float)
        if self.kind == 'multi':
            out = np.zeros_like(x)
            for p in self.pos:
                out += ((x >= p) & (x < p + self.len))
            return out
        out = np.zeros_like(x)
        for p in self.pos:
            out += np.exp(-np.pi * self.N ** 2 * (x - p) ** 2)
        return out

def density(A, b, laws, svals, Nsamp, chunk=4000):
    n = A.shape[0]
    Acol2 = np.sum(A * A, axis=0)              # |A[:, i]|^2
    diagA = np.diag(A).copy()
    acc = np.zeros(len(svals)); acc2 = np.zeros(len(svals)); done = 0
    while done < Nsamp:
        m = min(chunk, Nsamp - done)
        X = np.stack([laws[i].sample(m) for i in range(n)], axis=1)   # m x n
        AX = X @ A
        Qv = np.sum(X * AX, axis=1) + X @ b
        g = 2 * AX + b                                               # gradient, m x n
        g2 = np.sum(g * g, axis=1)
        gA = g @ A                                                   # <g, A[:, i]>
        tot = np.zeros((m, len(svals)))
        for i in range(n):
            a = diagA[i]; Xi = X[:, i]
            B = g[:, i] - 2 * a * Xi
            C = Qv - a * Xi ** 2 - B * Xi
            for k, s in enumerate(svals):
                if abs(a) < 1e-14:
                    with np.errstate(divide='ignore', invalid='ignore'):
                        r = (s - C) / B
                    roots = [np.where(np.isfinite(r), r, 1e300)]
                else:
                    disc = B * B - 4 * a * (C - s)
                    ok = disc > 0; sq = np.sqrt(np.where(ok, disc, 0.0))
                    roots = [np.where(ok, (-B + sq) / (2 * a), 1e300), np.where(ok, (-B - sq) / (2 * a), 1e300)]
                for r in roots:
                    fr = laws[i].f(r)
                    nz = fr > 0
                    if not np.any(nz):
                        continue
                    d = r - Xi
                    dQ = 2 * a * r + B
                    G2 = g2 + 4 * d * gA[:, i] + 4 * d * d * Acol2[i]
                    with np.errstate(divide='ignore', invalid='ignore'):
                        c = np.where(nz, fr * np.abs(dQ) / G2, 0.0)
                    tot[:, k] += np.where(np.isfinite(c), c, 0.0)
        acc += tot.sum(0); acc2 += (tot ** 2).sum(0); done += m
    mean = acc / done; sd = np.sqrt(np.maximum(acc2 / done - mean ** 2, 0) / done)
    return mean, sd
