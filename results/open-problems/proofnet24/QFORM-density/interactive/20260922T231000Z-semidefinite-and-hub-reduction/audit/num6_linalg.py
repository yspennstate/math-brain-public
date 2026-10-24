try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations
np.random.seed(9)
# Prop 4.1(b): max-volume 3x3 row block S of an orthonormal n x 3 frame has sigma_min(R_S)^2 >= 1/(3(n-2)).
worst = np.inf
for trial in range(300):
    n = np.random.randint(3, 11)
    R = np.linalg.qr(np.random.randn(n, 3) * np.exp(np.random.randn(n, 1)))[0]
    best = max(combinations(range(n), 3), key=lambda S: abs(np.linalg.det(R[list(S)])))
    smin2 = np.linalg.svd(R[list(best)], compute_uv=False)[-1]**2
    worst = min(worst, smin2 * 3 * (n - 2))
print(f"Prop 4.1(b): min over 300 frames of sigma_min(R_S)^2 * 3(n-2) = {worst:.4f} (must be >= 1)", flush=True)
# Lemma 1.5: #{|eig(A/A_PP)| >= 1} >= #{|eig(A)| >= 1} - |P|, including singular A.
bad = 0; tot = 0
for trial in range(4000):
    n = np.random.randint(3, 8)
    k = np.random.randint(0, n)
    Q = np.linalg.qr(np.random.randn(n, n))[0]
    ev = np.concatenate([np.random.choice([-1, 1], k) * (1 + np.random.exponential(1, k)),
                         np.random.uniform(-0.999, 0.999, n - k)])
    if trial % 4 == 0: ev[-1] = 0.0          # singular cases
    if trial % 7 == 0 and k > 0: ev[0] = np.sign(ev[0])   # eigenvalue exactly +-1
    A = Q @ np.diag(ev) @ Q.T
    cnt = np.sum(np.abs(np.linalg.eigvalsh(A)) >= 1 - 1e-12)
    for p in (1, 2):
        P = list(np.random.choice(n, p, replace=False)); C = [i for i in range(n) if i not in P]
        App = A[np.ix_(P, P)]
        if abs(np.linalg.det(App)) < 1e-8: continue
        S = A[np.ix_(C, C)] - A[np.ix_(C, P)] @ np.linalg.solve(App, A[np.ix_(P, C)])
        c2 = np.sum(np.abs(np.linalg.eigvalsh(S)) >= 1 - 1e-9)
        tot += 1
        if c2 < cnt - p: bad += 1
print(f"Lemma 1.5: {bad} violations in {tot} Schur complements (singular and +-1 cases included)", flush=True)
