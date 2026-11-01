# Averaged restriction step over ALL monotone Boolean functions on n <= 6 variables.
# For each nonconstant f and each coordinate i:
#   Delta_i = H(f) - (H(f|x_i=0) + H(f|x_i=1))/2         (restriction step)
#   B_i     = H(S) - H(S minus i) = H(1[i in S] | S minus i)   (erasure term of the spectral sample S)
#   JS_i    = Delta_i - B_i                              (Jensen-Shannon part, always O(Inf_i))
# Reported maxima: sum_i Delta_i / I (the averaged step), sum_i B_i / I (erasure entropy over influence),
# min_i Delta_i/Inf_i (rho_0, as in mono_enum.py) and the largest single B_i/Inf_i.
# If sum_i Delta_i <= K I for every monotone f, then H <= K I for every monotone f (induction on n, choosing a
# coordinate with Delta_i <= K Inf_i, which exists by averaging; restrictions of monotone functions are monotone).
import sys, time, os, numpy as np
from multiprocessing import Pool
from mono_enum import monotone_masks, walsh, phi

def analyse(args):
    mk, n = args
    N = 1 << n
    G = walsh(mk, n)
    P = G * G
    H = phi(P).sum(1)
    sizes = np.array([bin(s).count('1') for s in range(N)], dtype=np.float64)
    I = (P * sizes[None, :]).sum(1)
    sD = np.zeros(len(mk)); sB = np.zeros(len(mk)); sJ = np.zeros(len(mk))
    rho = np.full(len(mk), np.inf); maxBr = np.zeros(len(mk))
    for i in range(n):
        idx0 = np.array([s for s in range(N) if not (s >> i) & 1])
        a = G[:, idx0]; b = G[:, idx0 | (1 << i)]
        inf = (b * b).sum(1)
        Her = phi(a * a + b * b).sum(1)                   # H(S minus i)
        hch = 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)).sum(1)
        d = H - hch; Bi = H - Her; Ji = Her - hch
        sD += d; sB += Bi; sJ += Ji
        rel = inf > 1e-12
        rho = np.minimum(rho, np.where(rel, d / np.where(rel, inf, 1.0), np.inf))
        maxBr = np.maximum(maxBr, np.where(rel, Bi / np.where(rel, inf, 1.0), 0.0))
    nc = I > 1e-12
    Isafe = np.where(nc, I, 1.0)
    out = {}
    for name, v in (('H/I', H / Isafe), ('sumDelta/I', sD / Isafe), ('sumB/I', sB / Isafe), ('sumJS/I', sJ / Isafe),
                    ('rho0', np.where(np.isfinite(rho), rho, 0.0)), ('maxB_i/Inf_i', maxBr)):
        v = np.where(nc, v, -1.0)
        k = int(np.argmax(v))
        out[name] = (float(v[k]), int(mk[k]), float(H[k]), float(I[k]))
    # minimum JS_i/Inf_i sanity: JS >= 0 always
    out['minJS'] = float(sJ.min())
    return out

if __name__ == '__main__':
    try:
        import psutil
        p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception as e:
        print('priority/affinity not set:', e)
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for n in [int(v) for v in sys.argv[1].split(',')]:
        t0 = time.time()
        masks = monotone_masks(n)
        chunk = 50000
        jobs = [(masks[s:s + chunk], n) for s in range(0, len(masks), chunk)]
        best = {}
        minJS = 0.0
        with Pool(workers) as pool:
            for out in pool.imap_unordered(analyse, jobs):
                minJS = min(minJS, out.pop('minJS'))
                for k, v in out.items():
                    if k not in best or v[0] > best[k][0]:
                        best[k] = v
        print('n %d: %d monotone functions, %.1f s' % (n, len(masks), time.time() - t0))
        for k in ('H/I', 'sumDelta/I', 'sumB/I', 'sumJS/I', 'rho0', 'maxB_i/Inf_i'):
            v, m, h, i = best[k]
            print('  max %-13s %.6f  mask %s  (H %.6f, I %.6f)' % (k, v, hex(m), h, i))
        print('  min sum JS (should be >= -1e-12): %.3e' % minJS, flush=True)
