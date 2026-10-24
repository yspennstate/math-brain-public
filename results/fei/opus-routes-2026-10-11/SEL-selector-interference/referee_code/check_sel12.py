"""Referee checks of SEL-12.
(b) coordinate decision-tree cells with adjacent-leaf correlation <= 1-delta:
    cost(F) = H(F) - sum_j p_j H(G_j) <= K(delta/2) I_sel(F), and H(F) <= max(C, K(delta/2)) I(F).
    Exhaustive at total n = 4 over every decision-tree partition of the a-bit selector (a = 1,2,3) and every
    Boolean leaf assignment; random beyond.  Also checks the telescoping and influence identities.
(a) recursive fresh-selector multiplexers whose nodes all have energy fraction >= c:
    H(F) <= max(C_leaf, K(c)) I(F) on random constructions.
"""
import itertools
import math
import numpy as np
from rlib import wht, ent, popcount_table, K_of_c, h2, LOG2E

rng = np.random.default_rng(2026)
WORST = {}


def rec(name, v, info=None):
    if name not in WORST or v > WORST[name][0]:
        WORST[name] = (float(v), info)


def dt_partitions(a):
    """All distinct partitions of {0..2^a-1} given by coordinate decision trees, as tuples of cells
    (each cell = (fixed_mask, fixed_value) subcube)."""
    def rec_(free_mask, fixed_mask, fixed_val):
        out = {((fixed_mask, fixed_val),)}
        for v in range(a):
            if (free_mask >> v) & 1:
                fm = free_mask & ~(1 << v)
                L = rec_(fm, fixed_mask | (1 << v), fixed_val)
                R = rec_(fm, fixed_mask | (1 << v), fixed_val | (1 << v))
                for l in L:
                    for r in R:
                        out.add(tuple(sorted(l + r)))
        return out
    return sorted(rec_((1 << a) - 1, 0, 0))


def cell_labels(cells, a):
    L = np.empty(1 << a, dtype=np.int64)
    for k, (m, v) in enumerate(cells):
        for x in range(1 << a):
            if (x & m) == v:
                L[x] = k
    return L


def adjacency(L, a):
    adj = set()
    for x in range(1 << a):
        for i in range(a):
            y = x ^ (1 << i)
            if L[x] != L[y]:
                adj.add((min(L[x], L[y]), max(L[x], L[y])))
    return sorted(adj)


