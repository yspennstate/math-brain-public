"""tower_vi.py - value iteration for composition towers with drifting bias (lower bounds on the FEI constant).

State of a Boolean function g on uniform bits: p = Pr[g = -1], G(g) = entropy of the normalised non-constant spectrum,
J(g) = I(g)/Var(g).  Composing with F (independent copies of g in each input):
    p' = Pr_p[F = -1],   G' = G_p(F) + J_p(F) G,   J' = J_p(F) J,
and H(g)/I(g) >= G(g)/J(g) for every g, with equality in the limit J -> infinity.  Along a tower F_1, F_2, ... started
from one uniform bit (p = 1/2, G = 0, J = 1) the ratio G/J increases to  sum_s G_{p_{s-1}}(F_s) / prod_{r<=s} J_{p_{r-1}}(F_r).
W(p) = sup over towers started at bias p solves  W(p) = max_F [G_p(F) + W(p')] / J_p(F).

The script iterates that equation on a grid in log-odds over a library of small functions (all functions on <= 4
inputs and all monotone functions on 5 inputs, up to permutations of the inputs, plus tables given with --extra
K:HEX), then rolls the greedy policy out from p = 1/2 with the true (not interpolated) quantities.  The rollout
value is the G/J of an explicit finite composition, so it is a lower bound on sup H/I up to rounding.

usage: python tower_vi.py [--grid M] [--span L] [--sweeps S] [--extra K:HEX ...] [--nomono5] [--depth D]
"""
import itertools
import sys

import numpy as np


