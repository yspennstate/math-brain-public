try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
np.random.seed(5)
# Proposition P sharpness: Q = G(X_h) + 2 X_h L with G chosen so that the conditional centres align (G(x) = -a x^2 gives
# Q = 2 X_h L). Exact conditional: P(|2 x L| <= u | L) for X_h uniform = min(1, u/|L|).
N = 4_000_000
for name, w in [("spread w (60 coords)", np.ones(60)/np.sqrt(60)), ("w = (e1+e2)/sqrt2", np.array([1, 1])/np.sqrt(2))]:
    L = np.zeros(N)
    for j in range(len(w)):
        L += w[j] * (np.random.rand(N) - 0.5)
    row = []
    for k in range(2, 8):
        u = 10.0**-k
        P = np.mean(np.minimum(1.0, u / np.abs(L)))
        row.append(P / (u * (1 + np.log(1/u))))
    print(f"{name:22s}: P(|Q|<=u)/(u(1+log 1/u)), u=1e-2..1e-7: " + " ".join(f"{r:.3f}" for r in row) +
          f"   bound 2 sqrt2 = {2*np.sqrt(2):.3f}", flush=True)
