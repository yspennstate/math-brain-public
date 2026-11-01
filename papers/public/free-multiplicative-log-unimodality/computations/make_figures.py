"""Figures 1 and 2 of the paper, drawn from the curves written by lscan.py and thmB_density.py.

fig_loguniform.pdf: the density g_L of log_*(mu_L boxtimes mu_L) for L = 3, 4, 6, 8 (lscan_curves.json).
fig_twoatoms.pdf:   the density of log_*(sigma_t boxtimes nu), nu = (delta_{1/10} + delta_{10})/2, for t = 2, 10, 30
                    (thmB_curves.json).
Usage: python make_figures.py   (writes both PDFs into ../paper)
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "paper")
plt.rcParams.update({"pdf.fonttype": 42, "font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def draw(curves, keys, label, fname, xlabel):
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for k, style in zip(keys, ["-", "--", "-.", ":"]):
        c = curves[k]
        ax.plot(c["y"], c["g"], style, lw=1.4, label=label % k)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("density")
    ax.set_ylim(bottom=0)
    ax.legend(frameon=False)
    fig.tight_layout()
    path = os.path.join(OUT, fname)
    fig.savefig(path)
    plt.close(fig)
    print("wrote", os.path.normpath(path))


draw(load("lscan_curves.json"), ["3", "4", "6", "8"], "$L=%s$", "fig_loguniform.pdf", "$y=\\log x$")
draw(load("thmB_curves.json"), ["2", "10", "30"], "$t=%s$", "fig_twoatoms.pdf", "$y=\\log x$")
