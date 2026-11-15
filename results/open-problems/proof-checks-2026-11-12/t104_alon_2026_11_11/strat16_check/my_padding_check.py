"""an agent: float check of Codex padding_monotonicity.py claim F'(z) <= -3I/50 on 0<=z<=1/5 for feasible S
(A=J/5+S entrywise >=0, S PSD, S1=Su=0, rank<=2). F'(z) = Bp + 2 z Ep. Samples S scaled to the entrywise boundary
and interior. Prints the largest eigenvalue of F'(z) found. Corroboration, not proof."""
import sys
import numpy as np
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
I = np.eye(5); top = -np.inf
for trial in range(20000):
    u = rng.standard_normal(5) * (rng.random(5) < 0.8); u -= u.mean()
    if np.linalg.norm(u) < 1e-9: continue
    u /= np.linalg.norm(u)
    K = np.linalg.svd(np.vstack([np.ones(5) / np.sqrt(5), u]))[2][2:].T
    S0 = K @ (lambda G: G @ G.T)(rng.standard_normal((3, 2))) @ K.T
    off = S0[np.triu_indices(5, 1)].min()
    smax = (0.2 / -off) if off < 0 else 10.0
    for s in (smax, smax * rng.random()):
        S = s * S0
        if np.linalg.eigvalsh(np.eye(5) - np.ones((5, 5)) / 5 - S).min() < -1e-12: continue  # need S <= H5
        tau = np.trace(S); D = np.diag(np.diag(S)); Cs = S * S
        Bp = 4 * Cs + (3 - tau) * (tau - 4.7) * I - (3 - tau) * D
        Ep = (3 - tau) * (0.6 * I - 2 * D)
        for z in (0.0, 0.1, 0.2):
            top = max(top, np.linalg.eigvalsh(Bp + 2 * z * Ep)[-1])
print("largest eigenvalue of F'(z) found: %.6f ; claimed bound -0.06" % top)
