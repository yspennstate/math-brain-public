"""Hazard bound (H) for Rademacher sums at the scale of the largest step.

X = sum_j w_j eps_j, integer weights 0 < w_j <= a (a may exceed every weight), sigma^2 = sum w_j^2.
For t >= 0 with no atom of X at t - a or t + a:
    ratio(t) = P[X > t + a] / ( (1 + sigma/a) * P[t - a < X < t + a] ).
(H) says ratio <= C for an absolute constant C.  FLOW section 11(i): (H) plus the Kolmogorov-Rogozin inequality
gives the Cross-Stay inequality, hence FEI for threshold functions.

usage:
  python hazard.py rand  reps maxN maxw seed      random weight multisets, all t, a in {max w, max w + 1/2, 2 max w, 5 max w}
  python hazard.py hill  iters maxN maxw seed     hill-climb on the weights for the largest ratio
  python hazard.py one   a  w1 w2 ...             one multiset, prints the ten largest ratios with their t
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


def ratios(ws, a):
    """all admissible t in (1/2) Z, t >= 0; returns list of (ratio, t, tail, window)."""
    p, W = pmf(ws)
    sig = float(np.sqrt(sum(w * w for w in ws)))
    cum = np.concatenate([[0.0], np.cumsum(p)])      # cum[k] = P[X < k - W]
    out = []
    for t2 in range(0, 2 * W + 2):
        t = t2 / 2.0
        hi = t + a
        lo = t - a
        # atoms at lo, hi?
        tie = False
        for v in (lo, hi):
            if abs(v - round(v)) < 1e-9:
                k = int(round(v)) + W
                if 0 <= k <= 2 * W and p[k] > 0:
                    tie = True
        if tie:
            continue
        # integers x with lo < x < hi ; tail x > hi
        x0 = int(np.floor(lo)) + 1
        x1 = int(np.ceil(hi)) - 1
        k0 = min(max(x0 + W, 0), 2 * W + 1)
        k1 = min(max(x1 + W + 1, 0), 2 * W + 1)
        win = cum[k1] - cum[k0] if k1 > k0 else 0.0
        kt = min(max(int(np.floor(hi)) + 1 + W, 0), 2 * W + 1)
        tail = 1.0 - cum[kt]
        if tail <= 1e-300:
            break
        if win <= 0:
            out.append((float('inf'), t, tail, win))
        else:
            out.append((tail / ((1 + sig / a) * win), t, tail, win))
    return out, sig


def best(ws, a):
    out, sig = ratios(ws, a)
    if not out:
        return 0.0, None, sig
    r = max(out)
    return r[0], r, sig


def a_values(ws):
    m = max(ws)
    return [m, m + 0.5, 2 * m, 5 * m]


def main():
    mode = sys.argv[1]
    if mode == 'one':
        a = float(sys.argv[2])
        ws = [int(x) for x in sys.argv[3:]]
        out, sig = ratios(ws, a)
        out.sort(reverse=True)
        print('sigma=%.3f a=%g' % (sig, a))
        for r in out[:10]:
            print('  ratio=%.4f t=%.1f tail=%.3e window=%.3e' % r)
        return
    n1 = int(sys.argv[2])
    maxN = int(sys.argv[3])
    maxw = int(sys.argv[4])
    rng = np.random.default_rng(int(sys.argv[5]))
    top = (0.0, None, None, None)
    if mode == 'rand':
        for rep in range(n1):
            N = int(rng.integers(1, maxN + 1))
            kind = rng.integers(0, 4)
            if kind == 0:
                ws = [int(x) for x in rng.integers(1, maxw + 1, N)]
            elif kind == 1:
                ws = [maxw] * int(rng.integers(1, 4)) + [1] * N
            elif kind == 2:
                b = int(rng.integers(1, maxw + 1))
                ws = [b] * N
            else:
                ws = [int(max(1, round(maxw * rng.random() ** 3))) for _ in range(N)]
            for a in a_values(ws):
                r, rec, sig = best(ws, a)
                if r > top[0]:
                    top = (r, rec, a, sorted(ws))
                    print('ratio=%.4f a=%g t=%.1f tail=%.3e win=%.3e sigma=%.2f ws=%s'
                          % (r, a, rec[1], rec[2], rec[3], sig, sorted(ws)))
                    sys.stdout.flush()
    elif mode == 'hill':
        N = int(rng.integers(2, maxN + 1))
        ws = [int(x) for x in rng.integers(1, maxw + 1, N)]
        amul = float(rng.choice([1.0, 1.0, 1.5, 2.0, 4.0]))

        def val(ws):
            a = amul * max(ws)
            return best(ws, a) + (a,)
        cur = val(ws)
        for it in range(n1):
            new = list(ws)
            mv = rng.integers(0, 4)
            if mv == 0 and len(new) < maxN:
                new.append(int(rng.integers(1, maxw + 1)))
            elif mv == 1 and len(new) > 1:
                new.pop(int(rng.integers(0, len(new))))
            else:
                i = int(rng.integers(0, len(new)))
                new[i] = int(min(maxw, max(1, new[i] + rng.integers(-3, 4))))
            v = val(new)
            if v[0] >= cur[0]:
                if v[0] > cur[0] + 1e-12:
                    print('it=%d ratio=%.4f a=%g t=%.1f tail=%.3e win=%.3e sigma=%.2f ws=%s'
                          % (it, v[0], v[3], v[1][1], v[1][2], v[1][3], v[2], sorted(new)))
                    sys.stdout.flush()
                ws, cur = new, v
    print('done')


if __name__ == '__main__':
    main()
