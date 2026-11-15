"""Hill-climb over truth tables against the thinning predictor of FLOW 12(z).

Objectives (all exact to float64, any Boolean f on n <= 14 bits):
  ov    overhead of the "thin" predictor at noise lam:  log2 K + E_Q log2(1/p) - L(f)
  full  the bound itself:                               log2 K + E_Q log2(1/p)
  mt    tilted excess:                                  E_{T ~ mu} m_lam(T) / I,   m_lam(T) = lam sum_i up(T+i)/up(T)
  ex    the exact erasure cost L(f) (control; sup is at least H/I - 2/ln 2 of the record function)
Notation as in predictor.py. A fixed-lam bound on "full" for all f would prove FEI; "mt" bounded for each fixed lam
is necessary for FEI.

Usage: python ov_hill.py <n> <ov|full|mt|ex> <lam> <seed> <outdir> [hours]
Writes <outdir>/ovhill_n<n>_<obj>_l<lam>_s<seed>.best.txt (rewritten at each new record: value, parts, hex table)
and appends local maxima to .log.txt (one short line each, capped). Stops when <outdir>/STOP exists.
"""
import math
import os
import sys
import time

import numpy as np


def wht(v):
    v = np.array(v, dtype=np.float64)
    n = v.size.bit_length() - 1
    h = 1
    while h < v.size:
        v = v.reshape(-1, 2, h)
        v = np.concatenate((v[:, 0, :] + v[:, 1, :], v[:, 0, :] - v[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return v / (1 << n)


class Ev:
    def __init__(self, n, lam):
        self.n = n
        self.lam = lam
        idx = np.arange(1 << n)
        self.lo = [idx[(idx >> i) & 1 == 0] for i in range(n)]
        self.hi = [l | (1 << i) for i, l in enumerate(self.lo)]
        pc = np.zeros(1 << n, dtype=np.int64)
        for i in range(n):
            pc += (idx >> i) & 1
        self.pc = pc.astype(np.float64)

    def parts(self, f):
        n, lam = self.n, self.lam
        mu = wht(f) ** 2
        I = float((self.pc * mu).sum())
        if I < 1e-12:
            return None
        up = mu.copy()
        for i in range(n):
            up[self.lo[i]] += lam * up[self.hi[i]]
        KI = 0.0
        cI = 0.0
        eI = 0.0
        mI = 0.0
        for i in range(n):
            a = mu[self.lo[i]]
            b = mu[self.hi[i]]
            u0 = up[self.lo[i]]
            u1 = up[self.hi[i]]
            ok = u0 > 0
            r = np.zeros_like(u0)
            r[ok] = u1[ok] / u0[ok]
            p = (1 - lam) * r / (1.0 + (1 - lam) * r)
            KI += float(((a + b) * p).sum())
            m = b > 0
            cI += float((b[m] * np.log2(1.0 / p[m])).sum())
            eI += float((b[m] * np.log2(1.0 + a[m] / b[m])).sum())
            mI += float((a * lam * r).sum())
        return I, math.log2(KI / I), cI / I, eI / I, mI / I

    def value(self, f, obj):
        pr = self.parts(f)
        if pr is None:
            return -1e9, None
        I, lk, c, e, mt = pr
        if obj == "ov":
            v = lk + c - e
        elif obj == "full":
            v = lk + c
        elif obj == "mt":
            v = mt
        else:
            v = e
        return v, pr


def start(n, rng, kind):
    N = 1 << n
    if kind == 0:
        return np.where(rng.random(N) < 0.5, -1.0, 1.0)
    if kind == 1:
        return np.where(rng.random(N) < rng.choice([0.05, 0.1, 0.25]), -1.0, 1.0)
    x = np.arange(N)
    bits = np.array([((x >> i) & 1) * 2 - 1 for i in range(n)], dtype=np.float64)
    if kind == 2:  # random threshold
        w = rng.normal(size=n) * rng.choice([1.0, 3.0], size=n)
        return np.where(w @ bits + rng.normal() * 0.5 > 0, -1.0, 1.0)
    # random DNF of mixed widths
    f = np.zeros(N, dtype=bool)
    for _ in range(int(rng.integers(2, 2 * n))):
        wdt = int(rng.integers(1, 5))
        vs = rng.choice(n, size=wdt, replace=False)
        sg = rng.choice([-1.0, 1.0], size=wdt) if rng.random() < 0.5 else np.ones(wdt)
        t = np.ones(N, dtype=bool)
        for v, s in zip(vs, sg):
            t &= bits[v] == s
        f |= t
    return np.where(f, -1.0, 1.0)


def hexof(f):
    return np.packbits((f < 0).astype(np.uint8)).tobytes().hex()


def main():
    n = int(sys.argv[1])
    obj = sys.argv[2]
    lam = float(sys.argv[3])
    seed = int(sys.argv[4])
    out = sys.argv[5]
    hours = float(sys.argv[6]) if len(sys.argv) > 6 else 1e9
    tag = "ovhill_n%d_%s_l%s_s%d" % (n, obj, sys.argv[3], seed)
    best_path = os.path.join(out, tag + ".best.txt")
    log_path = os.path.join(out, tag + ".log.txt")
    stop = os.path.join(out, "STOP")
    rng = np.random.default_rng(seed)
    ev = Ev(n, lam)
    N = 1 << n
    t0 = time.time()
    gbest = -1e9
    nlog = 0
    evals = 0
    restarts = 0
    while True:
        f = start(n, rng, restarts % 4)
        restarts += 1
        val, pr = ev.value(f, obj)
        evals += 1
        stale = 0
        while stale < 6000 + 40 * N // 16:
            k = 1 if rng.random() < 0.6 else int(rng.integers(2, 4))
            pos = rng.integers(0, N, size=k)
            f[pos] = -f[pos]
            v2, pr2 = ev.value(f, obj)
            evals += 1
            if v2 > val + 1e-12 or (v2 >= val - 1e-12 and rng.random() < 0.05):
                if v2 > val + 1e-12:
                    stale = 0
                val, pr = v2, pr2
            else:
                f[pos] = -f[pos]
                stale += 1
            if val > gbest + 1e-9:
                gbest = val
                with open(best_path, "w") as fh:
                    fh.write("%.9f n %d obj %s lam %s I %.6f log2K %.6f cost %.6f exact %.6f mt %.6f evals %d restarts %d\n%s\n"
                             % (val, n, obj, sys.argv[3], pr[0], pr[1], pr[2], pr[3], pr[4], evals, restarts, hexof(f)))
            if evals % 2000 == 0 and (os.path.exists(stop) or time.time() - t0 > hours * 3600):
                return
        if nlog < 400:
            nlog += 1
            with open(log_path, "a") as fh:
                fh.write("%.6f start %d I %.4f exact %.4f evals %d\n" % (val, (restarts - 1) % 4, pr[0], pr[3], evals))


if __name__ == "__main__":
    main()
