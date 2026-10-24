# Exhaustive check over all monotone functions on n <= 6 variables of
#  (T1) the restriction-step bound at every coordinate:
#        Delta_v <= Inf_v * (2/ln2 + c0 + Psi(4m/Inf_v - 2)),   m = min(Pr[f=0], Pr[f=1]),
#        c0 = 2 e^{-1/2}/ln 2 = 1.7499,  Psi(r) = log2(e (r + 2 sqrt(r) + 2));
#  (T2) the relative Han bound: H <= sum_v Inf_v * (2/ln2 + c0 + Psi(4m/Inf_v - 2)).
# Prints the largest ratio left/right for each (must stay below 1 if the proofs are right).
import sys, time, numpy as np
from multiprocessing import Pool
from mono_enum import monotone_masks, walsh, phi

C0 = 2 * np.exp(-0.5) / np.log(2); JSC = 2 / np.log(2)

def Psi(r):
    r = np.maximum(r, 0.0)
    return np.log2(np.e * (r + 2 * np.sqrt(r) + 2))

def analyse(args):
    mk, n = args
    N = 1 << n
    G = walsh(mk, n)
    P = G * G
    H = phi(P).sum(1)
    q = (1.0 + G[:, 0]) / 2.0
    m = np.minimum(q, 1.0 - q)
    rhs2 = np.zeros(len(mk)); worst1 = (0.0, None)
    for v in range(n):
        idx0 = np.array([s for s in range(N) if not (s >> v) & 1])
        a = G[:, idx0]; b = G[:, idx0 | (1 << v)]
        inf = (b * b).sum(1)
        hch = 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)).sum(1)
        d = H - hch
        rel = inf > 1e-14
        infs = np.where(rel, inf, 1.0)
        bnd = np.where(rel, inf * (JSC + C0 + Psi(4 * m / infs - 2)), 0.0)
        rhs2 += bnd
        ratio = np.where(rel, d / np.where(bnd > 0, bnd, 1.0), 0.0)
        k = int(np.argmax(ratio))
        if ratio[k] > worst1[0]:
            worst1 = (float(ratio[k]), (int(mk[k]), v, float(d[k]), float(bnd[k]), float(inf[k]), float(m[k])))
    nc = rhs2 > 1e-14
    r2 = np.where(nc, H / np.where(nc, rhs2, 1.0), 0.0)
    k = int(np.argmax(r2))
    worst2 = (float(r2[k]), (int(mk[k]), float(H[k]), float(rhs2[k])))
    return worst1, worst2

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
        b1 = (0.0, None); b2 = (0.0, None)
        with Pool(workers) as pool:
            for w1, w2 in pool.imap_unordered(analyse, jobs):
                if w1[0] > b1[0]: b1 = w1
                if w2[0] > b2[0]: b2 = w2
        print('n %d: %d functions (%.1f s)' % (n, len(masks), time.time() - t0))
        print('   T1 max Delta_v / bound = %.6f   at (mask, v, Delta, bound, Inf, m) = %s' % b1)
        print('   T2 max H / (relative Han bound) = %.6f   at (mask, H, bound) = %s' % b2, flush=True)
