"""Slack value iteration on a two-sided geometric grid (points rho^k and 1 - rho^k plus 1/2), so that on the small-p
side every product of grid points is a grid point (p = rho^a, r = rho^c -> q = rho^(c-a)) and the AND constraints
carry no interpolation error there. Gamma is interpolated linearly in logit(p) elsewhere. Same operator as
fei_readonce_gamma.py. Usage: python -u fei_readonce_gamma_geo.py <per_octave> <octaves> <C or 'bisect'> <tag>
"""
import sys, math, time, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_readonce_gamma import Ht_and, h2

def make_grid(per_octave, octaves, mid_step=0.0005, tail_top=0.02):
    """hybrid: geometric tails (per_octave points per octave from tail_top down to 2^-octaves) on both sides and a
    uniform middle with spacing mid_step; symmetric about 1/2"""
    ks = np.arange(0, per_octave * octaves + 1)
    small = tail_top * 2.0 ** (-ks / per_octave)
    small = small[small >= 2.0 ** -octaves]
    mid = np.arange(tail_top, 0.5 + 1e-12, mid_step)
    pts = np.concatenate([small, mid, 1 - small, 1 - mid, [0.5]])
    pts = np.unique(np.round(pts, 15))
    return pts

def iterate(C, ps, iters=600, tol=1e-11, cap=60.0):
    N = len(ps); i_half = int(np.argmin(np.abs(ps - 0.5)))
    logit = np.log(ps / (1 - ps))
    G = np.full(N, cap); G[i_half] = C
    hV = h2(4 * ps * (1 - ps))
    def interp(Gv, x):
        lx = np.log(x / (1 - x))
        return np.interp(lx, logit, Gv)
    def T(Gv):
        newG = np.full(N, np.inf)
        for i0 in range(0, N, 150):
            i1 = min(N, i0 + 150)
            r = ps[i0:i1][:, None]; p = ps[None, :]
            q = r / p
            valid = (q < 1 - 1e-13) & (q > 1e-13)
            qc = np.clip(q, 1e-13, 1 - 1e-13)
            Gq = interp(Gv, qc)
            rhs = q * (Gv[None, :] + hV[None, :]) + p * (Gq + h2(4 * qc * (1 - qc))) - Ht_and(p, qc)
            rhs = np.where(valid & np.isfinite(rhs), rhs, np.inf)
            newG[i0:i1] = np.min(rhs, axis=1)
        # symmetry (the OR constraints): Gamma(r) = Gamma(1-r); grid is symmetric so reverse the array
        newG = np.minimum(newG, newG[::-1])
        return newG
    for k in range(iters):
        G2 = np.minimum(G, T(G))
        done = np.all(np.abs(G2 - G) < tol)
        G = G2
        if G.min() < -1e-9:
            return False, G
        if done:
            break
    return bool(G.min() >= -1e-9), G

if __name__ == "__main__":
    per, octs, mode, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
    ps = make_grid(per, octs)
    here = os.path.dirname(os.path.abspath(__file__))
    print("grid: %d points, smallest %.2e" % (len(ps), ps.min()), flush=True)
    if mode == "bisect":
        lo, hi = 6.40, 6.60
        for _ in range(16):
            mid = (lo + hi) / 2
            t0 = time.time(); ok, G = iterate(mid, ps)
            print("  C=%.7f %s (%.0f s)" % (mid, "feasible" if ok else "infeasible", time.time() - t0), flush=True)
            if ok: hi = mid
            else: lo = mid
        print("smallest feasible C (per_octave %d, octaves %d): %.7f  [Hod 6.4547837]" % (per, octs, hi), flush=True)
        C = hi
    else:
        C = float(mode)
    ok, G = iterate(C, ps)
    np.save(os.path.join(here, f"gamma_geo_{tag}.npy"), np.stack([ps, G]))
    print("C=%.7f feasible=%s min Gamma %.6f at p=%.3e" % (C, ok, G.min(), ps[np.argmin(G)]), flush=True)
    # asymptotics near 0: Gamma(p)/p against log2(1/p)
    print("edge expansion: p, Gamma, Gamma/p, (Gamma/p - 2(C-4) log2(1/p)) [AND-chain predicts the constant 8 - 8/ln4 = %.5f]" % (8 - 8 / math.log(4)))
    for k in range(1, octs + 1):
        p = 2.0 ** -k; j = int(np.argmin(np.abs(ps - p)))
        print("  p=2^-%2d  Gamma=%.7f  Gamma/p=%.5f  minus 2(C-4)log2(1/p) = %.5f" % (k, G[j], G[j] / ps[j], G[j] / ps[j] - 2 * (C - 4) * k))
    # and at a few non-dyadic small p
    for p in (0.75 * 2 ** -6, 0.6 * 2 ** -8, 0.7 * 2 ** -10):
        j = int(np.argmin(np.abs(ps - p)))
        print("  p=%.3e  Gamma/p=%.5f  minus 2(C-4)log2(1/p) = %.5f" % (ps[j], G[j] / ps[j], G[j] / ps[j] - 2 * (C - 4) * math.log2(1 / ps[j])))
