"""Draw the two figures of the paper (imports the density code from free_unimodality.py).
The pair-threshold sweep takes about ten minutes; pass --cached to reuse the values printed by the last run."""
import os, sys, math, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from free_unimodality import biane_density, tstar_density
HERE = os.path.dirname(os.path.abspath(__file__)); FIG = os.path.normpath(os.path.join(HERE, "..", "figures"))
os.makedirs(FIG, exist_ok=True)

fig, ax = plt.subplots(1, 3, figsize=(11, 3.3))
for k, t in enumerate([2.0, 4.0, 6.0]):
    u = np.linspace(-1 - 3 * math.sqrt(t), 1 + 3 * math.sqrt(t), 6001)
    x, p = biane_density([-1.0, 1.0], [0.5, 0.5], t, u)
    ax[k].plot(x, p, lw=1.4); ax[k].set_title(f"$t = {t:g}$"); ax[k].set_xlabel("$x$")
    ax[k].set_ylim(0, 1.08 * p.max())
ax[0].set_ylabel("density")
fig.suptitle("symmetric two-point law on {-1, 1} under free Brownian motion: two modes for t < 4, one mode from t = 4")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "bernoulli_densities.pdf")); fig.savefig(os.path.join(FIG, "bernoulli_densities.png"), dpi=150)

ws = np.linspace(0.05, 0.5, 19)
if "--cached" in sys.argv:
    ts = [0.5405, 0.5184, 0.5068, 0.5013, 0.5000, 0.5020, 0.5068, 0.5142, 0.5240, 0.5365, 0.5518, 0.5704, 0.5927,
          0.6198, 0.6531, 0.6948, 0.7494, 0.8271, 1.0000]   # values from the run of 2026-09-14 (results.md)
else:
    ts = [tstar_density([-0.5, 0.5], [w, 1 - w]) for w in ws]
fig, ax = plt.subplots(figsize=(4.8, 3.3))
ax.plot(ws, ts, "o-", ms=3); ax.axhline(1.0, ls="--", lw=0.8, color="k")
ax.set_xlabel("weight $w$ of the atom at $-1/2$"); ax.set_ylabel("$t^*(\\mu)$")
ax.set_title("two atoms at $\\pm 1/2$: threshold against the bound $1$")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "pair_threshold.pdf")); fig.savefig(os.path.join(FIG, "pair_threshold.png"), dpi=150)
print("figures written;", ", ".join(f"w={a:.2f}: {b:.4f}" for a, b in zip(ws, ts)))
