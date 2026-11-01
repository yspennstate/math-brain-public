"""Candidate sum-type inequalities, each of which would imply FEI through the erasure reduction.

  L(f)   = sum_S p_S sum_{i in S} log2(1 + p_{S-i}/p_S)            (L <= B <= L + I/ln2)
  A(f)   = sum_S |S| p_S log2( mean_{i in S} p_{S-i} / p_S )_+       (A >= L - I by Jensen)
  Wt(f)  = sum_i Inf_i B_i / sum_i Inf_i^2                           (influence-weighted selector)
and the q-profile split of B: up-heavy edges (p_T < p_{T+i}), down-heavy edges with q >= eps, and
sprinkled down-heavy edges (0 < q < eps), q = min/(sum) on the edge.  Reported as ratios to I.
Exhaustive over n = 4 and over hard families."""
import sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *

set_polite()
EPS = 2.0 ** -6


def quantities(tt, n):
    tt = np.atleast_2d(np.asarray(tt, dtype=np.float64))
    fh, p = spectra(tt)
    N = 1 << n
    pc = popcounts(N)
    I = total_influence(p, n)
    L = np.zeros(len(tt)); A = np.zeros(len(tt))
    meanratio_num = np.zeros_like(p)
    Bup = np.zeros(len(tt)); Bdn = np.zeros(len(tt)); Bsp = np.zeros(len(tt))
    Binf = []; Infs = []
    S = np.arange(N)
    for i in range(n):
        low = S[((S >> i) & 1) == 0]; up = low | (1 << i)
        pl, pu = p[:, low], p[:, up]
        m = pl + pu
        with np.errstate(divide="ignore", invalid="ignore"):
            q = np.where(m > 0, np.minimum(pl, pu) / np.where(m > 0, m, 1), 0.0)
            Lt = np.where(pu > 0, pu * np.log2(1 + pl / np.where(pu > 0, pu, 1)), 0.0)
        L += Lt.sum(axis=1)
        meanratio_num[:, up] += pl
        e = phi(pl) + phi(pu) - phi(m)
        upheavy = pu > pl
        spr = (~upheavy) & (q > 0) & (q < EPS)
        Bup += np.where(upheavy, e, 0).sum(axis=1)
        Bsp += np.where(spr, e, 0).sum(axis=1)
        Bdn += np.where((~upheavy) & ~spr, e, 0).sum(axis=1)
        Binf.append(e.sum(axis=1)); Infs.append(pu.sum(axis=1))
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where((p > 0) & (pc[None, :] > 0), meanratio_num / np.where(pc[None, :] > 0, pc[None, :], 1) / np.where(p > 0, p, 1), 1.0)
        A = (pc[None, :] * p * np.maximum(np.log2(np.where(ratio > 0, ratio, 1)), 0)).sum(axis=1)
    Binf = np.stack(Binf, 1); Infs = np.stack(Infs, 1)
    Wt = (Infs * Binf).sum(1) / np.maximum((Infs ** 2).sum(1), 1e-300)
    B = Binf.sum(1)
    return dict(I=I, B=B, L=L, A=A, Wt=Wt, Bup=Bup, Bdn=Bdn, Bsp=Bsp)


out = {}
# exhaustive n = 4
n = 4; N = 16
codes = np.arange(1 << N, dtype=np.int64)
tt = (1 - 2 * ((codes[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.float64)
Q = quantities(tt, n)
nc = Q["I"] > 1e-12
row = {k: float((Q[k][nc] / Q["I"][nc]).max()) for k in ("B", "L", "A", "Bup", "Bdn", "Bsp")}
row["Wt"] = float(Q["Wt"][nc].max())
out["exhaustive n=4 (max of ratio to I)"] = row
print("n=4 exhaustive:", json.dumps(row))

from families_lib import family_list  # noqa
for name, t, nn in family_list():
    Qf = quantities(t, nn)
    r = {k: float(Qf[k][0] / Qf["I"][0]) for k in ("B", "L", "A", "Bup", "Bdn", "Bsp")}
    r["Wt"] = float(Qf["Wt"][0])
    out[name] = r
    print(f"{name:34s} " + " ".join(f"{k}={v:.3f}" for k, v in r.items()))
    sys.stdout.flush()
json.dump(out, open(os.path.join(HERE, "..", "logs", "candidates.json"), "w"), indent=1)
