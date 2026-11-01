"""Density of Q = 2 X_h L + lambda V^2 + 2 eps L P for light laws with J nested scales (Cantor-type):
X = sum_{j<J} 3^j B_j + 2^{-J} U, B_j fair bits, U uniform on [0,1]; 2^J intervals of length 2^{-J}, density 1.
Same window estimator as small_eps.py (exact in the hub). One fixed frame per row. Printed: sup over a grid of y
of P(|Q - y| <= delta)/(2 delta), delta = 0.002, for J = 1..6, eps = 0.01 and eps = 0."""
import sys
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
rng = np.random.default_rng(11)

def light_cantor(J, size, base=3.0):
    X = np.zeros(size)
    for j in range(J):
        X += (base ** j) * rng.integers(0, 2, size)
    X += rng.random(size) * 2.0 ** (-J)
    mean = sum(base ** j for j in range(J)) * 0.5 + 0.5 * 2.0 ** (-J)
    return X - mean

def hub_cdf(kind, cell=0.01):
    if kind == "unif":
        return np.array([0.0, 1.0]), np.array([0.0, 1.0])
    n = int(round(2.0 / cell)); keep = rng.random(n) < 0.5
    xs = np.arange(n + 1) * cell
    Fs = np.concatenate([[0.0], np.cumsum(np.where(keep, cell, 0.0))]); Fs /= Fs[-1]
    return xs, Fs

def frame(kind, m):
    if kind == "walsh":
        return np.array([1, 1, 1, 1]) / 2.0, np.array([1, -1, 1, -1]) / 2.0, np.array([1, 1, -1, -1]) / 2.0
    Q, _ = np.linalg.qr(rng.standard_normal((m, 3)))
    return Q[:, 0], Q[:, 1], Q[:, 2]

def peak(J, eps, hub, fr, lam=1.0, nsamp=2_000_000, B=200_000, scale=1.0):
    xs, Fs = hub
    w, v, p = fr
    delta = 0.002
    ys = np.concatenate([np.linspace(-2.0, 2.0, 161), np.linspace(-0.1, 0.1, 101)])
    acc = np.zeros_like(ys); done = 0
    while done < nsamp:
        X = light_cantor(J, (B, len(w))) * scale
        L, V, P = X @ w, X @ v, X @ p
        R = lam * V * V + 2 * eps * L * P
        s = 2 * L; s = np.where(np.abs(s) < 1e-12, 1e-12, s)
        for j, y in enumerate(ys):
            x1 = (y - R - delta) / s; x2 = (y - R + delta) / s
            acc[j] += np.abs(np.interp(x2, xs, Fs) - np.interp(x1, xs, Fs)).sum()
        done += B
    return (acc / done / (2 * delta)).max()

if __name__ == "__main__":
    kind = sys.argv[1]; m = int(sys.argv[2])
    fr = frame(kind, m)
    for hk in ("rough", "unif"):
        hub = hub_cdf(hk)
        for eps in (0.01, 0.0):
            out = []
            for J in range(1, 7):
                out.append(f"J={J}: {peak(J, eps, hub, fr):.3f}")
            print(f"{kind} m={m} hub={hk} eps={eps}:  " + "  ".join(out), flush=True)
    print("done", flush=True)
