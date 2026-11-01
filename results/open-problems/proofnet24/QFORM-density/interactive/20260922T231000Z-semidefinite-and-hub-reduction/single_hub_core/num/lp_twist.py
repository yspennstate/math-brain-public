"""Frame integral with a mixed twist: J(kappa) = int int |E exp(i zeta L + i xi V + i kappa L P)| d zeta d xi.

Four comb coordinates (N teeth of width 1/N at the integers 0..N-1), w = (1,1,1,1)/2, v = (1,-1,1,-1)/2 and
p = (1,1,-1,-1)/2, so P is orthogonal to the frame but lives on the same coordinates.  Inside a tooth box the phase
kappa (L_K + d<w,t>)(P_K + d<p,t>) is linearised to kappa L_K P_K + kappa d (P_K <w,t> + L_K <p,t>), error of order
kappa d^2.  Compared with the aligned twist kappa L^2 and the orthogonal twist kappa P^2 of tlperp_comb.py.
"""
import sys, time
import numpy as np

W = np.array([1, 1, 1, 1]) / 2.0
V = np.array([1, -1, 1, -1]) / 2.0
P = np.array([1, 1, -1, -1]) / 2.0


def S(x):
    return np.exp(0.5j * x) * np.sinc(x / (2.0 * np.pi))


def frame_integral(N, kappa, kind, zmax, h):
    d = 1.0 / N
    ks = np.arange(N, dtype=float)
    K = np.stack(np.meshgrid(ks, ks, ks, ks, indexing="ij"), -1).reshape(-1, 4)
    LK, VK, PK = K @ W, K @ V, K @ P
    if kind == "LP":
        ph = kappa * LK * PK
        grad = kappa * (PK[:, None] * W[None, :] + LK[:, None] * P[None, :])   # d(phase)/dx_i
    elif kind == "LL":
        ph = kappa * LK ** 2
        grad = 2 * kappa * LK[:, None] * W[None, :]
    else:  # "PP"
        ph = kappa * PK ** 2
        grad = 2 * kappa * PK[:, None] * P[None, :]
    g = np.arange(-zmax, zmax + 1e-9, h)
    total = 0.0
    for z in g:
        xi = g[:, None]
        phase = z * LK[None, :] + xi * VK[None, :] + ph[None, :]
        env = np.ones((len(g), len(K)), dtype=complex)
        for i in range(4):
            env *= S(d * (z * W[i] + xi * V[i] + grad[None, :, i]))
        T = (np.exp(1j * phase) * env).sum(axis=1) / len(K)
        total += np.abs(T).sum() * h * h
    return total


if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    zm = float(sys.argv[2]) if len(sys.argv) > 2 else 8.0
    h = float(sys.argv[3]) if len(sys.argv) > 3 else 0.2
    t0 = time.time()
    base = frame_integral(N, 0.0, "LP", zm * N, h)
    print(f"N={N} zmax={zm*N:g} h={h} J(0)={base:.4f} ({time.time()-t0:.0f}s)", flush=True)
    kinds = sys.argv[4].split(",") if len(sys.argv) > 4 else ["LP", "LL", "PP"]
    for kind in kinds:
        out = []
        for q in (8, 12, 16, 24):
            J = frame_integral(N, 4 * np.pi / q, kind, zm * N, h)
            out.append(f"q={q}:{J/base:.3f}")
            print(f"  {kind} q={q} J/J0={J/base:.3f} ({time.time()-t0:.0f}s)", flush=True)
        print(f"  {kind}  " + "  ".join(out), flush=True)
    print("done", flush=True)
