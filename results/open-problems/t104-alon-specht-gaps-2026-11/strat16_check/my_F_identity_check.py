"""an agent: float check that Codex's rank-three reduction u^T F(z) u (RESULT.md, verify_rank_three_algebra.py)
equals my own T* from formula (1) (my_min_search.py's Tval code), at random S PSD with S1=Su=0, rank<=2, z=1/k.
A = J/5 + S, C = I - A. Identity check only (entrywise A>=0 not needed). Corroboration, not proof."""
import sys
import numpy as np
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
iu = np.triu_indices(5, 1)

def Tstar(A, u, k):
    C = np.eye(5) - A; trC = np.trace(C); M = (1 + trC) / 2
    h = 0.5 + np.sum(u * u * np.diag(C)); B = np.sum(np.outer(u, u) * A * A)
    w = A[iu]; dC = np.diag(C)
    Y = 2 * np.sum(w * (u[iu[0]] - u[iu[1]]) ** 2 * (2 - dC[iu[0]] - dC[iu[1]] - 2 * w))
    return (2 * (trC - np.trace(C @ C)) + 2 * (k + 2) * B / k
            + (M - 1) / k**2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h) - Y)

def Fz(S, z):
    I = np.eye(5); tau = np.trace(S); v = np.trace(S @ S); d = np.diag(S); D = np.diag(d); Cs = S * S
    F0 = (3 + 3 * tau / 5 - 2 * v) * I - 2 * D - 2 * np.diag(S @ d) + 4 * np.diag(np.diag(S @ S)) - 2 * Cs
    Bp = 4 * Cs + (3 - tau) * (tau - 4.7) * I - (3 - tau) * D
    Ep = (3 - tau) * (0.6 * I - 2 * D)
    return F0 + Bp * z + Ep * z * z

worst = 0.0
for trial in range(2000):
    u = rng.standard_normal(5); u -= u.mean(); u /= np.linalg.norm(u)
    Mx = np.vstack([np.ones(5) / np.sqrt(5), u]); K = np.linalg.svd(Mx)[2][2:].T
    G = rng.standard_normal((3, 2)) * rng.uniform(0.05, 0.6)
    S = K @ G @ G.T @ K.T
    A = np.ones((5, 5)) / 5 + S
    for k in (5.0, 6.0, 9.5, 40.0):
        lhs = Tstar(A, u, k); rhs = u @ Fz(S, 1 / k) @ u
        worst = max(worst, abs(lhs - rhs) / (1 + abs(lhs)))
print('max relative |T*(1) - u^T F(1/k) u| over 8000 cases = %.3e' % worst)
print('S=0, k=5: u^T F u =', Fz(np.zeros((5, 5)), 0.2)[0, 0], '(63/250 =', 63 / 250, ')')
print('PASS' if worst < 1e-9 else 'FAIL')
