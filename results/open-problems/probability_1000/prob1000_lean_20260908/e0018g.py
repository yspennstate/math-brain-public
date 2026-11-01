"""Standalone check of an optimiser candidate x = (log R1, k0, k1, psi)."""
import numpy as np, sys
from e0018 import G_of_r
def mats(x):
    u1,k0,k1,psi = x
    R0, R1 = 1.0, float(np.exp(u1))
    def B(R,k,ps):
        rho = k*R; s = R*np.cos(ps); d = -R*np.sin(ps)
        return np.array([[d, s-rho],[s+rho, -d]])
    return B(R0,k0,0.0), B(R1,k1,psi)
if __name__ == "__main__":
    x = np.array([float(v) for v in sys.argv[1:5]]); N = int(sys.argv[5]) if len(sys.argv)>5 else 300
    B0,B1 = mats(x)
    print("B0 =", np.round(B0,4).tolist(), " eig", np.round(np.linalg.eigvals(B0),4))
    print("B1 =", np.round(B1,4).tolist(), " eig", np.round(np.linalg.eigvals(B1),4))
    print("avg eig", np.round(np.linalg.eigvals((B0+B1)/2),4))
    rf = np.geomspace(1e-3, 1e3, 37)
    G = [G_of_r(B0,B1,r,N) for r in rf]
    print(f"N={N}: " + " ".join(f"{g:.3f}" for g in G))
    print("r:    " + " ".join(f"{r:.2g}" for r in rf))
