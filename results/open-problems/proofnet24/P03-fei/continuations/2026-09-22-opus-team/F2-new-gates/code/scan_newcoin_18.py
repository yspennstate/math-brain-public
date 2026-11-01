"""Add one new coin to Numaro's g: for every cube edge (a, b = a ^ e_i) of the 18-cube with g(a) = +1, g(b) = -1,
replace both values by a fresh variable z (F = z on {a, b}).  Balance is preserved.  Exact incremental formulas:
  Walsh change:   W(S) -> W(S) - 2 chi_S(a) for S containing i, unchanged otherwise;
  I2 change:      core   (the true-false edge formula 2m-6-4(t_a+f_b); t_a = true neighbours of a other than b, f_b = false neighbours of b
                  other than a), plus the new pair's own term 2m + 2;
  H change:       core entropy change + 4(m-1)/N for the pair.
All 2^18 x (edges) candidates are scanned; top results printed and re-verified from scratch."""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, numba as nb, time
from holecore import fwht_int, make_phi, make_par, summarize

BASE = r"~/mop-fei-opus/proofnet24/P03-fei/continuations/2026-09-22-opus-team"


@nb.njit(cache=True)
def scan(g, m, phi, par, topk):
    N = g.shape[0]
    W = fwht_int(g)
    Hc = 0.0
    for S in range(N):
        Hc += phi[abs(W[S])]
    I2 = 0
    for x in range(N):
        for i in range(m):
            y = x ^ (1 << i)
            if y > x:
                d = g[x] - g[y]
                I2 += d * d
    R0 = Hc / (I2 / (2.0 * N) - 1.0)
    outR = np.full(topk, -1e9); outm = np.zeros((topk, 2), dtype=np.int64)
    for a in range(N):
        if g[a] != 1:
            continue
        for i in range(m):
            b = a ^ (1 << i)
            if g[b] != -1:
                continue
            ta = 0; fb = 0
            for j in range(m):
                if j == i:
                    continue
                if g[a ^ (1 << j)] == -1:
                    ta += 1
                if g[b ^ (1 << j)] == 1:
                    fb += 1
            # core: a (+1 -> 0): m-1-4ta ; b (-1 -> 0): m-1-4fb ; edge ab: -4 ; new pair: (m+2)*2 - 2
            dI2 = (2 * m - 6 - 4 * (ta + fb)) + (2 * m + 2)
            # entropy change over S containing i
            dH = 0.0
            bit = 1 << i
            # enumerate S with bit i set: S = s | bit for s over subsets without bit i
            for s in range(N >> 1):
                lo = s & (bit - 1)
                S = ((s - lo) << 1) | bit | lo
                chi = 1 - 2 * par[S & a]
                v = W[S] - 2 * chi
                dH += phi[abs(v)] - phi[abs(W[S])]
            H = Hc + dH + 4.0 * (m - 1) / N
            I = (I2 + dI2) / (2.0 * N)
            R = H / (I - 1.0)
            if R > outR[topk - 1]:
                j = topk - 1
                while j > 0 and outR[j - 1] < R:
                    outR[j] = outR[j - 1]; outm[j] = outm[j - 1]; j -= 1
                outR[j] = R; outm[j, 0] = a; outm[j, 1] = i
    return R0, outR, outm


if __name__ == '__main__':
    g = np.load(BASE + "/inputs/numaro18_pm1_table.npy").astype(np.int64)
    m = 18; N = 1 << m
    phi = make_phi(N); par = make_par(N)
    t = time.time()
    R0, R, mv = scan(g, m, phi, par, 15)
    print(f"scan time {time.time()-t:.0f}s  base R0 = {R0:.15f}")
    for r, (a, i) in zip(R, mv):
        print(f"  R = {r:.15f}  ({r - R0:+.3e})  edge a={a} dir={i}  core cell={a & 511} aux bits={a >> 9:09b}")
    # re-verify the best from scratch with the generic evaluator (m = 18 core with one hole pair)
    a, i = mv[0]
    c = g.copy(); c[a] = 0; c[a ^ (1 << i)] = 0
    s = summarize(c, 18)
    print("recheck best from scratch:", s['R'], s['holes'], s['nvars'])
