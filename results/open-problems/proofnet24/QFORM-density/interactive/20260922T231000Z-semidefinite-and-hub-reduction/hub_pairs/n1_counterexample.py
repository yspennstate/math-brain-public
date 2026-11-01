"""N1. Two hubs with an indefinite hub block and the Schur-matching remainder R = L^T B^{-1} L.
Prediction: Q = Y^T B Y with Y = X_H + B^{-1} L has a logarithmically divergent density at 0,
p_Q(s) ~ (rho(0)/b) log(b/|s|) for B = diag(b,-b), and ~ (rho(0)/e) log(e/|s|) for B = [[0,e],[e,0]],
where rho(0) = E[f1(-Z1) f2(-Z2)] is the density of Y at the origin.
Estimator: exact conditional sublevel probability given (X', X1), averaged over samples."""
try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('/', 1)[0])
from hubpair_lib import UnionLaw, pair_prob, spread_rows

rng = np.random.default_rng(20260923)
m, sigma = 80, 1.0
A = spread_rows(m, sigma, rng)
print("row norms", np.linalg.norm(A, axis=1), "max |entry|", np.abs(A).max(), flush=True)
lawU = UnionLaw.interval()
N = 300_000
t0 = time.time()

def run(B, label, nrep=4):
    B = np.array(B, float)
    Binv = np.linalg.inv(B)
    eps_list = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
    acc = np.zeros(len(eps_list))
    acc2 = np.zeros(len(eps_list))
    rho0 = 0.0
    for rep in range(nrep):
        Xp = rng.random((N, m)) - 0.5
        L = Xp @ A.T                      # (N, 2), beta = 0
        c = 2 * L
        r = np.einsum('ni,ij,nj->n', L, Binv, L)   # R = L^T B^{-1} L
        x1 = lawU.sample(N, rng)
        Z = L @ Binv.T                    # Z = B^{-1} L, Y = X_H + Z
        rho0 += np.mean(lawU.measure(-Z[:, 0] - 1e-3, -Z[:, 0] + 1e-3) / 2e-3 *
                        lawU.measure(-Z[:, 1] - 1e-3, -Z[:, 1] + 1e-3) / 2e-3)
        for k, eps in enumerate(eps_list):
            p = pair_prob(B, c[:, 0], c[:, 1], r, x1, 0.0, eps, lawU) / (2 * eps)
            acc[k] += p.mean()
            acc2[k] += (p ** 2).mean()
    acc /= nrep; acc2 /= nrep; rho0 /= nrep
    se = np.sqrt((acc2 - acc ** 2) / (N * nrep))
    scale = abs(np.linalg.det(B)) ** 0.5
    print(f"--- {label}: B = {B.tolist()}, rho_Y(0) ~ {rho0:.4f}, predicted log slope rho0/sqrt|detB| = {rho0/scale:.4f}", flush=True)
    for k, eps in enumerate(eps_list):
        print(f"   eps={eps:.0e}  P(|Q|<=eps)/(2eps) = {acc[k]:.4f} +- {se[k]:.4f}", flush=True)
    sl = np.polyfit(np.log(1 / np.array(eps_list[2:])), acc[2:], 1)[0]
    print(f"   fitted slope in log(1/eps) over eps<=1e-3: {sl:.4f}   (elapsed {time.time()-t0:.0f}s)", flush=True)

run([[0.2, 0.0], [0.0, -0.2]], "indefinite diagonal hub block, b = 0.2")
run([[0.0, 0.2], [0.2, 0.0]], "pure hub-hub coupling e = 0.2, zero hub diagonals")
run([[0.05, 0.0], [0.0, -0.05]], "indefinite diagonal hub block, b = 0.05")
# control: same remainder shape but definite hub block -> bounded (perfect square b|Y|^2)
run([[0.2, 0.0], [0.0, 0.2]], "CONTROL definite hub block b = 0.2 (perfect square)")
