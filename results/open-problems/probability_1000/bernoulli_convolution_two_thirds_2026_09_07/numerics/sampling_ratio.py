# Direct diagnostic of the Nyquist sampling step: compare the octave SUM with the integral prediction.
#   E(R) = sum_{R<=k<2R} |hat_mu(k)|^2      vs      (1/h) * int over the seed interval, h the seed spacing.
# For k in [R,2R) the seed is x_k = k (2/3)^K / 3 with K = floor(log_{3/2}(k/3)); K is NOT constant across an
# octave (it steps once or twice), so do it per K-block: for each K the k with x_k in [1,3/2) are an AP of
# length L_K = (1/2)*3*(3/2)^K, spacing h_K = (2/3)^K/3.  Compare sum over that block to (1/h_K) I_K.
import numpy as np, math
def P2(x, K):
    out = np.ones_like(x)
    for j in range(K+1):
        out *= np.cos(np.pi*(1.5**j)*x)**2
    return out
print(" K |   k-range for seeds in [1,3/2)   |  block sum  | (1/h) I_K  | ratio sum/integral")
for K in range(4, 21):
    h = (2.0/3.0)**K/3.0
    klo = math.ceil(1.0/h); khi = math.ceil(1.5/h)          # x_k = k h in [1, 1.5)
    n = khi - klo
    if n > 6_000_000: 
        print(f"{K:2d} | block too large ({n}) - stopping"); break
    kk = np.arange(klo, khi, dtype=np.float64)
    x = kk*h
    s = float(P2(x, K).sum())
    # integral at 40 points per oscillation of the top frequency
    N = int(min(3e7, max(1 << 14, 40*(1.5**K))))
    xg = np.linspace(1.0, 1.5, N, endpoint=False) + 0.25/N
    I = float(P2(xg, K).mean()*0.5)
    pred = I/h
    print(f"{K:2d} | [{klo:>9d},{khi:>10d}) n={n:>9d} | {s:.4e} | {pred:.4e} | {s/pred:.4f}", flush=True)
