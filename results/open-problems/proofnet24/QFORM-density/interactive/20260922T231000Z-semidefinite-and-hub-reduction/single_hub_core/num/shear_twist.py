"""Frame integral with the twist exp(i kappa L P) on a sheared rational frame, where on the lattice the value of <q,K>
mod 5 is a fixed linear function of (<w,K>, <v,K>).  w = (1,1,1,1,1)/sqrt5, v = (2,-1,1,0,-2)/sqrt10,
q = (2,0,-2,-1,1)/sqrt10.  At kappa0 = 2 pi sqrt50/5 the twist restricted to the lattice is a Gauss-type phase in
(<w,K>, <v,K>) mod 5, that is an aligned twist; at a nearby kappa it is not.  Comb laws: N teeth of width 1/N at the
integers; the phase is linearised inside a tooth as in tlperp_comb.py.  Printed: J(kappa)/J(0)."""
import sys, time
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

W = np.array([1, 1, 1, 1, 1]) / np.sqrt(5)
V = np.array([2, -1, 1, 0, -2]) / np.sqrt(10)
P = np.array([2, 0, -2, -1, 1]) / np.sqrt(10)

def S(x):
    return np.exp(0.5j * x) * np.sinc(x / (2 * np.pi))

def J(N, kappa, zmax, h, kind="LP"):
    d = 1.0 / N
    ks = np.arange(N, dtype=float)
    K = np.stack(np.meshgrid(*([ks] * 5), indexing="ij"), -1).reshape(-1, 5)
    K = K - K.mean(0)
    LK, VK, PK = K @ W, K @ V, K @ P
    if kind == "LP":
        ph = kappa * LK * PK; grad = kappa * (PK[:, None] * W[None, :] + LK[:, None] * P[None, :])
    else:
        ph = kappa * LK ** 2; grad = 2 * kappa * LK[:, None] * W[None, :]
    g = np.arange(-zmax, zmax + 1e-9, h)
    tot = 0.0
    for z in g:
        xi = g[:, None]
        env = np.ones((len(g), len(K)), dtype=complex)
        for i in range(5):
            env *= S(d * (z * W[i] + xi * V[i] + grad[None, :, i]))
        T = (np.exp(1j * (z * LK[None, :] + xi * VK[None, :] + ph[None, :])) * env).sum(1) / len(K)
        tot += np.abs(T).sum() * h * h
    return tot

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    zmax = 16.0 * N; h = 0.25
    t0 = time.time()
    J0 = J(N, 0.0, zmax, h)
    print(f"N={N} zmax={zmax} h={h} J0={J0:.3f} ({time.time()-t0:.0f}s)", flush=True)
    k0 = 2 * np.pi * np.sqrt(50) / 5
    for lab, kap in (("kappa0", k0), ("kappa0*1.0613", k0 * 1.0613), ("kappa0/2", k0 / 2), ("kappa0*0.7071", k0 * 0.70710678)):
        r = J(N, kap, zmax, h) / J0
        print(f"  LP {lab} (kappa={kap:.3f}): J/J0={r:.3f} ({time.time()-t0:.0f}s)", flush=True)
    print("done", flush=True)
