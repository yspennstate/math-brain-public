"""Numba version of the read-once value iteration in ro_gamma.py (same grid, same operator, same interpolation).

Usage: python ro_gamma_nb.py C tag [M K iters]
"""
import sys, os, time, math
import numpy as np
import numba as nb
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
nb.set_num_threads(2)
from ro_gamma import Grid

LN2 = math.log(2.0)
HERE = os.path.dirname(os.path.abspath(__file__))


@nb.njit(cache=True)
def psi_s(z):
    if z > 0.5:
        zz = 1.0 - z
        return psi_s(zz) * zz / z
    if z <= 0.25:
        u = 2.0 * z
        return (4.0 / LN2) * (1.0 - u) ** 2 * (-math.log1p(-u) / u)
    w = (1.0 - 2.0 * z) ** 2
    if w <= 0.0:
        return 0.0
    return -w * math.log2(w) / z


@nb.njit(cache=True)
def gam_s(xs, G, K, sig, q):
    small = q if q < 1.0 - q else 1.0 - q
    x = math.log2(1.0 / small)
    if x >= K:
        return small * (G[-1] + (x - K) * sig)
    if x <= xs[0]:
        return small * G[0]
    j = np.searchsorted(xs, x) - 1
    if j < 0:
        j = 0
    if j >= len(xs) - 1:
        j = len(xs) - 2
    t = (x - xs[j]) / (xs[j + 1] - xs[j])
    return small * ((1.0 - t) * G[j] + t * G[j + 1])


@nb.njit(parallel=True, cache=True)
def T_op(xs, G, K, rs, allp, Lall):
    sig = (G[-1] - G[-2]) / (xs[-1] - xs[-2])
    if sig < 0.0:
        sig = 0.0
    nA = len(allp)
    GamA = np.empty(nA)
    psiA = np.empty(nA)
    for a in range(nA):
        GamA[a] = gam_s(xs, G, K, sig, allp[a])
        psiA[a] = psi_s(allp[a])
    out = np.empty(len(rs))
    for k in nb.prange(len(rs)):
        r = rs[k]
        best = np.inf
        psir = psi_s(r)
        for a in range(nA):
            p = allp[a]
            if p <= r:
                continue
            q = r / p
            if q >= 1.0 - 1e-15:
                continue
            Lq = math.log2(1.0 / q)
            Gq = gam_s(xs, G, K, sig, q)
            E = 8 * p * (1 - q) * Lall[a] + 8 * q * (1 - p) * Lq + 8 * (1 - p) * (1 - q) + psir - psiA[a] - psi_s(q)
            v = q * GamA[a] + p * Gq - p * q * E
            if v < best:
                best = v
        out[k] = best
    return out


def iterate(grid, C, iters=3000, tol=1e-11, cap=60.0, verbose=True, G0=None):
    ps = grid.ps
    N = len(ps)
    if G0 is None:
        Gam = np.full(N, cap); Gam[0] = C
    else:
        Gam = G0 * ps
    G = Gam / ps
    rs = np.concatenate([ps, 1 - ps[1:]])
    t0 = time.time()
    for k in range(iters):
        Tv = T_op(grid.xs, G, float(grid.K), rs, grid.all_p, grid.Lall)
        Ts = Tv[:N].copy(); Ts[1:] = np.minimum(Ts[1:], Tv[N:])
        Gam2 = np.minimum(Gam, Ts)
        diff = np.max(np.abs(Gam2 - Gam) / ps)
        Gam = Gam2; G = Gam / ps
        if verbose and (k % 20 == 0 or diff < tol):
            print("  iter %4d  max dG %.3e  min Gamma %.4e  Gamma(1/2) %.12f  (%.0f s)" % (k, diff, Gam.min(), Gam[0], time.time() - t0), flush=True)
        if Gam.min() < -1e-9:
            return False, G
        if diff < tol:
            break
    return bool(Gam.min() >= -1e-9), G


if __name__ == "__main__":
    C = float(sys.argv[1]); tag = sys.argv[2]
    M = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    iters = int(sys.argv[5]) if len(sys.argv) > 5 else 3000
    grid = Grid(M, K)
    print("Gamma_RO at C=%.15f: %d nodes, %d factor points" % (C, len(grid.ps), len(grid.all_p)), flush=True)
    ok, G = iterate(grid, C, iters=iters)
    out = os.path.join(HERE, "..", "logs", "ro_gamma_%s.npz" % tag)
    np.savez(out, xs=grid.xs, G=G, C=C, M=M, K=K)
    print("feasible=%s  saved %s" % (ok, out))
    for p in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.48, 0.45, 0.4, 3 / 8, 0.35, 1 / 3, 0.3, 0.25, 0.2, 0.125, 0.1, 0.05, 1 / 32, 0.01, 1e-3):
        print("  Gamma(%.6f) = %.10f" % (p, float(grid.gamma_at(G, np.array([p]))[0])))
