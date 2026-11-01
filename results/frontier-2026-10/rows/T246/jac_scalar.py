"""T246 (agent A, 17 Oct 2026): the two-component scalar chain. Per layer draw z_i, g_i iid N(0,1), i <= n;
h_i = sqrt(qhat) z_i; qhat <- mean tanh(h)^2; log|v|^2 += log mean(sech(h)^4 g^2). No matrices: this keeps the forward-norm
walk and the per-layer coupling through the shared h, and drops everything else. argv: n L_list B seed"""
import sys, numpy as np, psutil
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
n = int(sys.argv[1]); Ls = [int(v) for v in sys.argv[2].split(',')]; B = int(sys.argv[3]); rng = np.random.default_rng(int(sys.argv[4]))
print(__doc__.strip(), flush=True)
for L in Ls:
    q = np.ones(B); lv = np.zeros(B)
    for l in range(L):
        h = np.sqrt(q)[:, None] * rng.standard_normal((B, n)); g = rng.standard_normal((B, n))
        lv += np.log(np.mean(np.cosh(h) ** -4 * g * g, 1)); q = np.mean(np.tanh(h) ** 2, 1)
    v = lv.var(ddof=1)
    print(f"scalar n={n} L={L:4d} t={L/n:.3f} | mean {lv.mean():.4f} | n Var {n*v:8.1f} (+- {n*v*np.sqrt(2/(B-1)):.1f}) n Var/L {n*v/L:.3f} | B={B}", flush=True)
