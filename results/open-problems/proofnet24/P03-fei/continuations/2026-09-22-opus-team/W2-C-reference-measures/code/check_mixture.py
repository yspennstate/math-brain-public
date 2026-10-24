"""Non-tautological check used by the block lemma: law(S cap J) = E_z spectrum(f_{J|z}) (Parseval over z),
computed by two independent paths (marginal of the full spectrum vs average of restricted spectra)."""
import itertools
import numpy as np
import wlib as W
W.set_polite()
rng = np.random.default_rng(43)
worst = 0.0
for n in (3, 4, 5, 6, 7):
    for trial in range(25):
        tt = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
        r = int(rng.integers(1, n))
        R = sorted(rng.choice(n, size=r, replace=False).tolist())
        J = [j for j in range(n) if j not in R]
        N = 1 << n; x = np.arange(N)
        p = W.spectrum(tt)
        # path 1: marginal of full spectrum on J, indexed by compressed J-mask
        comp = np.zeros(N, dtype=np.int64)
        for k, j in enumerate(J):
            comp |= ((x >> j) & 1) << k
        law1 = np.bincount(comp, weights=p, minlength=1 << len(J))
        # path 2: average of restricted spectra
        law2 = np.zeros(1 << len(J))
        for z in itertools.product((0, 1), repeat=r):
            ok = np.ones(N, dtype=bool)
            for t, b in zip(R, z):
                ok &= ((x >> t) & 1) == b
            law2 += W.spectrum(tt[ok])
        law2 /= 2 ** r
        worst = max(worst, np.abs(law1 - law2).max())
    print(f"n={n}: max |law(S_J) - E_z spec(f_J|z)| = {worst:.2e}")
