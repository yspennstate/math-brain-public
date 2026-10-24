try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
"""Checks of the block lemma (N4) and the coupling-gain lemma (N9) on the adversarial bump laws of N2.

n = 4, k = 1, v = (1,1,1,1)/2, K = {0,1}, I = {2,3}.  Laws: N Gaussian bumps of height 1 per coordinate, positions
chosen so that <v, X> has N^4 distinct, well separated bump centres (the laws that make J(kappa vv^T) ~ 2 pi N).
 (1) E = kappa vv^T                          (aligned coupling K-I)             -> grows like 2 pi N
 (2) E = kappa (v_K v_K^T + v_I v_I^T)        (same twist inside each block, no coupling) -> block lemma: J <= 4 pi
 (3) E = (2) + sigma (a b^T + b a^T), a = (1,-1,0,0)/sqrt2, b = (0,0,1,-1)/sqrt2 (non-aligned coupling)
        gain lemma: J <= (2 pi)^{3/2} 2 (det Gram[P_K,a] det Gram[P_I,b])^{-1/4} (2 sigma)^{-1/2}
"""
import numpy as np, sys, math, time
sys.path.insert(0, '.')
from gmix import components, J_k1_windowed

def laws_for(n, N, D, v):
    s0 = 1.0 / (N * math.sqrt(2 * math.pi))
    return [(np.full(N, 1.0 / N), np.array([p * N ** i * D / v[i] for p in range(N)], float), np.full(N, s0)) for i in range(n)]

t0 = time.time()
v = np.full(4, 0.5); vK = np.array([.5, .5, 0, 0]); vI = np.array([0, 0, .5, .5])
a = np.array([1, -1, 0, 0]) / math.sqrt(2); b = np.array([0, 0, 1, -1]) / math.sqrt(2)
kappa = 1.0
# Gram[P_K, a]: P_K = (1/2,1/2) on K; a = (1,-1)/sqrt2 -> Gram = diag(1/2, 1); same for I
gainC = (2 * math.pi) ** 1.5 * 2 * (0.5 * 0.5) ** (-0.25)
print(f"block-lemma bound 4 pi = {4*math.pi:.3f};  gain-lemma constant {gainC:.2f} * (2 sigma)^(-1/2)", flush=True)
for N in [2, 3, 4]:
    D = 8.0 * N / kappa
    laws = laws_for(4, N, D, v); W, MU, S = components(laws)
    du = min(0.02, 0.1 / D)
    J1 = J_k1_windowed(v, kappa * np.outer(v, v), W, MU, S, du)
    E2 = kappa * (np.outer(vK, vK) + np.outer(vI, vI))
    J2 = J_k1_windowed(v, E2, W, MU, S, du)
    row = f"N={N}: (1) aligned J={J1:7.3f}  (2) no coupling J={J2:6.3f}"
    for sigma in [0.1, 1.0, 10.0]:
        E3 = E2 + sigma * (np.outer(a, b) + np.outer(b, a))
        J3 = J_k1_windowed(v, E3, W, MU, S, du)
        row += f"  (3) sigma={sigma:4.1f}: J={J3:6.3f} (bound {gainC*(2*sigma)**-0.5:6.2f})"
    print(row + f"  [{time.time()-t0:.0f}s]", flush=True)
