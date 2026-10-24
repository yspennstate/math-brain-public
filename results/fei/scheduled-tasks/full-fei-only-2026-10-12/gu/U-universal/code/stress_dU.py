"""Stress the local U-decrement on campaign falsifiers and lexicographic (Hod-type) functions. EVIDENCE."""
import numpy as np, time
from feilib import spectrum, entropy, influences, restrict, nbits
from upward import Uprime

def all_local(t):
    t = np.asarray(t, dtype=np.int64); n = nbits(len(t)); p = spectrum(t); inf = influences(p, n)
    U = float(Uprime(p, n)); H = float(entropy(p))
    dU = np.zeros(n); dH = np.zeros(n)
    for i in range(n):
        pp = spectrum(restrict(t, n, i, 0)); pm = spectrum(restrict(t, n, i, 1))
        dU[i] = U - 0.5 * (float(Uprime(pp, n - 1)) + float(Uprime(pm, n - 1)))
        dH[i] = H - 0.5 * (float(entropy(pp)) + float(entropy(pm)))
    rel = inf > 1e-12
    if not rel.any(): return dict(n=n,H=H,I=0.0,U=U,maxdU=-1,mindU=-1,maxdH=-1,mindH=-1)
    return dict(n=n, H=H, I=float(inf.sum()), U=U, maxdU=float((dU[rel] / inf[rel]).max()), mindU=float((dU[rel] / inf[rel]).min()),
                maxdH=float((dH[rel] / inf[rel]).max()), mindH=float((dH[rel] / inf[rel]).min()))

def lex(n, t_bits):
    """f(x)=-1 iff x < t in lexicographic order with x_0 the most significant bit (bit=1 means x_i=-1)."""
    N = 1 << n; xs = np.arange(N)
    # value of x as binary number with coordinate 0 most significant
    val = np.zeros(N, dtype=np.int64)
    for i in range(n): val = val * 2 + ((xs >> i) & 1)
    T = int(''.join(str(b) for b in t_bits[:n]).ljust(n, '0'), 2)
    return np.where(val < T, -1, 1)

def x009(m):
    # F(t,y)=g(y)(1-2 t 1_{y=0}), g quadratic bent on m bits; coordinate 0 = t
    n = m + 1; N = 1 << n; xs = np.arange(N); tb = xs & 1; yb = xs >> 1
    g = np.ones(N, dtype=np.int64)
    for j in range(m // 2): g *= np.where(((yb >> (2*j)) & 1) & ((yb >> (2*j+1)) & 1), -1, 1)
    return np.where((tb == 1) & (yb == 0), -g, g)

def x002(m):
    # b(t)=(-1)^{t1t2+...+t_{m-2}t_{m-1}} on m-1 bits; g0(y)=b(y1+ym,...,y_{m-1}+ym); g1=(-1)^{ym} g0; F(s,y)=g_s(y)
    n = m + 1; N = 1 << n; xs = np.arange(N); s = xs & 1; y = xs >> 1
    ym = (y >> (m - 1)) & 1
    tt = [((y >> j) & 1) ^ ym for j in range(m - 1)]
    b = np.ones(N, dtype=np.int64)
    for j in range(0, m - 2, 2): b *= np.where(tt[j] & tt[j + 1], -1, 1)
    return np.where(s == 1, np.where(ym == 1, -b, b), b)

if __name__ == "__main__":
    import itertools
    t0 = time.time()
    for m in []:
        r = all_local(x009(m)); print(f"X009 m={m:2d} maxdU/Inf={r['maxdU']:.3f} maxdH/Inf={r['maxdH']:.3f} U/I={r['U']/r['I']:.3f} H/I={r['H']/r['I']:.3f}", flush=True)
    for m in []:
        r = all_local(x002(m)); print(f"X002 m={m:2d} maxdU/Inf={r['maxdU']:.3f} maxdH/Inf={r['maxdH']:.3f} U/I={r['U']/r['I']:.3f} H/I={r['H']/r['I']:.3f}", flush=True)
    # lexicographic functions with random thresholds and with t = 0.0101010... / 0.0110110... patterns
    rng = np.random.default_rng(1)
    best = None
    for n in [8, 10, 12]:
        for trial in range(40):
            tb = list(rng.integers(0, 2, size=n))
            r = all_local(lex(n, tb))
            if r['I'] < 1e-9: continue
            if best is None or r['maxdU'] > best[0]: best = (r['maxdU'], n, tb, r)
        print('lex n', n, 'best maxdU so far', round(best[0], 3), 'H/I', round(best[3]['H']/best[3]['I'], 3), flush=True)
    for pat in ['01', '011', '0011', '001', '0001']:
        for n in [12, 14]:
            tb = [int(c) for c in (pat * 20)[:n]]
            r = all_local(lex(n, tb))
            print(f"lex pattern {pat} n={n} maxdU/Inf={r['maxdU']:.3f} mindU={r['mindU']:.3f} maxdH/Inf={r['maxdH']:.3f} H/I={r['H']/r['I']:.3f} U/I={r['U']/r['I']:.3f}", flush=True)
    print('time', round(time.time() - t0, 1))
