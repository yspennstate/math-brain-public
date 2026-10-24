"""Exact conditional sublevel estimator for two hubs.

Q = X_H^T B X_H + 2 X_H^T (A X' + beta) + R(X'),   H = {1, 2},  X' = leaves (m coordinates).
Given X' and X_1, Q is a one-dimensional quadratic in X_2:
    Q = b22 X2^2 + (c2 + 2 b12 X1) X2 + (b11 X1^2 + c1 X1 + r),   c = 2(A X' + beta), r = R(X').
P(|Q - s| <= eps | X', X1) is computed exactly (union of <= 2 intervals intersected with the support of X2),
then averaged over Monte Carlo samples of (X', X1).  The estimator is bounded by 1, so there is no variance blow-up.
Laws: each coordinate uniform on a set of measure one (a union of intervals).
"""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np


class UnionLaw:
    """Uniform law on a union of disjoint intervals of total length 1."""

    def __init__(self, lefts, width):
        self.lefts = np.sort(np.asarray(lefts, dtype=float))
        self.width = float(width)
        assert abs(len(self.lefts) * self.width - 1.0) < 1e-12

    @staticmethod
    def interval():
        return UnionLaw([-0.5], 1.0)

    @staticmethod
    def spread(npieces, span, rng):
        # npieces intervals of length 1/npieces, left ends spaced at least 2/npieces apart inside [-span, span]
        w = 1.0 / npieces
        while True:
            lefts = np.sort(rng.uniform(-span, span - w, size=npieces))
            if npieces == 1 or np.min(np.diff(lefts)) > 2 * w:
                return UnionLaw(lefts, w)

    def sample(self, n, rng):
        k = rng.integers(0, len(self.lefts), size=n)
        return self.lefts[k] + self.width * rng.random(n)

    def measure(self, lo, hi):
        """Measure of [lo, hi] intersected with the support (vectorised over lo, hi; lo <= hi)."""
        lo = np.asarray(lo)[..., None]
        hi = np.asarray(hi)[..., None]
        a = self.lefts[None, :]
        b = a + self.width
        return np.clip(np.minimum(hi, b) - np.maximum(lo, a), 0.0, None).sum(axis=-1)


def quad_sublevel_prob(alpha, beta, gamma, s, eps, law):
    """P(|alpha x^2 + beta x + gamma - s| <= eps) for x ~ law, vectorised over alpha, beta, gamma arrays."""
    alpha = np.asarray(alpha, float)
    beta = np.asarray(beta, float)
    gamma = np.asarray(gamma, float)
    out = np.zeros(np.broadcast(alpha, beta, gamma).shape)
    alpha, beta, gamma = np.broadcast_arrays(alpha, beta, gamma)
    lin = np.abs(alpha) < 1e-300
    if np.any(lin):
        b = beta[lin]
        g = gamma[lin]
        with np.errstate(divide="ignore", invalid="ignore"):
            e1 = (s - g - eps) / b
            e2 = (s - g + eps) / b
        lo = np.minimum(e1, e2)
        hi = np.maximum(e1, e2)
        res = law.measure(lo, hi)
        # beta = 0 exactly: the event is |g - s| <= eps with probability 1 or 0
        z = (b == 0)
        res[z] = (np.abs(g[z] - s) <= eps).astype(float)
        out[lin] = res
    q = ~lin
    if np.any(q):
        a = alpha[q]
        b = beta[q]
        g = gamma[q]
        shift = -b / (2 * a)
        kappa = g - b * b / (4 * a)
        u1 = (s - eps - kappa) / a
        u2 = (s + eps - kappa) / a
        lo = np.maximum(np.minimum(u1, u2), 0.0)
        hi = np.maximum(u1, u2)
        ok = hi > 0
        rlo = np.sqrt(lo)
        rhi = np.sqrt(np.maximum(hi, 0.0))
        m = law.measure(shift + rlo, shift + rhi) + law.measure(shift - rhi, shift - rlo)
        m[~ok] = 0.0
        out[q] = m
    return out


def pair_prob(B, c1, c2, r, x1, s, eps, law2):
    """P(|Q - s| <= eps | X', X1) for the pair, vectorised over samples."""
    alpha = B[1][1] + 0.0 * c2
    beta = c2 + 2 * B[0][1] * x1
    gamma = B[0][0] * x1 ** 2 + c1 * x1 + r
    return quad_sublevel_prob(alpha, beta, gamma, s, eps, law2)


def spread_rows(m, sigma, rng, orth=True):
    """Two hub rows with entries of size ~ sigma/sqrt(m), orthogonal, each of norm sigma."""
    G = rng.standard_normal((2, m))
    if orth:
        Qm, _ = np.linalg.qr(G.T)
        A = Qm.T[:2] * sigma
    else:
        A = G / np.linalg.norm(G, axis=1, keepdims=True) * sigma
    return A
