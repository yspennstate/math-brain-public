"""Width-2 monotone DNF with a bad pendant variable (FLOW 12(v)).

Graph: a clique on y_0..y_k and a pendant vertex x attached to y_0.
f = [at least two of y_0..y_k are one] OR (x AND y_0)  =  "the set of ones is not independent".
D_x f = 1[y_0 = 1, all other y are 0]: Inf_x = 2^-(k+1), flat spectrum on all subsets of the y's.
Prediction (hand): the spectrum of f restricted to x = 0 at a set T of the y's is 2^-(k+1) (k + 2 - 2|T|), so
ghat^2 / hhat^2 ~ 4k on typical T and E_x / Inf_x ~ log2 k + const.

Prints Inf and E/Inf for x, for y_0 (the neighbour of x) and for one other clique vertex, then H/I.
Usage: python graph_pendant.py K [K ...]
"""
import sys
import numpy as np
from mono_hidden import wht, erasure


def build(k):
    m = k + 1                      # clique size
    n = m + 1                      # bit m is x
    idx = np.arange(1 << n)
    wt = np.zeros(idx.size, dtype=np.int64)
    for j in range(m):
        wt += (idx >> j) & 1
    x = (idx >> m) & 1
    y0 = idx & 1
    f = (wt >= 2) | ((x == 1) & (y0 == 1))
    return n, np.where(f, -1.0, 1.0)


def main():
    for k in [int(a) for a in sys.argv[1:]]:
        n, f = build(k)
        mu = wht(f) ** 2
        res = erasure(mu, n)
        tot_i = sum(r[0] for r in res)
        nz = mu[mu > 0]
        ent = float(-(nz * np.log2(nz)).sum())
        m = k + 1
        (ix, ex), (i0, e0), (i1, e1) = res[m], res[0], res[1]
        print(f"k={k:2d} n={n:2d}  x: Inf={ix:.3e} E/Inf={ex/ix:.4f}   y0: Inf={i0:.3e} E/Inf={e0/i0:.4f}   "
              f"y1: Inf={i1:.3e} E/Inf={e1/i1:.4f}   H/I={ent/tot_i:.4f}  log2k={np.log2(k):.3f}", flush=True)


if __name__ == "__main__":
    main()
