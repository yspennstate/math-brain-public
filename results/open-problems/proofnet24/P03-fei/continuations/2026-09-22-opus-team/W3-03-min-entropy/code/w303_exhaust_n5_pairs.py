"""Exhaustive over all Boolean functions of 5 variables via pairs f = (f0, f1) of 4-variable functions
(f0 = restriction x_4 = 0, f1 = restriction x_4 = 1).

With integer Walsh tables W0, W1 of the halves (length 16, sum of squares 256 each):
    W(S') = W0(S') + W1(S'),  W(S' u {4}) = W0(S') - W1(S'),
    Wmax = max_S' (|W0(S')| + |W1(S')|),
    J := 1024 I = 2 (J0 + J1) + 512 - 2 <W0, W1>,   J_k := sum_{|S'|} |S'| W_k(S')^2,
    Q := sum_S W(S)^4 = sum_S' [(W0+W1)^4 + (W0-W1)^4]      (H2 = log2(2^20 / Q)).
f0 ranges over representatives of the 222 classes of 4-variable functions under input permutations,
input negations and output negation (acting on both halves at once), f1 over all 65,536 functions.
Integer arithmetic throughout: exact.
"""
import sys, json, time, itertools
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])

t0 = time.time()
n0 = 4
N0 = 16
X = np.arange(N0)
masks = np.arange(1 << N0, dtype=np.int64)
bits = ((masks[:, None] >> X[None, :]) & 1).astype(np.int64)        # bit=1 -> f(x) = -1
pm = 1 - 2 * bits
chi = np.array([[1 - 2 * (bin(x & S).count("1") & 1) for S in range(N0)] for x in range(N0)], dtype=np.int64)
Wall = pm @ chi                                                     # (65536, 16) integer Walsh
pc = np.array([bin(S).count("1") for S in range(N0)], dtype=np.int64)
Jall = (Wall * Wall) @ pc

# canonical forms under B4 x Z2
canon = masks.copy()
for perm in itertools.permutations(range(n0)):
    for sig in range(N0):
        idx = np.array([sum(((x >> perm[j]) & 1) << j for j in range(n0)) ^ sig for x in X])
        m2 = (bits[:, idx] << X[None, :]).sum(axis=1)
        canon = np.minimum(canon, m2)
        canon = np.minimum(canon, m2 ^ 0xFFFF)
reps = np.unique(canon)
print("classes:", len(reps), f"{time.time() - t0:.1f}s", flush=True)

absW1 = np.abs(Wall)
best = {}          # Wmax -> (minJ, mask5)
bestH2 = (-1.0, None)
best_minus4 = (-1e9, None)
count = 0
for r in reps:
    W0 = Wall[r]
    wmax = (np.abs(W0)[None, :] + absW1).max(axis=1)
    J = 2 * (Jall[r] + Jall) + 512 - 2 * (Wall @ W0)
    Q = (((W0[None, :] + Wall) ** 4) + ((W0[None, :] - Wall) ** 4)).sum(axis=1)
    count += len(Wall)
    for wv in np.unique(wmax):
        sel = (wmax == wv) & (J > 0)
        if not sel.any():
            continue
        k = np.argmin(np.where(sel, J, 1 << 40))
        if wv not in best or J[k] < best[wv][0]:
            best[int(wv)] = (int(J[k]), int(r) | (int(k) << 16))
    nz = J > 0
    with np.errstate(divide="ignore"):
        h2r = np.where(nz, np.log2(2.0 ** 20 / Q) / np.where(nz, J / 1024.0, 1), -1)
        hinf = 10 - 2 * np.log2(wmax)
        d4 = np.where(nz, hinf - 4 * J / 1024.0, -1e9)
    k = int(np.argmax(h2r))
    if h2r[k] > bestH2[0]:
        bestH2 = (float(h2r[k]), int(r) | (k << 16))
    k = int(np.argmax(d4))
    if d4[k] > best_minus4[0]:
        best_minus4 = (float(d4[k]), int(r) | (k << 16))
table = []
for wv in sorted(best):
    J, m = best[wv]
    Hinf = 10 - 2 * np.log2(wv)
    table.append(dict(Wmax=wv, minJ=J, I=J / 1024, Hinf=float(Hinf), ratio=float(Hinf / (J / 1024)), mask=hex(m)))
out = dict(pairs_checked=count, seconds=time.time() - t0, table=table,
           max_H2_over_I=bestH2[0], max_H2_over_I_mask=hex(bestH2[1]),
           max_Hinf_minus_4I=best_minus4[0], max_Hinf_minus_4I_mask=hex(best_minus4[1]))
print(json.dumps(out, indent=1))
