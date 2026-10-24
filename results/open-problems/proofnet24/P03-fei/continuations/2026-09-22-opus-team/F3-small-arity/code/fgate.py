"""Gate defect D_G(p), Poincare denominator W_G(p) and margin c_G = -D_G/W_G for a Boolean gate at a product bias.

Conventions (as in continuations/2026-09-22-gate-reformulation): a gate is a +-1 table `vals` of length 2^k, entry x
is G at the input whose bit i is 1 iff input i is TRUE (= -1).  Pr[input i true] = p_i, V_i = 4 p_i (1-p_i).  The
biased basis is phi_i = (x_i - mu_i)/sigma_i; along one coordinate the transform is [[1-p, p], [s, -s]],
s = sqrt(p(1-p)).  Then

    D_G(p) = sum_i It_i (Gamma(p_i) + h(V_i))/V_i - Htilde_G(p) - Gamma(p_out),
    W_G(p) = sum_i It_i / 4 - p_out (1 - p_out),          c_G = -D_G / W_G.

Gamma is the certificate potential p*G_num(log2(1/p)) + c p(1-p) on p <= 1/2 (mirrored), G_num piecewise linear
in x = log2(1/p) through the stored nodes, tail slope (G_J - b*)/K beyond x = K, exactly as gam.py / fei_cert.py.
"""
import math
import numpy as np

LN2 = math.log(2.0)
BSTAR = 8 - 4 / LN2


def lowprio():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 14, 15])
    except Exception:
        pass


class Pot:
    def __init__(self, npz, c=0.0):
        d = np.load(npz)
        self.xs = np.asarray(d["xs"], float)
        self.G = np.asarray(d["G"], float)
        self.K = float(self.xs[-1])
        self.C0 = float(d["C"])
        self.c = float(c)
        self.sig_t = (self.G[-1] - BSTAR) / self.K

    def Ghat(self, x):
        x = np.asarray(x, float)
        return np.where(x <= self.K, np.interp(np.minimum(x, self.K), self.xs, self.G),
                        self.G[-1] + (x - self.K) * self.sig_t)

    def __call__(self, z):
        z = np.asarray(z, float)
        s = np.clip(np.minimum(z, 1 - z), 1e-300, 0.5)
        return s * self.Ghat(np.log2(1.0 / s)) + self.c * z * (1 - z)


def h2(v):
    v = np.asarray(v, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        a = np.where((v > 0) & (v < 1), -v * np.log2(np.where(v > 0, v, 1.0)), 0.0)
        b = np.where((v > 0) & (v < 1), -(1 - v) * np.log2(np.where(v < 1, 1 - v, 1.0)), 0.0)
    return a + b


def spectrum(vals, P):
    """biased coefficients.  vals: (2^k,) or (B, 2^k); P: (B, k).  Returns C of shape (B, 2^k), index T = bitmask."""
    P = np.atleast_2d(np.asarray(P, float))
    B, k = P.shape
    n = 1 << k
    V = np.asarray(vals, float)
    if V.ndim == 1:
        A = np.broadcast_to(V, (B, n)).copy()
    else:
        A = V.astype(float).copy()
    # bit i of the index <-> axis (k-1-i) of the C-order reshape (2,)*k
    A = A.reshape((B,) + (2,) * k)
    for i in range(k):
        ax = 1 + (k - 1 - i)
        p = P[:, i]
        s = np.sqrt(p * (1 - p))
        a0 = np.take(A, 0, axis=ax)
        a1 = np.take(A, 1, axis=ax)
        shp = (B,) + (1,) * (k - 1)
        e = (1 - p).reshape(shp) * a0 + p.reshape(shp) * a1
        o = s.reshape(shp) * (a0 - a1)
        A = np.stack([e, o], axis=ax)
    return A.reshape(B, n)


_SEL = {}


def sel(k):
    if k not in _SEL:
        n = 1 << k
        _SEL[k] = ((np.arange(n)[:, None] >> np.arange(k)[None, :]) & 1).astype(float)
    return _SEL[k]


def stats(vals, P, pot):
    """returns D, W, p_out, It (B,k) for bias rows P"""
    P = np.atleast_2d(np.asarray(P, float))
    B, k = P.shape
    C = spectrum(vals, P)
    pS = C * C
    with np.errstate(divide="ignore", invalid="ignore"):
        Ht = -np.sum(np.where(pS > 0, pS * np.log2(np.where(pS > 0, pS, 1.0)), 0.0), axis=1)
    It = pS @ sel(k)
    p_out = np.clip((1.0 - C[:, 0]) * 0.5, 0.0, 1.0)
    V = 4 * P * (1 - P)
    base = (pot(P) + h2(V)) / V
    D = np.sum(It * base, axis=1) - Ht - pot(p_out)
    W = np.sum(It, axis=1) / 4.0 - p_out * (1 - p_out)
    return D, W, p_out, It


def cG(vals, P, pot, wmin=1e-12):
    D, W, po, It = stats(vals, P, pot)
    return np.where(W > wmin, -D / np.maximum(W, wmin), -1e9), D, W


def maximize_c(vals, pot, p0, iters=4000, step0=1.0, tol=1e-7, wmin=1e-10, rng=None, lo=-30.0, hi=30.0):
    """pattern search in logit_2 coordinates u_i = log2(p_i/(1-p_i)); all 2k moves evaluated in one batch."""
    k = len(p0)
    p0 = np.clip(np.asarray(p0, float), 1e-9, 1 - 1e-9)
    u = np.log2(p0 / (1 - p0))
    def P_of(U):
        return 1.0 / (1.0 + 2.0 ** (-np.clip(U, lo, hi)))
    cur = float(cG(vals, P_of(u)[None, :], pot, wmin)[0][0])
    step = step0
    moves = np.concatenate([np.eye(k), -np.eye(k)])
    it = 0
    while step > tol and it < iters:
        it += 1
        U = u[None, :] + step * moves
        vals_c = cG(vals, P_of(U), pot, wmin)[0]
        j = int(np.argmax(vals_c))
        if vals_c[j] > cur + 1e-15:
            cur = float(vals_c[j]); u = U[j]
            # try to keep going in that direction with a doubled step
            U2 = u[None, :] + 2 * step * moves[j][None, :]
            v2 = float(cG(vals, P_of(U2), pot, wmin)[0][0])
            if v2 > cur:
                cur = v2; u = U2[0]
        else:
            step *= 0.5
    return cur, P_of(u)


def table_from_bits(tt, k):
    n = 1 << k
    return 1.0 - 2.0 * ((np.int64(tt) >> np.arange(n)) & 1).astype(float) if k <= 6 else None


def pm_from_int(tt, k):
    n = 1 << k
    return np.array([1.0 - 2.0 * ((int(tt) >> x) & 1) for x in range(n)])
