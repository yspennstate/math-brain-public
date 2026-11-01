"""Value iteration with, in addition to the vi_g families, 'full' g-families in which all 9 core inputs share one bias
(the solver, chosen so that Pr[F] lands exactly on a node) and all 9 auxiliary inputs share a bias from a small grid.
E F(mu_c, mu_a) = sum_{k,l} A[k,l] mu_c^k mu_a^l with A[k,l] = sum of ghat(S u B) over core S (|S| = k), aux B (|B| = l).
Every configuration is evaluated with the full biased transform (gate.evaluate).
Usage: python vi_full.py C tag [npar] [auxgrid] [rlo rhi]
"""
import sys, os, time
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from ro_gamma import Grid
import ro_gamma_nb as RB
from vi_g import FAMILIES, build_family, g_move, h2
from gate import load_table, biased_spectrum, N
import fast_gate
def evaluate(tab, p):
    Ht, It, po, _ = fast_gate.evaluate(p)
    return Ht, It, po

HERE = os.path.dirname(os.path.abspath(__file__))
TAB = load_table()


def ef_table():
    c = biased_spectrum(TAB, [0.5] * N)
    idx = np.arange(1 << N)
    kc = np.array([bin(x & 511).count("1") for x in idx]); ka = np.array([bin(x >> 9).count("1") for x in idx])
    A = np.zeros((10, 10))
    np.add.at(A, (kc, ka), c)
    return A


def solve_muc(A, target, mua):
    """E F(mu_c, mu_a) = target; E F is increasing in mu_c (monotone g); bisection on (-1, 1)."""
    powa = mua ** np.arange(10)
    coef = A @ powa                         # polynomial in mu_c
    f = lambda m: np.polyval(coef[::-1], m) - target
    lo, hi = -1.0, 1.0
    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def build_full(rnodes, ridx, aux_grid):
    A = ef_table()
    P, R, Ht, It = [], [], [], []
    for mua in aux_grid:
        for r, k in zip(rnodes, ridx):
            m = solve_muc(A, 1.0 - 2.0 * r, mua)
            if m is None or abs(m) > 0.999:
                continue
            p = np.array([(1 - m) / 2] * 9 + [(1 - mua) / 2] * 9)
            ht, it, po = evaluate(TAB, p)
            assert abs(po - r) < 1e-9, (po, r)
            P.append(p); R.append(k); Ht.append(ht); It.append(it)
    return {"p": np.array(P), "r_idx": np.array(R), "Ht": np.array(Ht), "It": np.array(It)}


def full_move(fam, gam_fn, nR):
    p = fam["p"]; V = 4 * p * (1 - p)
    cost = (fam["It"] / V * (gam_fn(p.ravel()).reshape(p.shape) + h2(V.ravel()).reshape(p.shape))).sum(axis=1) - fam["Ht"]
    best = np.full(nR, np.inf)
    np.minimum.at(best, fam["r_idx"], cost)
    return best


def run(C, pair_names, npar, aux_grid, rlo, rhi, tag, iters=400, tol=1e-12):
    grid = Grid(24, 40); ps = grid.ps; Nn = len(ps)
    rs = np.concatenate([ps, 1 - ps[1:]])
    t0 = time.time()
    fams = {nm: build_family(FAMILIES[nm][0], FAMILIES[nm][1], rs, np.arange(1, npar) / npar) for nm in pair_names}
    sel = np.nonzero((rs >= rlo) & (rs <= rhi))[0]
    full = build_full(rs[sel], sel, aux_grid)
    print("full family: %d configs over %d nodes in [%.3f, %.3f], aux grid %s (%.0f s)" % (len(full["r_idx"]), len(sel), rlo, rhi, aux_grid, time.time() - t0), flush=True)
    Gam = np.full(Nn, 60.0); Gam[0] = C; G = Gam / ps
    for it in range(iters):
        gam_fn = lambda q: grid.gamma_at(G, q)
        Tv = RB.T_op(grid.xs, G, float(grid.K), rs, grid.all_p, grid.Lall)
        for nm in pair_names:
            b, _ = g_move(fams[nm], gam_fn, C, len(rs)); Tv = np.minimum(Tv, b)
        bf = full_move(full, gam_fn, len(rs))
        nfull = int((bf < Tv - 1e-13).sum())
        Tv = np.minimum(Tv, bf)
        Ts = Tv[:Nn].copy(); Ts[1:] = np.minimum(Ts[1:], Tv[Nn:])
        Gam2 = np.minimum(Gam, Ts)
        diff = np.max(np.abs(Gam2 - Gam) / ps); Gam = Gam2; G = Gam / ps
        if it % 10 == 0 or diff < tol:
            print("  iter %3d  max dG %.2e  V(1/2) - C = %+.3e  nodes won by full family %d  (%.0f s)" % (it, diff, Gam[0] - C, nfull, time.time() - t0), flush=True)
        if Gam[0] < C - 1e-9 or Gam.min() < -1e-9:
            print("DIVERGES: V(1/2) - C = %+.3e" % (Gam[0] - C), flush=True); break
        if diff < tol:
            print("converged, V(1/2) = C", flush=True); break
    np.savez(os.path.join(HERE, "..", "logs", "vig_%s.npz" % tag), xs=grid.xs, G=G, C=C, M=24, K=40)
    return G, grid


if __name__ == "__main__":
    C = float(sys.argv[1]); tag = sys.argv[2]
    npar = int(sys.argv[3]) if len(sys.argv) > 3 else 64
    aux_grid = [float(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else [0.0]
    rlo = float(sys.argv[5]) if len(sys.argv) > 5 else 0.3
    rhi = float(sys.argv[6]) if len(sys.argv) > 6 else 0.7
    G, grid = run(C, list(FAMILIES), npar, aux_grid, rlo, rhi, tag)
    for q in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.485, 0.48, 0.47, 0.45, 0.4):
        print("  V(%.4f) - C = %+.6e" % (q, grid.gamma_at(G, np.array([q]))[0] - C))
