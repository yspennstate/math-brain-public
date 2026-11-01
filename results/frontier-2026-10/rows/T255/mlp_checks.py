# Checks for sections 11-12 of M2_EXACT.md (agent Q, 17 Oct). Corollary 4.3 MLP drift of 2306.17759 Thm 3.2:
# b_res = gamma^2 [nu(rho_ab) sqrt(V_aa V_bb)], nu(rho) = (c+-c-)^2/(2 pi) (sqrt(1-rho^2) - rho arccos rho).
import numpy as np
rng = np.random.default_rng(7)
# (a) sqrt(1-r^2) - r arccos r == pi (k1(r) - r), k1(r) = 2 E[relu(x) relu(y)] for unit normals with correlation r
for r in (-0.95, -0.4, 0.0, 0.3, 0.9):
    x = rng.standard_normal(2_000_000); y = r * x + np.sqrt(1 - r * r) * rng.standard_normal(x.size)
    k1 = 2 * np.mean(np.maximum(x, 0) * np.maximum(y, 0))
    print(f"r {r:+.2f}: sqrt(1-r^2)-r*arccos r = {np.sqrt(1-r*r)-r*np.arccos(r):.4f}  pi(k1-r) MC = {np.pi*(k1-r):.4f}")
# (b) tr(R^-1 Nhat) >= -pi m on correlation matrices, Nhat_ab = sqrt(1-r^2) - r arccos r (diag 0); worst case near degenerate R
def nhat(R):
    Rc = np.clip(R, -1, 1); N = np.sqrt(1 - Rc**2) - Rc * np.arccos(Rc); np.fill_diagonal(N, 0); return N
worst = {}
for m in (2, 3, 4, 6, 8):
    w = np.inf
    for _ in range(20000):
        k = rng.integers(1, m + 1); G = rng.standard_normal((m, k)) ; G += 1e-3 * rng.standard_normal((m, m)) @ rng.standard_normal((m, 1)) if False else 0
        V = G @ G.T + 10.0 ** rng.uniform(-8, 0) * np.eye(m); d = np.sqrt(np.diag(V)); R = V / np.outer(d, d)
        w = min(w, np.trace(np.linalg.solve(R, nhat(R))))
    worst[m] = w; print(f"m {m}: min tr(R^-1 Nhat) over 20000 near-degenerate R = {w:.4f}   bound -pi m = {-np.pi*m:.4f}")
# (c) tr b_res = 0 (nu(1) = 0) - immediate; (d) Lyapunov f=(trV)^q: no further check needed beyond section 1's noise form.
