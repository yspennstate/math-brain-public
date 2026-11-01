"""B18 lead check: does the n<=4 good-coordinate constant K* survive on lexicographic (threshold-on-index) functions?
f_t(x) = 1 - 2*[sum_i x_i 2^i < t] on n uniform bits (x_{n-1} most significant).
For each f: min over relevant i of B_i/Inf_i (bits), and H/I.
Frozen domain: n=2..12 every t in 1..2^n-1; n=13,14: t on an equally spaced grid of 1024 values plus floor/ceil of
N/3, 2N/3, N/5, N/7.  Float64 (evidence; exact recheck of the reported maxima is a follow-up). Memory < 60 MB.
"""
import numpy as np, math, json, sys
KSTAR = 4 + 2.5 * math.log2(5) - 4.5 * math.log2(3)
C_IND = KSTAR + 2 / math.log(2)
def fwht_rows(A):
    R, N = A.shape; h = 1
    while h < N:
        B = A.reshape(R, N // (2 * h), 2, h)
        x = B[:, :, 0, :].copy(); y = B[:, :, 1, :].copy()
        B[:, :, 0, :] = x + y; B[:, :, 1, :] = x - y
        h *= 2
    return A
def analyse(n, ts):
    N = 1 << n
    idx = np.arange(N)
    pc = np.array([bin(s).count('1') for s in range(N)], dtype=float)
    rows = []
    for c0 in range(0, len(ts), 64):
        tt = np.array(ts[c0:c0 + 64])
        F = np.where(idx[None, :] < tt[:, None], -1.0, 1.0)
        W = fwht_rows(F.copy()) / N
        p = W * W
        with np.errstate(divide='ignore', invalid='ignore'):
            H = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1)), 0).sum(1)
        I = (p * pc[None, :]).sum(1)
        minr = np.full(len(tt), np.inf); argi = np.full(len(tt), -1)
        for i in range(n):
            B4 = p.reshape(len(tt), N // (2 << i), 2, 1 << i)
            pa = B4[:, :, 0, :]; pb = B4[:, :, 1, :]; m = pa + pb
            with np.errstate(divide='ignore', invalid='ignore'):
                xb = np.where(m > 0, pb / np.where(m > 0, m, 1), 0)
                h2 = np.where((xb > 0) & (xb < 1), -xb * np.log2(np.where(xb > 0, xb, 1)) - (1 - xb) * np.log2(np.where(xb < 1, 1 - xb, 1)), 0)
            Bi = (m * h2).sum((1, 2)); Inf = pb.sum((1, 2))
            r = np.where(Inf > 1e-14, Bi / np.where(Inf > 1e-14, Inf, 1), np.inf)
            better = r < minr; minr = np.where(better, r, minr); argi = np.where(better, i, argi)
        for k in range(len(tt)):
            rows.append((int(tt[k]), float(minr[k]), int(argi[k]), float(H[k]), float(I[k])))
    return rows
res = {'Kstar': KSTAR, 'Kstar_plus_2_over_ln2': C_IND, 'per_n': {}}
for n in range(2, 15):
    N = 1 << n
    if n <= 12:
        ts = list(range(1, N))
    else:
        ts = sorted(set([int(round(N * (j + 0.5) / 1024)) for j in range(1024)] + [N // 3, N // 3 + 1, 2 * N // 3, 2 * N // 3 + 1, N // 5, N // 5 + 1, N // 7, N // 7 + 1]))
    rows = analyse(n, ts)
    best = max(rows, key=lambda r: r[1])
    bestHI = max(rows, key=lambda r: r[3] / r[4])
    nabove = sum(1 for r in rows if r[1] > KSTAR + 1e-9)
    res['per_n'][n] = {'n_t': len(ts), 'max_min_ratio': best[1], 't_at_max': best[0], 'coord_at_max': best[2],
                       'H_over_I_at_max': best[3] / best[4], 'max_H_over_I': bestHI[3] / bestHI[4], 't_max_H_over_I': bestHI[0],
                       'min_ratio_at_max_H_over_I': bestHI[1], 'count_min_ratio_above_Kstar': nabove}
    print(n, res['per_n'][n], flush=True)
json.dump(res, open(sys.argv[1], 'w'), indent=1)
