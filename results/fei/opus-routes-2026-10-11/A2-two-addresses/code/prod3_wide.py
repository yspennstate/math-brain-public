"""Enumerate all functions S on 3 bits with values in [-4,4] whose integer Walsh transform has FULL support
and a product magnitude pattern |W(U)| = c * prod_i (A_i if U_i=0 else B_i).  Saves them grouped by the
normalized magnitude pattern (the primitive integer vector of |W|).  Used to build full-support product
rows on 4 bits: V(x,x4) with V_lo = (S+D)/2, V_hi = (S-D)/2, S and D sharing a pattern."""
import numpy as np, sys, time, pickle, math
from math import gcd
from functools import reduce

def hadamard(m):
    Hm = np.array([[1]], dtype=np.int64)
    for _ in range(m):
        Hm = np.block([[Hm, Hm], [Hm, -Hm]])
    return Hm

def main(out):
    H3 = hadamard(3)
    vals = np.arange(-4, 5, dtype=np.int64)
    total = 9 ** 8
    chunk = 1 << 20
    keep = []
    t0 = time.time()
    for start in range(0, total, chunk):
        ids = np.arange(start, min(total, start + chunk), dtype=np.int64)
        S = np.empty((len(ids), 8), dtype=np.int64)
        t = ids.copy()
        for x in range(8):
            S[:, x] = vals[t % 9]
            t //= 9
        W = S @ H3.T
        A = np.abs(W)
        ok = np.all(A > 0, axis=1)
        # product magnitude: for each coordinate i, A[U|bit]*A[V] == A[U]*A[V|bit] for all U,V without bit
        for i in range(3):
            bit = 1 << i
            Us = [U for U in range(8) if not U & bit]
            for j in range(len(Us)):
                for k in range(j + 1, len(Us)):
                    u, v = Us[j], Us[k]
                    ok &= (A[:, u | bit] * A[:, v] == A[:, u] * A[:, v | bit])
        sel = S[ok]
        if len(sel):
            keep.append(sel)
    S_all = np.concatenate(keep) if keep else np.zeros((0, 8), dtype=np.int64)
    W_all = S_all @ H3.T
    print("full-support product-magnitude S on 3 bits, values in [-4,4]:", len(S_all), "time", round(time.time() - t0, 1), flush=True)
    groups = {}
    for s, w in zip(S_all, W_all):
        a = [int(abs(v)) for v in w]
        g = reduce(gcd, a)
        key = tuple(v // g for v in a)
        groups.setdefault(key, []).append((tuple(int(v) for v in s), g))
    print("patterns:", len(groups), flush=True)
    with open(out, "wb") as fh:
        pickle.dump(groups, fh)

if __name__ == "__main__":
    main(sys.argv[1])
