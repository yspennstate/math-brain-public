"""Scan s_10 and H next to the uniform star K_{1,n-1}: leaf weights 1/(n-1) + (d, 0, -d, 0, ...) and a few other shapes."""
import sys
N = int(sys.argv[1])
sys.argv = ["t104_gpu_hsearch.py", str(N), "1", "1", "1", "1", "--cpu"]
import numpy as np
import torch
import t104_gpu_hsearch as T

k = N - 1
shapes = {
    "d,0,-d": lambda d: [d, 0, -d] + [0] * (k - 3),
    "d,-d":   lambda d: [d, -d] + [0] * (k - 2),
    "d,d,-2d": lambda d: [d, d, -2 * d] + [0] * (k - 3),
    "spread": lambda d: list(np.linspace(-d, d, k)),
}
for name, f in shapes.items():
    best = (1.0, None)
    for d in 10 ** np.linspace(-6, -1.5, 46):
        w = np.zeros(len(T.pairs))
        for j in range(1, N):
            w[T.pairs.index((0, j))] = 1.0 / k + f(d)[j - 1]
        w = w / w.sum()
        wt = torch.tensor(w[None, :] + 1e-300, dtype=T.dt, device=T.dev)
        v10, sl, _ = T.values(wt, [10.0])
        vh, _, _ = T.values(wt, T.GRID)
        if float(v10[0]) < best[0]:
            best = (float(v10[0]), d, float(sl[0]), float(vh[0]))
    print("n %d shape %-8s min s_10 %+.4e at d %.2e (slack %.3e, H there %+.4e)" % ((N, name) + best), flush=True)
