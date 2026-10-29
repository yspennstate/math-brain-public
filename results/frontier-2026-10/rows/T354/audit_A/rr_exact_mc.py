# Validates rr_exact.py's reduction: D(x) at beta2 0.9 by direct RR simulation (frozen x) against the exact formula.
import sys, numpy as np, importlib.util
sys.argv = ["rr_exact.py", "0.9", "300"]
src = open("rr_exact.py", encoding="utf-8").read().split("x0 = None")[0]
ns = {}; exec(src, ns); D = ns["D"]
rng = np.random.default_rng(354); b2 = 0.9; n = 10; B = np.array([9.0] + [-1.0] * 9)
for x in (0.05, 0.2):
    g = x + B; v = np.mean(g * g); acc = []; E = 400000
    for blk in range(8):
        tot = 0.0
        perms = rng.permuted(np.tile(np.arange(n), (E // 8, 1)), axis=1)
        for row in perms:
            for i in row:
                v = b2 * v + (1 - b2) * g[i] ** 2; tot += g[i] / np.sqrt(v)
        acc.append(tot / (E // 8 * n))
    acc = np.array(acc)
    print("x %.2f: exact D %.6f | sim %.6f +/- %.6f" % (x, D(x), acc.mean(), acc.std(ddof=1) / np.sqrt(len(acc))), flush=True)