def bits_of(tabs, n):
    N = 1 << n
    return ((tabs[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.uint8)


def canon(tabs, n):
    """smallest table over permutations of the inputs; returns the sorted unique canonical tables."""
    N = 1 << n
    b = bits_of(tabs, n)
    best = tabs.copy()
    pw = (np.uint64(1) << np.arange(N, dtype=np.uint64))
    for perm in itertools.permutations(range(n)):
        idx = np.zeros(N, dtype=np.int64)
        for x in range(N):
            y = 0
            for i in range(n):
                if (x >> i) & 1:
                    y |= 1 << perm[i]
            idx[x] = y
        t = (b[:, idx].astype(np.uint64) * pw[None, :]).sum(axis=1, dtype=np.uint64)
        best = np.minimum(best, t)
    return np.unique(best)


def monotone_tables(n):
    """all monotone up-sets on n inputs as integers (bit x set <=> x in U), by the recursion on the last input."""
    cur = [0, 1]                       # n = 0: empty, full
    for m in range(1, n + 1):
        half = 1 << (m - 1)
        nxt = []
        for f0 in cur:
            for f1 in cur:
                if f0 & ~f1 == 0:      # f0 subset of f1
                    nxt.append(f0 | (f1 << half))
        cur = nxt
    return cur


def stats_grid(bits, n, ps):
    """bits: (L, 2^n) 0/1.  Returns G, J, P of shape (L, len(ps)); entries with tiny variance get J = inf."""
    L = bits.shape[0]
    G = np.empty((L, len(ps)))
    J = np.empty((L, len(ps)))
    P = np.empty((L, len(ps)))
    size = np.array([bin(t).count("1") for t in range(1 << n)], dtype=np.float64)
    f0 = 1.0 - 2.0 * bits.astype(np.float64)
    for c, p in enumerate(ps):
        s = np.sqrt(p * (1 - p))
        a = f0.copy()
        h = 1
        while h < (1 << n):
            a = a.reshape(L, -1, 2, h)
            lo, hi = a[:, :, 0, :], a[:, :, 1, :]
            a = np.stack([(1 - p) * lo + p * hi, s * (hi - lo)], axis=2).reshape(L, -1)
            h *= 2
        mean = a[:, 0]
        var = 1 - mean ** 2
        ok = var > 1e-13
        w = a ** 2
        w[:, 0] = 0
        with np.errstate(divide="ignore", invalid="ignore"):
            wn = w / np.where(ok, var, 1.0)[:, None]
            ent = np.where(wn > 1e-300, -wn * np.log2(np.where(wn > 1e-300, wn, 1.0)), 0.0).sum(axis=1)
            jj = (wn * size[None, :]).sum(axis=1)
        G[:, c] = np.where(ok, ent, 0.0)
        J[:, c] = np.where(ok, jj, np.inf)
        P[:, c] = (1 - mean) / 2
    return G, J, P


def one_stats(tab, n, p):
    b = np.array([[(tab >> x) & 1 for x in range(1 << n)]], dtype=np.uint8)
    G, J, P = stats_grid(b, n, [p])
    return G[0, 0], J[0, 0], P[0, 0]


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
    nomono5 = "--nomono5" in args
    dump = opt("--dump", "", str)
    keep = opt("--keep", "", str)                 # write the gates that are among the top 3 somewhere on the grid
    nobase = "--nobase" in args                   # library = only the --libfile / --extra tables
    extras = []
    while "--libfile" in args:                    # lines: n hex
        i = args.index("--libfile")
        with open(args[i + 1], encoding="utf-8") as fh:
            for line in fh:
                parts = line.split()
                if len(parts) == 2 and not line.startswith("#"):
                    extras.append((int(parts[0]), int(parts[1], 16)))
        del args[i:i + 2]
    while "--extra" in args:
        i = args.index("--extra")
        kk, hx = args[i + 1].split(":")
        extras.append((int(kk), int(hx, 16)))
        del args[i:i + 2]

    t = np.linspace(-span, span, M)               # log-odds base 2
    ps = 1.0 / (1.0 + 2.0 ** (-t))
    lib = []                                      # (n, table)
    for n in (() if nobase else (1, 2, 3, 4)):
        tabs = np.arange(1, (1 << (1 << n)) - 1, dtype=np.uint64)
        for tb in canon(tabs, n):
            lib.append((n, int(tb)))
    if not nomono5 and not nobase:
        m5 = np.array([x for x in monotone_tables(5) if x not in (0, (1 << 32) - 1)], dtype=np.uint64)
        for tb in canon(m5, 5):
            lib.append((5, int(tb)))
    lib += extras
    print("library:", len(lib), "functions; grid", M, "points, log-odds span", span, flush=True)

    Gs, Js, Ps, owner = [], [], [], []
    for n in sorted(set(k for k, _ in lib)):
        tabs = [tb for k, tb in lib if k == n]
        for lo in range(0, len(tabs), 512):
            chunk = tabs[lo:lo + 512]
            if n > 12:                             # one big table at a time
                for tb in chunk:
                    b = np.array([[(tb >> x) & 1 for x in range(1 << n)]], dtype=np.uint8)
                    G, J, P = stats_grid(b, n, ps)
                    Gs.append(G); Js.append(J); Ps.append(P)
                owner += [(n, tb) for tb in chunk]
                continue
            b = np.array([[(tb >> x) & 1 for x in range(1 << n)] for tb in chunk], dtype=np.uint8)
            G, J, P = stats_grid(b, n, ps)
            Gs.append(G); Js.append(J); Ps.append(P)
            owner += [(n, tb) for tb in chunk]
    G = np.vstack(Gs); J = np.vstack(Js); P = np.vstack(Ps)
    with np.errstate(divide="ignore"):
        T = np.log2(P / (1 - P))
    T = np.clip(np.nan_to_num(T, nan=0.0, posinf=span, neginf=-span), -span, span)
    live = J > 1 + 1e-9                            # drop dictators and constants at that bias

    W = np.zeros(M)
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
    if keep:
        cont = np.interp(T.reshape(-1), t, W).reshape(T.shape)
        val = np.where(live, (G + cont) / np.where(live, J, 1.0), -1.0)
        kk = min(3, val.shape[0])
        top = np.argpartition(-val, kk - 1, axis=0)[:kk]
        used = sorted(set(int(i) for i in top.reshape(-1)))
        with open(keep, "w", encoding="utf-8") as fh:
            for i in used:
                fh.write("%d %x\n" % owner[i])
        print("kept", len(used), "gates in", keep)
    for q in (0.5, 0.25, 0.125, 1 / 16, 7 / 16, 3 / 8, 1 / 3, 11 / 32, 0.381966011250105, 0.45, 0.48, 0.49, 0.495, 0.51, 0.52, 0.55):
        print("  W(%.4f) ~ %.6f" % (q, np.interp(np.log2(q / (1 - q)), t, W)))

    # greedy rollout from p = 1/2 with true quantities at the true bias
    p, Gt, Jt = 0.5, 0.0, 1.0
    print("rollout: step  n table  p_in -> p_out  G_p J_p   G/J so far")
    for step in range(depth):
        best = None
        tq = min(max(np.log2(p / (1 - p)), -span), span)
        # shortlist by the grid, then evaluate the shortlist exactly at p
        c = int(np.argmin(np.abs(t - tq)))
        cont = np.interp(T[:, c], t, W)
        score = np.where(live[:, c], (G[:, c] + cont) / np.where(live[:, c], J[:, c], 1.0), -1.0)
        for idx in np.argsort(-score)[:40]:
            n, tb = owner[idx]
            g, j, pn = one_stats(tb, n, p)
            if not np.isfinite(j) or j <= 1 + 1e-9 or pn <= 0 or pn >= 1:
                continue
            v = (g + np.interp(min(max(np.log2(pn / (1 - pn)), -span), span), t, W)) / j
            if best is None or v > best[0]:
                best = (v, n, tb, g, j, pn)
        if best is None:
            break
        v, n, tb, g, j, pn = best
        Gt = g + j * Gt
        Jt = j * Jt
        if step < 30 or step % 10 == 0:
            print("  %2d  n=%d %x  %.12f -> %.12f  G=%.6f J=%.6f  G/J=%.9f" % (step, n, tb, p, pn, g, j, Gt / Jt))
        p = pn
        if Jt > 1e15:
            break
    print("rollout value G/J = %.9f after %d steps (J = %.3e)" % (Gt / Jt, step + 1, Jt))


if __name__ == "__main__":
    main()
