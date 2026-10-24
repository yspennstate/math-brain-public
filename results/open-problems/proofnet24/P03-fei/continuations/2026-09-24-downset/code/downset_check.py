# Check of the down-set erasure lemma over ALL monotone Boolean functions on n <= 6 variables.
# Claim: for monotone f with q = Pr[f = 0], F = 1 - 2f, every coordinate v satisfies
#     B_v(F) <= 1.75*Inf_v + log2(5e)*(4*min(q, 1-q) - Inf_v),
# where B_v = H(S) - H(S minus v) is the erasure term and Inf_v the influence.  Intermediate identities checked on the
# way (down-set side, mu uniform on {f = 0}, a(T) = coefficient of T+v over 2q, b(T) = coefficient of T over 2q - a):
#     sum_T q a(T)^2 = eps_v = Inf_v/(4q),   sum_T q b(T)^2 = 1 - 2 eps_v.
# Reports the largest ratio (left side)/(right side) and the largest violation, if any.
import sys, time, numpy as np
from multiprocessing import Pool
from mono_enum import monotone_masks, walsh, phi

L5E = np.log2(5 * np.e)

def Efun(x, y):
    return phi(x) + phi(y) - phi(x + y)

def analyse(args):
    mk, n = args
    N = 1 << n
    G = walsh(mk, n)                      # G = fhat for F = +1 where f = 0, -1 where f = 1
    P = G * G
    q = (1.0 + G[:, 0]) / 2.0             # Pr[f = 0]  (E F = 1 - 2 Pr[f=1] = 2q - 1)
    qm = np.minimum(q, 1.0 - q)
    worst_ratio = 0.0; worst_info = None; max_viol = -np.inf; id_err = 0.0
    for v in range(n):
        idx0 = np.array([s for s in range(N) if not (s >> v) & 1])
        u = G[:, idx0]; w = G[:, idx0 | (1 << v)]
        inf = (w * w).sum(1)
        B = Efun(u * u, w * w).sum(1)
        rhs = 1.75 * inf + L5E * (4.0 * qm - inf)
        rel = inf > 1e-14
        viol = np.where(rel, B - rhs, -np.inf)
        k = int(np.argmax(viol))
        max_viol = max(max_viol, float(viol[k]))
        ratio = np.where(rel & (rhs > 1e-300), B / np.where(rhs > 1e-300, rhs, 1.0), 0.0)
        k = int(np.argmax(ratio))
        if ratio[k] > worst_ratio:
            worst_ratio = float(ratio[k]); worst_info = (int(mk[k]), v, float(B[k]), float(rhs[k]), float(inf[k]), float(q[k]))
        # identities on the down-set side (only where 0 < q): a = w/(2q) for T nonempty... use full vectors:
        # F-hat(T) = 2q mu~(T) - [T = empty], so mu~(T) = (G(T) + [T=empty])/(2q).
        qs = np.where(q > 1e-14, q, 1.0)
        mt_T = u.copy(); mt_T[:, 0] += 1.0; mt_T /= (2 * qs)[:, None]     # mu~(T) for T not containing v
        mt_Tv = w / (2 * qs)[:, None]                                    # mu~(T + v)
        a = mt_Tv; b = mt_T - mt_Tv
        eps = inf / (4 * qs)
        e1 = np.abs((qs[:, None] * a * a).sum(1) - eps)
        e2 = np.abs((qs[:, None] * b * b).sum(1) - (1 - 2 * eps))
        ok = q > 1e-14
        id_err = max(id_err, float(np.where(ok, np.maximum(e1, e2), 0).max()))
    return worst_ratio, worst_info, max_viol, id_err

if __name__ == '__main__':
    try:
        import psutil
        p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception as e:
        print('priority/affinity not set:', e)
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for n in [int(t) for t in sys.argv[1].split(',')]:
        t0 = time.time()
        masks = monotone_masks(n)
        jobs = [(masks[s:s + 50000], n) for s in range(0, len(masks), 50000)]
        best = (0.0, None); mv = -np.inf; ie = 0.0
        with Pool(workers) as pool:
            for r, info, viol, err in pool.imap_unordered(analyse, jobs):
                if r > best[0]: best = (r, info)
                mv = max(mv, viol); ie = max(ie, err)
        print('n %d: %d functions (%.1f s): max B_v/bound = %.6f at %s; max violation %.3e; identity error %.2e'
              % (n, len(masks), time.time() - t0, best[0], best[1], mv, ie), flush=True)
