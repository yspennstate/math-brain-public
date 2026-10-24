try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Deterministic chain of the no-pivot PSD proposition, big block = top k eigen-indices.
# For each random partition compute:
#   S   = sum_{m<=k} |N e_m|^2 / lambda_m^2              (Lemma S needs <= 1/8)
#   E1  = ||Lambda_b^{-1/2} N_bb Lambda_b^{-1/2}||_F^2      (needs <= 1/64)
#   E2  = (2/rho) ||N_sb Lambda_b^{-1/2}||_F^2               (needs <= 1/8), rho = kappa/lambda_k, kappa = lambda_k^2/(16k)
# and check: s_k(A_IJ) >= lambda_k/4 ; ridge bound ; alpha_i <= 8 l_i + (4/rho)|b_i^s|^2 ; true alpha (k-volume).
# Also compare empirical means of S, E1, E2 with the formulas used in the Markov steps.
import numpy as np
from scipy.linalg import hadamard
rng = np.random.default_rng(2026)

def esym_all(vals, k):
    e = np.zeros(k + 1); e[0] = 1.0
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += e[j - 1] * v
    return e

def true_marg(M, k):
    G = M @ M.T
    sig, U = np.linalg.eigh(G); sig = np.clip(sig, 0, None)
    ek = esym_all(sig, k)
    p = np.zeros_like(sig)
    for m in range(len(sig)):
        em = np.zeros(k + 1); em[0] = 1.0
        for j in range(1, k + 1):
            em[j] = ek[j] - sig[m] * em[j - 1]
        p[m] = sig[m] * em[k - 1] / ek[k]
    return (U ** 2) @ p, np.sort(sig)[::-1]

def build(n, spec):
    H = hadamard(n) / np.sqrt(n)
    D = np.diag(rng.choice([-1.0, 1.0], size=n))
    P = rng.permutation(n)
    Q = (D @ H)[P][:, rng.permutation(n)]   # flat orthonormal basis, |entries| = 1/sqrt(n)
    lam = np.zeros(n)
    lam[:len(spec)] = spec
    idx = lam > 0
    B = Q[:, idx] * np.sqrt(lam[idx])
    return B, lam[idx]

n = 1024
cases = {
    "three at 1":            [1.0, 1.0, 1.0],
    "huge + two":            [0.4 * 1024 / 640 * 0 + 1.4, 1.0, 1.0],
    "3 + bulk at lambda_3":  [1.0, 1.0, 1.0] + [1.0] * 0 + [0.999] * 0,
}
specs = [
    ("three at 1", [1.0] * 3),
    ("big+two (lam1=1.5)", [1.5, 1.0, 1.0]),
    ("3 + 60 at 0.9", [1.0] * 3 + [0.9] * 60),
    ("3 + 300 at 0.05", [1.0] * 3 + [0.05] * 300),
    ("30 equal at 1", [1.0] * 30),
]
for name, spec in specs:
    B, lam = build(n, spec)
    order = np.argsort(-lam); B = B[:, order]; lam = lam[order]
    a = np.sum(B ** 2, axis=1); c = a.max()
    for k in (1, 2, 3):
        lk = lam[k - 1]
        kappa = lk ** 2 / (16 * k); rho = kappa / lk
        rows = []
        Svals, E1vals, E2vals = [], [], []
        for rep in range(12):
            eps = rng.choice([-1.0, 1.0], size=n)
            I = np.where(eps > 0)[0]; J = np.where(eps < 0)[0]
            Nm = 0.5 * (B.T * eps) @ B          # N = (1/2) sum eps_i b_i b_i^T
            Lam = np.diag(lam)
            Sval = sum(np.sum(Nm[:, m] ** 2) / lam[m] ** 2 for m in range(k))
            Lb = lam[:k]
            Nbb = Nm[:k, :k] / np.sqrt(np.outer(Lb, Lb))
            E1 = np.sum(Nbb ** 2)
            Nsb = Nm[k:, :k] / np.sqrt(Lb)[None, :]
            E2 = (2 / rho) * np.sum(Nsb ** 2)
            Svals.append(Sval); E1vals.append(E1); E2vals.append(E2)
            M = B[I] @ B[J].T
            alpha, sig = true_marg(M, k)
            sk = np.sqrt(sig[k - 1])
            HI = B[I].T @ B[I]
            ridge = np.array([B[i] @ np.linalg.solve(HI + kappa * np.diag(1 / lam), B[i]) for i in I])
            lev = np.sum(B[I][:, :k] ** 2 / lam[:k][None, :], axis=1)
            bs2 = np.sum(B[I][:, k:] ** 2, axis=1)
            chain = 8 * lev + (4 / rho) * bs2
            conds = (Sval <= 1 / 8, E1 <= 1 / 64, E2 <= 1 / 8)
            ok = (sk >= lk / 4 - 1e-12 or not conds[0]) and (np.all(2 * ridge <= chain + 1e-12) or not (conds[1] and conds[2])) \
                 and np.all(alpha <= 2 * ridge + 1e-12)
            rows.append((sk / lk, alpha.max(), (2 * ridge).max(), chain.max(), all(conds), ok))
        rows = np.array(rows, dtype=float)
        # predicted means: E S <= (1/4) sum_{m<=k} sum_i b_i(m)^2 |b_i|^2 / lam_m^2 ; E E1 = (1/4) sum l_i^2 ; E E2 = (2/rho)(1/4) sum |b^s|^2 l
        l_all = np.sum(B[:, :k] ** 2 / lam[:k][None, :], axis=1)
        pS = 0.25 * sum(np.sum(B[:, m] ** 2 * a) / lam[m] ** 2 for m in range(k))
        pE1 = 0.25 * np.sum(l_all ** 2)
        pE2 = (2 / rho) * 0.25 * np.sum(np.sum(B[:, k:] ** 2, axis=1) * l_all)
        print(f"{name:22s} k={k} c={c:.5f} c/lam_k={c/lk:.5f} | s_k/lam_k min {rows[:,0].min():.3f} | "
              f"alpha max {rows[:,1].max():.4f} <= 2ridge {rows[:,2].max():.4f} <= chain {rows[:,3].max():.4f} "
              f"(64kc/lam_k={64*k*c/lk:.3f}) | conds held {int(rows[:,4].sum())}/12, chain ok {int(rows[:,5].sum())}/12 | "
              f"mean S {np.mean(Svals):.2e} (pred {pS:.2e}) E1 {np.mean(E1vals):.2e} (pred {pE1:.2e}) "
              f"E2 {np.mean(E2vals):.2e} (pred {pE2:.2e})", flush=True)
