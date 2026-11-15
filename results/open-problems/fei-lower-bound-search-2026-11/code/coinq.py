#!/usr/bin/env python3
"""coinq.py - anneal over Boolean functions g(x, y) on m base bits x and blocks of fresh bits y.

Every point x of the base cube carries one label:
    0: g = +1    1: g = -1    2+2j: g = Y_j    3+2j: g = -Y_j
where Y_j is the AND of k_j fresh uniform bits (Y_j = -1 exactly when all k_j bits are -1).  k_j = 1 is a
plain coin, and with all k_j = 1 this is the family searched by fei_coin.c; the 18-input record is m = 9 with
nine plain coins.  k_j >= 2 gives labels of mean 1 - 2^(1-k_j), which fei_coin cannot express.

The function lives on m + sum k_j uniform bits.  Its Fourier weights are those of
    a'(x) = constant label or (+-)mean of the label's coin,    and for every coin j and nonempty T: b_j^(S)^2 h_j^(T)^2,
so one evaluation costs (coins + 1) 2^m whatever the number of inputs.

Score:  G = entropy of the normalised non-constant weights, J = I / Var, p' = Pr[g = -1],
        slack = G - c J + W(p'),  c = W(1/2) of the table.  slack > 0 would beat the table's constant.

usage: python3 coinq.py WFILE OUT --init lab:FILE[:LINE] | hex:FILE[:LINE] --types 1:12,2:12,3:6
                        [--secs 3000] [--seed 1] [--iters 400000] [--T0 0.01] [--T1 0.00002]
                        [--pedge 0.15] [--qpair 0.6]
       python3 coinq.py WFILE - --selftest
output lines: run seed value slack | G J mean | coins used | types of all coins | labels
"""
import argparse
import math
import sys
import time

import numpy as np


def load_w(fn):
    t, w = [], []
    for ln in open(fn):
        if ln.startswith("#") or not ln.strip():
            continue
        a = ln.split()
        t.append(float(a[0]))
        w.append(float(a[1]))
    return np.array(t), np.array(w)


class Model:
    def __init__(self, m, types, wtab):
        self.m = m
        self.N = N = 1 << m
        self.types = list(types)
        self.k = len(self.types)
        idx = np.arange(N, dtype=np.int64)
        pc = np.zeros(N, dtype=np.int64)
        for i in range(m):
            pc += (idx >> i) & 1
        self.pcS = pc.astype(np.float64)
        par = np.zeros((N, N), dtype=np.int8)
        for i in range(m):
            par ^= (((idx[:, None] >> i) & 1) & ((idx[None, :] >> i) & 1)).astype(np.int8)
        self.H = (1 - 2 * par).astype(np.float64)
        ks = np.array(self.types, dtype=np.float64)
        self.mu = 1.0 - 2.0 ** (1.0 - ks)
        self.sig2 = (2.0 ** ks - 1.0) * 4.0 ** (1.0 - ks)
        self.L = -2.0 * (ks - 1.0) * self.sig2          # sum over nonempty T of v log2 v
        self.K = ks * 2.0 ** (ks - 1.0) * 4.0 ** (1.0 - ks)  # sum over T of |T| v
        self.WX, self.WY = wtab
        self.c = self.Wof(0.5)
        self.lab = np.zeros(N, dtype=np.int64)
        self.R = np.zeros((self.k + 1, N))
        self.R[0] = self.H.sum(axis=0)                  # all labels +1
        self.cnt = np.zeros(self.k, dtype=np.int64)
        self.st = [self.rowstat(r) for r in range(self.k + 1)]

    def Wof(self, p):
        t = math.log2(p / (1.0 - p))
        return float(np.interp(t, self.WX, self.WY))

    def rowstat(self, r):
        w = (self.R[r] / self.N) ** 2
        if r == 0:
            w[0] = 0.0
        nz = w > 0
        e = float(np.sum(w[nz] * np.log2(w[nz])))
        return e, float(np.dot(self.pcS, w)), float(w.sum())

    def contrib(self, x, lab, sgn, dirty):
        if lab < 2:
            self.R[0] += (sgn * (1 - 2 * lab)) * self.H[x]
            dirty.add(0)
        else:
            j = (lab - 2) >> 1
            s = sgn * (1 - 2 * (lab & 1))
            if self.mu[j] != 0.0:
                self.R[0] += (s * self.mu[j]) * self.H[x]
                dirty.add(0)
            self.R[1 + j] += s * self.H[x]
            self.cnt[j] += sgn
            dirty.add(1 + j)

    def apply(self, mv):
        """mv: list of (x, newlabel).  Returns the undo record."""
        dirty = set()
        olds = []
        for x, nl in mv:
            ol = int(self.lab[x])
            olds.append((x, ol))
            if ol == nl:
                continue
            self.contrib(x, ol, -1, dirty)
            self.contrib(x, nl, +1, dirty)
            self.lab[x] = nl
        saved = {r: self.st[r] for r in dirty}
        for r in dirty:
            self.st[r] = self.rowstat(r)
        return olds, saved

    def undo(self, rec):
        olds, saved = rec
        dirty = set()
        for x, ol in reversed(olds):
            nl = int(self.lab[x])
            if ol == nl:
                continue
            self.contrib(x, nl, -1, dirty)
            self.contrib(x, ol, +1, dirty)
            self.lab[x] = ol
        for r, s in saved.items():
            self.st[r] = s

    def score(self):
        e0, i0, w0 = self.st[0]
        var, ent, inf = w0, e0, i0
        for j in range(self.k):
            if self.cnt[j] == 0:
                continue
            ej, ij, wj = self.st[1 + j]
            s2 = self.sig2[j]
            var += s2 * wj
            ent += s2 * ej + wj * self.L[j]
            inf += s2 * ij + wj * self.K[j]
        mean = self.R[0][0] / self.N
        if var < 1e-12 or abs(mean) >= 1.0:
            return -1e9, 0.0, 0.0, mean
        G = -ent / var + math.log2(var)
        J = inf / var
        slack = G - self.c * J + self.Wof((1.0 - mean) / 2.0)
        return slack, G, J, mean

    def set_labels(self, labels):
        self.apply([(x, int(l)) for x, l in enumerate(labels)])

    def labstr(self):
        return "".join(chr(48 + int(l)) for l in self.lab)


