import numpy as np, math
from verify_forms import wht, upsum, stats
def chk(name, F):
    s = stats(F); H, I, A, B = s['H'], s['I'], s['A'], s['B']
    fh = wht(F); var = 1 - fh[:, 0] ** 2
    nz = I > 1e-12
    g1 = (A - (B + 2 * I - 2 * var))[nz].max()
    g2 = (H - (2 * B + 2 * I - 2 * var))[nz].max()
    rB = (B[nz] / I[nz]); j = rB.argmax()
    rH = (H[nz] / I[nz])
    slack = ((2 * B + 2 * I - 2 * var) / np.maximum(H, 1e-300))[nz]
    print(f"{name}: max A-(B+2I-2Var)={g1:.3e}  max H-(2B+2I-2Var)={g2:.3e}  supB/I={rB[j]:.5f} (H/I there {rH[j]:.4f})  supH/I={rH.max():.5f}  min bound/H={slack.min():.4f}")
n = 4; N = 1 << n
tt = np.arange(1 << N, dtype=np.uint32)
F = 1 - 2 * ((tt[:, None] >> np.arange(N)[None, :]) & 1).astype(np.float64)
chk('all n=4', F)
rng = np.random.default_rng(7)
for n, M in ((5, 300000), (6, 60000), (7, 20000)):
    for p in (0.5, 0.2, 0.05):
        F = np.where(rng.random((M, 1 << n)) < p, -1.0, 1.0)
        chk(f'random n={n} p={p}', F)
