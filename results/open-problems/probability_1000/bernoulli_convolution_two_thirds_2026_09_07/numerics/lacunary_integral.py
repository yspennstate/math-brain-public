# |hat_mu(xi)| = prod_{j=0}^{K} |cos(pi (3/2)^j x)| with x = xi (2/3)^K / 3 in [1, 3/2), K ~ log(xi)/log(3/2).
# For an octave the seeds x_k form an arithmetic progression of ~R points in [1,3/2), so heuristically
#     E(R) ~ (1/h) * I_K,     I_K = int_1^{3/2} prod_{j=0}^{K} cos^2(pi (3/2)^j x) dx,   h = spacing ~ 1/(2R).
# Need E(R) <= C R^{-delta}: with R ~ (3/2)^K this asks  I_K <= C q^K with q < 2/3.
# Independence of lacunary cosines would give I_K ~ (1/2)^K, i.e. q = 1/2 < 2/3 with room.  MEASURE q.
import numpy as np, math, sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 26
print(" K |      I_K      | ratio I_K/I_{K-1} | (I_K)^(1/K) | needed q < 2/3 = 0.6667")
prev = None
for K in range(1, KMAX+1):
    # integrate on a grid fine enough for the top frequency (3/2)^K: use 40 points per oscillation
    N = int(min(4e7, max(1 << 14, 40*(1.5**K))))
    x = np.linspace(1.0, 1.5, N, endpoint=False) + 0.25/N
    P = np.ones(N)
    for j in range(K+1):
        P *= np.cos(np.pi*(1.5**j)*x)**2
    I = float(P.mean()*0.5)
    r = (I/prev) if prev else float('nan')
    prev = I
    print(f"{K:2d} | {I:.6e} | {r:.4f} | {I**(1.0/K):.4f} | {'OK' if r < 2/3 else 'TOO SLOW'}", flush=True)
