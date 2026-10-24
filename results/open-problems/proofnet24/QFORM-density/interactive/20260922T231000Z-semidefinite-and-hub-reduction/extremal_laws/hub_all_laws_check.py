"""Q = 4 X_h L + 2 L^2 + 2 V^2 (+ small diagonal): completing the square in L gives
Q = 2(L + X_h)^2 - 2 X_h^2 + 2V^2, so given X_h = x the density is that of a definite binary form in the 2D
projection (L, V) (density <= 2): <= pi for EVERY hub law.  Check with spread hub laws (combs) and spread leaves."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
rng = np.random.default_rng(2)
n = 40
G = rng.normal(size=(n, 2)); Qm, _ = np.linalg.qr(G); w, v = Qm[:, 0], Qm[:, 1]
def comb(N, m, spread):      # uniform on N teeth of total length 1, teeth spread over [-spread, spread]
    pos = np.sort(rng.uniform(-spread, spread, N)); k = rng.integers(0, N, m)
    return pos[k] + rng.random(m)/N
for hub in ["interval", "comb5", "comb40"]:
    for leaves in ["interval", "comb"]:
        for dscale in [0.0, 0.05]:
            N = 1_500_000
            Xh = rng.random(N) - 0.5 if hub == "interval" else comb(int(hub[4:]), N, 6.0)
            X = rng.random((N, n)) - 0.5 if leaves == "interval" else np.column_stack([comb(3, N, 2.0) for _ in range(n)])
            L = X @ w; V = X @ v
            d = dscale*rng.normal(size=n)
            Q = 4*Xh*L + 2*L**2 + 2*V**2 + (X**2) @ d
            lo, hi = np.quantile(Q, [0.001, 0.999]); wdt = (hi-lo)/800
            h, e = np.histogram(Q, bins=np.arange(lo, hi+wdt, wdt))
            print(f"hub={hub:8s} leaves={leaves:8s} diag={dscale}: max density ~ {h.max()/N/wdt:.3f}   (bound pi for diag=0)", flush=True)
