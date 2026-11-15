"""neg_screen.py - input-negated variants of library gates, screened against a Bellman table.

A tower may feed a gate the state g or its negation -g (same G and J, bias p or 1 - p).  For a gate F that is the
gate x -> F(x xor mask) at the homogeneous bias p.  For every gate of the given files and every mask this computes,
on a coarse grid of biases, slack_p = G_p - W(p) J_p + W(p'), keeps per source gate the variants that are among the
best few at some bias, and writes the overall best few per bias (plus everything with positive slack).

usage: python3 neg_screen.py WFILE OUTPREFIX [--lib FILE]... [--coin LABFILE]... [--nmax 10] [--topk 6]
                                             [--pts 121] [--tspan 3.0]
writes OUTPREFIX.lib ("n hex") and OUTPREFIX.coin ("m k labels"); each kept variant comes with its partner
(all inputs negated), so the table built from them stays symmetric.
"""
import sys
import time

import numpy as np

from tower_vi import stats_grid


def load_w(path):
    t, w = [], []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            a, b = line.split()[:2]
            t.append(float(a)); w.append(float(b))
    return np.array(t), np.array(w)


def w_of(P, t, w):
    with np.errstate(divide="ignore", invalid="ignore"):
        x = np.log2(P / (1 - P))
    x = np.clip(np.nan_to_num(x, nan=0.0, posinf=t[-1], neginf=t[0]), t[0], t[-1])
    return np.interp(x.reshape(-1), t, w).reshape(x.shape)


def top_rows(S, k):
    """indices of rows that are among the k largest in some column"""
    if S.shape[0] <= k:
        return np.arange(S.shape[0])
    part = np.argpartition(-S, k - 1, axis=0)[:k]
    return np.unique(part.reshape(-1))


def uniq(S):
    keys = {}
    for i in range(S.shape[0]):
        kb = np.round(S[i], 8).tobytes()
        if kb not in keys:
            keys[kb] = i
    return np.array(sorted(keys.values()), dtype=np.int64)


