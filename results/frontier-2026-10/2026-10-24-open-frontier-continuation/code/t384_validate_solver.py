"""Independent per-neuron and tolerance audit of t384_event_clock.py."""

import argparse
import json
import math
from pathlib import Path

import numpy as np

from t384_event_clock import flow_one_input, symmetric_stable


def direct_values(U, W, alpha, y, times, flow, r0):
    m = len(U)
    a = (m * math.log(m)) ** (-1 / alpha)
    knorm = m ** (-2 / alpha)
    sigma = 1.0 if r0 >= 0 else -1.0
    V = sigma * W
    initially_active = U > 0
    records = []
    for t, s, k_agg, r_agg in zip(times, flow.clock, flow.kernel, flow.residual):
        us = U[initially_active] * math.cosh(s) + V[initially_active] * math.sinh(s)
        vs = V[initially_active] * math.cosh(s) + U[initially_active] * math.sinh(s)
        gate = us > 0
        k_direct = knorm * np.sum(us[gate] ** 2 + vs[gate] ** 2, dtype=np.float64)
        f_direct = sigma * a * np.sum(us[gate] * vs[gate], dtype=np.float64)
        records.append({
            "time": float(t),
            "kernel_aggregate_minus_direct": float(k_agg - k_direct),
            "residual_aggregate_minus_direct": float(r_agg - (y - f_direct)),
        })
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=388104)
    parser.add_argument("--reps", type=int, default=8)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    times = np.array([0.0, 0.03, 0.1, 0.25, 0.5, 1.0])
    records = []
    for alpha in [1.0, 1.5]:
        for m in [512, 8192, 131072]:
            for rep in range(args.reps):
                U = symmetric_stable(alpha, rng, m)
                W = symmetric_stable(alpha, rng, m)
                flow, meta = flow_one_input(U, W, alpha, 0.7, times)
                stringent, _ = flow_one_input(U, W, alpha, 0.7, times, rtol=5e-12, atol=5e-14)
                direct = direct_values(U, W, alpha, 0.7, times, flow, meta["r0"])
                records.append({
                    "alpha": alpha, "m": m, "rep": rep,
                    "events": flow.event_count,
                    "max_abs_kernel_aggregate_direct": max(abs(x["kernel_aggregate_minus_direct"]) for x in direct),
                    "max_abs_residual_aggregate_direct": max(abs(x["residual_aggregate_minus_direct"]) for x in direct),
                    "max_abs_clock_tolerance": float(np.max(np.abs(flow.clock - stringent.clock))),
                    "max_abs_kernel_tolerance": float(np.max(np.abs(flow.kernel - stringent.kernel))),
                    "max_abs_residual_tolerance": float(np.max(np.abs(flow.residual - stringent.residual))),
                    "max_scaled_residual_tolerance": float(np.max(np.abs(flow.residual - stringent.residual)) / (1 + abs(meta["r0"]))),
                })
    summary = {key: max(row[key] for row in records) for key in [
        "max_abs_kernel_aggregate_direct", "max_abs_residual_aggregate_direct",
        "max_abs_clock_tolerance", "max_abs_kernel_tolerance", "max_abs_residual_tolerance",
        "max_scaled_residual_tolerance",
    ]}
    output = {"seed": args.seed, "reps_per_cell": args.reps, "times": times.tolist(),
              "summary_max_over_48_runs": summary, "records": records}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
