"""Reproducible one-input heavy-tailed ReLU gradient-flow validation.

The clock ODE is integrated on intervals separated by exact gate-hit clocks.
Within each interval K(clock) is an exact hyperbolic expression; solve_ivp
integrates a scalar residual/clock equation and terminates at the next hit.
No Euler updates, approximate gate polling, or frozen-kernel substitution occur.

Model and normalizations: T384_scalar_dynamics.md and T384_joint_limit.md.
This script is numerical evidence, not a proof of a large-width theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import solve_ivp


def symmetric_stable(alpha: float, rng: np.random.Generator, size: int) -> np.ndarray:
    """CMS sampler for characteristic function exp(-|t|**alpha), skewness 0."""
    angle = rng.uniform(-math.pi / 2, math.pi / 2, size)
    if alpha == 1.0:
        return np.tan(angle)
    expo = rng.exponential(1.0, size)
    return (
        np.sin(alpha * angle)
        / np.cos(angle) ** (1.0 / alpha)
        * (np.cos((1.0 - alpha) * angle) / expo)
        ** ((1.0 - alpha) / alpha)
    )


@dataclass
class FlowResult:
    clock: np.ndarray
    residual: np.ndarray
    kernel: np.ndarray
    output_residual_discrepancy: np.ndarray
    event_count: int
    function_evaluations: int


def flow_one_input(
    U: np.ndarray,
    W: np.ndarray,
    alpha: float,
    y: float,
    observation_times: np.ndarray,
    rtol: float = 2e-10,
    atol: float = 2e-12,
) -> tuple[FlowResult, dict]:
    """Exact-gate scalar flow, with piecewise solve_ivp in physical time.

    On a fixed survivor set K(s)=a[q cosh(2s)+c sinh(2s)]. Its integral from
    segment start s_j over ξ=s-s_j is K_j*sinh(2ξ)/2+J_j*sinh(ξ)^2, where
    J_j=a[q sinh(2s_j)+c cosh(2s_j)]. Hence ξ'=β |r_j|-integral K,
    avoiding y-f(s) cancellation as the residual becomes small.
    """
    m = U.size
    norm_output = (m * math.log(m)) ** (-1.0 / alpha)
    norm_kernel = m ** (-2.0 / alpha)
    beta_clock = (math.log(m) / m) ** (1.0 / alpha)
    F0 = norm_output * np.sum(W * np.maximum(U, 0.0), dtype=np.float64)
    r0 = y - F0
    sigma = 1.0 if r0 >= 0.0 else -1.0
    active = U > 0.0
    V = sigma * W
    Q = norm_kernel * (
        np.sum(np.square(np.maximum(U, 0.0)), dtype=np.float64)
        + np.sum(np.square(W[active & (V > 0.0)]), dtype=np.float64)
    )
    K0 = norm_kernel * np.sum(U[active] ** 2 + W[active] ** 2, dtype=np.float64)
    meta = {"m": m, "F0": float(F0), "r0": float(r0), "Q": float(Q), "K0": float(K0)}

    times = np.asarray(observation_times, dtype=float)
    if not np.all(np.diff(times) > 0) or times[0] < 0:
        raise ValueError("Observation times must be strictly increasing and nonnegative")
    nobs = len(times)
    clocks = np.full(nobs, np.nan)
    residuals = np.full(nobs, np.nan)
    kernels = np.full(nobs, np.nan)
    discrepancies = np.full(nobs, np.nan)
    if r0 == 0.0:
        clocks.fill(0.0)
        residuals.fill(0.0)
        kernels.fill(K0)
        discrepancies.fill(0.0)
        return FlowResult(clocks, residuals, kernels, discrepancies, 0, 0), meta

    initially_active_U = U[active]
    initially_active_V = V[active]
    hit_mask = initially_active_V < -initially_active_U
    hit_U = initially_active_U[hit_mask]
    hit_V = initially_active_V[hit_mask]
    hit_clock = np.arctanh(hit_U / (-hit_V))
    order = np.argsort(hit_clock)
    hit_clock = hit_clock[order]
    hit_U = hit_U[order]
    hit_V = hit_V[order]
    hit_q = hit_U**2 + hit_V**2
    hit_c = 2.0 * hit_U * hit_V
    persistent_U = initially_active_U[~hit_mask]
    persistent_V = initially_active_V[~hit_mask]
    persist_q = np.sum(persistent_U**2 + persistent_V**2, dtype=np.float64)
    persist_c = np.sum(2.0 * persistent_U * persistent_V, dtype=np.float64)
    suffix_q = np.r_[np.cumsum(hit_q[::-1], dtype=np.float64)[::-1], 0.0]
    suffix_c = np.r_[np.cumsum(hit_c[::-1], dtype=np.float64)[::-1], 0.0]

    def sums_for_survivors(j: int) -> tuple[float, float]:
        return float(persist_q + suffix_q[j]), float(persist_c + suffix_c[j])

    def kernel_output(s: float, j: int) -> tuple[float, float]:
        q, c = sums_for_survivors(j)
        cosine = math.cosh(2.0 * s)
        sine = math.sinh(2.0 * s)
        kernel = norm_kernel * (q * cosine + c * sine)
        output = sigma * norm_output * 0.5 * (c * cosine + q * sine)
        if kernel < -1e-9 * (1.0 + K0):
            raise ArithmeticError("Negative kernel from floating-point cancellation")
        return max(kernel, 0.0), output

    T = float(times[-1])
    t_start = 0.0
    s_start = 0.0
    abs_r_start = abs(r0)
    j = 0
    event_count = 0
    nfev = 0
    next_obs = 0
    if times[0] == 0.0:
        clocks[0], residuals[0], kernels[0], discrepancies[0] = 0.0, r0, K0, 0.0
        next_obs = 1

    while t_start < T - 1e-13:
        q, c = sums_for_survivors(j)
        co = math.cosh(2.0 * s_start)
        si = math.sinh(2.0 * s_start)
        k_start = norm_kernel * (q * co + c * si)
        j_start = norm_kernel * (q * si + c * co)
        if k_start < -1e-9 * (1.0 + K0):
            raise ArithmeticError("Negative segment-start kernel")
        next_hit = float(hit_clock[j]) if j < len(hit_clock) else math.inf
        delta_hit = next_hit - s_start
        if delta_hit < -1e-10:
            raise ArithmeticError("Hit clocks are not monotone")

        def integral_kernel(xi: float) -> float:
            return 0.5 * k_start * math.sinh(2.0 * xi) + j_start * math.sinh(xi) ** 2

        def rhs(_t: float, state: np.ndarray) -> np.ndarray:
            xi = float(state[0])
            velocity = beta_clock * abs_r_start - integral_kernel(xi)
            # Extend the scalar vector field by zero beyond its equilibrium.
            # A Runge--Kutta internal stage can overshoot either the terminal
            # gate event or this equilibrium; the accepted trajectory cannot.
            return np.array([max(velocity, 0.0)])

        def hit_event(_t: float, state: np.ndarray) -> float:
            return float(state[0]) - delta_hit

        hit_event.terminal = True
        hit_event.direction = 1.0
        events = [hit_event] if math.isfinite(next_hit) else None
        sol = solve_ivp(
            rhs, (t_start, T), [0.0], events=events, dense_output=True,
            rtol=rtol, atol=atol, method="DOP853",
        )
        nfev += sol.nfev
        if not sol.success:
            raise RuntimeError(sol.message)
        t_end = float(sol.t[-1])
        hit = bool(events is not None and sol.t_events[0].size)
        for k in range(next_obs, nobs):
            t = float(times[k])
            if t > t_end + 1e-12:
                break
            xi = float(sol.sol(t)[0])
            s = s_start + xi
            abs_r = abs_r_start - integral_kernel(xi) / beta_clock
            r = sigma * abs_r
            gate_j = j + 1 if hit and abs(t - t_end) < 1e-12 else j
            kernel, output = kernel_output(s, gate_j)
            clocks[k], residuals[k], kernels[k] = s, r, kernel
            discrepancies[k] = (y - output) - r
            next_obs = k + 1
        if not hit:
            break
        xi_hit = float(sol.y[0, -1])
        abs_r_new = abs_r_start - integral_kernel(xi_hit) / beta_clock
        if abs_r_new < -1e-9 * (1.0 + abs_r_start):
            raise ArithmeticError("Negative residual at exact gate hit")
        abs_r_start = max(0.0, abs_r_new)
        s_start = next_hit
        t_start = t_end
        j += 1
        event_count += 1
        if event_count > len(hit_clock):
            raise RuntimeError("More gate events than initially active hittable neurons")

    if not np.all(np.isfinite(clocks)):
        raise RuntimeError("Some requested observation times were not recorded")
    return FlowResult(clocks, residuals, kernels, discrepancies, event_count, nfev), meta


def quantile_summary(values: list[float]) -> dict:
    a = np.asarray(values, dtype=float)
    return {
        "p50": float(np.quantile(a, 0.5)),
        "p90": float(np.quantile(a, 0.9)),
        "p95": float(np.quantile(a, 0.95)),
        "fraction_gt_0.05": float(np.mean(a > 0.05)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", type=int, nargs="+", default=[512, 2048, 8192, 32768])
    parser.add_argument("--alphas", type=float, nargs="+", default=[1.0, 1.5])
    parser.add_argument("--reps", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20261023)
    parser.add_argument("--label", type=float, default=0.7)
    parser.add_argument("--times", type=float, nargs="+", default=[0.0, 0.25, 1.0])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    widths = sorted(set(args.widths))
    times = np.asarray(args.times, dtype=float)
    if widths[0] <= 1 or args.reps <= 0 or times[0] != 0.0:
        parser.error("widths >1, reps >0, and first time 0 are required")

    root = np.random.SeedSequence(args.seed)
    alpha_seeds = root.spawn(len(args.alphas))
    results = {"experiment": "one-input exact-gate scalar flow", "code": "t384_event_clock.py",
               "seed": args.seed, "alphas": args.alphas, "widths": widths,
               "reps": args.reps, "label": args.label, "times": times.tolist(),
               "numpy_version": np.__version__, "scipy_version": scipy.__version__,
               "results": {}}
    for alpha, alpha_seed in zip(args.alphas, alpha_seeds):
        key = str(alpha)
        results["results"][key] = {}
        replicate_seeds = alpha_seed.spawn(args.reps)
        raw_by_width = {str(m): [] for m in widths}
        for rep, seed in enumerate(replicate_seeds):
            rng = np.random.default_rng(seed)
            U_all = symmetric_stable(alpha, rng, widths[-1])
            W_all = symmetric_stable(alpha, rng, widths[-1])
            for m in widths:
                flow, meta = flow_one_input(U_all[:m], W_all[:m], alpha, args.label, times)
                K = flow.kernel
                r = flow.residual
                Q = meta["Q"]
                r0 = meta["r0"]
                raw_by_width[str(m)].append({
                    "rep": rep,
                    "r0": r0,
                    "Q": Q,
                    "K0": meta["K0"],
                    "clock": flow.clock.tolist(),
                    "kernel": K.tolist(),
                    "residual": r.tolist(),
                    "kernel_abs_error": np.abs(K - Q).tolist(),
                    "residual_abs_error": np.abs(r - r0 * np.exp(-Q * times)).tolist(),
                    "max_conservation_error": float(np.max(np.abs(flow.output_residual_discrepancy))),
                    "gate_events": flow.event_count,
                    "ode_evaluations": flow.function_evaluations,
                })
        for m in widths:
            raw = raw_by_width[str(m)]
            summaries = {}
            for i, t in enumerate(times):
                if t == 0:
                    continue
                summaries[str(t)] = {
                    "kernel_abs": quantile_summary([r["kernel_abs_error"][i] for r in raw]),
                    "kernel_scaled": quantile_summary([
                        r["kernel_abs_error"][i] / (1.0 + r["Q"]) for r in raw
                    ]),
                    "residual_abs": quantile_summary([r["residual_abs_error"][i] for r in raw]),
                    "residual_scaled": quantile_summary([
                        r["residual_abs_error"][i] / (1.0 + abs(r["r0"])) for r in raw
                    ]),
                }
            results["results"][key][str(m)] = {
                "summary_by_time": summaries,
                "initial_kernel_gap": quantile_summary([r["K0"] - r["Q"] for r in raw]),
                "max_conservation_error": max(r["max_conservation_error"] for r in raw),
                "median_gate_events": float(np.median([r["gate_events"] for r in raw])),
                "raw": raw,
            }
        print(f"alpha={alpha} finished: {args.reps} replicates x {len(widths)} widths", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n")
    print(f"saved {args.output}")


if __name__ == "__main__":
    main()
