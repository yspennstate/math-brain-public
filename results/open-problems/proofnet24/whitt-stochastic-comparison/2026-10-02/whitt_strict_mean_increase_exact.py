"""Exact infinite-queue certificate with a strictly larger comparison mean.

This extends the existing positive H2 example by scaling the comparison
services by 10001/10000. See the separate proof for the strict ICX argument.
"""
from fractions import Fraction as F
import json
from whitt_positive_service_exact import certify, dec


if __name__ == "__main__":
    scale = F(10001, 10000)
    base_lo, base_hi, base = certify(
        "base_positive_H2_mean_1", F(11, 10),
        [F(3, 7), F(4, 7)], [F(5), F(5, 8)])
    target_lo, target_hi, target = certify(
        "strictly_larger_mean_positive_H2", F(11, 10),
        [F(200, 533), F(333, 533)],
        [F(1000) / scale, F(5, 8) / scale])
    gap = base_lo - target_hi
    assert gap > F(12, 5000)
    threshold = F(1, 100000)
    tail_gap = gap - 10 * threshold
    assert tail_gap > F(23, 10000)
    assert sum(p / mu for p, mu in zip(
        [F(200, 533), F(333, 533)],
        [F(1000) / scale, F(5, 8) / scale])) == scale
    result = {
        "arithmetic": "exact Fraction; decimal strings only display",
        "service_scale": str(scale),
        "service_means": {"base": "1", "target": str(scale)},
        "models": [base, target],
        "delay_gap_lower_display": dec(gap),
        "positive_waiting_threshold": str(threshold),
        "waiting_tail_gap_lower_display": dec(tail_gap),
        "exact_assertions": [
            "E[target service]=10001/10000>E[base service]=1",
            "P(W_base>0)-P(W_target>0)>12/5000",
            "P(W_base>1/100000)-P(W_target>1/100000)>23/10000"
        ],
        "strict_increasing_convex_order":
            "The existing equal-mean martingale coupling gives S<=cx T; "
            "target=(10001/10000)T. Its stop-loss strictly exceeds S "
            "at every finite threshold t>=0, including t=0."
    }
    print(json.dumps(result, indent=2))
