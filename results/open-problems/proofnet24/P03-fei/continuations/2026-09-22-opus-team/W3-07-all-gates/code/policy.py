"""Policy check: for a gate G and a potential V (grid G-array), minimise the gate defect

    D_V(G; p) = sum_i w_i (V(p_i) + h(V_i)) - Htilde_G(p) - V(p_out)

over all bias vectors p in (0,1)^k.  D < 0 at p means one composition step with G lowers V at p_out by |D|, i.e. V is not
a fixed point of the value iteration over a gate set containing G.  Search: a curve screen (a common bias b on every
input subset S, the other inputs single variables at 1/2, plus a coarse product grid for k <= 4 and random logit-normal
starts), then a vectorised multi-start pattern search in the coordinates u_i = log2(p_i/(1-p_i)).
"""
import itertools
import numpy as np
import vicore as V


def P_of(U):
    return 1.0 / (1.0 + 2.0 ** (-np.clip(U, -40.0, 40.0)))


def U_of(P):
    P = np.clip(P, 1e-12, 1 - 1e-12)
    return np.log2(P / (1 - P))


def Dfun(tab, k, P, grid, G):
    P = np.ascontiguousarray(P, dtype=float)
    if P.shape[0] * (1 << k) < 2_000_000:
        return V.D_serial(tab, k, P, grid.xs, G, grid.K, grid.sig(G))
    return V.D_batch(tab, k, P, grid.xs, G, grid.K, grid.sig(G))


def pattern_multi(tab, k, grid, G, P0, iters=400, step0=1.0, tol=1e-7, wmin=0.0):
    """vectorised pattern search from each row of P0; returns (D, P, pout, W) at the end points."""
    U = U_of(np.asarray(P0, float))
    ns = U.shape[0]
    D, Wd, po = Dfun(tab, k, P_of(U), grid, G)
    step = np.full(ns, step0)
    moves = np.concatenate([np.eye(k), -np.eye(k)])
    active = np.ones(ns, bool)
    for it in range(iters):
        idx = np.flatnonzero(active & (step > tol))
        if len(idx) == 0:
            break
        UU = (U[idx, None, :] + step[idx, None, None] * moves[None, :, :]).reshape(-1, k)
        Dm, Wm, pm = Dfun(tab, k, P_of(UU), grid, G)
        Dm = Dm.reshape(len(idx), 2 * k)
        j = np.argmin(Dm, axis=1)
        best = Dm[np.arange(len(idx)), j]
        imp = best < D[idx] - 1e-15
        for a in np.flatnonzero(imp):
            s = idx[a]
            U[s] = U[s] + step[s] * moves[j[a]]
            D[s] = best[a]
        for a in np.flatnonzero(~imp):
            step[idx[a]] *= 0.5
    D, Wd, po = Dfun(tab, k, P_of(U), grid, G)
    return D, P_of(U), po, Wd


def curve_starts(tab, k, grid, G, nb=161, maxsub=None, others=(0.5,)):
    """common bias b on each input subset S (others fixed); returns candidate bias vectors sorted by D."""
    bs = P_of(np.linspace(-12, 12, nb))
    rows = []
    subsets = []
    for r in range(1, k + 1):
        if maxsub is not None and r > maxsub:
            break
        subsets.extend(itertools.combinations(range(k), r))
    for oth in others:
        for S in subsets:
            P = np.full((nb, k), oth)
            P[:, list(S)] = bs[:, None]
            rows.append(P)
    P = np.concatenate(rows)
    out = []
    B = 200000
    Ds = np.empty(len(P))
    for s in range(0, len(P), B):
        Ds[s:s + B] = Dfun(tab, k, P[s:s + B], grid, G)[0]
    return P, Ds


def check_gate(tab, k, grid, G, nstart=24, rng=None, nrand=400, grid_vals=(1 / 16, 1 / 4, 3 / 8, 1 / 2, 5 / 8, 3 / 4, 15 / 16),
               maxsub=None, iters=400):
    rng = np.random.default_rng(0) if rng is None else rng
    cands = []
    Pc, Dc = curve_starts(tab, k, grid, G, maxsub=maxsub)
    cands.append((Pc, Dc))
    if k <= 4:
        Pg = np.array(list(itertools.product(grid_vals, repeat=k)), float)
        cands.append((Pg, Dfun(tab, k, Pg, grid, G)[0]))
    Pr = P_of(rng.normal(0, 3.0, (nrand, k)))
    cands.append((Pr, Dfun(tab, k, Pr, grid, G)[0]))
    P = np.concatenate([c[0] for c in cands])
    D = np.concatenate([c[1] for c in cands])
    order = np.argsort(D)
    starts = []
    for i in order:
        if len(starts) >= nstart:
            break
        if all(np.max(np.abs(P[i] - s)) > 0.02 for s in starts):
            starts.append(P[i])
    starts = np.array(starts)
    Df, Pf, pof, Wf = pattern_multi(tab, k, grid, G, starts, iters=iters)
    j = int(np.argmin(Df))
    return dict(D=float(Df[j]), p=Pf[j], pout=float(pof[j]), W=float(Wf[j]), D_all=Df, P_all=Pf, pout_all=pof,
                screen_min=float(D.min()))
