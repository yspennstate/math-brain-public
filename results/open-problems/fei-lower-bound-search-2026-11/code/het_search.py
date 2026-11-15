"""het_search.py - compositions whose gates take independent inputs of DIFFERENT biases.

For g on uniform bits: p = Pr[g = -1], G = entropy of the normalised non-constant spectrum, J = I / Var, and the
potential U(g) = G - c J at the record c.  For a gate F with independent inputs g_1..g_k,
    G(F(g)) = G_pvec(F) + sum_j J^(j) G(g_j),      J(F(g)) = sum_j J^(j) J(g_j),
where w_T are the normalised pvec-biased Fourier weights of F and J^(j) = sum_{T contains j} w_T.  With W the value
table of the homogeneous towers (tower_vi.py --dump), a function g with slack(g) = U(g) + W(p_g) > 0 gives
sup H/I > c.  A bit and the record gate on bits have slack 0.

The program keeps a menu: for each bin of log-odds the function with the largest U found so far, as an explicit tree
(gate, children).  Each round it (1) forms AND and XOR of every pair of menu entries, (2) for every library gate runs
coordinate ascent over which menu entry feeds each input, offering every evaluated combination to the menu.  Output
negation is offered too, so the menu stays symmetric under p -> 1 - p and input negations need no extra code.

usage: python het_search.py W_table.txt OUTPREFIX --lib FILE[:maxn[:maxcount]] [--lib ...] [--rounds R] [--bins B]
       [--span L] [--starts S] [--seconds T] [--seed N]
library files have lines "n hex" (hex of the truth table, input x at bit x).
"""
import argparse
import sys
import time

import numpy as np

C = 6.521845710923


def xlogx_sum(w):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(w > 1e-300, w * np.log2(np.where(w > 1e-300, w, 1.0)), 0.0).sum(axis=-1)


class Menu:
    def __init__(self, nbins, span, Wof):
        self.nbins, self.span, self.Wof = nbins, span, Wof
        self.p, self.G, self.J, self.gate, self.kids = [], [], [], [], []
        self.node = -np.ones(nbins + 1, dtype=np.int64)     # node index per bin
        self.U = np.full(nbins + 1, -np.inf)
        self.improved = 0
        self.refresh()

    def refresh(self):
        idx = self.node[self.node >= 0]
        self.ep = np.array([self.p[i] for i in idx])
        self.eG = np.array([self.G[i] for i in idx])
        self.eJ = np.array([self.J[i] for i in idx])
        self.eid = idx.copy()
        self.eU = self.eG - C * self.eJ
        self.eslack = self.eU + self.Wof(self.ep) if len(idx) else np.array([])

    def offer(self, p, G, J, gate, kidfn):
        """p, G, J arrays; gate id; kidfn(i) -> tuple of child node ids for offer i.  Offers f and NOT f."""
        p = np.asarray(p, dtype=np.float64).ravel()
        G = np.asarray(G, dtype=np.float64).ravel()
        J = np.asarray(J, dtype=np.float64).ravel()
        ok = np.isfinite(G) & np.isfinite(J) & (p > 0) & (p < 1)
        t = np.zeros_like(p)
        t[ok] = np.log2(p[ok] / (1 - p[ok]))
        ok &= np.abs(t) < self.span
        if not ok.any():
            return
        U = G - C * J
        b = np.round((t + self.span) / (2 * self.span) * self.nbins).astype(np.int64)
        for sign in (0, 1):
            bb = (self.nbins - b) if sign else b
            cand = np.flatnonzero(ok & (U > self.U[np.clip(bb, 0, self.nbins)] + 1e-9))
            if cand.size == 0:
                continue
            order = cand[np.argsort(U[cand], kind="stable")]
            win = {}
            for i in order:              # ascending U: the last one written per bin is the best
                win[int(bb[i])] = int(i)
            for bi, i in win.items():
                self.p.append(float(1 - p[i]) if sign else float(p[i]))
                self.G.append(float(G[i]))
                self.J.append(float(J[i]))
                self.gate.append(-(gate + 1) if sign else gate + 1)
                self.kids.append(tuple(kidfn(i)))
                self.node[bi] = len(self.p) - 1
                self.U[bi] = U[i]
                self.improved += 1

    def recipe(self, i, names, depth=0, out=None, maxlines=400):
        out = [] if out is None else out
        if len(out) >= maxlines:
            return out
        g = self.gate[i]
        nm = "bit" if g == 0 else ("NOT " if g < 0 else "") + names[abs(g) - 1]
        out.append("%s%s  p=%.12f G=%.12f J=%.12f U=%.9f" % ("  " * depth, nm, self.p[i], self.G[i], self.J[i],
                                                             self.G[i] - C * self.J[i]))
        for kchild in self.kids[i]:
            self.recipe(kchild, names, depth + 1, out, maxlines)
        return out


