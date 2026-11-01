"""Read-once slack function Gamma_RO,C(p) = inf{ C I(f) - H(f) : f read-once AND/OR/NOT, Pr[f] = p } by value iteration.

Representation and operator as in continuations/2026-09-21-readonce-certificate/code/fei_cert_vi.py (copied here so the
folder is self-contained): on p <= 1/2 write x = log2(1/p), G(x) = Gamma(p)/p, piecewise linear in x through the nodes
(uniform step 2^-11 in p on [1/32, 1/2], M nodes per octave below, down to 2^-K), Gamma(1-p) = Gamma(p).
T Gamma(r) = min over r = p q of q Gamma(p) + p Gamma(q) - p q E(p, q), which equals
q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q).  Iterate Gamma <- min(Gamma, T Gamma) from the cap
Gamma(1/2) = C (one variable), 60 elsewhere.
Usage: python ro_gamma.py C tag [M K iters]
"""
import sys, os, time, math
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
LN2 = math.log(2.0)
HERE = os.path.dirname(os.path.abspath(__file__))


def ell(u):
    return -np.log1p(-u) / u


def psi(z):
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
    def __init__(self, M=24, K=40):
        self.M, self.K = M, K
        mid = np.arange(64, 1024 + 1) / 2048.0
        tail = 2.0 ** (-(5 + np.arange(1, (K - 5) * M + 1) / M))
        self.ps = np.unique(np.concatenate([mid, tail]))[::-1]
        self.xs = np.log2(1 / self.ps)
        self.xs[0] = 1.0; self.xs[-1] = float(K)
        self.all_p = np.unique(np.concatenate([self.ps, 1 - self.ps]))
        self.Lall = np.log2(1 / self.all_p)

    def gamma_at(self, G, q):
        q = np.asarray(q, dtype=float)
        small = np.minimum(q, 1 - q)
        x = np.log2(1 / np.maximum(small, 1e-300))
        xs, K = self.xs, self.K
        inside = x <= K
        Gq = np.empty_like(x)
        Gq[inside] = np.interp(x[inside], xs, G)
        sig = max((G[-1] - G[-2]) / (xs[-1] - xs[-2]), 0.0)
        Gq[~inside] = G[-1] + (x[~inside] - K) * sig
        return small * Gq


def iterate(grid, C, iters=2000, tol=1e-11, cap=60.0, verbose=True):
    ps = grid.ps
    N = len(ps)
    Gam = np.full(N, cap); Gam[0] = C
    G = Gam / ps
    allp, Lall = grid.all_p, grid.Lall
    rs = np.concatenate([ps, 1 - ps[1:]])

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
        Tsmall = Tvals[:N].copy(); Tsmall[1:] = np.minimum(Tsmall[1:], Tvals[N:])
        return Tsmall

    t0 = time.time()
    for k in range(iters):
        Gam2 = np.minimum(Gam, T(G))
        diff = np.max(np.abs(Gam2 - Gam) / ps)
        Gam = Gam2; G = Gam / ps
        if verbose and (k % 10 == 0 or diff < tol):
            print("  iter %4d  max dG %.3e  min Gamma %.4e  Gamma(1/2) %.10f  (%.0f s)" % (k, diff, Gam.min(), Gam[0], time.time() - t0), flush=True)
        if Gam.min() < -1e-9:
            return False, G
        if diff < tol:
            break
    return bool(Gam.min() >= -1e-9), G


def load_gamma(path):
    """Return a callable Gamma(p) (vectorised) from a saved npz."""
    d = np.load(path)
    M, K = int(d["M"]), int(d["K"])
    grid = Grid(M, K)
    assert np.allclose(grid.xs, d["xs"])
    G = d["G"]
    return (lambda q: grid.gamma_at(G, q)), float(d["C"])


if __name__ == "__main__":
    C = float(sys.argv[1]); tag = sys.argv[2]
    M = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    iters = int(sys.argv[5]) if len(sys.argv) > 5 else 3000
    grid = Grid(M, K)
    print("Gamma_RO at C=%.12f: %d nodes, %d factor points" % (C, len(grid.ps), len(grid.all_p)), flush=True)
    ok, G = iterate(grid, C, iters=iters)
    out = os.path.join(HERE, "..", "logs", "ro_gamma_%s.npz" % tag)
    np.savez(out, xs=grid.xs, G=G, C=C, M=M, K=K)
    Gam = G * grid.ps
    print("feasible=%s  saved %s" % (ok, out))
    for p in (0.5, 0.49, 0.48, 0.45, 0.4, 3 / 8, 0.35, 1 / 3, 0.3, 0.25, 0.2, 0.125, 0.1, 0.05, 1 / 32, 0.01, 1e-3):
        print("  Gamma(%.6f) = %.8f" % (p, float(grid.gamma_at(G, np.array([p]))[0])))
