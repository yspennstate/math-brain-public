"""Referee checks of SEL-9 (C1 for affine partitions, real leaves), SEL-10 (correlation-gap closure) and
SEL-11 (reverse uncertainty for cell-constant functions).

Part A (exhaustive, total variables <= 4): every affine partition of F_2^a and every assignment of Boolean
        leaves on n = 4-a data bits (a = 1, 2, 3), plus a = 4 with constant +-1 leaves (ACKSW case).
Part B: a = 3 (all 912 partitions) with random Boolean leaves on n = 2, 3; a = 4, 5 random affine partitions.
Part C: real leaves of random norms (SEL-9 weighted form), constant real leaves (SEL-11).
Part D: adversarial optimisation of real leaves on irreducible partitions (try to break SEL-9).
SEL-10 is checked on every Boolean instance with delta > 0.
"""
import itertools
import math
import sys
import numpy as np
from affine import affine_partitions, random_affine_partition, reducible, labels, codim, support_coords
from rlib import wht, ent, popcount_table, h2

rng = np.random.default_rng(99)
WORST = {}
COUNT = {}


def rec(name, v, info=None):
    COUNT[name] = COUNT.get(name, 0) + 1
    if name not in WORST or v > WORST[name][0]:
        WORST[name] = (float(v), info)


def part_info(cells, a):
    p = np.array([len(c) / (1 << a) for c in cells])
    c = np.array([codim(cl, a) for cl in cells])
    r = np.array([support_coords(cl, a) for cl in cells])
    L = labels(cells, a)
    N = 1 << a
    adj = set()
    for x in range(N):
        for i in range(a):
            y = x ^ (1 << i)
            if L[x] != L[y]:
                adj.add((min(L[x], L[y]), max(L[x], L[y])))
    return p, c, r, L, sorted(adj)


def batch_boolean(cells, a, n, leaves, label):
    """leaves: (B, K, D) int +-1."""
    p, c, r, L, adj = part_info(cells, a)
    B, K, Dn = leaves.shape
    N = 1 << a
    F = leaves[:, L, :]                         # (B, N, D)
    F = F.transpose(0, 2, 1).reshape(B, -1)     # index x + N*y
    W = wht(F)
    P = W.astype(np.float64) ** 2 / float((N * Dn) ** 2)
    HF = ent(P)
    pc = popcount_table(a + n)
    IF = (P * pc[None, :]).sum(axis=1)
    Wl = wht(leaves)                            # (B, K, D)
    Pl = Wl.astype(np.float64) ** 2 / float(Dn * Dn)
    Hl = ent(Pl, axis=2)
    Il = (Pl * popcount_table(n)[None, None, :]).sum(axis=2) if n > 0 else np.zeros((B, K))
    rhs = 2 * (p * c).sum() + (Hl * p[None, :]).sum(axis=1)
    v = HF - rhs
    rec("SEL9 Boolean: H(F) - [2 sum p c + sum p H(g)]", v.max(), label)
    # SEL-10
    idx = np.arange(N * Dn)
    Fsel = F.reshape(B, Dn, N)
    Isel = np.zeros(B)
    for i in range(a):
        Isel += (Fsel != Fsel[:, :, np.arange(N) ^ (1 << i)]).mean(axis=(1, 2))
    if adj:
        corr = np.stack([(leaves[:, j, :] * leaves[:, l, :]).mean(axis=1) for j, l in adj], axis=1)
        delta = 1 - corr.max(axis=1)
    else:
        delta = np.full(B, np.inf)
    lowI = (delta / 2) * (p * r).sum()
    ok = np.isfinite(delta)
    if ok.any():
        rec("SEL10 (delta/2) sum p r - I_sel", (lowI - Isel)[ok].max(), label)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(Il > 1e-12, Hl / np.where(Il > 1e-12, Il, 1), 0.0)
    C = ratio.max(axis=1)
    good = ok & (delta > 1e-12)
    if good.any():
        K10 = np.maximum(4 / delta[good], C[good])
        rec("SEL10 H(F) - max(4/delta, C) I(F)", (HF[good] - K10 * IF[good]).max(), label)
        # strong form for balanced leaves
        bal = (np.abs(leaves.sum(axis=2)) == 0).all(axis=1) & good
        if bal.any():
            with np.errstate(divide="ignore", invalid="ignore"):
                rs = np.where(Il - 1 > 1e-12, Hl / np.where(Il - 1 > 1e-12, Il - 1, 1), 0.0)
            Cg = rs.max(axis=1)
            K10s = np.maximum(4 / delta[bal], Cg[bal])
            rec("SEL10 strong H(F) - max(4/delta,Cg)(I(F)-1)", (HF[bal] - K10s * (IF[bal] - 1)).max(), label)
    return B


