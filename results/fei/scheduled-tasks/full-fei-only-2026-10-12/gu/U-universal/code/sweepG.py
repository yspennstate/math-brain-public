"""Structured sweep of G/I (G = sum_i Delta_i U), U/I, H/I at larger n.  EVIDENCE."""
import numpy as np, json, time, sys
from feilib import spectrum, entropy, influences, restrict, nbits, fwht_int
from upward import Uprime

def evalf(t):
    t = np.asarray(t, dtype=np.int64); n = nbits(len(t)); p = spectrum(t); inf = influences(p, n); I = float(inf.sum())
    if I < 1e-12: return None
    U = float(Uprime(p, n)); H = float(entropy(p)); G = 0.0; mn = np.inf; mx = -np.inf
    for i in range(n):
        if inf[i] < 1e-15: continue
        d = U - 0.5 * (float(Uprime(spectrum(restrict(t, n, i, 0)), n - 1)) + float(Uprime(spectrum(restrict(t, n, i, 1)), n - 1)))
        G += d; mn = min(mn, d / inf[i]); mx = max(mx, d / inf[i])
    return dict(n=n, GI=G / I, UI=U / I, HI=H / I, minloc=mn, maxloc=mx, I=I)

def bits_of(N, n): xs = np.arange(N); return [(xs >> i) & 1 for i in range(n)]

def compose(g, n_g, h, n_h):
    """f(x^1..x^k) = g(h(x^1),...,h(x^k)); variable blocks of size n_h; g indexed with bit j = (h(x^j)==-1)."""
    n = n_g * n_h; N = 1 << n; xs = np.arange(N); idx = np.zeros(N, dtype=np.int64)
    for j in range(n_g):
        blk = (xs >> (j * n_h)) & ((1 << n_h) - 1)
        hv = h[blk]
        idx |= ((hv == -1).astype(np.int64) << j)
    return g[idx]

def tribes_t(w, m):
    n = w * m; N = 1 << n; xs = np.arange(N); sat = np.zeros(N, bool)
    for j in range(m): sat |= (((xs >> (j * w)) & ((1 << w) - 1)) == (1 << w) - 1)
    return np.where(sat, -1, 1)

def addressing_t(a):
    n = a + (1 << a); N = 1 << n; xs = np.arange(N); addr = xs & ((1 << a) - 1)
    return np.where(((xs >> (a + addr)) & 1) == 1, -1, 1)

def lex_t(n, tb):
    N = 1 << n; xs = np.arange(N); val = np.zeros(N, dtype=np.int64)
    for i in range(n): val = val * 2 + ((xs >> i) & 1)
    T = int(''.join(str(b) for b in tb[:n]).ljust(n, '0'), 2); return np.where(val < T, -1, 1)

def ltf_t(n, w, thr):
    N = 1 << n; xs = np.arange(N); X = 1 - 2 * np.stack([(xs >> i) & 1 for i in range(n)], 1)
    return np.where(X @ w > thr, 1, -1)

if __name__ == "__main__":
    res = {}; t0 = time.time()
    g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
    maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
    and2 = np.array([1, 1, 1, -1]); xor2 = np.array([1, -1, -1, 1]); or2 = np.array([1, -1, -1, -1])
    cases = {}
    cases['g5'] = g5
    cases['g5 o and2'] = compose(g5, 5, and2, 2)
    cases['g5 o or2'] = compose(g5, 5, or2, 2)
    cases['g5 o maj3'] = compose(g5, 5, maj3, 3)
    cases['maj3 o g5'] = compose(maj3, 3, g5, 5)
    cases['and2 o g5'] = compose(and2, 2, g5, 5)
    cases['g5 o xor2'] = compose(g5, 5, xor2, 2)
    for w, m in [(3, 5), (4, 4), (5, 3), (2, 8)]: cases[f'tribes{w}x{m}'] = tribes_t(w, m)
    for a in [3, 4]: cases[f'addr{a}'] = addressing_t(a)
    for pat in ['01', '011', '001', '0001', '0101101']: cases[f'lex{pat}_16'] = lex_t(16, [int(c) for c in (pat * 30)[:16]])
    rng = np.random.default_rng(5)
    for s in range(3): cases[f'ltf16_{s}'] = ltf_t(16, rng.normal(size=16), 0.0); cases[f'ltf16b_{s}'] = ltf_t(16, rng.normal(size=16), 4.0)
    for s in range(2): cases[f'rand12_{s}'] = rng.choice([-1, 1], size=1 << 12)
    for k, t in cases.items():
        r = evalf(t); res[k] = r
        print(f"{k:14s} n={r['n']:2d} G/I={r['GI']:.3f} U/I={r['UI']:.3f} H/I={r['HI']:.3f} minloc={r['minloc']:.3f} maxloc={r['maxloc']:.3f} ({time.time()-t0:.0f}s)", flush=True)
    json.dump(res, open("../data/sweepG.json", "w"), indent=1)