def brute(m, types, labels):
    """G, J, mean from the explicit truth table on m + sum(types) bits."""
    n = m + sum(types)
    off = []
    o = m
    for k in types:
        off.append(o)
        o += k
    z = np.arange(1 << n, dtype=np.int64)
    x = z & ((1 << m) - 1)
    f = np.ones(1 << n)
    lab = np.array(labels, dtype=np.int64)[x]
    f[lab == 1] = -1.0
    for j, k in enumerate(types):
        allone = ((z >> off[j]) & ((1 << k) - 1)) == (1 << k) - 1
        Y = np.where(allone, -1.0, 1.0)
        f = np.where(lab == 2 + 2 * j, Y, f)
        f = np.where(lab == 3 + 2 * j, -Y, f)
    a = f.copy()
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        a = np.concatenate((a[:, 0, :] + a[:, 1, :], a[:, 0, :] - a[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    a /= len(a)
    w = a * a
    mean = a[0]
    w[0] = 0.0
    var = w.sum()
    pc = np.zeros(1 << n)
    for i in range(n):
        pc += (z >> i) & 1
    nz = w > 0
    G = -float(np.sum(w[nz] * np.log2(w[nz]))) / var + math.log2(var)
    return G, float(np.dot(pc, w)) / var, float(mean)


def selftest(wtab):
    rng = np.random.default_rng(7)
    worst = 0.0
    for trial in range(6):
        m = 4 + trial % 3
        types = [1, 2, 3, 2, 1][: 3 + trial % 3]
        M = Model(m, types, wtab)
        labels = rng.integers(0, 2 + 2 * len(types), size=1 << m)
        M.set_labels(labels)
        # a few applies and undos on top, to exercise the incremental path
        for _ in range(50):
            rec = M.apply([(int(rng.integers(1 << m)), int(rng.integers(2 + 2 * len(types))))])
            if rng.random() < 0.5:
                M.undo(rec)
        s, G, J, mean = M.score()
        G2, J2, mean2 = brute(m, types, M.lab)
        d = max(abs(G - G2), abs(J - J2), abs(mean - mean2))
        worst = max(worst, d)
        print("selftest m %d types %s  G %.12f %.12f  J %.12f %.12f  mean %.6f %.6f  diff %.2e" % (
            m, types, G, G2, J, J2, mean, mean2, d))
    print("selftest worst diff %.2e %s" % (worst, "OK" if worst < 1e-9 else "FAIL"))
    return worst < 1e-9


def read_init(spec, wtab, types):
    kind, rest = spec.split(":", 1)
    parts = rest.split(":")
    fn = parts[0]
    line = int(parts[1]) if len(parts) > 1 else 0
    rows = [ln for ln in open(fn) if ln.strip() and not ln.startswith("#")]
    a = rows[line].split()
    m = int(a[0])
    if kind == "hex":
        v = int(a[1], 16)
        labels = [(v >> x) & 1 for x in range(1 << m)]
        return m, list(types), labels
    k0 = int(a[1])
    labels = [ord(ch) - 48 for ch in a[2]]
    assert len(labels) == 1 << m
    # the file's k0 plain coins come first, then the pool
    return m, [1] * k0 + list(types), labels


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wfile")
    ap.add_argument("out")
    ap.add_argument("--init")
    ap.add_argument("--types", default="1:8,2:12,3:6")
    ap.add_argument("--secs", type=float, default=3000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--iters", type=int, default=400000)
    ap.add_argument("--T0", type=float, default=0.01)
    ap.add_argument("--T1", type=float, default=0.00002)
    ap.add_argument("--pedge", type=float, default=0.15)
    ap.add_argument("--qpair", type=float, default=0.6)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--jmin", type=float, default=1.2)
    ap.add_argument("--pad", type=int, default=0)
    ap.add_argument("--pcube", type=float, default=0.0)
    a = ap.parse_args()
    wtab = load_w(a.wfile)
    if a.selftest:
        sys.exit(0 if selftest(wtab) else 1)
    pool = []
    for tok in a.types.split(","):
        k, c = tok.split(":")
        pool += [int(k)] * int(c)
    m, types, labels = read_init(a.init, wtab, pool)
    if a.pad > 0:
        # --pad k: k new base inputs that the start function ignores (same G, J and slack as the start)
        labels = list(labels) * (1 << a.pad)
        m += a.pad
    M = Model(m, types, wtab)
    M.set_labels(labels)
    # a single bit has slack 0 (G 0, J 1) and an annealer drifts to it: states with J below jmin are penalised,
    # so every slack this program prints for J < jmin is the penalised one (lower than the true slack)
    _raw_score = M.score

    def _pen_score():
        s, G, J, mean = _raw_score()
        return s - 4.0 * max(0.0, a.jmin - J), G, J, mean
    M.score = _pen_score
    rng = np.random.default_rng(a.seed)
    N, k = M.N, M.k
    kinds = sorted(set(types))
    out = open(a.out, "a")
    tstr = "".join(str(t) for t in types)

    def emit(run, tag=""):
        s, G, J, mean = M.score()
        val = (G + M.Wof((1.0 - mean) / 2.0)) / J if J > 0 else 0.0
        used = [types[j] for j in range(k) if M.cnt[j] > 0]
        out.write("%d %d %.12f %+.12f | %.12f %.12f %.12f | %d (%s) | %s | %s\n" % (
            run, a.seed, val, s, G, J, mean, len(used),
            " ".join("%d:%d" % (t, used.count(t)) for t in kinds), tstr, M.labstr()))
        if s > 1e-7:
            out.write("!!! POSITIVE SLACK %+.12f (check from an explicit table before believing)\n" % s)
        out.flush()

    out.write("# coinq m %d init %s types %s seed %d c %.12f T0 %g T1 %g iters %d\n" % (
        m, a.init, a.types, a.seed, M.c, a.T0, a.T1, a.iters))
    emit(-1)
    init_lab = M.lab.copy()
    gbest = M.score()[0]
    gbest_lab = M.lab.copy()

    def coinlabel():
        cand = [j for j in range(k) if M.cnt[j] > 0]
        for t in kinds:
            for j in range(k):
                if types[j] == t and M.cnt[j] == 0:
                    cand.append(j)
                    break
        j = cand[int(rng.integers(len(cand)))]
        return 2 + 2 * j + int(rng.integers(2))

    def anylabel():
        if rng.random() < 0.5:
            return int(rng.integers(2))
        return coinlabel()

    t_end = time.time() + a.secs
    run = 0
    while time.time() < t_end:
        start = init_lab if run % 2 == 0 else gbest_lab
        M.apply([(x, int(l)) for x, l in enumerate(start)])
        cur = M.score()[0]
        rbest = cur
        for it in range(a.iters):
            if (it & 1023) == 0 and time.time() > t_end:
                break
            T = a.T0 * (a.T1 / a.T0) ** (it / a.iters)
            if rng.random() < a.pedge:
                x = int(rng.integers(N))
                l = coinlabel()
                mv = [(x, l), (x ^ (1 << int(rng.integers(m))), l)]
            else:
                mv = [(int(rng.integers(N)), anylabel())]
            if rng.random() < a.qpair:
                mv.append((int(rng.integers(N)), anylabel()))
            if a.pcube > 0 and rng.random() < a.pcube:
                # --pcube: one label on a whole subcube of dimension 1 to 3, or a subcube copied from its mirror image
                d = 1 + int(rng.integers(3))
                bits = [int(b) for b in rng.choice(m, size=d, replace=False)]
                x0 = int(rng.integers(N))
                pts = [x0]
                for b in bits:
                    pts = pts + [p ^ (1 << b) for p in pts]
                if rng.random() < 0.5:
                    l = anylabel()
                    mv = [(p, l) for p in pts]
                else:
                    fb = 1 << int(rng.integers(m))
                    mv = [(p, int(M.lab[p ^ fb])) for p in pts]
            rec = M.apply(mv)
            new = M.score()[0]
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
                if cur > rbest + 1e-12:
                    rbest = cur
                    if cur > gbest + 1e-10:
                        gbest = cur
                        gbest_lab = M.lab.copy()
                        emit(run)
            else:
                M.undo(rec)
        out.write("# run %d end: run best %+.12f global best %+.12f\n" % (run, rbest, gbest))
        out.flush()
        run += 1
    M.apply([(x, int(l)) for x, l in enumerate(gbest_lab)])
    out.write("BEST ")
    emit(run)
    out.close()


if __name__ == "__main__":
    main()
