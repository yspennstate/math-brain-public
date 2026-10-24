# For each octave, find the dominant frequencies and factor them as k = 2^a 3^b m (gcd(m,6)=1).
# Prediction from identity (A): the dominant k in an octave are lattice members 2^a 3^b m whose PRIMITIVE value
# hat_mu(2^{a+b} m) is large, with small m; and each (m,s) family contributes about log2/log(3/2) = 1.71 members
# per octave it spans.  If so, the octave energy is a sum over a few (m,s) of a multiplicity times one lacunary value.
import numpy as np, math, sys
JLO, JHI = 6, int(sys.argv[1]) if len(sys.argv) > 1 else 20
def hat_abs2(xi, terms=4000):
    out = np.ones(xi.shape); a = xi/3.0
    for _ in range(terms):
        out *= np.abs(np.cos(np.pi*a)); a = a*(2.0/3.0)
        if np.max(np.abs(a)) < 1e-16: break
    return out*out
def fac(k):
    a = 0; b = 0
    while k % 2 == 0: k //= 2; a += 1
    while k % 3 == 0: k //= 3; b += 1
    return a, b, k
print(" j | rank | k | a b m (k = 2^a 3^b m) | s=a+b | |hat|^2 | share of octave energy")
for j in range(JLO, JHI+1):
    lo, hi = 1 << j, 1 << (j+1); step = 1 << 17
    best = []
    E = 0.0
    for a0 in range(lo, hi, step):
        kk = np.arange(a0, min(a0+step, hi), dtype=np.float64)
        v = hat_abs2(kk); E += float(v.sum())
        idx = np.argsort(v)[-4:]
        for i in idx: best.append((float(v[i]), int(kk[i])))
    best.sort(reverse=True)
    for r, (val, k) in enumerate(best[:3]):
        a, b, m = fac(k)
        print(f"{j:2d} | {r+1} | {k:>9d} | a={a:2d} b={b:2d} m={m:>7d} | s={a+b:2d} | {val:.3e} | {val/E*100:5.1f}%")
