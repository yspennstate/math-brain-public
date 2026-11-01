#!/usr/bin/env python3
"""Reproduce the two-panel scaling figure and its numerical source data.

Run from any directory with Python, NumPy, SciPy, and Matplotlib installed.
The default outputs are results/scaling_data.json and paper/scaling_limits.pdf
relative to this script's project directory.

All eigenvalues below are floating-point finite-matrix computations.  The
separately recorded truncation widths are evaluations of exact analytic
formulas; they do not certify rounding errors of the finite eigenvalues.
"""

from __future__ import annotations

import json
import math
import platform
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, LogFormatterMathtext, NullFormatter
import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal


PROJECT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT / "results" / "scaling_data.json"
FIGURE_PATH = PROJECT / "paper" / "scaling_limits.pdf"


def lowest_eigenvalue(diagonal: np.ndarray, off_diagonal: np.ndarray) -> float:
    """Smallest eigenvalue of a real symmetric Jacobi matrix, numerically."""
    if diagonal.size == 1:
        return float(diagonal[0])
    return float(
        eigh_tridiagonal(
            diagonal,
            off_diagonal,
            eigvals_only=True,
            select="i",
            select_range=(0, 0),
            lapack_driver="stebz",
            tol=1e-13,
            check_finite=False,
        )[0]
    )


def finite_count_gap(n: int, beta: float) -> float:
    """Bottom of the count derivative on k=1,...,n-1.

    Its births are beta*(n-k-1), deaths k*(k-1)/n, and killing
    beta+2*k/n.  Symmetrization uses adjacent birth/death products.
    """
    k = np.arange(1, n, dtype=np.float64)
    diagonal = beta * (n - k) + k * (k + 1.0) / n
    off_diagonal = -np.sqrt(
        beta * (n - k[:-1] - 1.0) * k[:-1] * (k[:-1] + 1.0) / n
    )
    return lowest_eigenvalue(diagonal, off_diagonal)


def sharp_count_bracket(n: int, beta: float) -> tuple[float, float]:
    """Evaluate the exact positive-vector endpoint bracket in the paper."""
    a = (
        beta * n
        + 1.0
        + math.sqrt((beta * n + 1.0) ** 2 + 4.0 * beta * n * (n + 1.0))
    ) / 2.0
    c = 2.0 * a / n - beta
    lower = c - 6.0 * (a - 1.0) / (n * (a + 3.0))
    upper = c - 6.0 * a * (a - 1.0) / (
        n * (n + a - 2.0) * (n + a + 1.0)
    )
    return lower, upper


def rho_truncation(b: float, r: int) -> float:
    """Reflecting truncation of H_b on k=1,...,r."""
    k = np.arange(1, r + 1, dtype=np.float64)
    diagonal = k * (k + 1.0) + b
    diagonal[-1] -= b  # suppress the last birth, retaining killing 2*k
    off_diagonal = -np.sqrt(b * k[:-1] * (k[:-1] + 1.0))
    return lowest_eigenvalue(diagonal, off_diagonal)


def sigma_truncation(b: float, r: int) -> float:
    """Reflecting truncation of H_b^(1) on j=0,...,r."""
    j = np.arange(0, r + 1, dtype=np.float64)
    diagonal = j * (j + 1.0) + b
    diagonal[-1] -= b  # suppress the last birth, retaining killing j
    off_diagonal = -math.sqrt(b) * (j[:-1] + 1.0)
    return lowest_eigenvalue(diagonal, off_diagonal)


