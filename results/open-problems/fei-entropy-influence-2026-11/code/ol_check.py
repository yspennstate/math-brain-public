"""One-layer comparison (OL) and hazard bound (H) for Rademacher sums, exact check.

X = sum_j w_j eps_j, integer weights 0 < w_j <= a (a integer), t a half-integer (so t +- a are not atoms), t >= 0.
  OL(t) = P[t + a < X <= t + 2a] / P[t - a < X < t + a]            proved <= 2    (FLOW 11(i), Lemma A)
  H(t)  = P[X > t + a] / ((1 + sigma/a) P[t - a < X < t + a])      proved <= 16/3 (FLOW 11(j), Lemma B)
Windows of zero mass with a positive numerator would be counterexamples and are reported as inf.

usage: python ol_check.py reps maxN maxw seed
"""
import sys
import numpy as np


def pmf(ws):
    W = int(sum(ws))
    p = np.zeros(2 * W + 1)
    p[W] = 1.0
    for w in ws:
        q = np.zeros_like(p)
        q[w:] += 0.5 * p[:-w]
        q[:-w] += 0.5 * p[w:]
        p = q
    return p, W


def scan(ws, a):
    p, W = pmf(ws)
    sig = float(np.sqrt(sum(w * w for w in ws)))
    cum = np.concatenate([[0.0], np.cumsum(p)])     # cum[k] = P[X <= k - 1 - W]

    def le(v):                                       # P[X <= v], v real
        k = int(np.floor(v)) + W + 1
        return float(cum[min(max(k, 0), 2 * W + 1)])
    bo = (0.0, None)
    bh = (0.0, None)
    for i in range(0, W + 2):
        t = i + 0.5
        win = le(t + a) - le(t - a)
        lay = le(t + 2 * a) - le(t + a)
        tail = 1.0 - le(t + a)
        if tail <= 0:
            break
        ro = float('inf') if (win <= 0 and lay > 0) else (lay / win if win > 0 else 0.0)
        rh = float('inf') if win <= 0 else tail / ((1 + sig / a) * win)
        if ro > bo[0]:
            bo = (ro, t)
        if rh > bh[0]:
            bh = (rh, t)
    return bo, bh, sig


def main():
    reps, maxN, maxw, seed = (int(x) for x in sys.argv[1:5])
    rng = np.random.default_rng(seed)
    topo = 0.0
    toph = 0.0
    for rep in range(reps):
        N = int(rng.integers(1, maxN + 1))
        kind = int(rng.integers(0, 6))
        if kind == 0:
            ws = [int(x) for x in rng.integers(1, maxw + 1, N)]
        elif kind == 1:
            ws = [maxw] * int(rng.integers(1, 6)) + [1] * N
        elif kind == 2:
            ws = [int(rng.integers(1, maxw + 1))] * N
        elif kind == 3:
            ws = [int(max(1, round(maxw * rng.random() ** 3))) for _ in range(N)]
        elif kind == 4:
            lo = maxw // 2 + 1
            ws = [int(x) for x in rng.integers(lo, maxw + 1, N)]
        else:
            ws = [int(x) for x in rng.integers(maxw // 2 + 1, maxw + 1, int(rng.integers(1, 8)))] + \
                 [int(x) for x in rng.integers(1, max(2, maxw // 4), N)]
        a = max(ws)
        bo, bh, sig = scan(ws, a)
        if bo[0] > topo:
            topo = bo[0]
            print('OL=%.4f t=%.1f a=%d sigma=%.2f ws=%s' % (bo[0], bo[1], a, sig, sorted(ws)[-12:]))
        if bh[0] > toph:
            toph = bh[0]
            print('H =%.4f t=%.1f a=%d sigma=%.2f ws=%s' % (bh[0], bh[1], a, sig, sorted(ws)[-12:]))
        sys.stdout.flush()
    print('max OL = %.4f   max H = %.4f   (%d weight sets)' % (topo, toph, reps))


if __name__ == '__main__':
    main()
