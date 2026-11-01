"""Q = 2 X_1 X_2 + 2 X_1 L_1 + 2 X_2 L_2 + 2 L_1 L_2 + lambda V^2 = 2 (X_1 + L_2)(X_2 + L_1) + lambda V^2: the rank-two
counterexample of hub_pairs/ (hub block [[0,1],[1,0]], Schur-matched remainder) plus a transverse square. Hubs uniform on
[0,1]; six light coordinates uniform on [-1/2, 1/2]; (l_1, l_2, v) a random orthonormal frame. Exact in X_2: given
(X', X_1), Q is affine in X_2. Printed: max over s in a grid near the singular level of P(|Q - s| <= delta)/(2 delta)."""
import sys
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
rng = np.random.default_rng(5)
Qm, _ = np.linalg.qr(rng.standard_normal((6, 3)))
l1, l2, v = Qm[:, 0], Qm[:, 1], Qm[:, 2]

def peak(lam, delta, nsamp=4_000_000, B=250_000):
    ss = np.linspace(-0.05, 0.05, 41)
    acc = np.zeros_like(ss); done = 0
    while done < nsamp:
        X = rng.random((B, 6)) - 0.5
        L1, L2, V = X @ l1, X @ l2, X @ v
        X1 = rng.random(B)
        slope = 2 * (X1 + L2); slope = np.where(np.abs(slope) < 1e-12, 1e-12, slope)
        off = 2 * X1 * L1 + 2 * L1 * L2 + lam * V * V
        for j, s in enumerate(ss):
            a = (s - delta - off) / slope; b = (s + delta - off) / slope
            lo = np.minimum(a, b); hi = np.maximum(a, b)
            acc[j] += (np.clip(hi, 0, 1) - np.clip(lo, 0, 1)).sum()
        done += B
    return (acc / done / (2 * delta)).max()

if __name__ == "__main__":
    for lam in (0.0, 1.0):
        out = [f"delta={d:g}: {peak(lam, d):.3f}" for d in (0.01, 0.003, 0.001, 0.0003)]
        print(f"lambda={lam}:  " + "  ".join(out), flush=True)
    print("done", flush=True)