def check_batch(cells, a, n, leaves, label):
    """leaves: (B, K, D) +-1."""
    L = cell_labels(cells, a)
    adj = adjacency(L, a)
    B, K, Dn = leaves.shape
    N = 1 << a
    F = leaves[:, L, :].transpose(0, 2, 1).reshape(B, -1)
    W = wht(F)
    P = W.astype(np.float64) ** 2 / float((N * Dn) ** 2)
    HF = ent(P)
    IF = (P * popcount_table(a + n)[None, :]).sum(axis=1)
    Pl = wht(leaves).astype(np.float64) ** 2 / float(Dn * Dn)
    Hl = ent(Pl, axis=2)
    Il = (Pl * popcount_table(n)[None, None, :]).sum(axis=2)
    p = np.array([np.mean(L == k) for k in range(K)])
    cost = HF - (Hl * p[None, :]).sum(axis=1)
    Fs = F.reshape(B, Dn, N)
    Isel = np.zeros(B)
    for i in range(a):
        Isel += (Fs != Fs[:, :, np.arange(N) ^ (1 << i)]).mean(axis=(1, 2))
    if not adj:
        return 0
    corr = np.stack([(leaves[:, j, :] * leaves[:, l, :]).mean(axis=1) for j, l in adj], axis=1)
    delta = 1 - corr.max(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        C = np.where(Il > 1e-12, Hl / np.where(Il > 1e-12, Il, 1), 0.0).max(axis=1)
    cnt = 0
    for b in range(B):
        if delta[b] <= 1e-12:
            continue
        K12 = K_of_c(delta[b] / 2)
        rec("SEL12b cost - K(delta/2) I_sel", cost[b] - K12 * Isel[b], label)
        rec("SEL12b H(F) - max(C,K(delta/2)) I(F)", HF[b] - max(C[b], K12) * IF[b], label)
        cnt += 1
    return cnt


def all_tables(nv):
    M = 1 << nv
    return 1 - 2 * ((np.arange(1 << M)[:, None] >> np.arange(M)[None, :]) & 1)


def exhaustive():
    tot = 0
    for a in (1, 2, 3):
        n = 4 - a
        funcs = all_tables(n)
        parts = dt_partitions(a)
        for cells in parts:
            K = len(cells)
            M = funcs.shape[0]
            if M ** K <= 70000:
                idx = np.array(list(itertools.product(range(M), repeat=K)))
            else:
                idx = rng.integers(0, M, size=(70000, K))
            leaves = funcs[idx].astype(np.int64)
            for s in range(0, len(leaves), 20000):
                tot += check_batch(cells, a, n, leaves[s:s + 20000], ("exh", a, n, K))
        print("a=%d: %d decision-tree partitions" % (a, len(parts)), flush=True)
    print("exhaustive SEL-12b instances with delta>0:", tot, flush=True)


def telescoping_check():
    """For random trees, verify cost = sum_v P(v) cost_v and I_sel = sum_v P(v) pi_v (exact by construction)."""
    bad = 0
    for t in range(200):
        a = rng.integers(2, 5); n = rng.integers(1, 4)
        parts = dt_partitions(int(a)) if a <= 3 else None
        # build a random tree explicitly
        def build(free, fm, fv, depth):
            if not free or rng.random() < 0.25:
                return ("leaf", fm, fv)
            v = int(rng.choice(free))
            nf = [u for u in free if u != v]
            return ("node", v, build(nf, fm | (1 << v), fv, depth + 1), build(nf, fm | (1 << v), fv | (1 << v), depth + 1))
        tree = build(list(range(int(a))), 0, 0, 0)
        leaves_cells = []
        def collect(tn):
            if tn[0] == "leaf":
                leaves_cells.append((tn[1], tn[2]))
            else:
                collect(tn[2]); collect(tn[3])
        collect(tree)
        a = int(a); n = int(n); K = len(leaves_cells)
        G = rng.choice([-1, 1], size=(K, 1 << n)).astype(np.int64)
        L = cell_labels(tuple(leaves_cells), a)
        def func_of(tn):
            """truth table (over all a+n vars) of the subtree function."""
            if tn[0] == "leaf":
                k = leaves_cells.index((tn[1], tn[2]))
                tab = np.tile(G[k][:, None], (1, 1 << a)).reshape(-1)    # index x + N*y, independent of x
                return tab
            return None
        N = 1 << a; Dn = 1 << n
        def tab_sub(tn):
            if tn[0] == "leaf":
                k = leaves_cells.index((tn[1], tn[2]))
                return np.repeat(G[k][:, None], N, axis=1).reshape(-1)  # [y, x] -> x + N*y
            v = tn[1]
            Tp = tab_sub(tn[2]); Tm = tab_sub(tn[3])
            idx = np.arange(N * Dn)
            xv = (idx >> v) & 1
            return np.where(xv == 0, Tp, Tm)
        def H_(T):
            W = wht(T); P = W.astype(np.float64) ** 2 / float((N * Dn) ** 2)
            return float(ent(P))
        total_cost = 0.0
        total_pi = 0.0
        def walk(tn, prob):
            nonlocal total_cost, total_pi
            if tn[0] == "leaf":
                return
            v = tn[1]
            Tv = tab_sub(tn); Tp = tab_sub(tn[2]); Tm = tab_sub(tn[3])
            total_cost += prob * (H_(Tv) - (H_(Tp) + H_(Tm)) / 2)
            total_pi += prob * float(np.mean(Tp != Tm))
            walk(tn[2], prob / 2); walk(tn[3], prob / 2)
        walk(tree, 1.0)
        F = tab_sub(tree)
        p = np.array([np.mean(L == k) for k in range(K)])
        HG = np.array([float(ent((wht(G[k]).astype(np.float64) / Dn) ** 2)) for k in range(K)])
        cost = H_(F) - float((p * HG).sum())
        idx = np.arange(N * Dn)
        Isel = sum(float(np.mean(F != F[idx ^ (1 << i)])) for i in range(a))
        if abs(cost - total_cost) > 1e-9 or abs(Isel - total_pi) > 1e-12:
            bad += 1
    print("telescoping identities on 200 random trees: failures =", bad, flush=True)


def recursive_a():
    """(a): random recursive fresh-selector multiplexers; record min node energy fraction c and check
    H <= max(C_leaf, K(c)) I."""
    worst = -1e9
    for t in range(150):
        n = int(rng.integers(2, 4))                 # data bits for leaves
        Dn = 1 << n
        leaves = [rng.choice([-1, 1], size=Dn).astype(np.int64) for _ in range(4)]
        Cleaf = 0.0
        for g in leaves:
            P = (wht(g).astype(np.float64) / Dn) ** 2
            I = float((P * popcount_table(n)).sum())
            if I > 1e-12:
                Cleaf = max(Cleaf, float(ent(P)) / I)
        # build: level 1 node on a1 fresh bits over the leaves (functions on n data bits)
        funcs = [(g, n) for g in leaves]           # (table, nvars) with data = the low n bits... we keep tables over growing var sets
        cmin = 1.0
        cur = funcs
        ok = True
        for level in range(2):
            a_v = int(rng.integers(1, 3))
            Nv = 1 << a_v
            # all current functions are over the same variable set of size m (pad)
            m = max(nv for _, nv in cur)
            tabs = []
            for tab, nv in cur:
                idx = np.arange(1 << m)
                tabs.append(tab[idx & ((1 << nv) - 1)])
            choice = rng.integers(0, len(tabs), size=Nv)
            # low-energy option: copies with a single flipped branch
            Bm = np.array([tabs[c] for c in choice])
            Fv = Bm.T.reshape(-1)                  # index x + Nv*y, total a_v + m variables
            tot = a_v + m
            idx = np.arange(1 << tot)
            Isel = sum(float(np.mean(Fv != Fv[idx ^ (1 << i)])) for i in range(a_v))
            if Isel <= 1e-12:
                ok = False
                break
            cmin = min(cmin, Isel / a_v)
            cur = [(Fv, tot)] + [(Bm[0], m)]
            # next level re-indexes: put the new function's variables as 'data' for the next node
        if not ok:
            continue
        F, tot = cur[0]
        P = (wht(F).astype(np.float64) / (1 << tot)) ** 2
        H = float(ent(P)); I = float((P * popcount_table(tot)).sum())
        worst = max(worst, H - max(Cleaf, K_of_c(cmin)) * I)
    print("SEL-12a random recursive constructions: max H - max(C_leaf,K(c_min)) I = %.3e" % worst, flush=True)
    rec("SEL12a H - max(Cleaf, K(cmin)) I", worst, "rand")


def random_larger():
    tot = 0
    for a in (3, 4, 5):
        parts = dt_partitions(a) if a <= 4 else None
        for t in range(120 if a < 5 else 40):
            if a <= 4:
                cells = parts[rng.integers(len(parts))]
            else:
                # random tree on 5 bits
                def build(free, fm, fv):
                    if not free or rng.random() < 0.3:
                        return [(fm, fv)]
                    v = int(rng.choice(free)); nf = [u for u in free if u != v]
                    return build(nf, fm | (1 << v), fv) + build(nf, fm | (1 << v), fv | (1 << v))
                cells = tuple(sorted(build(list(range(5)), 0, 0)))
            K = len(cells)
            n = int(rng.integers(2, 5))
            Dn = 1 << n
            base = rng.choice([-1, 1], size=(1, 1, Dn))
            near = np.where(rng.random((30, K, Dn)) < rng.uniform(0.02, 0.4), -base, base)   # small gaps
            randl = rng.choice([-1, 1], size=(30, K, Dn))
            leaves = np.concatenate([near, randl]).astype(np.int64)
            tot += check_batch(cells, a, n, leaves, ("rand", a, n, K))
    print("random SEL-12b instances:", tot, flush=True)


if __name__ == "__main__":
    exhaustive()
    telescoping_check()
    random_larger()
    recursive_a()
    for k, (v, info) in sorted(WORST.items()):
        print("%-45s %+.3e  at %s" % (k, v, info))
