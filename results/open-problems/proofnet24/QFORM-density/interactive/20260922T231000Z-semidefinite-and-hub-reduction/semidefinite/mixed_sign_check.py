try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Mixed-sign version: M = B S B^T, |b_i|^2 = |M|_ii.
# (1) identity <B_I S g, M_IJ B_J g> = |Lam g|^2/4 - (g_-^T|Lam| N g_+ + g_+^T |Lam| N g_-) - (S N S g).(N g)
# (2) |B_I S g|^2 + |B_J g|^2 = g^T|Lam| g - 4 g_+^T N g_-
# (3) Lemma S': if sum_K |N e_m|^2/lam_m^2 <= eta^2 and ||Lam_G^{-1/2} N_GG Lam_G^{-1/2}|| <= eta',
#     then s_k(M_IJ) >= theta (1/4 - eta - 2 eta^2)/(1/2 + eta')
# (4) Lemma M: alpha_i <= 2 b_i^T (H_I + kappa |Lam|^{-1})^{-1} b_i for kappa <= s_k^2/k
import numpy as np
from scipy.linalg import hadamard
rng = np.random.default_rng(99)

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

worst_id = 0.0; worst_id2 = 0.0; viol_S = 0; viol_M = 0; tested_S = 0; tested_M = 0
n = 512
H = hadamard(n) / np.sqrt(n)
for trial in range(8):
    Q = (np.diag(rng.choice([-1.0, 1.0], size=n)) @ H)[rng.permutation(n)][:, rng.permutation(n)]
    specs = [
        [1.0, 1.0, -1.0],
        [1.3, -1.0, -1.0] + [0.5] * 20 + [-0.5] * 20,
        [2.0, 1.0, -1.0] + [0.2] * 100 + [-0.2] * 100,
        [1.0, -1.0, 1.0, -1.0, 1.0],
    ]
    spec = np.array(specs[trial % 4])
    r = len(spec)
    B = Q[:, :r] * np.sqrt(np.abs(spec))
    S = np.sign(spec)
    order = np.argsort(-np.abs(spec)); B = B[:, order]; S = S[order]; lamabs = np.abs(spec)[order]
    Mfull = (B * S) @ B.T
    d = np.sum(B ** 2, axis=1)
    for rep in range(3):
        eps = rng.choice([-1.0, 1.0], size=n)
        I = np.where(eps > 0)[0]; J = np.where(eps < 0)[0]
        N = 0.5 * (B.T * eps) @ B
        MIJ = Mfull[np.ix_(I, J)]
        L = np.diag(lamabs)
        for _ in range(4):
            g = rng.standard_normal(r) * (np.arange(r) < 3)
            gp = g * (S > 0); gm = g * (S < 0)
            lhs = (B[I] @ (S * g)) @ MIJ @ (B[J] @ g)
            rhs = np.sum((L @ g) ** 2) / 4 - (gm @ L @ N @ gp + gp @ L @ N @ gm) - (S * (N @ (S * g))) @ (N @ g)
            worst_id = max(worst_id, abs(lhs - rhs) / (1 + abs(rhs)))
            lhs2 = np.sum((B[I] @ (S * g)) ** 2) + np.sum((B[J] @ g) ** 2)
            rhs2 = g @ L @ g - 4 * gp @ N @ gm
            worst_id2 = max(worst_id2, abs(lhs2 - rhs2) / (1 + abs(rhs2)))
        for k in (1, 2, 3):
            K = np.arange(k); theta = lamabs[K].min()
            eta = np.sqrt(sum(np.sum(N[:, m] ** 2) / lamabs[m] ** 2 for m in K))
            NG = N[np.ix_(K, K)] / np.sqrt(np.outer(lamabs[K], lamabs[K]))
            etap = np.linalg.norm(NG, 2)
            alpha, sig = true_marg(MIJ, k)
            sk = np.sqrt(sig[k - 1])
            bound = theta * (0.25 - eta - 2 * eta ** 2) / (0.5 + etap)
            tested_S += 1
            if sk < bound - 1e-12:
                viol_S += 1
            kappa = sk ** 2 / k
            HI = B[I].T @ B[I]
            X = np.linalg.solve(HI + kappa * np.diag(1 / lamabs), B[I].T)
            ridge = np.sum(B[I].T * X, axis=0)
            tested_M += 1
            if np.any(alpha > 2 * ridge + 1e-12):
                viol_M += 1
            if rep == 0:
                print(f"trial {trial} k={k} max|M|_ii={d.max():.4f} eta={eta:.3f} eta'={etap:.3f} "
                      f"s_k/theta={sk/theta:.3f} bound/theta={bound/theta:.3f} alpha_max={alpha.max():.4f} 2ridge_max={2*ridge.max():.4f}", flush=True)
print("identity (1) max rel err:", worst_id, " identity (2):", worst_id2, flush=True)
print(f"Lemma S' violations {viol_S}/{tested_S}; Lemma M violations {viol_M}/{tested_M}", flush=True)