class Gate:
    def __init__(self, n, hx, name):
        self.n, self.name = n, name
        tab = int(hx, 16)
        bits = np.unpackbits(np.frombuffer(tab.to_bytes(max(1, (1 << n) // 8), "little"), dtype=np.uint8),
                             bitorder="little")[: 1 << n]
        self.vals = 1.0 - 2.0 * bits.astype(np.float64)
        m = 1 << (n - 1)
        idx = np.arange(m)
        self.B = np.stack([(idx >> i) & 1 for i in range(n - 1)], axis=1).astype(np.float64) if n > 1 else np.zeros((1, 0))

    def sweep(self, pv, j, pc):
        """input j ranges over biases pc (array), the others fixed at pv.  Returns p', G, Jmat (len(pc), n)."""
        n = self.n
        a = self.vals.copy()
        for i in range(n):
            if i == j:
                continue
            p = pv[i]
            s = np.sqrt(p * (1 - p))
            a = a.reshape(-1, 2, 1 << i)
            lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
            a[:, 0, :] = (1 - p) * lo + p * hi
            a[:, 1, :] = s * (hi - lo)
            a = a.reshape(-1)
        a = a.reshape(-1, 2, 1 << j)
        lo, hi = a[:, 0, :].reshape(-1), a[:, 1, :].reshape(-1)
        A0 = np.outer(1 - pc, lo) + np.outer(pc, hi)
        A1 = np.outer(np.sqrt(pc * (1 - pc)), hi - lo)
        mean = A0[:, 0].copy()
        var = 1 - mean * mean
        good = var > 1e-13
        v = np.where(good, var, 1.0)[:, None]
        w0 = A0 * A0 / v
        w0[:, 0] = 0
        w1 = A1 * A1 / v
        G = -(xlogx_sum(w0) + xlogx_sum(w1))
        Jm = np.empty((len(pc), n))
        with np.errstate(all="ignore"):                 # Accelerate raises spurious flags in matmul
            other = (w0 + w1) @ self.B                  # columns: the inputs other than j, in order
        cols = [i for i in range(n) if i != j]
        for c, i in enumerate(cols):
            Jm[:, i] = other[:, c]
        Jm[:, j] = w1.sum(axis=1)
        G = np.where(good, G, np.nan)
        return (1 - mean) / 2, G, Jm


def pair_ops(pa, pb):
    """AND and XOR of independent inputs with biases pa, pb (arrays).  Returns list of (p', G, J1, J2)."""
    out = []
    with np.errstate(divide="ignore", invalid="ignore"):
        sa2, sb2 = pa * (1 - pa), pb * (1 - pb)
        q = pa * pb
        var = 4 * q * (1 - q)
        w = np.stack([4 * pb * pb * sa2 / var, 4 * pa * pa * sb2 / var, 4 * sa2 * sb2 / var], axis=-1)
        out.append((q, -xlogx_sum(w), w[..., 0] + w[..., 2], w[..., 1] + w[..., 2]))
        ma, mb = 1 - 2 * pa, 1 - 2 * pb
        var = 1 - ma * ma * mb * mb
        w = np.stack([(1 - ma * ma) * mb * mb / var, ma * ma * (1 - mb * mb) / var, (1 - ma * ma) * (1 - mb * mb) / var],
                     axis=-1)
        out.append(((1 - ma * mb) / 2, -xlogx_sum(w), w[..., 0] + w[..., 2], w[..., 1] + w[..., 2]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wfile")
    ap.add_argument("out")
    ap.add_argument("--lib", action="append", default=[])
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--bins", type=int, default=1200)
    ap.add_argument("--span", type=float, default=9.0)
    ap.add_argument("--starts", type=int, default=4)
    ap.add_argument("--seconds", type=float, default=3e5)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--maxelem", type=float, default=4e6)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    t_start = time.time()

    wt = np.loadtxt(args.wfile, comments="#")
    tw, Wv = wt[:, 0], wt[:, 1]

    def Wof(p):
        p = np.clip(np.asarray(p, dtype=np.float64), 1e-12, 1 - 1e-12)
        return np.interp(np.clip(np.log2(p / (1 - p)), tw[0], tw[-1]), tw, Wv)

    gates, names = [], ["AND2", "XOR2"]
    for spec in args.lib:
        parts = spec.split(":")
        maxn = int(parts[1]) if len(parts) > 1 and parts[1] else 99
        maxc = int(parts[2]) if len(parts) > 2 else 10 ** 9
        cnt = 0
        with open(parts[0], encoding="utf-8") as fh:
            for ln, line in enumerate(fh):
                f = line.split()
                if len(f) < 2 or line.startswith("#"):
                    continue
                n = int(f[0])
                if n < 3 or n > maxn or cnt >= maxc:
                    continue
                gates.append(Gate(n, f[1], "%s#%d(n=%d)" % (parts[0].split("/")[-1], ln + 1, n)))
                names.append(gates[-1].name)
                cnt += 1
    log = open(args.out + ".log", "a", encoding="utf-8")

    def say(s):
        print(s, flush=True)
        log.write(s + "\n")
        log.flush()

    say("# het_search wfile=%s gates=%d bins=%d span=%g starts=%d seed=%d c=%.12f W(1/2)=%.12f" % (
        args.wfile, len(gates), args.bins, args.span, args.starts, args.seed, C, float(Wof(0.5))))
    menu = Menu(args.bins, args.span, Wof)
    menu.offer(np.array([0.5]), np.array([0.0]), np.array([1.0]), -1, lambda i: ())   # the bit: gate id 0
    menu.refresh()

    def report(tag):
        s = menu.eslack
        o = np.argsort(-s)[:6]
        say("%s: entries %d, improved %d, %.0f s; largest slack: %s" % (
            tag, len(s), menu.improved, time.time() - t_start,
            "  ".join("%+.9f@p=%.6f" % (s[i], menu.ep[i]) for i in o)))
        nb = np.flatnonzero((s > 1e-7) & (np.abs(menu.ep - 0.5) > 1e-9) | (s > 1e-6))
        if nb.size:
            say("!!! POSITIVE SLACK - verify before believing")
            for i in nb[np.argsort(-s[nb])][:3]:
                for line in menu.recipe(int(menu.eid[i]), names):
                    say("    " + line)

    for rnd in range(1, args.rounds + 1):
        menu.improved = 0
        # (1) all pairs under AND and XOR
        ep, eG, eJ, eid = menu.ep, menu.eG, menu.eJ, menu.eid
        M = len(ep)
        A, B = np.meshgrid(ep, ep, indexing="ij")
        GA, GB = np.meshgrid(eG, eG, indexing="ij")
        JA, JB = np.meshgrid(eJ, eJ, indexing="ij")
        for gi, (q, g, j1, j2) in enumerate(pair_ops(A, B)):
            menu.offer(q, g + j1 * GA + j2 * GB, j1 * JA + j2 * JB, gi,
                       lambda i, eid=eid, M=M: (int(eid[i // M]), int(eid[i % M])))
        menu.refresh()
        report("round %d pairs" % rnd)
        # (2) library gates, coordinate ascent
        for gnum, gt in enumerate(gates):
            if time.time() - t_start > args.seconds:
                break
            ep, eG, eJ, eid, es = menu.ep, menu.eG, menu.eJ, menu.eid, menu.eslack
            M = len(ep)
            chunk = max(1, int(args.maxelem // (1 << (gt.n - 1))))
            top = np.argsort(-es)[: max(8, M // 20)]
            ibit = int(np.argmin(np.abs(ep - 0.5)))
            for st in range(args.starts):
                if st == 0:
                    cur = np.full(gt.n, ibit)
                elif st == 1:
                    cur = rng.choice(top, size=gt.n)
                else:
                    cur = rng.integers(0, M, size=gt.n)
                best = -np.inf
                for sweep in range(3):
                    moved = False
                    for j in rng.permutation(gt.n):
                        pv = ep[cur]
                        Gs, Js, Ps = [], [], []
                        for c0 in range(0, M, chunk):
                            pp, g, Jm = gt.sweep(pv, j, ep[c0:c0 + chunk])
                            Jo = Jm.copy()
                            Jo[:, j] = 0
                            with np.errstate(all="ignore"):
                                Gs.append(g + Jo @ eG[cur] + Jm[:, j] * eG[c0:c0 + chunk])
                                Js.append(Jo @ eJ[cur] + Jm[:, j] * eJ[c0:c0 + chunk])
                            Ps.append(pp)
                        Gt, Jt, Pt = np.concatenate(Gs), np.concatenate(Js), np.concatenate(Ps)
                        base = cur.copy()
                        menu.offer(Pt, Gt, Jt, 2 + gnum,
                                   lambda i, base=base, j=j, eid=eid: tuple(int(eid[i]) if x == j else int(eid[base[x]])
                                                                            for x in range(len(base))))
                        sl = np.where(np.isfinite(Gt), Gt - C * Jt + Wof(Pt), -np.inf)
                        m = int(np.argmax(sl))
                        if sl[m] > best + 1e-12:
                            best = sl[m]
                            if cur[j] != m:
                                cur[j] = m
                                moved = True
                    if not moved:
                        break
            if gnum % 200 == 199:
                menu.refresh()
                report("round %d gate %d/%d" % (rnd, gnum + 1, len(gates)))
        menu.refresh()
        report("round %d gates" % rnd)
        with open(args.out + ".menu", "w", encoding="utf-8") as fh:
            fh.write("# p U G J slack node gate\n")
            for i in np.argsort(menu.ep):
                fh.write("%.15f %.12f %.12f %.12f %+.12f %d %d\n" % (menu.ep[i], menu.eU[i], menu.eG[i], menu.eJ[i],
                                                                   menu.eslack[i], menu.eid[i], menu.gate[menu.eid[i]]))
        if menu.improved == 0 or time.time() - t_start > args.seconds:
            break
    say("# done %.0f s" % (time.time() - t_start))


if __name__ == "__main__":
    main()
