"""Make original SVG figures from numerical CSV data; no paper images."""
import os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
os.environ["MPLCONFIGDIR"] = str(ROOT / "data" / ".mplconfig")
os.environ["XDG_CACHE_HOME"] = str(ROOT / "data" / ".cache")
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import csv
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rows = list(csv.DictReader((ROOT / "data" / "summary.csv").open()))
groups = defaultdict(list)
for row in rows:
    groups[float(row["L"]), int(row["resolution"])].append(row)
plt.rcParams.update({"font.size": 10, "svg.fonttype": "none"})
colours = ["#2171b5", "#e6550d", "#238b45", "#88419d", "#a63603"]
fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for ((L, resolution), values), colour in zip(sorted(groups.items()), colours):
    values.sort(key=lambda row: float(row["alpha_grid"]))
    x = np.array([float(v["alpha_grid"]) for v in values])
    for ax, phase in zip(axes, ("claimed", "vacant")):
        y4 = np.array([float(v[f"{phase}4_wrap_rate"]) for v in values])
        y8 = np.array([float(v[f"{phase}8_wrap_rate"]) for v in values])
        ax.fill_between(x, y4, y8, color=colour, alpha=.12)
        ax.plot(x, y4, "o-", color=colour, ms=4, label=f"L={L:g}, h=1/{resolution}")
        ax.plot(x, y8, ":", color=colour, alpha=.8)
        ax.set_title(f"{phase.capitalize()} phase")
        ax.set_xlabel("Realised grid appetite per centre")
        ax.set_xlim(.5, .85)
        ax.set_ylim(-.03, 1.03)
        ax.axhline(.5, color=".7", lw=.7)
        ax.grid(alpha=.2)
axes[0].set_ylabel("Fraction of tori with a winding component")
axes[1].legend(fontsize=8, loc="lower left")
fig.suptitle("Stable allocation on Poisson tori: finite-grid evidence")
fig.text(.5, .015, "Solid: 4-neighbour; dotted: 8-neighbour. Shading is connectivity sensitivity, not a confidence interval.", ha="center", fontsize=8)
fig.tight_layout(rect=[0, .05, 1, .94])
fig.savefig(ROOT / "data" / "torus_winding.svg")
fig.savefig(ROOT / "data" / "torus_winding.png", dpi=150)
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for ((L, resolution), values), colour in zip(sorted(groups.items()), colours):
    values.sort(key=lambda row: float(row["alpha_grid"]))
    x = [float(v["alpha_grid"]) for v in values]
    for ax, phase in zip(axes, ("claimed", "vacant")):
        y = [float(v[f"{phase}4_largest_fraction_torus_mean"]) for v in values]
        ax.plot(x, y, "o-", color=colour, ms=4, label=f"L={L:g}, h=1/{resolution}")
        ax.set_title(f"{phase.capitalize()} phase")
        ax.set_xlabel("Realised grid appetite per centre")
        ax.set_xlim(.2, .96)
        ax.set_ylim(-.03, 1.03)
        ax.grid(alpha=.2)
axes[0].set_ylabel("Mean largest component / torus area")
axes[1].legend(fontsize=8)
fig.suptitle("Largest components with periodic 4-neighbour connectivity")
fig.tight_layout(rect=[0, 0, 1, .94])
fig.savefig(ROOT / "data" / "torus_largest_components.svg")
plt.close(fig)
