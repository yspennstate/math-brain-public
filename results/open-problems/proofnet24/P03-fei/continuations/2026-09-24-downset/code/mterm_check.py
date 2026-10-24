# Monotone DNFs with m terms: the least expected depth E*(f) of a decision tree and the hereditary L(f), against the
# bound L(f) <= 2m of the term-by-term tree; and H/I against log2 m + 8.85.
import math, numpy as np
from dt_check import subcube_dp, spectral
rng = np.random.default_rng(11)
worst_ratio = 0.0; worst_fei = 0.0; rows = 0
for n in (6, 8, 9, 10):
    N = 1 << n; x = np.arange(N); tts = []; ms = []
    for t in range(120 if n < 10 else 40):
        m = int(rng.integers(1, 3 * n)); f = np.zeros(N, dtype=bool)
        for _ in range(m):
            w = int(rng.integers(1, n + 1)); S = rng.choice(n, size=w, replace=False); mask = int(sum(1 << int(v) for v in S))
            f |= (x & mask) == mask
        if f.any() and not f.all(): tts.append(f); ms.append(m)
    tts = np.array(tts); ms = np.array(ms)
    E, Lv, D, Eh = subcube_dp(tts, n)
    H, I, infs, q = spectral(tts, n)
    r = Eh / (2 * ms)
    fei = (H / I) / (np.log2(ms) + 8.85)
    worst_ratio = max(worst_ratio, r.max()); worst_fei = max(worst_fei, fei.max()); rows += len(tts)
    print('n=%2d: %d DNFs, m from %d to %d | max L/(2m) %.3f | max (H/I)/(log2 m + 8.85) %.3f' % (n, len(tts), ms.min(), ms.max(), r.max(), fei.max()), flush=True)
print('%d formulas: max L(f)/(2m) = %.3f (claim <= 1), max (H/I)/(log2 m + 8.85) = %.3f (claim <= 1)' % (rows, worst_ratio, worst_fei))
