# Pooled local log-log slopes of the annealed MSD for I0001 over several exact runs (full grid or cropped window).
# Each dyadic window [a, 2a] uses every environment whose run reaches 2a; window rows whose edge_max exceeds 1e-9 are
# dropped. The MSD is sampled every 10 steps in every run, so curves are compared on the same time points.
# Bootstrap over environments. Evidence only, not a proof.
# usage: pooled_slopes.py run1.npz run2.npz ...
import sys
import numpy as np

curves = []  # (T, msd_t, msd rows)
for path in sys.argv[1:]:
    z = np.load(path)
    msd = z["msd"]
    keep = np.ones(msd.shape[0], bool)
    if "edge_max" in z.files:
        em = np.repeat(z["edge_max"], msd.shape[0] // len(z["edge_max"]))
        keep = em <= 1e-9
    curves.append((int(z["T"]), z["msd_t"], msd[keep]))
    print(f"{path}: T={int(z['T'])} envs={msd.shape[0]} kept={keep.sum()}")

Tmax = max(c[0] for c in curves)
rng = np.random.default_rng(7)
a = 125
print("window          envs   msd slope   boot sd")
while 2 * a <= Tmax:
    b = 2 * a
    tgrid = np.arange(10 * ((a + 9) // 10), b + 1, 10)
    rows = []
    for T, mt, msd in curves:
        if T >= b and len(msd):
            idx = np.searchsorted(mt, tgrid)
            rows.append(msd[:, idx])
    R = np.concatenate(rows)
    n = R.shape[0]
    s0 = np.polyfit(np.log(tgrid), np.log(R.mean(0)), 1)[0]
    bs = [np.polyfit(np.log(tgrid), np.log(R[rng.integers(0, n, n)].mean(0)), 1)[0] for _ in range(400)]
    print(f"[{a:5d},{b:5d}]  {n:5d}   {s0:.4f}      {np.std(bs):.4f}")
    a = b
