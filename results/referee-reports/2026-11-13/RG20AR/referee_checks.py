"""Independent, bounded numerical checks for PAPER.tex; no author code used.

Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 10 python3 referee_checks.py
All output files stay beside this script. No subprocesses or network access.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
import hashlib
import itertools
import json
import math
import resource
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.special import beta as beta_function, betainc, gamma

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
DEADLINE = START + 240
P = 1.5
CP = 2 ** (P / 2) * gamma((P + 1) / 2) / math.sqrt(math.pi)
SEED = 20261114
ROWS = []


def emit(s):
    print(s, flush=True)
    ROWS.append(s)


def time_check():
    if time.monotonic() > DEADLINE:
        raise RuntimeError("240-second computation budget exhausted")


def exact_coupling_check():
    def h(t):
        return t * (1 - t)
    def a(t):
        return -(t - F(1, 2)) ** 2 if t < F(1, 2) else F(0)
    def b(t):
        return (t - F(1, 2)) ** 2 if t > F(1, 2) else F(0)
    grid = [F(k, 8) for k in range(1, 8)]
    cases = 0
    for n in range(1, 7):
        for sample in itertools.combinations_with_replacement(grid, n):
            # Reverse the input to require genuine sorting, with repeated values.
            raw = sample[::-1]
            av = sorted(map(a, raw))
            bv = sorted(map(b, raw))
            assert av == list(map(a, sample))
            assert bv == list(map(b, sample))
            for u, aa, bb in zip(sample, av, bv):
                for t in (F(1, 10), F(1, 2), F(9, 10)):
                    assert h(u) - h(t) == aa - a(t) - (bb - b(t))
            cases += 1
    emit(f"FRACTIONS: {cases} samples, n=1..6; tied ranks, flat a/b, signed linearity: PASS")


def atom_losses(x, theta):
    """Exact cell integrals for Q(t)=max(t-theta,0)/(1-theta)."""
    n = x.shape[1]
    lo = np.arange(n, dtype=float) / n
    hi = lo + 1 / n
    zero_length = np.maximum(0, np.minimum(hi, theta) - lo)
    yl = np.maximum(lo - theta, 0) / (1 - theta)
    yh = np.maximum(hi - theta, 0) / (1 - theta)
    # Integral of |x-y|^p dy has primitive sign(y-x)|y-x|^(p+1)/(p+1).
    dl, dh = yl[None, :] - x, yh[None, :] - x
    cell = zero_length[None, :] * x ** P
    cell += (1 - theta) / (P + 1) * (
        np.sign(dh) * np.abs(dh) ** (P + 1)
        - np.sign(dl) * np.abs(dl) ** (P + 1))
    return n ** (P / 2) * cell.sum(axis=1)


def pareto_losses(x, beta, order=24):
    """Cell quadrature including the whole endpoint, with no cutoff.

    s=1-t=v^12 removes the endpoint integrable power singularity.
    Every cell is split where s=x^(-1/beta), so |.|^p has no interior cusp.
    x is in increasing order (the empirical quantile cell values).
    """
    n = x.shape[1]
    nodes, weights = leggauss(order)
    lo = (np.arange(n - 1, -1, -1, dtype=float) / n) ** (1 / 12)
    hi = (np.arange(n, 0, -1, dtype=float) / n) ** (1 / 12)
    root = np.minimum(np.maximum(x ** (-1 / (12 * beta)), lo), hi)
    cell = np.zeros_like(x)
    # Accumulate one quadrature node at a time: O(batch*n) memory.
    for left, right in ((lo, root), (root, hi)):
        middle, half = (left + right) / 2, (right - left) / 2
        for z, w in zip(nodes, weights):
            v = middle + half * z
            cell += w * half * 12 * v ** 11 * np.abs(x - v ** (-12 * beta)) ** P
    return n ** (P / 2) * cell.sum(axis=1)


def integration_checks():
    global P
    rng = np.random.default_rng(SEED + 1)
    for beta in (1 / 6, 1 / 5):
        x = np.sort((1 - rng.random((3, 31))) ** (-beta), axis=1)
        z16 = pareto_losses(x, beta, 16)
        z24 = pareto_losses(x, beta, 24)
        z48 = pareto_losses(x, beta, 48)
        # Independent adaptive integration in v; include every cell endpoint.
        direct = []
        for row in x:
            total = 0.0
            n = len(row)
            for k, xx in enumerate(row):
                lo = ((n - k - 1) / n) ** (1 / 12)
                hi = ((n - k) / n) ** (1 / 12)
                cut = min(max(xx ** (-1 / (12 * beta)), lo), hi)
                def f(v):
                    return 12 * v ** 11 * abs(xx - v ** (-12 * beta)) ** P
                for l, r in ((lo, cut), (cut, hi)):
                    if l < r:
                        total += quad(f, l, r, epsabs=2e-12, epsrel=2e-10)[0]
            direct.append(n ** (P / 2) * total)
        direct = np.asarray(direct)
        rel16 = max(abs(z16 - direct) / np.maximum(abs(direct), 1e-12))
        rel24 = max(abs(z24 - direct) / np.maximum(abs(direct), 1e-12))
        rel48 = max(abs(z48 - direct) / np.maximum(abs(direct), 1e-12))
        emit(f"INTEGRATION beta={beta:.10f}: max relative error, 16 nodes={rel16:.3g}, 24 nodes={rel24:.3g}, 48 nodes={rel48:.3g}")
        assert rel24 < 2e-6 and rel48 < 1e-7
    # n=1 expectation for p=2 is independently 2 Var(X).
    original_p = P
    P = 2.0
    beta = 0.2
    x = np.array([[1.0], [2.0], [10.0]])
    numeric = pareto_losses(x, beta, 48)
    exact = x[:, 0] ** 2 - 2 * x[:, 0] / (1 - beta) + 1 / (1 - 2 * beta)
    emit(f"P2 PARETO n=1 analytic cell check: max abs error={max(abs(numeric-exact)):.3g}; E loss=2 Var(X)={2*(1/(1-2*beta)-1/(1-beta)**2):.12g}")
    assert np.allclose(numeric, exact, rtol=1e-10, atol=1e-10)
    P = original_p


def simulate():
    theta = 0.35
    jp_atom = (1 - theta) ** (-P) * beta_function(P / 2 + 1, P / 2 + 1) * (
        1 - betainc(P / 2 + 1, P / 2 + 1, theta))
    jp_quad = quad(lambda t: (t * (1 - t)) ** (P / 2) / (1 - theta) ** P,
                   theta, 1, epsabs=1e-12)[0]
    assert abs(jp_atom - jp_quad) < 1e-10
    emit(f"PARAMETERS p={P}, c_p={CP:.12g}, seed={SEED}, replicates=3000, batch=24")
    emit(f"ATOM theta={theta}: J_p={jp_atom:.12g} (beta function and adaptive integral agree); c_p J_p={CP*jp_atom:.12g}")
    emit("PARETO Q(t)=(1-t)^(-beta): J_p=beta^p * integral t^(p/2)(1-t)^(-p*beta-p/2)dt")
    emit("Critical beta=1/6: J_p=infinity (log divergence); beta=1/5: J_p=infinity (power exponent 1.05).")
    emit("Both Pareto laws have finite p-th moments. Their full BL bound and E||qB||_p^p are infinity.")
    emit("law,n,mean,Monte_Carlo_SE,BL_bound,bridge_mean,truncated_bridge_integral_to_1_minus_1_over_n")
    rng = np.random.default_rng(SEED)
    records = []
    reps, batch = 3000, 24
    for n in (32, 128, 512, 2048, 8192):
        samples = {"atom": [], "critical": [], "beyond": []}
        for begin in range(0, reps, batch):
            time_check()
            m = min(batch, reps - begin)
            u = np.sort(rng.random((m, n)), axis=1)
            x = np.maximum(u - theta, 0) / (1 - theta)
            samples["atom"].extend(atom_losses(x, theta))
            for name, beta in (("critical", 1 / 6), ("beyond", 1 / 5)):
                x = (1 - u) ** (-beta)
                samples[name].extend(pareto_losses(x, beta))
        for name, losses in samples.items():
            arr = np.array(losses)
            mean = float(arr.mean())
            se = float(arr.std(ddof=1) / math.sqrt(reps))
            bound = (5 * P) ** P * (n / (n + 2)) ** (P / 2) * jp_atom if name == "atom" else math.inf
            target = CP * jp_atom if name == "atom" else math.inf
            truncated = None
            if name != "atom":
                beta = 1 / 6 if name == "critical" else 1 / 5
                # y=-log(1-t) avoids quadrature of a near-endpoint singularity.
                truncated = CP * beta ** P * quad(
                    lambda y: (-math.expm1(-y)) ** (P / 2) * math.exp((P * beta + P / 2 - 1) * y),
                    0, math.log(n), epsabs=1e-12)[0]
            emit(f"{name},{n},{mean:.9g},{se:.4g},{bound:.9g},{target:.9g},{truncated if truncated is not None else '-'}")
            records.append({"law": name, "n": n, "mean": mean, "SE": se,
                            "BL_bound": bound if math.isfinite(bound) else "infinity",
                            "bridge_mean": target if math.isfinite(target) else "infinity",
                            "truncated_bridge_integral": truncated})
    return records


def main():
    emit("Independent referee numerical checks; finite simulations are not proofs.")
    emit("Input SHA256 PAPER.tex=" + hashlib.sha256((ROOT / "PAPER.tex").read_bytes()).hexdigest())
    emit(f"Python/numpy versions: numpy={np.__version__}")
    exact_coupling_check()
    integration_checks()
    records = simulate()
    elapsed = time.monotonic() - START
    # ru_maxrss is bytes on macOS, kilobytes on Linux.
    import sys
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mb = peak / (1024 ** 2 if sys.platform == "darwin" else 1024)
    emit(f"RESOURCE elapsed={elapsed:.2f}s, process_peak_RSS={peak_mb:.2f} MiB; no workers spawned")
    (ROOT / "referee_checks_output.txt").write_text("\n".join(ROWS) + "\n")
    (ROOT / "referee_checks_output.json").write_text(json.dumps(records, indent=2) + "\n")


if __name__ == "__main__":
    main()