def all_leaf_assignments(K, n, cap=70000):
    funcs = 1 - 2 * ((np.arange(1 << (1 << n))[:, None] >> np.arange(1 << n)[None, :]) & 1)  # all tables
    M = funcs.shape[0]
    total = M ** K
    if total <= cap:
        idx = np.array(list(itertools.product(range(M), repeat=K)))
    else:
        idx = rng.integers(0, M, size=(cap, K))
    return funcs[idx], total <= cap


def partA():
    tot = 0
    exhaustive_flags = []
    for a in (1, 2, 3):
        n = 4 - a
        parts = affine_partitions(a)
        for cells in parts:
            K = len(cells)
            leaves, exh = all_leaf_assignments(K, n)
            exhaustive_flags.append(exh)
            for s in range(0, len(leaves), 20000):
                tot += batch_boolean(cells, a, n, leaves[s:s + 20000].astype(np.int64), ("A", a, n))
    # a = 4, constant leaves (ACKSW): random partitions, all sign patterns up to cap
    for t in range(60):
        cells = random_affine_partition(4, rng)
        K = len(cells)
        leaves, exh = all_leaf_assignments(K, 0, cap=4096)
        tot += batch_boolean(cells, 4, 0, leaves.astype(np.int64), ("A4const",))
    print("Part A instances:", tot, " (every partition with a<=3 fully enumerated:", all(exhaustive_flags), ")", flush=True)


def partB():
    tot = 0
    parts3 = affine_partitions(3)
    for n in (2, 3):
        for cells in parts3:
            K = len(cells)
            leaves, _ = all_leaf_assignments(K, n, cap=300)
            tot += batch_boolean(cells, 3, n, leaves.astype(np.int64), ("B", 3, n))
    for a, n, reps in ((4, 2, 300), (4, 3, 200), (5, 2, 60)):
        for t in range(reps):
            cells = random_affine_partition(a, rng)
            K = len(cells)
            # mixtures: random leaves, near-copies, orthogonal-ish
            funcs = rng.choice([-1, 1], size=(40, K, 1 << n))
            base = rng.choice([-1, 1], size=(1, 1, 1 << n))
            near = np.where(rng.random((40, K, 1 << n)) < 0.15, -base, base)
            leaves = np.concatenate([funcs, near], axis=0).astype(np.int64)
            tot += batch_boolean(cells, a, n, leaves, ("B", a, n, "irr" if not reducible(cells, a) else "pdt"))
    print("Part B instances:", tot, flush=True)


def real_instance(cells, a, n, G):
    """G: (K, D) real leaves (any norms). Normalise sum p_j l_j = 1. Return H(Fhat^2) - RHS of SEL-9."""
    p, c, r, L, adj = part_info(cells, a)
    N = 1 << a
    Dn = 1 << n
    l = (G ** 2).mean(axis=1)
    s = (p * l).sum()
    G = G / math.sqrt(s)
    l = l / s
    w = p * l
    F = G[L, :].T.reshape(-1)
    W = wht(F) / float(N * Dn)
    P = W ** 2
    HF = float(ent(P))
    Wg = wht(G) / float(Dn)
    Lam = (Wg ** 2) / l[:, None]
    rhs = float(ent(w)) + float((w * c).sum()) + float((w * ent(Lam, axis=1)).sum())
    return HF - rhs, float(P.sum())


