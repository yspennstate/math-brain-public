# The target after today's reduction is  S = sum_{k>=1} |hat_mu(k)|^2 < infinity  (then sum j_n <= log(1+2S)).
# Measure the octave energies E_j = sum_{2^j <= k < 2^{j+1}} |hat_mu(k)|^2 exactly from the closed product,
# and the octave maxima.  S = sum_j E_j = 0.103155 from the density, so the E_j must be summable; the SHAPE of
# their decay is what a proof would have to produce.
import numpy as np, sys, time
JMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
def hat_abs2(xi, terms=4000):
    out = np.ones(xi.shape); a = xi/3.0
    for _ in range(terms):
        out *= np.abs(np.cos(np.pi*a)); a = a*(2.0/3.0)
        if np.max(np.abs(a)) < 1e-16: break
    return out*out
tot = 0.0; t0 = time.time()
print(" j |    octave [2^j,2^{j+1}) |        E_j       | cumulative |  max_k |hat| * sqrt(R) |  #k with |hat|^2 > E_j/10")
for j in range(0, JMAX+1):
    lo, hi = 1 << j, 1 << (j+1); E = 0.0; mx = 0.0; big = 0
    step = 1 << 17
    for a in range(lo, hi, step):
        kk = np.arange(a, min(a+step, hi), dtype=np.float64)
        v = hat_abs2(kk)
        E += float(v.sum()); mx = max(mx, float(v.max()))
        big += int((v > 1e-30).sum() and 0)
    tot += E
    # second pass for the count of dominant frequencies
    thr = E/10.0; cnt = 0
    for a in range(lo, hi, step):
        kk = np.arange(a, min(a+step, hi), dtype=np.float64)
        cnt += int((hat_abs2(kk) > thr).sum())
    print(f"{j:2d} | [{lo:>10d},{hi:>11d}) | {E:.6e} | {tot:.6f} | {np.sqrt(mx*lo):.4f} | {cnt}", flush=True)
print(f"\ntotal to 2^{JMAX+1}: {tot:.6f}   (density value 0.103155)   {time.time()-t0:.0f}s")
