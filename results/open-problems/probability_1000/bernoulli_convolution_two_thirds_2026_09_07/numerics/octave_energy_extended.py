"""Extend the octave energy record and test whether the decay exponent is stable.

E(R) = sum_{R <= |k| < 2R} |muhat(k)|^2 with |muhat(xi)| = prod_j |cos(pi xi (2/3)^j / 3)|.
The note quotes E(R) ~ R^-0.78 over octaves 4 to 18.  S < infinity needs only E(R) <= C R^-delta for
SOME delta > 0, so the measured 0.78 has enormous room -- but the whole question is whether the
exponent is stable or creeping toward 0.  If it drifts up to 0 as R grows, the numerical case
collapses.  Measure it as far as this laptop will go, in chunks, at low priority.
"""
import numpy as np, sys

def energy_octave(j, chunk=1 << 21):
    lo, hi = 1 << j, 1 << (j + 1)
    tot = 0.0
    mx = 0.0
    k0 = lo
    while k0 < hi:
        k1 = min(k0 + chunk, hi)
        k = np.arange(k0, k1, dtype=np.float64)
        out = np.ones_like(k)
        r = 1.0
        while True:
            arg = np.pi * k * r / 3.0
            if arg.max() < 1e-14:
                break
            out *= np.abs(np.cos(arg))
            r *= 2.0 / 3.0
        tot += float((out ** 2).sum())
        mx = max(mx, float(out.max()))
        k0 = k1
    return tot, mx

print(f"{'j':>3} {'R=2^j':>12} {'E(R)':>14} {'log2 E':>10} {'slope':>9} {'max|muhat| sqrt(R)':>20}")
prev = None
rows = []
for j in range(4, 26):
    e, mx = energy_octave(j)
    l2 = np.log2(e)
    slope = (l2 - prev) if prev is not None else float("nan")
    prev = l2
    rows.append((j, e, l2, slope, mx * np.sqrt(2 ** j)))
    print(f"{j:>3} {2**j:>12} {e:>14.6e} {l2:>10.4f} {slope:>9.4f} {mx*np.sqrt(2**j):>20.4f}")
    sys.stdout.flush()

js = np.array([r[0] for r in rows], float)
l2 = np.array([r[2] for r in rows])
for name, sel in (("all octaves 4-25", slice(None)),
                  ("octaves 4-18", slice(0, 15)),
                  ("octaves 14-25", slice(10, None)),
                  ("octaves 20-25", slice(16, None))):
    a, b = np.polyfit(js[sel], l2[sel], 1)
    print(f"fit {name:>18}: E(R) ~ R^({a:+.4f})")