def main():
    args = sys.argv[1:]

    def opt(name, default, typ=float):
        if name in args:
            i = args.index(name)
            v = typ(args[i + 1])
            del args[i:i + 2]
            return v
        return default

    def multi(name):
        out = []
        while name in args:
            i = args.index(name)
            out.append(args[i + 1])
            del args[i:i + 2]
        return out
    nmax = opt("--nmax", 10, int)
    topk = opt("--topk", 6, int)
    pts = opt("--pts", 121, int)
    tspan = opt("--tspan", 3.0)
    allpos = opt("--allpos", 0, int)
    libs = multi("--lib")
    coinfiles = multi("--coin")
    wfile, outp = args[0], args[1]
    t, w = load_w(wfile)
    tt = np.linspace(-tspan, tspan, pts)
    ps = 1.0 / (1.0 + 2.0 ** (-tt))
    Wp = np.interp(tt, t, w)
    cand_S, cand_d = [], []          # slack rows, descriptors ("x", n, table int) or ("c", m, k, labels string)
    t0 = time.time()

    # explicit gates
    seen = set()
    for lf in libs:
        with open(lf, encoding="utf-8") as fh:
            gates = [(int(a), int(b, 16)) for a, b in (ln.split()[:2] for ln in fh if ln.strip() and not ln.startswith("#"))]
        hist = {}
        for n, _ in gates:
            hist[n] = hist.get(n, 0) + 1
        print("lib", lf, "gates by inputs:", sorted(hist.items()), flush=True)
        for n, tb in gates:
            if n > nmax or n < 2 or (n, tb) in seen:
                continue
            seen.add((n, tb))
            N = 1 << n
            base = np.array([(tb >> x) & 1 for x in range(N)], dtype=np.uint8)
            idx = np.arange(N)
            rows, masks = [], []
            step = max(1, min(N, (1 << 19) // N))
            for lo in range(0, N, step):
                mk = np.arange(lo, min(N, lo + step))
                b = base[idx[None, :] ^ mk[:, None]]
                G, J, P = stats_grid(b, n, ps)
                ok = np.isfinite(J) & (J > 1 + 1e-9)
                S = np.where(ok, G - Wp[None, :] * np.where(ok, J, 1.0) + w_of(P, t, w), -np.inf)
                rows.append(S); masks.append(mk)
            S = np.vstack(rows); masks = np.concatenate(masks)
            u = uniq(S)
            S = S[u]; masks = masks[u]
            keep = top_rows(S, topk)
            best = S.max(axis=1)
            b0 = float(S[np.where(masks == 0)[0][0]].max()) if (masks == 0).any() else float("nan")
            j = int(np.argmax(best))
            print("x n=%d %s  variants %d  plain max slack %+.6f  best %+.6f at p=%.4f (mask %x)  [%.0fs]"
                  % (n, ("%x" % tb)[:24], len(u), b0, best[j], ps[int(np.argmax(S[j]))], int(masks[j]), time.time() - t0),
                  flush=True)
            for i in keep:
                tv = 0
                bb = base[idx ^ int(masks[i])]
                for x in np.nonzero(bb)[0]:
                    tv |= 1 << int(x)
                cand_S.append(S[i]); cand_d.append(("x", n, tv))

    # coin gates
    for cf in coinfiles:
        with open(cf, encoding="utf-8") as fh:
            lines = [ln.split() for ln in fh if ln.strip() and not ln.startswith("#")]
        for parts in lines:
            m = int(parts[0])
            lab = np.array([ord(ch) - 48 for ch in parts[2]], dtype=np.int64)
            N = 1 << m
            if len(lab) != N:
                continue
            used = sorted({int((l - 2) // 2) for l in lab if l >= 2})
            K = len(used)
            if K <= 10:
                sig = 1.0 - 2.0 * ((np.arange(1 << K)[:, None] >> np.arange(K)[None, :]) & 1)
            else:
                sig = np.vstack([np.ones(K), -np.ones(K)] + [np.where(np.arange(K) == j, -1.0, 1.0) for j in range(K)]
                                + [np.where(np.arange(K) == j, 1.0, -1.0) for j in range(K)])
            size = np.array([bin(x).count("1") for x in range(N)], dtype=np.float64)
            idx = np.arange(N)
            gbest = (-np.inf, None)
            for mask in range(N):
                lm = lab[idx ^ mask]
                rows = [np.where(lm == 0, 1.0, np.where(lm == 1, -1.0, 0.0))]
                for j in used:
                    rows.append(np.where(lm == 2 + 2 * j, 1.0, np.where(lm == 3 + 2 * j, -1.0, 0.0)))
                rows = np.array(rows)
                S = np.empty((sig.shape[0], pts))
                for c, p in enumerate(ps):
                    s = np.sqrt(p * (1 - p))
                    a = rows.copy()
                    h = 1
                    while h < N:
                        a = a.reshape(K + 1, -1, 2, h)
                        lo, hi = a[:, :, 0, :], a[:, :, 1, :]
                        a = np.stack([(1 - p) * lo + p * hi, s * (hi - lo)], axis=2).reshape(K + 1, -1)
                        h *= 2
                    a0 = a[0][None, :] + (1 - 2 * p) * (sig @ a[1:])
                    mean = a0[:, 0].copy()
                    var = 1 - mean * mean
                    w0 = a0 * a0
                    w0[:, 0] = 0.0
                    wc = 4 * p * (1 - p) * a[1:] ** 2
                    with np.errstate(divide="ignore", invalid="ignore"):
                        e0 = np.where(w0 > 1e-300, -w0 * np.log2(np.where(w0 > 1e-300, w0, 1.0)), 0.0).sum(axis=1)
                        ec = float(np.where(wc > 1e-300, -wc * np.log2(np.where(wc > 1e-300, wc, 1.0)), 0.0).sum())
                        ok = var > 1e-13
                        vv = np.where(ok, var, 1.0)
                        G = (e0 + ec) / vv + np.log2(vv)
                        J = ((w0 * size[None, :]).sum(axis=1) + float((wc * (size[None, :] + 1)).sum())) / vv
                    P = (1 - mean) / 2
                    ok &= J > 1 + 1e-9
                    S[:, c] = np.where(ok, G - Wp[c] * J + w_of(P, t, w), -np.inf)
                u = uniq(S)
                Su = S[u]
                keep = top_rows(Su, topk)
                bm = Su.max(axis=1)
                jb = int(np.argmax(bm))
                if bm[jb] > gbest[0]:
                    gbest = (float(bm[jb]), (mask, int(u[jb]), float(ps[int(np.argmax(Su[jb]))])))
                for i in keep:
                    sg = sig[int(u[i])]
                    out = lm.copy()
                    for jj, j in enumerate(used):
                        if sg[jj] < 0:
                            a_, b_ = out == 2 + 2 * j, out == 3 + 2 * j
                            out[a_] = 3 + 2 * j; out[b_] = 2 + 2 * j
                    cand_S.append(Su[i]); cand_d.append(("c", m, int(parts[1]), "".join(chr(48 + int(v)) for v in out)))
                if mask % 64 == 0:
                    print("coin m=%d mask %d of %d  best so far %+.6f %s  [%.0fs]" % (m, mask, N, gbest[0], gbest[1],
                                                                                    time.time() - t0), flush=True)
            print("coin gate m=%d coins=%d: best slack %+.6f (main mask, coin pattern, p) %s" % (m, K, gbest[0], gbest[1]),
                  flush=True)

    S = np.array(cand_S)
    u = uniq(S)
    S = S[u]; desc = [cand_d[int(i)] for i in u]
    keep = set(int(i) for i in top_rows(S, topk))
    if allpos:
        keep |= set(int(i) for i in np.nonzero(S.max(axis=1) > 1e-9)[0])
    print("candidates %d, kept %d, with positive slack %d" % (len(desc), len(keep), int((S.max(axis=1) > 1e-9).sum())))
    order = sorted(keep, key=lambda i: -float(S[i].max()))
    for i in order[:30]:
        d = desc[i]
        c = int(np.argmax(S[i]))
        print("  %+.6f at p=%.4f  %s %s" % (S[i, c], ps[c], d[0], ("n=%d %x" % (d[1], d[2]))[:40] if d[0] == "x"
                                           else "m=%d %s" % (d[1], d[3][:40])))
    # slack near 1/2 of the best row at each grid point
    mid = pts // 2
    print("best slack by bias:", " ".join("%.4f:%+.5f" % (ps[c], S[:, c].max()) for c in range(mid, pts, max(1, pts // 24))))
    xl, cl = set(), set()
    for i in order:
        d = desc[i]
        if d[0] == "x":
            n, tv = d[1], d[2]
            N = 1 << n
            rev = 0
            for x in range(N):
                if (tv >> x) & 1:
                    rev |= 1 << (N - 1 - x)
            xl.add("%d %x" % (n, tv)); xl.add("%d %x" % (n, rev))
        else:
            m, k, labs = d[1], d[2], d[3]
            arr = np.array([ord(ch) - 48 for ch in labs], dtype=np.int64)[::-1].copy()
            odd = (arr >= 2) & (arr % 2 == 1)
            even = (arr >= 2) & (arr % 2 == 0)
            arr[odd] -= 1; arr[even] += 1
            cl.add("%d %d %s" % (m, k, labs)); cl.add("%d %d %s" % (m, k, "".join(chr(48 + int(v)) for v in arr)))
    with open(outp + ".lib", "w", encoding="utf-8", newline="\n") as fh:
        fh.write("".join(s + "\n" for s in sorted(xl)))
    with open(outp + ".coin", "w", encoding="utf-8", newline="\n") as fh:
        fh.write("".join(s + "\n" for s in sorted(cl)))
    print("wrote %d explicit and %d coin gates to %s.lib / .coin  [%.0fs]" % (len(xl), len(cl), outp, time.time() - t0))


if __name__ == "__main__":
    main()
