"""Parallel value iteration for the read-once slack on the certificate grid, plus a convergence check on an
existing candidate.  Same operator as fei_cert_vi.py (exact same E, grid and interpolation), split over cores.

  vi_par.py check <npz>                       one T step on a saved candidate: how far from a fixed point
  vi_par.py run <M> <K> <C> <tag> <iters> <fine> <procs>
"""
import sys, os, time, math
import numpy as np
from multiprocessing import Pool
import fei_cert_vi as V
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

_W = {}
def _init(M, K, fine):
    _W["grid"] = V.Grid(M, K, fine)

def _chunk(args):
    lo, hi, G = args
    g = _W["grid"]
    allp, Lall = g.all_p, g.Lall
    rs = np.concatenate([g.ps, 1 - g.ps[1:]])[lo:hi]
    Gam_all = g.gamma_at(G, allp)
    out = np.full(len(rs), np.inf)
    Bsz = 64
    for i0 in range(0, len(rs), Bsz):
        r = rs[i0:i0 + Bsz][:, None]; p = allp[None, :]
        q = r / p
        valid = (q < 1 - 1e-15) & (q > 1e-300)
        qc = np.where(valid, q, 0.5)
        Lq = np.log2(1 / qc)
        Gq = g.gamma_at(G, qc)
        rhs = qc * Gam_all[None, :] + p * Gq - p * qc * V.E_fun(p, qc, Lall[None, :], Lq)
        out[i0:i0 + Bsz] = np.where(valid, rhs, np.inf).min(axis=1)
    return lo, out

def Tpar(pool, G, N, total, procs):
    step = max(1, (total + procs - 1) // procs)
    jobs = [(lo, min(lo + step, total), G) for lo in range(0, total, step)]
    Tv = np.empty(total)
    for lo, out in pool.imap_unordered(_chunk, jobs):
        Tv[lo:lo + len(out)] = out
    Ts = Tv[:N].copy(); Ts[1:] = np.minimum(Ts[1:], Tv[N:])
    return Ts

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "check":
        d = np.load(sys.argv[2]); M, K = int(d["M"]), int(d["K"]); fine = int(d["fine"]) if "fine" in d else 1
        procs = int(sys.argv[3]) if len(sys.argv) > 3 else 6
        g = V.Grid(M, K, fine); G = np.asarray(d["G"], float); Gam = G * g.ps
        N = len(g.ps); total = 2 * N - 1
        with Pool(procs, initializer=_init, initargs=(M, K, fine)) as pool:
            t0 = time.time(); Ts = Tpar(pool, G, N, total, procs)
        drop = Gam - np.minimum(Gam, Ts)
        print("candidate %s  M=%d K=%d fine=%d  nodes=%d   one T step took %.0f s" % (sys.argv[2], M, K, fine, N, time.time() - t0))
        print("  max drop (Gamma units) %.3e at p=%.6g ; max drop in G units %.3e ; nodes needing a drop: %d/%d"
              % (drop.max(), g.ps[int(np.argmax(drop))], (drop / g.ps).max(), int((drop > 1e-12).sum()), N))
        print("  min Gamma after one more step: %.3e" % np.minimum(Gam, Ts).min())
    else:
        M, K, C, tag = int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
        iters = int(sys.argv[6]); fine = int(sys.argv[7]); procs = int(sys.argv[8])
        g = V.Grid(M, K, fine); N = len(g.ps); total = 2 * N - 1
        Gam = np.full(N, 60.0); Gam[0] = C; G = Gam / g.ps
        here = os.path.dirname(os.path.abspath(__file__))
        print("vi_par M=%d K=%d fine=%d C=%.7f nodes=%d procs=%d" % (M, K, fine, C, N, procs), flush=True)
        t0 = time.time()
        with Pool(procs, initializer=_init, initargs=(M, K, fine)) as pool:
            for k in range(iters):
                Ts = Tpar(pool, G, N, total, procs)
                Gam2 = np.minimum(Gam, Ts)
                diff = np.max(np.abs(Gam2 - Gam) / g.ps)
                Gam = Gam2; G = Gam / g.ps
                if k % 5 == 0 or diff < 1e-12:
                    print("  iter %4d  max dG %.3e  min Gamma %.3e  (%.0f s)" % (k, diff, Gam.min(), time.time() - t0), flush=True)
                    np.savez(os.path.join(here, "cert_vi_%s.npz" % tag), xs=g.xs, G=G, C=C, M=M, K=K, fine=fine, iters=k + 1)
                if Gam.min() < -1e-9:
                    print("  INFEASIBLE at iter %d (min Gamma %.3e)" % (k, Gam.min())); break
                if diff < 1e-12:
                    print("  converged at iter %d" % k); break
        np.savez(os.path.join(here, "cert_vi_%s.npz" % tag), xs=g.xs, G=G, C=C, M=M, K=K, fine=fine, iters=k + 1)
        alpha = 2 * (C - 4); w = G - alpha * g.xs
        print("done: min Gamma %.3e  wobble min %.6f max %.6f end %.6f" % ((G * g.ps).min(), w.min(), w.max(), w[-1]))