def make_data() -> dict:
    n_values = sorted(
        set(int(round(x)) for x in np.geomspace(8, 32768, 31))
        | {8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768}
    )
    finite = []
    for n in n_values:
        beta = 1.0 / n
        gap = finite_count_gap(n, beta)
        lower, upper = sharp_count_bracket(n, beta)
        finite.append(
            {
                "n": n,
                "beta": beta,
                "gamma_Q_numerical": gap,
                "sqrt_n_times_gap": math.sqrt(n) * gap,
                "sharp_lower_bound_evaluated_float": lower,
                "sharp_upper_bound_evaluated_float": upper,
                "leading_value": 2.0,
            }
        )

    critical = []
    for b_value in np.geomspace(1e-3, 1e4, 121):
        b = float(b_value)
        r = int(math.ceil(600.0 * (1.0 + math.sqrt(b))))
        rho = rho_truncation(b, r)
        sigma = sigma_truncation(b, r)
        if min(rho, sigma) <= 0 or not math.isfinite(rho + sigma):
            raise ArithmeticError(f"Unexpected numerical ground eigenvalue at b={b}")
        critical.append(
            {
                "b": b,
                "R": r,
                "rho_R_numerical": rho,
                "rho_analytic_truncation_width_evaluated_float": 2.0 * b / (r + 3.0),
                "sigma_R_numerical": sigma,
                "sigma_analytic_truncation_width_evaluated_float": b / (r + 2.0),
                "rho_large_b_asymptote": 2.0 * math.sqrt(b),
                "sigma_large_b_asymptote": math.sqrt(b),
            }
        )

    return {
        "schema_version": 1,
        "generator": "code/plot_scaling.py",
        "numerical_method": {
            "solver": "scipy.linalg.eigh_tridiagonal",
            "lapack_driver": "stebz",
            "select": "smallest eigenvalue only",
            "absolute_tolerance_requested": 1e-13,
            "eigenvalue_arithmetic": "IEEE 754 floating point; not interval certified",
            "R_rule": "ceil(600*(1+sqrt(b)))",
            "rho_states": "1,...,R; birth at R suppressed; killing 2*k retained",
            "sigma_states": "0,...,R; birth at R suppressed; killing j retained",
            "rho_truncation_theorem": "rho_R <= rho <= rho_R + 2*b/(R+3)",
            "sigma_truncation_theorem": "sigma_R <= sigma <= sigma_R + b/(R+2)",
            "qualification": (
                "The truncation theorems concern exact finite eigenvalues. "
                "The stored finite eigenvalues and evaluated widths are floating-point values."
            ),
        },
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "finite_count": finite,
        "critical_limits": critical,
    }


