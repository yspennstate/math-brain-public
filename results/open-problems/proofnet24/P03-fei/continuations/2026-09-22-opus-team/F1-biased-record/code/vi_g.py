"""Value iteration of the slack function over AND, OR, NOT and Numaro's gate g with biased inputs.

V(r) ~ inf{ C I(F) - H(F) : Pr[F] = r }.  Moves:
  read-once: V(pq) <= q (V(p) + h(V_p)) + p (V(q) + h(V_q)) - Ht_AND(p, q), V symmetric (ro_gamma_nb.T_op);
  gate g with the inputs in a set K biased, the others single variables (slack C, V = 1):
      s = sum_{i in K} (It_i/V_i)(V(p_i) + h(V_i)) + C * sum_{l not in K} It_l - Htilde_g(p),
  placed at r = Pr[F true].  For each family (K, solver j) and each output node r, the free biases run over a grid
  and the solver's bias is solved from the (linear in mu_j) output mean so that Pr[F] = r exactly.
The g data (Htilde, It, p) depend only on the biases and are precomputed once per family.
C is beaten by the gate set if the iteration drives V(1/2) below C (then some finite balanced F has s < C).
Usage: python vi_g.py C [families] [npar]
"""
import sys, os, time, math, itertools
import numpy as np
try:
    import psutil
    _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
except Exception:
    pass
from ro_gamma import Grid
import ro_gamma_nb as RB
from compressed import Compressed

HERE = os.path.dirname(os.path.abspath(__file__))


def h2(v):
    v = np.clip(v, 1e-300, 1.0)
    out = np.zeros_like(v)
    m = v < 1.0
    vm = v[m]
    out[m] = -vm * np.log2(vm) - (1 - vm) * np.log2(1 - vm)
    return out


FAMILIES = {
    # name: (K, solver position in K)
    "c": ([0], 0),
    "a": ([9], 0),
    "cc+": ([0, 1], 1),
    "cc-": ([0, 4], 1),
    "ca0": ([0, 9], 1),     # ghat({0,9}) = 0
    "ca-": ([0, 10], 1),
    "ca+": ([0, 11], 1),
    "ac0": ([9, 0], 1),     # same pair, solver on the core input
    "aa1": ([9, 10], 1),
    "aa2": ([9, 11], 1),
}


def build_family(K, jpos, rnodes, free_grid):
    """Configs for every output node r and every choice of the free biases on free_grid (list over free positions)."""
    cm = Compressed(K)
    k = len(K)
    free = [q for q in range(k) if q != jpos]
    # output mean E F = sum_S prod mu ghatK[S]; linear in mu_j: EF = alpha + beta mu_j
    if free:
        grids = np.array(list(itertools.product(*[free_grid] * len(free))))     # (nf, len(free))
    else:
        grids = np.zeros((1, 0))
    nf = len(grids)
    mu_free = 1.0 - 2.0 * grids
    alpha = np.zeros(nf); beta = np.zeros(nf)
    for a in range(1 << k):
        term = np.full(nf, cm.ghatK[a])
        for q in range(k):
            if (a >> q) & 1 and q != jpos:
                term = term * mu_free[:, free.index(q)]
        if (a >> jpos) & 1:
            beta += term
        else:
            alpha += term
    R = len(rnodes)
    target = (1.0 - 2.0 * rnodes)[:, None]                        # (R,1)
    with np.errstate(divide="ignore", invalid="ignore"):
        muj = (target - alpha[None, :]) / beta[None, :]          # (R, nf)
    valid = np.isfinite(muj) & (np.abs(muj) < 1.0 - 1e-9)
    P = np.empty((R, nf, k))
    for q in range(k):
        if q == jpos:
            P[:, :, q] = np.where(valid, (1.0 - muj) / 2.0, 0.5)
        else:
            P[:, :, q] = grids[None, :, free.index(q)]
    rr, ff = np.nonzero(valid)
    Pv = P[rr, ff]
    out = {"r_idx": rr, "p": Pv}
    # evaluate in chunks
    Ht = np.empty(len(rr)); It = np.empty((len(rr), k)); Ir = np.empty(len(rr)); po = np.empty(len(rr))
    B = 20000
    for s in range(0, len(rr), B):
        e = cm.evaluate(Pv[s:s + B])
        Ht[s:s + B] = e["Ht"]; It[s:s + B] = e["It"]; Ir[s:s + B] = e["Irest"]; po[s:s + B] = e["pout"]
    err = np.abs(po - rnodes[rr]).max() if len(rr) else 0.0
    out.update(Ht=Ht, It=It, Irest=Ir, pout_err=err, K=K)
    return out


