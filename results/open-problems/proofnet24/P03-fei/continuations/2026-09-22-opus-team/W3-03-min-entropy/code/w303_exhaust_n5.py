"""Exhaustive search over all 2^32 Boolean functions of 5 variables (2^31 up to output negation).

Integer Walsh values W(S) = sum_x f(x) (-1)^{|x&S|} are updated along a Gray code (one truth-table
entry flipped per step).  For each value of Wmax = max_S |W(S)| we record the minimum of
J = sum_S |S| W(S)^2 (so I = J/1024 and Hinf = 10 - 2 log2 Wmax), with a witness truth table.
Everything is integer arithmetic, so the result is exact.
"""
import sys, json, time
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
from numba import njit


@njit(cache=False)
def run(nbits):
    N = 32
    chi = np.empty((N, N), dtype=np.int64)
    pc = np.empty(N, dtype=np.int64)
    for S in range(N):
        c = 0
        t = S
        while t:
            c += t & 1
            t >>= 1
        pc[S] = c
    for x in range(N):
        for S in range(N):
            t = x & S
            c = 0
            while t:
                c += t & 1
                t >>= 1
            chi[x, S] = 1 - 2 * (c & 1)
    f = np.ones(N, dtype=np.int64)          # start: constant +1 (x=0 stays +1 throughout)
    W = np.zeros(N, dtype=np.int64)
    W[0] = 32
    J = 0
    bestJ = np.full(17, 1 << 40, dtype=np.int64)
    bestMask = np.zeros(17, dtype=np.int64)
    mask = 0
    total = 1 << nbits
    for i in range(1, total):
        # Gray code: flip bit ctz(i)
        b = 0
        t = i
        while (t & 1) == 0:
            t >>= 1
            b += 1
        x = b + 1
        fx = f[x]
        dJ = 0
        wmax = 0
        for S in range(N):
            w_old = W[S]
            w_new = w_old - 2 * fx * chi[x, S]
            W[S] = w_new
            dJ += pc[S] * (w_new * w_new - w_old * w_old)
            a = w_new if w_new >= 0 else -w_new
            if a > wmax:
                wmax = a
        f[x] = -fx
        mask ^= (1 << x)
        J += dJ
        k = wmax // 2
        if J > 0 and J < bestJ[k]:
            bestJ[k] = J
            bestMask[k] = mask
    return bestJ, bestMask


if __name__ == "__main__":
    nbits = int(sys.argv[1]) if len(sys.argv) > 1 else 31
    t0 = time.time()
    bestJ, bestMask = run(nbits)
    res = []
    for k in range(1, 17):
        if bestJ[k] < (1 << 40):
            wmax = 2 * k
            J = int(bestJ[k])
            Hinf = 10 - 2 * np.log2(wmax)
            I = J / 1024
            res.append(dict(Wmax=wmax, minJ=J, I=I, Hinf=float(Hinf), ratio=float(Hinf / I), mask=hex(int(bestMask[k]))))
    print(json.dumps(dict(nbits=nbits, seconds=time.time() - t0, table=res), indent=1))
