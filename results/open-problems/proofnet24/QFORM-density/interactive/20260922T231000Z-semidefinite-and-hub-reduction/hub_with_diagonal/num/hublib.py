# Exact conditional estimator for Q = a X_h^2 + 2 X_h (L + beta) + R(X'):
#   p_Q(s) = E_{X'} sum_{roots x} f_h(x) / |2 a x + 2 (L + beta)|
# with roots of a x^2 + 2 x t + R = s:  Delta = t^2 + a (s - R), x_pm = (pm sqrt(Delta) - t)/a  (a != 0),
#                                         x = (s - R)/(2 t)                                   (a == 0).
import numpy as np

class Law:
    """density 1 on a union of intervals of total length 1 (uniform law when one interval)."""
    def __init__(self, starts, length):
        self.starts = np.asarray(starts, float); self.len = float(length)
    def sample(self, rng, size):
        k = rng.integers(0, len(self.starts), size=size)
        return self.starts[k] + self.len*rng.random(size)
    def pdf(self, x):
        out = np.zeros_like(x, dtype=float)
        for a0 in self.starts:
            out += ((x >= a0) & (x < a0 + self.len))
        return out

def uniform_law():
    return Law([-0.5], 1.0)

def spread_law(rng, m=5, span=10.0):
    L = 1.0/m
    # non-overlapping random starts in [-span, span]
    while True:
        st = np.sort(rng.uniform(-span, span - L, m))
        if np.all(np.diff(st) > L):
            return Law(st, L)

def density_on_grid(a, beta, tR_sampler, fh, s_grid, nchunks, rng):
    """tR_sampler(rng) -> (t_without_beta, R) arrays; returns mean of conditional density over chunks, per s."""
    acc = np.zeros(len(s_grid)); cnt = 0
    for _ in range(nchunks):
        L, R = tR_sampler(rng)
        t = L + beta
        n = len(t); cnt += n
        for j, s in enumerate(s_grid):
            if a == 0.0:
                x = (s - R)/(2*t)
                acc[j] += np.sum(fh.pdf(x)/(2*np.abs(t)))
            else:
                D = t*t + a*(s - R)
                ok = D > 0
                sq = np.sqrt(D[ok]); tt = t[ok]
                xp = (sq - tt)/a; xm = (-sq - tt)/a
                acc[j] += np.sum((fh.pdf(xp) + fh.pdf(xm))/(2*sq))
    return acc/cnt

def refine_max(a, beta, sampler, fh, s0, width, nchunks, rng, npts=21):
    sg = np.linspace(s0 - width, s0 + width, npts)
    d = density_on_grid(a, beta, sampler, fh, sg, nchunks, rng)
    j = int(np.argmax(d))
    return sg[j], d[j], d