def partC():
    tot = 0
    parts3 = affine_partitions(3)
    for cells in parts3:
        for n in (1, 2, 3):
            for rep in range(3):
                K = len(cells)
                G = rng.normal(size=(K, 1 << n)) * rng.exponential(size=(K, 1))
                v, norm = real_instance(cells, 3, n, G)
                rec("SEL9 real: H - [H(w)+sum w c+sum w H(Lam)]", v, ("C", 3, n))
                rec("SEL9 real: |sum Fhat^2 - 1|", abs(norm - 1), ("C", 3, n))
                tot += 1
    for a in (4, 5):
        for t in range(150):
            cells = random_affine_partition(a, rng)
            K = len(cells)
            for n in (0, 2, 3):
                G = rng.normal(size=(K, 1 << n)) * rng.exponential(size=(K, 1))
                if rng.random() < 0.3:                     # sparse-ish coherent leaves
                    G = G * (rng.random(G.shape) < 0.3)
                    G[:, 0] += 1e-3
                v, norm = real_instance(cells, a, n, G)
                rec("SEL9 real: H - [H(w)+sum w c+sum w H(Lam)]", v, ("C", a, n))
                tot += 1
                if n == 0:
                    # SEL-11: H(Psihat^2) + H(r) <= a + 2H(w)
                    p, c, r_, L, adj = part_info(cells, a)
                    vals = G[:, 0]
                    l = vals ** 2
                    s = (p * l).sum()
                    Psi = vals[L] / math.sqrt(s)
                    N = 1 << a
                    Ph = (wht(Psi) / N) ** 2
                    rpt = Psi ** 2 / N
                    w = p * l / s
                    rec("SEL11 H(Psihat^2)+H(r)-a-2H(w)", float(ent(Ph) + ent(rpt) - a - 2 * ent(w)), ("C11", a))
                    # identity H(r) = H(w) + sum w (a - c)
                    rec("SEL11 |H(r) - H(w) - sum w(a-c)|", abs(float(ent(rpt) - ent(w) - (w * (a - c)).sum())), ("C11", a))
    print("Part C instances:", tot, flush=True)


def partD(budget_starts=40):
    """Adversarial: maximise the SEL-9 gap over real leaves for irreducible partitions (Nelder-Mead/Powell)."""
    from scipy.optimize import minimize
    parts3 = [c for c in affine_partitions(3) if not reducible(c, 3)]
    best = -1e9
    cands = []
    for t in range(budget_starts):
        if t % 2 == 0:
            cells = parts3[rng.integers(len(parts3))]; a = 3
        else:
            while True:
                cells = random_affine_partition(4, rng)
                if not reducible(cells, 4) and len(cells) <= 6:
                    break
            a = 4
        K = len(cells)
        n = 2
        x0 = rng.normal(size=K * (1 << n))
        f = lambda x: -real_instance(cells, a, n, x.reshape(K, 1 << n))[0]
        res = minimize(f, x0, method="Powell", options={"maxiter": 4000, "xtol": 1e-6, "ftol": 1e-10})
        val = -res.fun
        best = max(best, val)
        cands.append((val, a, K))
    rec("SEL9 adversarial (Powell) max gap", best, "D")
    print("Part D: %d optimisations, best gap %.3e" % (budget_starts, best), flush=True)


if __name__ == "__main__":
    partA()
    partB()
    partC()
    partD()
    for k, (v, info) in sorted(WORST.items()):
        print("%-50s %+.3e  (n=%d)  at %s" % (k, v, COUNT[k], info))
