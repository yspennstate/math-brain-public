"""Search over transitive bases for the largest self-tower value of G = E_1/Inf_1 (FLOW 12(y) item 4).

Base F on k = a*b variables, invariant under Z_a x Z_b acting on the a x b grid of coordinates (a = 1: cyclic
shifts). Such F is transitive, so every self-tower F^(r) is transitive and G_r = E_1/Inf_1 = sum_i E_i / I is a
lower bound for G* and A*. The levels are computed with the composition law, in the cancellation-free form
    R' = sum_{A' nonempty} t^{|A'|} Phi(K_{A'}^2, K_{A'+1}^2 a) + (sum_{A'} t^{|A'|} K_{A'+1}^2) R,
    G  = (R + Phi(c^2, a)) / Inf,
where R = E - Phi(c^2, a) is the erasure entropy without the empty pair.

Usage: python tower_hill.py a b seed sweeps outdir [init] [temp]
  init: random (default) | pm33 (only a = b = 3) | best:<file .npy of orbit signs>
Stops early if a file named STOP exists in outdir. Writes <outdir>/tower_a<a>_b<b>_s<seed>.txt (log) and
.best.txt (value, depth, truth table in hex).
"""
import itertools
import os
import sys
import time
import numpy as np


def wht(v):
    a = np.array(v, dtype=np.float64)
    n = a.size.bit_length() - 1
    h = 1
    while h < a.size:
        a = a.reshape(-1, 2, h)
        a = np.concatenate((a[:, 0, :] + a[:, 1, :], a[:, 0, :] - a[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return a / (1 << n)


def orbits(a, b):
    k = a * b
    N = 1 << k
    idx = np.arange(N, dtype=np.int64)

    def act(x, da, db):
        y = np.zeros_like(x)
        for u in range(a):
            for v in range(b):
                src = u * b + v
                dst = ((u + da) % a) * b + (v + db) % b
                y |= ((x >> src) & 1) << dst
        return y

    rep = idx.copy()
    for da in range(a):
        for db in range(b):
            if da or db:
                rep = np.minimum(rep, act(idx, da, db))
    reps, inv = np.unique(rep, return_inverse=True)
    return reps.size, inv


def phi(p, q):
    s = p + q
    out = np.zeros_like(s)
    for x in (p, q):
        m = x > 0
        out[m] -= x[m] * np.log2(x[m] / s[m])
    return out


def phi1(p, q):
    s = p + q
    out = 0.0
    for x in (p, q):
        if x > 0:
            out -= x * np.log2(x / s)
    return out


class Tower:
    def __init__(self, k, maxdepth=14):
        self.k = k
        self.maxdepth = maxdepth
        idx = np.arange(1 << k)
        pc = np.zeros(idx.size, dtype=np.int64)
        for j in range(k):
            pc += (idx >> j) & 1
        self.even = idx[(idx & 1) == 0]
        self.pc_even = pc[self.even]

    def kcoef(self, Fh, c):
        K = Fh.copy()
        h = 1
        while h < K.size:
            K = K.reshape(-1, 2, h)
            K[:, 0, :] += c * K[:, 1, :]
            K = K.reshape(-1)
            h *= 2
        return K

    def value(self, f):
        """max over depths of G_r, and the list of G_r."""
        k = self.k
        Fh = wht(f)
        mu = Fh ** 2
        lo = self.even
        p, q = mu[lo], mu[lo | 1]
        d = float(q.sum())
        if d < 1e-12:
            return 0.0, []
        c, a = float(Fh[0]), float(mu[1])
        R = float(phi(p[1:], q[1:]).sum())
        gs = [(R + phi1(c * c, a)) / d]
        for r in range(2, self.maxdepth + 1):
            K = self.kcoef(Fh, c)
            t = 1.0 - c * c
            if t <= 0:
                break
            w = t ** self.pc_even
            k0, k1 = K[lo] ** 2, K[lo | 1] ** 2
            wk1 = w * k1
            infF = float(wk1.sum())
            R = float((w[1:] * phi(k0[1:], k1[1:] * a)).sum()) + infF * R
            c, a, d = float(K[0]), float(K[1] ** 2 * a), infF * d
            if d < 1e-200 or a < 1e-250:
                break
            gs.append((R + phi1(c * c, a)) / d)
        return max(gs), gs


def pm33():
    perms = list(itertools.permutations(range(3)))
    f = np.ones(512)
    for x in range(512):
        for p in perms:
            if all((x >> (3 * u + p[u])) & 1 for u in range(3)):
                f[x] = -1.0
                break
    return f


def main():
    a, b, seed, sweeps, outdir = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    init = sys.argv[6] if len(sys.argv) > 6 else "random"
    temp = float(sys.argv[7]) if len(sys.argv) > 7 else 0.05
    k = a * b
    os.makedirs(outdir, exist_ok=True)
    tag = os.path.join(outdir, "tower_a%d_b%d_s%d" % (a, b, seed))
    rng = np.random.default_rng(seed)
    norb, inv = orbits(a, b)
    tw = Tower(k)
    if init == "pm33":
        f0 = pm33()
        sg = np.ones(norb)
        sg[inv] = f0
    elif init.startswith("best:"):
        sg = np.load(init[5:])
    else:
        sg = rng.choice([-1.0, 1.0], size=norb)
    cur, gs = tw.value(sg[inv])
    best, bestsg, bestgs = cur, sg.copy(), gs
    log = open(tag + ".txt", "a", encoding="utf-8")
    log.write("start a=%d b=%d k=%d orbits=%d seed=%d init=%s temp=%g value=%.12f\n" % (a, b, k, norb, seed, init, temp, cur))
    log.flush()
    t0 = time.time()
    for sweep in range(sweeps):
        T = temp * (1.0 - sweep / max(1, sweeps)) + 1e-4
        for _ in range(norb):
            j = int(rng.integers(norb))
            sg[j] = -sg[j]
            j2 = -1
            if rng.random() < 0.3:
                j2 = int(rng.integers(norb))
                sg[j2] = -sg[j2]
            v, g = tw.value(sg[inv])
            if v >= cur or rng.random() < np.exp((v - cur) / T):
                cur = v
                if v > best:
                    best, bestsg, bestgs = v, sg.copy(), g
            else:
                sg[j] = -sg[j]
                if j2 >= 0:
                    sg[j2] = -sg[j2]
        log.write("sweep %d T=%.4f cur=%.10f best=%.12f depth=%d sec=%.0f\n" % (
            sweep, T, cur, best, int(np.argmax(bestgs)) + 1, time.time() - t0))
        log.flush()
        f = bestsg[inv]
        bits = "".join("1" if x < 0 else "0" for x in f[::-1])
        with open(tag + ".best.txt", "w", encoding="utf-8") as fh:
            fh.write("value %.15f\ndepth %d\nlevels %s\nmean %.12f\ntable_hex %0*x\n" % (
                best, int(np.argmax(bestgs)) + 1, " ".join("%.10f" % x for x in bestgs), float(f.mean()),
                (1 << k) // 4, int(bits, 2)))
        np.save(tag + ".best.npy", bestsg)
        if os.path.exists(os.path.join(outdir, "STOP")):
            log.write("STOP file seen\n")
            break
    log.write("end best=%.15f\n" % best)
    log.close()


if __name__ == "__main__":
    main()
