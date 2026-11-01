"""Frame integral J(kappa) = int int |E exp(i zeta L + i xi V + i kappa U^2)| d zeta d xi for four coordinates.

w = (1,1,1,1)/2, v = (1,-1,1,-1)/2 (leverages w_i^2 + v_i^2 = 1/2), and the twist direction u is either
aligned (u = w) or orthogonal to the frame (u = p = (1,1,-1,-1)/2).  Each X_i has the comb law: N bumps of
width delta = 1/N at the integers 0..N-1 (density exactly 1 on its support).  Inside a bump box the phase is
linearised, kappa (U_K + delta <u,t>)^2 ~ kappa U_K^2 + 2 kappa delta U_K <u,t> (error <= kappa delta^2), so

  T(zeta, xi) = N^-4 sum_K exp(i(zeta L_K + xi V_K + kappa U_K^2)) prod_i S(delta (zeta w_i + xi v_i + 2 kappa U_K u_i)),

S(x) = (e^{ix} - 1)/(ix).  Printed: J(kappa) and the ratio J(kappa)/J(0) for N = 4, 8, 12.
"""
import sys
import numpy as np

W = np.array([1, 1, 1, 1]) / 2.0
V = np.array([1, -1, 1, -1]) / 2.0
P = np.array([1, 1, -1, -1]) / 2.0


def S(x):
    # (e^{ix} - 1)/(ix) = e^{ix/2} sin(x/2)/(x/2)
    return np.exp(0.5j * x) * np.sinc(x / (2.0 * np.pi))


def frame_integral(N, kappa, u, zmax_mult=6.0, h=0.25):
    delta = 1.0 / N
    ks = np.arange(N, dtype=float)
    K = np.stack(np.meshgrid(ks, ks, ks, ks, indexing="ij"), -1).reshape(-1, 4)
    LK, VK, UK = K @ W, K @ V, K @ u
    zmax = zmax_mult * N
    g = np.arange(-zmax, zmax + 1e-9, h)
    total = 0.0
    for z in g:  # one zeta row at a time: grid of xi values x lattice points
        xi = g[:, None]
        phase = z * LK[None, :] + xi * VK[None, :] + kappa * UK[None, :] ** 2
        env = np.ones((len(g), len(K)), dtype=complex)
        for i in range(4):
            env *= S(delta * (z * W[i] + xi * V[i] + 2.0 * kappa * UK[None, :] * u[i]))
        T = (np.exp(1j * phase) * env).sum(axis=1) / len(K)
        total += np.abs(T).sum() * h * h
    return total


if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    # Gauss-sum prediction: U_K lies in Z/2, so kappa = 4 pi/q makes exp(i kappa U_K^2) q-periodic in 2U_K, a sum of
    # q linear phases of modulus q^{-1/2}.  Aligned (u = w): q translates of the untwisted transform, J ~ sqrt(q) J0.
    # Orthogonal (u = p): the shifts move the product off the revival lattice, J should stay ~ J0.
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    zm = float(sys.argv[2]) if len(sys.argv) > 2 else 8.0
    h = float(sys.argv[3]) if len(sys.argv) > 3 else 0.2
    qs = [1, 2, 3, 4, 6, 8, 12, 16, 24, 36]
    extra = [0.1, 0.3, 1.0]
    base = frame_integral(N, 0.0, W, zmax_mult=zm, h=h)
    print(f"N={N} zmax={zm*N:g} h={h}  J(0) = {base:.4f}", flush=True)
    for name, u in (("aligned u=w", W), ("orthogonal u=p", P)):
        out = []
        for q in qs:
            J = frame_integral(N, 4*np.pi/q, u, zmax_mult=zm, h=h)
            out.append(f"q={q}:{J/base:.3f}")
        for kap in extra:
            J = frame_integral(N, kap, u, zmax_mult=zm, h=h)
            out.append(f"k={kap}:{J/base:.3f}")
        print(f"  {name:15s} J/J0: " + "  ".join(out), flush=True)
