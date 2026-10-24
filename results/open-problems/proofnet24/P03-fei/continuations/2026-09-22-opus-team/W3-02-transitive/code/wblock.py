"""Block decomposition for functions invariant under the wreath product S_w wr S_s (blocks of size w).

For the spectral sample S let a_b = |S cap block b|, T = {b : a_b > 0}, J = |T|.  Exact identity
(Theorem 4 of the report):
    H(f) = H(T) + H(a | T) + E sum_b log2 C(w, a_b),    H(T) = H(J) + E log2 C(s, J).
The within-block term is bounded by 7.43 I (proved); H(a|T) <= I.  The open term is
X := E log2 C(s, J).  This script maximises X / I (exhaustively for small classes, by annealing
otherwise) and prints the full decomposition of the maximiser.
Usage: python wblock.py W S [steps restarts]
"""
import sys, os, json, math, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tlib
from anneal import anneal

tlib.setup_process()


def decompose(V, F, w, s, Jo, logCw):
    c = V.coeffs(F); p = c * c; mass = V.osize * p
    H = float((V.osize * tlib.phi(p)).sum()); I = float((V.level * mass).sum())
    Jd = np.bincount(Jo, weights=mass, minlength=s + 1)
    HJ = float(tlib.phi(Jd).sum())
    X = float((mass * np.array([math.log2(math.comb(s, j)) for j in Jo])).sum())
    W = float((mass * logCw).sum())
    HaT = H - HJ - X - W
    return dict(H=H, I=I, HJ=HJ, X=X, within=W, HaT=HaT, mean=float(c[0]))


def main():
    w, s = int(sys.argv[1]), int(sys.argv[2])
    steps = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    restarts = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    gens, n = tlib.wreath_gens(w, s)
    V = tlib.InvariantSpace(gens, n, 'W%d%d' % (w, s))
    Jo = np.zeros(V.k, dtype=np.int64)
    logCw = np.zeros(V.k)
    for o, r in enumerate(V.reps):
        r = int(r)
        for b in range(s):
            ab = bin((r >> (b * w)) & ((1 << w) - 1)).count('1')
            if ab:
                Jo[o] += 1
                logCw[o] += math.log2(math.comb(w, ab))
    logCs = np.array([math.log2(math.comb(s, j)) for j in Jo])
    osize = V.osize.astype(float); level = V.level.astype(float)
    best = (-1, None)
    if V.k <= 17:
        # exhaustive
        k = V.k; free = k - 1
        B = 1 << free
        idx = np.arange(B, dtype=np.int64)
        Fb = np.ones((B, k)); Fb[:, 1:] = 1 - 2 * ((idx[:, None] >> np.arange(free)) & 1)
        C = Fb @ V.K; P = C * C; mass = osize * P
        I = (level * mass).sum(1)
        X = (mass * logCs).sum(1)
        r = np.where(I > 1e-12, X / np.where(I > 1e-12, I, 1), -1)
        j = int(np.argmax(r)); best = (float(r[j]), Fb[j])
        mode = 'exhaustive (%d functions)' % B
    else:
        rng = np.random.default_rng(7)
        order = np.argsort(V.osize, kind='stable')
        mode = 'annealing'
        for rr in range(restarts):
            F = rng.choice([-1.0, 1.0], size=V.k)
            val, bF = anneal(F, V.K, osize, level, logCs, steps, 0.05, 1e-5, 3, 100 + rr,
                             order.astype(np.int64), np.zeros(1, dtype=np.int64), np.ones(1, dtype=np.int64), np.zeros(V.k, dtype=np.int64))
            if val > best[0]:
                best = (val, bF.copy())
    d = decompose(V, best[1], w, s, Jo, logCw)
    print("W%d%d n=%d orbits=%d %s: max E log2 C(s,J) / I = %.4f ; at maximiser H/I=%.3f H(J)/I=%.3f X/I=%.3f H(a|T)/I=%.3f within/I=%.3f mean=%+.3f" % (
        w, s, n, V.k, mode, best[0], d['H'] / d['I'], d['HJ'] / d['I'], d['X'] / d['I'], d['HaT'] / d['I'], d['within'] / d['I'], d['mean']), flush=True)
    # tribes-like reference: OR over blocks of AND_w
    F = np.ones(V.k)
    for o, r in enumerate(V.reps):
        r = int(r)
        full = any(((r >> (b * w)) & ((1 << w) - 1)) == (1 << w) - 1 for b in range(s))
        F[o] = -1.0 if full else 1.0
    d = decompose(V, F, w, s, Jo, logCw)
    print("   tribes OR_s(AND_w): H/I=%.3f H(J)/I=%.3f X/I=%.3f H(a|T)/I=%.3f within/I=%.3f mean=%+.3f" % (
        d['H'] / d['I'], d['HJ'] / d['I'], d['X'] / d['I'], d['HaT'] / d['I'], d['within'] / d['I'], d['mean']), flush=True)


if __name__ == '__main__':
    main()
