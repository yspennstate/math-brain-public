"""P0290 beyond light traffic: exact mean stationary workload of the MMPP/M/1 queue (Markov-modulated Poisson arrivals
with intensity eps f(X(ct)), exponential unit-mean service, rate-one server) via the matrix-geometric solution of the
QBD, then a scan of w(c) in c for Boolean f on doubly monotone (non-reversible) chains.
Levels n = number in system; phases = environment state.  A0 = eps diag(f) (up), A2 = I (down, n >= 1),
A1 = c Q - A0 - A2 (n >= 1), boundary B1 = c Q - A0.  R solves A0 + R A1 + R^2 A2 = 0; pi_n = pi_0 R^n;
E[N] = pi_0 R (I - R)^{-2} 1.  With exponential unit-mean service, E[workload] = E[N] (memorylessness).
A rise of w(c) in c at some load would refute Problem 2 for that f.
"""
import itertools
import numpy as np
from p0290_boolean_image_search import stationary, random_dm_chain, is_reversible, doubly_monotone

def mean_workload(Q, f, eps, c, tol=1e-13, itmax=20000):
    m = Q.shape[0]; I = np.eye(m)
    A0 = eps * np.diag(f); A2 = I; A1 = c * Q - A0 - A2
    # R by successive substitution R = -(A0 + R^2 A2) A1^{-1}
    A1i = np.linalg.inv(A1); R = np.zeros((m, m))
    for _ in range(itmax):
        Rn = -(A0 + R @ R @ A2) @ A1i
        if np.max(abs(Rn - R)) < tol: R = Rn; break
        R = Rn
    # boundary: pi_0 (B1 + R A2) = 0, normalised pi_0 (I - R)^{-1} 1 = 1
    B1 = c * Q - A0
    M = B1 + R @ A2
    w, v = np.linalg.eig(M.T); k = np.argmin(abs(w)); pi0 = np.real(v[:, k]); pi0 = pi0 / pi0.sum()
    IR = np.linalg.inv(I - R); pi0 = pi0 / (pi0 @ IR @ np.ones(m))
    EN = pi0 @ R @ IR @ IR @ np.ones(m)
    return float(EN)

def scan(Q, f, eps, cs):
    return np.array([mean_workload(Q, f, eps, c) for c in cs])

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    cs = np.exp(np.linspace(np.log(0.02), np.log(100), 60))
    # sanity: constant f -> M/M/1, w = rho/(1-rho) independent of c
    Q3 = np.array([[-1.3, 1.2, 0.1], [0.8, -2.0, 1.2], [0.5, 0.8, -1.3]])
    w = scan(Q3, np.ones(3), 0.5, cs[:3]); print("M/M/1 sanity (rho=0.5, expect 1.0):", np.round(w, 6))
    # the hand example, Boolean f, several loads
    pi = stationary(Q3)
    for f in (np.array([0, 1, 0.]), np.array([1, 0, 1.]), np.array([1, 0, 0.]), np.array([0, 0, 1.]), np.array([1, 1, 0.])):
        a = pi @ f
        for rho in (0.2, 0.5, 0.8):
            eps = rho / a; w = scan(Q3, f, eps, cs)
            rises = [(cs[k], cs[k+1], w[k+1] - w[k]) for k in range(len(cs) - 1) if w[k+1] > w[k] + 1e-10]
            print(f"hand Q, f={f}, rho={rho}: w(c) from {w[0]:.4f} to {w[-1]:.4f}; rises: {len(rises)}" + (f" e.g. {rises[0]}" if rises else ""), flush=True)
    # random doubly monotone non-reversible chains, all Boolean f, rho in {0.3, 0.6, 0.85}
    rng = np.random.default_rng(3)
    total = 0; found = 0
    for m in (3, 4):
        for trial in range(25):
            Q = random_dm_chain(rng, m)
            if Q is None: continue
            pi = stationary(Q)
            for f in [np.array(b, float) for b in itertools.product([0, 1], repeat=m) if 0 < sum(b) < m]:
                a = pi @ f
                for rho in (0.3, 0.6, 0.85):
                    w = scan(Q, f, rho / a, cs); total += 1
                    rise = max(w[k+1] - w[k] for k in range(len(cs) - 1))
                    if rise > 1e-9:
                        found += 1
                        print(f"RISE m={m} trial={trial} f={f} rho={rho}: max step rise {rise:.3e}; eigs {np.round(np.linalg.eigvals(Q),3)}\n  Q=\n{np.round(Q,4)}", flush=True)
    print(f"scanned {total} (chain, Boolean f, rho) cases; rises found: {found}")