def make_figure(data: dict) -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Serif",
            "font.size": 9.0,
            "mathtext.fontset": "stix",
            "axes.titlesize": 9.0,
            "axes.labelsize": 9.0,
            "xtick.labelsize": 8.0,
            "ytick.labelsize": 8.0,
            "legend.fontsize": 7.7,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.65,
            "xtick.major.width": 0.65,
            "ytick.major.width": 0.65,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.facecolor": "white",
        }
    )
    blue = "#235789"
    orange = "#C05A16"
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(7.05, 2.95))
    fig.subplots_adjust(left=0.083, right=0.987, bottom=0.195, top=0.865, wspace=0.36)

    finite = data["finite_count"]
    ns = np.asarray([row["n"] for row in finite])
    gaps = np.asarray([row["sqrt_n_times_gap"] for row in finite])
    ax0.plot(
        ns,
        gaps,
        color=blue,
        linewidth=1.45,
        marker="o",
        markersize=3.0,
        markerfacecolor="white",
        markeredgewidth=0.8,
        label=r"$\sqrt{n}\,\gamma_M(n,1/n)$",
    )
    ax0.axhline(2.0, color="#555555", linewidth=1.0, linestyle=(0, (4, 3)), label="Limit 2")
    ax0.set_xscale("log", base=2)
    ax0.set_xlim(7, 42000)
    ax0.set_ylim(1.863, 2.011)
    ax0.set_xticks([8, 128, 2048, 32768], [r"$2^3$", r"$2^7$", r"$2^{11}$", r"$2^{15}$"])
    ax0.xaxis.set_minor_locator(FixedLocator([]))
    ax0.set_yticks([1.88, 1.92, 1.96, 2.00])
    ax0.set_xlabel(r"System size $n$")
    ax0.set_ylabel("Scaled spectral gap")
    ax0.set_title("(a) Finite-system leading constant", loc="left", pad=8)
    ax0.grid(axis="y", color="#D7DCE2", linewidth=0.5, alpha=0.8)
    ax0.legend(loc="lower right", frameon=False, handlelength=2.5, borderaxespad=0.5)

    critical = data["critical_limits"]
    bs = np.asarray([row["b"] for row in critical])
    rho = np.asarray([row["rho_R_numerical"] for row in critical])
    sigma = np.asarray([row["sigma_R_numerical"] for row in critical])
    rho_width = np.asarray([row["rho_analytic_truncation_width_evaluated_float"] for row in critical])
    sigma_width = np.asarray([row["sigma_analytic_truncation_width_evaluated_float"] for row in critical])
    # These very thin bands visualize analytic tail widths around numerical
    # finite eigenvalues.  They are not rounding-error-certified intervals.
    ax1.fill_between(bs, rho, rho + rho_width, color=blue, alpha=0.14, linewidth=0)
    ax1.fill_between(bs, sigma, sigma + sigma_width, color=orange, alpha=0.14, linewidth=0)
    ax1.plot(bs, rho, color=blue, linewidth=1.7, label=r"$\rho(b)$")
    ax1.plot(bs, sigma, color=orange, linewidth=1.7, label=r"$\sigma(b)$")
    ax1.plot(bs, 2.0 * np.sqrt(bs), color=blue, linewidth=0.85, linestyle=(0, (4, 3)), alpha=0.72,
             label=r"$2\sqrt{b}$")
    ax1.plot(bs, np.sqrt(bs), color=orange, linewidth=0.85, linestyle=(0, (4, 3)), alpha=0.72,
             label=r"$\sqrt{b}$")
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlim(7e-4, 1.4e4)
    ax1.set_ylim(3.4e-4, 3.1e2)
    ax1.set_xticks([1e-3, 1e-1, 1e1, 1e3])
    ax1.xaxis.set_major_formatter(LogFormatterMathtext(base=10))
    ax1.xaxis.set_minor_locator(FixedLocator([]))
    ax1.yaxis.set_minor_formatter(NullFormatter())
    ax1.set_xlabel(r"Critical parameter $b=n^2\beta$")
    ax1.set_ylabel("Limiting scaled rate")
    ax1.set_title("(b) Count and spatial critical modes", loc="left", pad=8)
    ax1.grid(which="major", axis="y", color="#D7DCE2", linewidth=0.5, alpha=0.8)
    ax1.legend(loc="lower right", frameon=False, ncol=2, columnspacing=1.0,
               handlelength=2.4, borderaxespad=0.4)

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        FIGURE_PATH,
        format="pdf",
        metadata={
            "Title": "Finite-system and critical spectral scaling of linear polymers",
            "Subject": "Numerical finite radial eigenvalues with analytic truncation widths",
            "Creator": "plot_scaling.py / Matplotlib",
            "CreationDate": None,
            "ModDate": None,
        },
    )
    plt.close(fig)


def main() -> None:
    data = make_data()
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    make_figure(data)
    rows = data["critical_limits"]
    summary = {
        "figure": str(FIGURE_PATH),
        "data": str(DATA_PATH),
        "finite_points": len(data["finite_count"]),
        "critical_points": len(rows),
        "max_R": max(row["R"] for row in rows),
        "max_rho_width_over_finite_value": max(
            row["rho_analytic_truncation_width_evaluated_float"] / row["rho_R_numerical"] for row in rows
        ),
        "max_sigma_width_over_finite_value": max(
            row["sigma_analytic_truncation_width_evaluated_float"] / row["sigma_R_numerical"] for row in rows
        ),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
