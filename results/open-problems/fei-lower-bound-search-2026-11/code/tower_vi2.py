"""tower_vi2.py - tower_vi.py with coin gates in the library.

A coin gate is a line "m k labels" (fei_coin / fei_coinp format): one label per x in {0,1}^m,
0: +1, 1: -1, 2+2j: Y_j, 3+2j: -Y_j, and every input (the m main ones and the coins) is a copy of the state.
Its p-biased quantities come from the transforms of the constant part and of each coin part, (k+1) 2^m numbers,
so gates with many coins cost nothing extra.

usage: python tower_vi2.py --libfile LIB.txt [--libfile ...] --coinfile COINS.txt [--coinfile ...]
           [--grid M] [--span L] [--sweeps S] [--depth D] [--dump W.txt] [--keep KEEP.txt] [--nobase]
  --keep writes the explicit gates among the top 3 somewhere to KEEP.txt and the coin gates to KEEP.txt.coin
"""
import sys

import numpy as np

from tower_vi import canon, monotone_tables, stats_grid


def coin_parts(m, labels):
    lab = np.array(labels, dtype=np.int64)
    used = sorted({int((l - 2) // 2) for l in lab if l >= 2})
    s0 = np.where(lab == 0, 1.0, np.where(lab == 1, -1.0, 0.0))
    ca = np.where(lab >= 2, np.where(lab % 2 == 0, 1.0, -1.0), 0.0)
    rows = [s0, ca]
    for j in used:
        rows.append(np.where(lab == 2 + 2 * j, -1.0, np.where(lab == 3 + 2 * j, 1.0, 0.0)))
    return np.array(rows)


def coin_stats(m, rows, ps):
    """G, J, P over the biases ps for one coin gate given by coin_parts."""
    N = 1 << m
    size = np.zeros(1)
    for _ in range(m):
        size = np.concatenate([size, size + 1])
    L = rows.shape[0]
    G = np.empty(len(ps)); J = np.empty(len(ps)); P = np.empty(len(ps))
    for c, p in enumerate(ps):
        s = np.sqrt(p * (1 - p))
        a = rows.copy()
        h = 1
        while h < N:
            a = a.reshape(L, -1, 2, h)
            lo, hi = a[:, :, 0, :], a[:, :, 1, :]
            a = np.stack([(1 - p) * lo + p * hi, s * (hi - lo)], axis=2).reshape(L, -1)
            h *= 2
        a0 = a[0] + (1 - 2 * p) * a[1]
        mean = a0[0]
        var = 1 - mean * mean
        P[c] = (1 - mean) / 2
        if var < 1e-13:
            G[c] = 0.0; J[c] = np.inf
            continue
        w0 = a0 * a0
        w0[0] = 0.0
        wc = 4 * p * (1 - p) * a[2:] ** 2
        allw = np.concatenate([w0, wc.reshape(-1)]) / var
        nz = allw > 1e-300
        G[c] = float(-(allw[nz] * np.log2(allw[nz])).sum())
        J[c] = float(((w0 * size).sum() + (wc * (size[None, :] + 1)).sum()) / var)
    return G, J, P


def main():
    args = sys.argv[1:]

    def opt(name, default, typ=float):
        if name in args:
            i = args.index(name)
            v = typ(args[i + 1])
            del args[i:i + 2]
            return v
        return default
    M = opt("--grid", 801, int)
    span = opt("--span", 24.0)
    sweeps = opt("--sweeps", 4000, int)
    depth = opt("--depth", 80, int)
    dump = opt("--dump", "", str)
    keep = opt("--keep", "", str)
    init = opt("--init", "", str)
    nobase = "--nobase" in args
    extras, coins = [], []
    while "--libfile" in args:
        i = args.index("--libfile")
        with open(args[i + 1], encoding="utf-8") as fh:
            for line in fh:
                parts = line.split()
                if len(parts) == 2 and not line.startswith("#"):
                    extras.append((int(parts[0]), int(parts[1], 16)))
        del args[i:i + 2]
    while "--coinfile" in args:
        i = args.index("--coinfile")
        with open(args[i + 1], encoding="utf-8") as fh:
            for line in fh:
                parts = line.split()
                if len(parts) >= 3 and not line.startswith("#"):
                    mm = int(parts[0])
                    labs = [ord(ch) - 48 for ch in parts[2]]
                    if len(labs) == 1 << mm:
                        coins.append((mm, parts[2], coin_parts(mm, labs)))
        del args[i:i + 2]

    t = np.linspace(-span, span, M)
    ps = 1.0 / (1.0 + 2.0 ** (-t))
    lib = []
    if not nobase:
        for n in (1, 2, 3, 4):
            tabs = np.arange(1, (1 << (1 << n)) - 1, dtype=np.uint64)
            for tb in canon(tabs, n):
                lib.append((n, int(tb)))
        m5 = np.array([x for x in monotone_tables(5) if x not in (0, (1 << 32) - 1)], dtype=np.uint64)
        for tb in canon(m5, 5):
            lib.append((5, int(tb)))
    lib += extras
    print("library:", len(lib), "explicit gates,", len(coins), "coin gates; grid", M, "points, span", span, flush=True)

    Gs, Js, Ps, owner = [], [], [], []
    for n in sorted(set(k for k, _ in lib)):
        tabs = [tb for k, tb in lib if k == n]
        for lo in range(0, len(tabs), 512):
            chunk = tabs[lo:lo + 512]
            if n > 12:
                for tb in chunk:
                    b = np.array([[(tb >> x) & 1 for x in range(1 << n)]], dtype=np.uint8)
                    G, J, P = stats_grid(b, n, ps)
                    Gs.append(G); Js.append(J); Ps.append(P)
            else:
                b = np.array([[(tb >> x) & 1 for x in range(1 << n)] for tb in chunk], dtype=np.uint8)
                G, J, P = stats_grid(b, n, ps)
                Gs.append(G); Js.append(J); Ps.append(P)
            owner += [("x", n, tb) for tb in chunk]
    for ci, (mm, labs, rows) in enumerate(coins):
        G, J, P = coin_stats(mm, rows, ps)
        Gs.append(G[None, :]); Js.append(J[None, :]); Ps.append(P[None, :])
        owner.append(("c", mm, ci))
        if ci % 20 == 0:
            print("coin gate", ci, "of", len(coins), flush=True)
    G = np.vstack(Gs); J = np.vstack(Js); P = np.vstack(Ps)
    with np.errstate(divide="ignore"):
        T = np.log2(P / (1 - P))
    T = np.clip(np.nan_to_num(T, nan=0.0, posinf=span, neginf=-span), -span, span)
    live = J > 1 + 1e-9

    W = np.zeros(M)
    if init:
        ti, wi = [], []
        with open(init, encoding="utf-8") as fh:
            for line in fh:
                if not line.startswith("#") and line.strip():
                    a_, b_ = line.split()[:2]
                    ti.append(float(a_)); wi.append(float(b_))
        ti = np.array(ti); wi = np.array(wi)
        if len(ti) == M and np.abs(ti - t).max() < 1e-9:
            W = wi.copy()
        else:
            # a coarser start must not exceed the true table: take the lower of the two neighbours
            k = np.clip(np.searchsorted(ti, t, side="right") - 1, 0, len(ti) - 2)
            W = np.minimum(wi[k], wi[k + 1])
        print("start table from", init, flush=True)
    for sweep in range(sweeps):
        cont = np.interp(T.reshape(-1), t, W).reshape(T.shape)
        val = np.where(live, (G + cont) / np.where(live, J, 1.0), -1.0)
        Wn = np.maximum(W, val.max(axis=0))
        d = float(np.abs(Wn - W).max())
        W = Wn
        if sweep % 50 == 0:
            print("sweep %d  W(1/2)=%.9f  max change %.2e" % (sweep, W[M // 2], d), flush=True)
        if d < 1e-11:
            break
    print("converged after", sweep + 1, "sweeps;  W(1/2) on the grid = %.9f" % W[M // 2])
    if dump:
        with open(dump, "w", encoding="utf-8") as fh:
            fh.write("# log-odds(base 2)  W\n")
            for a, b in zip(t, W):
                fh.write("%.12f %.12f\n" % (a, b))
    cont = np.interp(T.reshape(-1), t, W).reshape(T.shape)
    val = np.where(live, (G + cont) / np.where(live, J, 1.0), -1.0)
    arg = val.argmax(axis=0)
    ncoin_best = int(sum(1 for i in arg if owner[int(i)][0] == "c"))
    print("grid points where a coin gate is the best gate: %d of %d" % (ncoin_best, M))
    if keep:
        kk = min(3, val.shape[0])
        top = np.argpartition(-val, kk - 1, axis=0)[:kk]
        used = sorted(set(int(i) for i in top.reshape(-1)))
        with open(keep, "w", encoding="utf-8") as fh, open(keep + ".coin", "w", encoding="utf-8") as fc:
            for i in used:
                if owner[i][0] == "x":
                    fh.write("%d %x\n" % (owner[i][1], owner[i][2]))
                else:
                    mm, labs, rows = coins[owner[i][2]]
                    fc.write("%d %d %s\n" % (mm, rows.shape[0] - 2, labs))
        print("kept", len(used), "gates in", keep)
    for q in (0.5, 0.25, 0.3, 11 / 32, 0.381966011250105, 0.42, 0.45, 0.47, 0.48, 0.49, 0.51, 0.52, 0.53, 0.55, 0.58,
              0.618033988749895, 0.65625, 0.7):
        print("  W(%.4f) ~ %.6f" % (q, np.interp(np.log2(q / (1 - q)), t, W)))

    def exact(idx, p):
        o = owner[idx]
        if o[0] == "x":
            b = np.array([[(o[2] >> x) & 1 for x in range(1 << o[1])]], dtype=np.uint8)
            g, j, pn = stats_grid(b, o[1], [p])
            return g[0, 0], j[0, 0], pn[0, 0]
        g, j, pn = coin_stats(o[1], coins[o[2]][2], [p])
        return g[0], j[0], pn[0]

    p, Gt, Jt = 0.5, 0.0, 1.0
    print("rollout: step  gate  p_in -> p_out  G_p J_p   G/J so far")
    for step in range(depth):
        best = None
        tq = min(max(np.log2(p / (1 - p)), -span), span)
        c = int(np.argmin(np.abs(t - tq)))
        cont = np.interp(T[:, c], t, W)
        score = np.where(live[:, c], (G[:, c] + cont) / np.where(live[:, c], J[:, c], 1.0), -1.0)
        for idx in np.argsort(-score)[:25]:
            g, j, pn = exact(int(idx), p)
            if not np.isfinite(j) or j <= 1 + 1e-9 or pn <= 0 or pn >= 1:
                continue
            v = (g + np.interp(min(max(np.log2(pn / (1 - pn)), -span), span), t, W)) / j
            if best is None or v > best[0]:
                best = (v, int(idx), g, j, pn)
        if best is None:
            break
        v, idx, g, j, pn = best
        Gt = g + j * Gt
        Jt = j * Jt
        o = owner[idx]
        name = ("n=%d %x" % (o[1], o[2]))[:40] if o[0] == "x" else "coin#%d m=%d" % (o[2], o[1])
        if step < 30 or step % 10 == 0:
            print("  %2d  %s  %.12f -> %.12f  G=%.6f J=%.6f  G/J=%.9f" % (step, name, p, pn, g, j, Gt / Jt))
        p = pn
        if Jt > 1e15:
            break
    print("rollout value G/J = %.9f after %d steps (J = %.3e)" % (Gt / Jt, step + 1, Jt))


if __name__ == "__main__":
    main()
