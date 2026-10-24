try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Milestone (15_architecture N4.1): Q = 4 X_h L + 2 L^2 + 2 V^2 + sum d_i X_i^2 + <b, X'>.
# Theorem H2 proves boundedness for hub laws supported in an interval; for M-piece hub laws the proof gives C(1 + log M).
# Question: does the true sup density grow with M (hub spread over M intervals) or with bumpy leaf laws?
import numpy as np, time, sys
sys.path.insert(0, r'~\AppData\Local\Temp\claude\<project>\9bfb8ed3-a0b8-4b06-94b3-3777f80a6d98\scratchpad\wave2\14_real_variable_hub_dense')
from fibre_density import Law, density
rng = np.random.default_rng(7)
n1 = 48; n = n1 + 1
Qm, _ = np.linalg.qr(rng.normal(size=(n1, 3))); w, v, u = Qm[:, 0], Qm[:, 1], Qm[:, 2]
def build(dscale, bperp):
    A = np.zeros((n, n))
    A[0, 1:] = 2 * w; A[1:, 0] = 2 * w
    A[1:, 1:] = 2 * np.outer(w, w) + 2 * np.outer(v, v) + np.diag(dscale * rng.choice([-1, 1], n1) * rng.uniform(0.5, 1, n1))
    b = np.zeros(n); b[1:] = bperp * u + 0.3 * v
    return A, b
svals = np.linspace(-3, 3, 31)
configs = [('unif', {}, 'unif', {}), ('multi', {'M': 4}, 'unif', {}), ('multi', {'M': 16}, 'unif', {}),
           ('multi', {'M': 64}, 'unif', {}), ('bumpy', {'N': 16}, 'unif', {}), ('unif', {}, 'bumpy', {'N': 8}),
           ('multi', {'M': 16}, 'bumpy', {'N': 8})]
for dscale, bperp in ((0.0, 0.0), (0.1, 0.0), (0.1, 1.0)):
    A, b = build(dscale, bperp)
    for hk, hkw, lk, lkw in configs:
        t = time.time()
        laws = [Law(hk, rng, **hkw)] + [Law(lk, rng, **lkw) for _ in range(n1)]
        m, sd = density(A, b, laws, svals, 16000)
        k = int(np.argmax(m))
        # refine around the peak
        s2 = np.linspace(svals[max(k - 1, 0)], svals[min(k + 1, len(svals) - 1)], 9)
        m2, sd2 = density(A, b, laws, s2, 24000)
        k2 = int(np.argmax(m2))
        print(f"d={dscale:.1f} bperp={bperp:.1f} hub={hk}{hkw} leaves={lk}{lkw}: max p ~ {m2[k2]:.3f} +- {sd2[k2]:.3f} at s={s2[k2]:+.2f}  ({time.time()-t:.0f}s)", flush=True)
