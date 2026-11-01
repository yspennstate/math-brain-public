"""Hard families: per-coordinate, existential and max-influence erasure ratios.

For every function: H, I, B = sum_i B_i, max_i B_i/Inf_i, min_i B_i/Inf_i (existential selector),
rho0 = min_i Delta_i/Inf_i, and the ratio at the max-influence coordinate."""
import sys, json, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from feilib import *

set_polite()


def report(name, tt, n):
    tt = np.asarray(tt, dtype=np.float64)[None, :]
    fh, p = spectra(tt)
    H = float(entropy(p)[0]); I = float(total_influence(p, n)[0])
    cq = coord_quantities(fh, n)
    Inf = cq["Inf"][0]; B = cq["B"][0]; D = cq["Delta"][0]; eta = cq["eta"][0]
    rel = Inf > 1e-13
    rB = np.where(rel, B / np.where(rel, Inf, 1), np.nan)
    rD = np.where(rel, D / np.where(rel, Inf, 1), np.nan)
    istar = int(np.argmax(Inf))
    row = dict(name=name, n=n, H=H, I=I, H_over_I=H / I, B_over_I=float(B.sum()) / I,
               max_i_BoverInf=float(np.nanmax(rB)), exist_min_i_BoverInf=float(np.nanmin(rB)),
               rho0=float(np.nanmin(rD)), maxinf_coord=istar, maxinf=float(Inf[istar]),
               ratio_at_maxinf=float(rB[istar]), eta_over_inf_min=float(np.nanmin(np.where(rel, eta / np.where(rel, Inf, 1), np.nan))))
    print(json.dumps(row))
    sys.stdout.flush()
    return row


def maj_plus_maxfalse_flip(n):
    """Monotone: Maj_n(y) OR (z AND y == y*), y* a maximal false point of Maj_n (weight (n-1)/2).
    Coordinates 0..n-1 are y, coordinate n is z.  -1 = true."""
    N = 1 << (n + 1)
    ystar = (1 << ((n - 1) // 2)) - 1  # first (n-1)/2 bits set
    tt = np.empty(N, dtype=np.int8)
    for x in range(N):
        y = x & ((1 << n) - 1); z = (x >> n) & 1
        maj = bin(y).count("1") * 2 > n
        val = maj or (z == 1 and y == ystar)
        tt[x] = -1 if val else 1
    return tt


def is_monotone(tt, n):
    for x in range(1 << n):
        for i in range(n):
            if not (x >> i) & 1:
                y = x | (1 << i)
                # true = -1 ; monotone increasing in 'true'
                if tt[x] == -1 and tt[y] == 1:
                    return False
    return True


rows = []
for m2 in range(1, 7):
    rows.append(report(f"bent_plus_flip m={2*m2}", bent_plus_flip(m2), 2 * m2 + 1))
for n in (3, 5, 7, 9, 11, 13, 15, 17):
    t = maj_plus_maxfalse_flip(n)
    if n <= 9:
        assert is_monotone(t, n + 1)
    rows.append(report(f"maj{n}+maxfalse_flip (monotone)", t, n + 1))
for n in (3, 5, 7, 9, 11, 13, 15, 17, 19):
    rows.append(report(f"maj{n}", majority(n), n))
for n in (2, 4, 6, 8, 10, 12, 14, 16):
    rows.append(report(f"one_point{n}", one_point(n), n))
for (w, s) in ((2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 2), (4, 3), (4, 4), (5, 3)):
    rows.append(report(f"tribes w{w} s{s}", tribes(w, s), w * s))
rows.append(report("recmaj3 depth2", rec_maj3(2), 9))
for k in (1, 2, 3, 4):
    rows.append(report(f"addressing k{k}", addressing(k), k + (1 << k)))
g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
rows.append(report("numaro18", g, 18))
json.dump(rows, open(os.path.join(HERE, "..", "logs", "families.json"), "w"), indent=1)