def g_move(fam, gam_fn, C, nR):
    p = fam["p"]
    V = 4 * p * (1 - p)
    cost = (fam["It"] / V * (gam_fn(p) + h2(V))).sum(axis=1) + C * fam["Irest"] - fam["Ht"]
    best = np.full(nR, np.inf)
    np.minimum.at(best, fam["r_idx"], cost)
    return best, cost


def run(C, fam_names, npar=128, iters=400, tol=1e-12, verbose=True, M=24, K=40, G0=None, save=None):
    grid = Grid(M, K)
    ps = grid.ps; N = len(ps)
    rs = np.concatenate([ps, 1 - ps[1:]])                     # all output nodes: small side then mirrors
    free_grid = (np.arange(1, npar) / npar)
    fams = {}
    t0 = time.time()
    for nm in fam_names:
        Kf, jpos = FAMILIES[nm]
        # only nodes the family can reach (the solver needs |mu_j|<1); build on all rs, invalid ones dropped
        fams[nm] = build_family(Kf, jpos, rs, free_grid)
        if verbose:
            print("family %-4s K=%s: %d configs, max |pout - r| = %.1e (%.0f s)" % (nm, Kf, len(fams[nm]["r_idx"]), fams[nm]["pout_err"], time.time() - t0), flush=True)
    if G0 is None:
        Gam = np.full(N, 60.0); Gam[0] = C
    else:
        Gam = G0 * ps
    G = Gam / ps
    hist = []
    for it in range(iters):
        gam_fn = lambda q: grid.gamma_at(G, q)
        Tv = RB.T_op(grid.xs, G, float(grid.K), rs, grid.all_p, grid.Lall)
        src = np.zeros(len(rs), dtype=int)
        for fi, nm in enumerate(fam_names):
            b, _ = g_move(fams[nm], gam_fn, C, len(rs))
            better = b < Tv
            src[better] = fi + 1
            Tv = np.minimum(Tv, b)
        Ts = Tv[:N].copy(); Ts[1:] = np.minimum(Ts[1:], Tv[N:])
        Gam2 = np.minimum(Gam, Ts)
        diff = np.max(np.abs(Gam2 - Gam) / ps)
        Gam = Gam2; G = Gam / ps
        hist.append((it, Gam[0], Gam.min()))
        if verbose and (it % 10 == 0 or diff < tol):
            print("  iter %4d  max dG %.3e  min V %.4e  V(1/2) - C = %+.3e  (%.0f s)" % (it, diff, Gam.min(), Gam[0] - C, time.time() - t0), flush=True)
        if Gam.min() < -1e-9 or Gam[0] < C - 1e-9:
            if verbose:
                print("  DIVERGES: V(1/2) - C = %+.3e, min V = %.3e at iter %d" % (Gam[0] - C, Gam.min(), it), flush=True)
            if save:
                np.savez(save, xs=grid.xs, G=G, C=C, M=M, K=K)
            return False, G, grid, fams
        if diff < tol:
            break
    if save:
        np.savez(save, xs=grid.xs, G=G, C=C, M=M, K=K)
    return True, G, grid, fams


if __name__ == "__main__":
    C = float(sys.argv[1])
    names = sys.argv[2].split(",") if len(sys.argv) > 2 else list(FAMILIES)
    npar = int(sys.argv[3]) if len(sys.argv) > 3 else 128
    tag = sys.argv[4] if len(sys.argv) > 4 else None
    save = os.path.join(HERE, "..", "logs", "vig_%s.npz" % tag) if tag else None
    ok, G, grid, fams = run(C, names, npar=npar, save=save)
    print("C = %.12f  families %s  npar %d:  %s" % (C, names, npar, "no divergence (C not beaten)" if ok else "DIVERGES (C beaten)"))
    for p in (0.5, 0.4995, 0.499, 0.495, 0.49, 0.48, 0.45, 0.4, 0.35, 0.3, 0.25):
        print("  V(%.4f) = %.10f" % (p, float(grid.gamma_at(G, np.array([p]))[0])))
