"""Exhaustive sweep over all Boolean functions of n variables (output negation halves it), BLAS transform.

  R = (H + Gamma(Pr f))/I     the sharpened FEI functional; conjecture max R = Gamma(1/2) = C0
  H/I                         the FEI ratio
usage: exhfast2.py <shard> <nshards> <npz> <n> [chunkbits]"""
import numpy as np, sys, time, json, os
import gam
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

if __name__ == "__main__":
    shard = int(sys.argv[1]); nsh = int(sys.argv[2]); npz = sys.argv[3]; n = int(sys.argv[4])
    cb = int(sys.argv[5]) if len(sys.argv) > 5 else 17
    N = 1 << n
    Gm = gam.Gam(npz, 0.0); C0 = Gm.cap
    sizes = np.array([bin(s).count("1") for s in range(N)], float)
    # Hadamard matrix Hmat[x, S] = chi_S(x)
    pop = np.array([bin(i).count("1") for i in range(N)], np.int64)
    Hmat = (1 - 2 * (pop[np.bitwise_and(np.arange(N)[:, None], np.arange(N)[None, :])] & 1)).astype(np.float64)
    bits = np.arange(N, dtype=np.uint64)
    TOTAL = 1 << (N - 1)
    CH = 1 << cb
    starts = list(range(0, TOTAL, CH))[shard::nsh]
    bestR = (-1e9, -1); bestHI = (-1e9, -1)
    t0 = time.time()
    for k, st in enumerate(starts):
        idx = np.arange(st, min(st + CH, TOTAL), dtype=np.uint64)[:, None]
        V = 1.0 - 2.0 * ((idx >> bits[None, :]) & np.uint64(1)).astype(np.float64)
        fh = (V @ Hmat) / N
        mu = fh * fh
        I = mu @ sizes
        with np.errstate(divide="ignore", invalid="ignore"):
            H = -np.where(mu > 1e-300, mu * np.log2(np.maximum(mu, 1e-300)), 0.0).sum(axis=1)
        pr = (1.0 - fh[:, 0]) * 0.5
        ok = I > 1e-9
        R = np.where(ok, (H + Gm(pr)) / np.maximum(I, 1e-300), -1e9)
        HI = np.where(ok, H / np.maximum(I, 1e-300), -1e9)
        j = int(np.argmax(R))
        if R[j] > bestR[0]: bestR = (float(R[j]), int(st + j))
        j = int(np.argmax(HI))
        if HI[j] > bestHI[0]: bestHI = (float(HI[j]), int(st + j))
        if (k + 1) % 100 == 0:
            el = time.time() - t0
            print("  shard %d: %d/%d chunks  %.0f s  (eta %.0f s)  maxR=%.9f  maxH/I=%.7f"
                  % (shard, k + 1, len(starts), el, el / (k + 1) * (len(starts) - k - 1), bestR[0], bestHI[0]), flush=True)
    print("SHARD %d DONE n=%d  C0=%.9f  maxR=%.9f (tt=%d)  maxH/I=%.7f (tt=%d)  margin C0-maxR=%+.3e  (%.0f s)"
          % (shard, n, C0, bestR[0], bestR[1], bestHI[0], bestHI[1], C0 - bestR[0], time.time() - t0), flush=True)
    json.dump({"R": list(bestR), "HI": list(bestHI), "C0": C0, "n": n}, open("exh2_n%d_shard%d.json" % (n, shard), "w"))
