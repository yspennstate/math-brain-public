# T354 check of remainder_iid.py, iid sampling, beta1 = 0 (agent B, 20 Oct 2026). For beta1 = 0 the frozen drift is
# D(x) = E_w sum_i (1/n) g_i(x) (beta2 w + d g_i(x)^2)^(-1/2), w ~ stationary v. Averaging the inner sum exactly over i for
# each sampled w removes the sampling noise of g; what remains is the (small) fluctuation in w. Argv: beta2 chains seed.
import sys, numpy as np
b2 = float(sys.argv[1]); d = 1 - b2; nch = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]))
B = np.array([9.0] + [-1.0] * 9); x0 = d * 72 / 18
xs = np.array([0.8, 1.0, 1.2]) * x0
burn, keep = int(25 / d), int(25 / d)
v = np.full((len(xs), nch), 9.0); acc = np.zeros(len(xs)); cnt = 0
for k in range(burn + keep):
    if k >= burn:
        g = xs[:, None, None] + B[None, None, :]                   # (x, 1, n)
        acc += (g / np.sqrt(b2 * v[:, :, None] + d * g * g)).mean(axis=2).sum(axis=1); cnt += nch
    idx = rng.integers(0, 10, size=nch)                              # same sample index for every x (common numbers)
    gk = xs[:, None] + B[idx][None, :]
    v = b2 * v + d * gk * gk
D = acc / cnt
sl = np.polyfit(xs, D, 1); xstar = -sl[1] / sl[0]
print("beta2 %s iid beta1 0: D at x0*(0.8,1,1.2) = %s; x*/x0 = %.5f (chains %d, %d kept steps)" % (sys.argv[1], np.array2string(D, precision=8), xstar / x0, nch, keep))
