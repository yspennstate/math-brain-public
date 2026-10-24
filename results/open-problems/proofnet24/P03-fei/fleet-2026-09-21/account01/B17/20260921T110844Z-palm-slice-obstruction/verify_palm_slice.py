#!/usr/bin/env python3
import json
from math import comb, exp, factorial, log, log2

BETA = 6.4547837

def pc_feasible_uniform_slice(n, k):
    if not (2 <= k <= n):
        return False
    return log(n / k) <= 2 * (k - 1)

def pc_log_margin(n, k, t):
    if t == 0.0:
        return float("inf")
    a = (1.0 - t) / (1.0 + t)
    return (k - 1) * (-log(t)) - a * log(n / k)

def entropy_ratio_uniform_slice(n, k):
    return log2(comb(n, k)) / k

def ordered_code_ratio_uniform_slice(n, k):
    return log2(n) - log2(factorial(k)) / k

def pair_convolution_term_count(n, k):
    return comb(n - 2, k - 1)

out = {
    "beta": BETA,
    "finite_example": {},
    "unbounded_family": [],
    "grid_check": {},
}

n, k = 161, 3
ts = [0.0, 1e-6, 1e-4, 1e-2, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 0.999999, 1.0]
margins = []
for t in ts:
    if t == 1.0:
        margins.append(0.0)
    else:
        margins.append(pc_log_margin(n, k, t))
out["finite_example"] = {
    "n": n,
    "k": k,
    "ln_n_over_k": log(n / k),
    "pc_threshold": 2 * (k - 1),
    "pc_feasible": pc_feasible_uniform_slice(n, k),
    "entropy_over_mean": entropy_ratio_uniform_slice(n, k),
    "ordered_code_U_over_mean": ordered_code_ratio_uniform_slice(n, k),
    "entropy_minus_beta": entropy_ratio_uniform_slice(n, k) - BETA,
    "U_minus_beta": ordered_code_ratio_uniform_slice(n, k) - BETA,
    "pair_convolution_term_count": pair_convolution_term_count(n, k),
    "pair_convolution_term_count_is_odd": pair_convolution_term_count(n, k) % 2 == 1,
    "sampled_t_log_margins": dict(zip(map(str, ts), margins)),
}
for k in range(2, 11):
    M = max(1, int(exp(2 * (k - 1))))
    n = k * M
    out["unbounded_family"].append({
        "k": k,
        "M": M,
        "n": n,
        "pc_feasible": pc_feasible_uniform_slice(n, k),
        "entropy_over_mean": entropy_ratio_uniform_slice(n, k),
        "ordered_code_U_over_mean": ordered_code_ratio_uniform_slice(n, k),
        "ln_M": log(M),
        "threshold": 2 * (k - 1),
    })

grid = [j / 10000 for j in range(1, 10000)]
analytic_gap_min = min(-log(t) - 2*(1-t)/(1+t) for t in grid)
out["grid_check"] = {
    "min_sampled_gap_of_minus_log_t_minus_2_cayley": analytic_gap_min,
    "all_unbounded_family_pc_feasible": all(x["pc_feasible"] for x in out["unbounded_family"]),
}
print(json.dumps(out, indent=2, sort_keys=True))
