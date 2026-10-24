"""Relocate one coin site of Numaro's g: the PM(K_{3,3}) core with 9 hole pairs; remove site k (its two cells return
to +1 = false) and put a hole pair on any other cube edge whose two cells are false in PM(K_{3,3}) and not holes.
Balance is preserved.  Also: relocate to a pair of non-adjacent false cells (two singleton coins).
Every candidate is evaluated from scratch (FWHT + component grouping)."""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import json, itertools, time
import numpy as np
import numba as nb
from holecore import fwht_int, make_phi, make_par, core_I2, aux_part

BASE = r"~/mop-fei-opus/proofnet24/P03-fei/continuations/2026-09-22-opus-team"


@nb.njit(cache=True)
def evalR(c0, m, phi, par):
    N = c0.shape[0]
    W = fwht_int(c0)
    Hc = 0.0
    for S in range(N):
        Hc += phi[abs(W[S])]
    I2c = core_I2(c0, m)
    Ha, I2a, nc, mx = aux_part(c0, m, phi, par)
    return (Hc + Ha) / ((I2c + I2a) / (2.0 * N) - 1.0)


@nb.njit(cache=True)
def scan(c0, sites, m, phi, par, topk):
    N = c0.shape[0]
    outR = np.full(topk, -1e9); outm = np.zeros((topk, 3), dtype=np.int64)
    ns = sites.shape[0]
    for k in range(ns):
        a0 = sites[k, 0]; b0 = sites[k, 1]
        c0[a0] = 1; c0[b0] = 1
        for a in range(N):
            if c0[a] != 1:
                continue
            for i in range(m):
                b = a ^ (1 << i)
                if b < a or c0[b] != 1:
                    continue
                if (a == a0 and b == b0) or (a == b0 and b == a0):
                    continue
                c0[a] = 0; c0[b] = 0
                R = evalR(c0, m, phi, par)
                c0[a] = 1; c0[b] = 1
                if R > outR[topk - 1]:
                    j = topk - 1
                    while j > 0 and outR[j - 1] < R:
                        outR[j] = outR[j - 1]; outm[j] = outm[j - 1]; j -= 1
                    outR[j] = R; outm[j, 0] = k; outm[j, 1] = a; outm[j, 2] = b
        c0[a0] = 0; c0[b0] = 0
    return outR, outm


if __name__ == '__main__':
    c0 = np.load(BASE + "/F2-new-gates/logs/numaro_core_c0.npy").astype(np.int64)
    hosts = json.load(open(BASE + "/F2-new-gates/logs/numaro_decomposition.json", encoding="utf-8"))["hosts"]
    sites = np.array(hosts, dtype=np.int64)
    m, N = 9, 512
    phi = make_phi(N); par = make_par(N)
    base = evalR(c0.copy(), m, phi, par)
    t = time.time()
    R, mv = scan(c0.copy(), sites, m, phi, par, 12)
    print(f"relocation scan {time.time()-t:.1f}s   base {base:.15f}")
    for r, (k, a, b) in zip(R, mv):
        print(f"  R = {r:.15f} ({r-base:+.3e})  site {k} {hosts[k]} -> edge ({a},{b}) weights {bin(a).count('1')},{bin(b).count('1')}")
