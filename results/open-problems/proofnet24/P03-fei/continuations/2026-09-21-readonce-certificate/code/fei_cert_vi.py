"""Value iteration for the read-once FEI slack on the CERTIFICATE grid.

Representation: on the small side p <= 1/2 write p = 2^-x, x >= 1, and G(x) = Gamma(p)/p; nodes x_j = 1 + j/M,
j = 0..(K-1)M (so every dyadic 2^-k, k <= K, is a node); G is linear in x between nodes; beyond x = K the tail
G(x) = G_J + (x - K) * sigma_last.  Gamma(1-p) = Gamma(p).  The operator T Gamma(r) = min over r = p q of
q Gamma(p) + p Gamma(q) - p q E(p,q), E(p,q) = 8p(1-q)L(p) + 8q(1-p)L(q) + 8(1-p)(1-q) + Psi(pq) - Psi(p) - Psi(q),
L = log2(1/.), Psi(z) = phi((1-2z)^2)/z (computed in a cancellation-free form), which equals the right-hand side
of (A) in THEOREM_NOTE.md.  Iterate Gamma <- min(Gamma, T Gamma) from the cap Gamma(1/2) = C, 60 elsewhere.
Usage: python -u fei_cert_vi.py <M> <K> <C> <tag> [iters]
"""
import sys, os, time, math
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
LN2 = math.log(2.0)

def ell(u):
    """-log(1-u)/u, u in (0,1)"""
    return -np.log1p(-u) / u

def psi(z):
    """phi((1-2z)^2)/z for z in (0,1), phi(w) = w log2(1/w); accurate for small z (ell form)"""
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    a = z <= 0.25
    out[a] = (4.0 / LN2) * (1 - 2 * z[a]) ** 2 * ell(2 * z[a])
    b = (~a) & (z <= 0.5)
    w = (1 - 2 * z[b]) ** 2
    with np.errstate(divide="ignore", invalid="ignore"):
        out[b] = np.where(w > 0, -w * np.log2(np.maximum(w, 1e-300)), 0.0) / z[b]
    c = z > 0.5
    if c.any():
        zz = 1 - z[c]
        out[c] = psi(zz) * zz / z[c]
    return out

def E_fun(p, q, Lp, Lq):
    return 8 * p * (1 - q) * Lp + 8 * q * (1 - p) * Lq + 8 * (1 - p) * (1 - q) + psi(p * q) - psi(p) - psi(q)

class Grid:
    def __init__(self, M, K):
        self.M, self.K = M, K
        # hybrid node set: uniform step 2^-11 in p on [2^-5, 1/2], then M nodes per octave down to 2^-K (dyadics included)
        mid = np.arange(64, 1024 + 1) / 2048.0
        tail = 2.0 ** (-(5 + np.arange(1, (K - 5) * M + 1) / M))
        self.ps = np.unique(np.concatenate([mid, tail]))[::-1]   # 1/2 down to 2^-K, decreasing
        self.xs = np.log2(1 / self.ps)                            # increasing from 1 to K
        self.xs[0] = 1.0; self.xs[-1] = float(K)
        self.all_p = np.concatenate([self.ps, 1 - self.ps[:-0 or None]])  # both sides (1-ps includes 1/2 twice; harmless)
        self.all_p = np.unique(self.all_p)
        self.Lall = np.log2(1 / self.all_p)
        self.psi_all = psi(self.all_p)

    def gamma_at(self, G, q):
        """Gamma(q) for arbitrary q in (0,1) from small-side node values G (Gamma/p at nodes)"""
        q = np.asarray(q, dtype=float)
        small = np.minimum(q, 1 - q)
        x = np.log2(1 / np.maximum(small, 1e-300))
        xs, K = self.xs, self.K
        inside = x <= K
        Gq = np.empty_like(x)
        Gq[inside] = np.interp(x[inside], xs, G)
        sig = max((G[-1] - G[-2]) / (xs[-1] - xs[-2]), 0.0)   # the tail extrapolation never turns downward
        Gq[~inside] = G[-1] + (x[~inside] - K) * sig
        return small * Gq

def iterate(grid, C, iters=2000, tol=1e-12, cap=60.0, verbose=True):
    xs, ps, M = grid.xs, grid.ps, grid.M
    N = len(ps)
    Gam = np.full(N, cap); Gam[0] = C            # Gamma at small-side nodes; node 0 is p = 1/2
    G = Gam / ps
    allp, Lall, psi_all = grid.all_p, grid.Lall, grid.psi_all
    Gam_all = grid.gamma_at(G, allp)
    rs = np.concatenate([ps, 1 - ps[1:]])        # LHS points r on both sides
    def T(G):
        Gam_all = grid.gamma_at(G, allp)
        Tvals = np.full(len(rs), np.inf)
        B = 64
        for i0 in range(0, len(rs), B):
            r = rs[i0:i0 + B][:, None]; p = allp[None, :]
            q = r / p
            valid = (q < 1 - 1e-15) & (q > 1e-300)
            qc = np.where(valid, q, 0.5)
            Lq = np.log2(1 / qc)
            Gq = grid.gamma_at(G, qc)
            rhs = qc * Gam_all[None, :] + p * Gq - p * qc * E_fun(p, qc, Lall[None, :], Lq)
            rhs = np.where(valid, rhs, np.inf)
            Tvals[i0:i0 + B] = rhs.min(axis=1)
        # symmetrise: Gamma(r) = Gamma(1-r): small-side value = min of T at r and at 1-r
        Tsmall = Tvals[:N].copy(); Tsmall[1:] = np.minimum(Tsmall[1:], Tvals[N:])
        return Tsmall
    t0 = time.time()
    for k in range(iters):
        Gam2 = np.minimum(Gam, T(G))
        diff = np.max(np.abs(Gam2 - Gam) / ps)     # in G units
        Gam = Gam2; G = Gam / ps
        if verbose and (k % 25 == 0 or diff < tol):
            print("  iter %4d  max dG %.3e  min Gamma %.3e  (%.0f s)" % (k, diff, Gam.min(), time.time() - t0), flush=True)
        if Gam.min() < -1e-9:
            return False, G
        if diff < tol:
            break
    return bool(Gam.min() >= -1e-9), G

if __name__ == "__main__":
    M, K, C, tag = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    iters = int(sys.argv[5]) if len(sys.argv) > 5 else 2000
    grid = Grid(M, K)
    print("certificate grid M=%d K=%d: %d small-side nodes, %d factor points; C=%.7f" % (M, K, len(grid.ps), len(grid.all_p), C), flush=True)
    ok, G = iterate(grid, C, iters=iters)
    here = os.path.dirname(os.path.abspath(__file__))
    np.savez(os.path.join(here, "cert_vi_%s.npz" % tag), xs=grid.xs, G=G, C=C, M=M, K=K)
    alpha = 2 * (C - 4); w = G - alpha * grid.xs
    print("feasible=%s  min Gamma %.3e; wobble G - 2(C-4)x: min %.5f max %.5f, at x=K: %.5f (b* = %.5f)" % (ok, (G * grid.ps).min(), w.min(), w.max(), w[-1], 8 - 4 / LN2), flush=True)
    for k in (1, 2, 3, 4, 6, 8, 10, 14, 20, 30, K):
        j = int(np.argmin(np.abs(grid.xs - k)))
        print("  wobble at 2^-%d: %.6f (node x=%.4f)" % (k, w[j], grid.xs[j]))
    print("G increasing everywhere: %s (min increment %.3e)" % (bool(np.all(np.diff(G) > 0)), np.diff(G).min()))
