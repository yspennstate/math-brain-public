#!/usr/bin/env python3
"""Reproducible finite checks for B18 marginal-profile FEI slack criterion.

This is supporting evidence only, not a proof of the universal selector lemma or
of full FEI. Uses the normalized Walsh transform and float64-compatible Python
floats for entropies. Exhaustive search quotients global output negation by
fixing f(0)=+1.
"""
from __future__ import annotations
import json
import math

C = 6.4547837


def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    n = len(a)
    return [x / n for x in a]


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def metrics(vals):
    n = len(vals).bit_length() - 1
    coeff = fwht(vals)
    prob = [x * x for x in coeff]
    H = -sum(p * math.log2(p) for p in prob if p > 0.0)
    inf = [sum(prob[s] for s in range(len(prob)) if (s >> i) & 1)
           for i in range(n)]
    I = sum(inf)
    M = sum(h2(a) for a in inf)
    P = max(0.0, C * I - M)
    return H, I, M, P, inf


def restrict(vals, i, bit):
    n = len(vals).bit_length() - 1
    out = []
    for y in range(1 << (n - 1)):
        lo = y & ((1 << i) - 1)
        hi = y >> i
        x = lo | (bit << i) | (hi << (i + 1))
        out.append(vals[x])
    return out


def min_selector_residual(vals):
    H, _, _, _, inf = metrics(vals)
    best = float("inf")
    for i, a in enumerate(inf):
        if a <= 1e-14:
            continue
        v0, v1 = restrict(vals, i, 0), restrict(vals, i, 1)
        H0, _, _, P0, _ = metrics(v0)
        H1, _, _, P1, _ = metrics(v1)
        delta = H - 0.5 * (H0 + H1)
        best = min(best, delta - C * a - 0.5 * (P0 + P1))
    return best


def exhaustive():
    out = {}
    for n in range(1, 5):
        N = 1 << n
        worst = -float("inf")
        arg = None
        for bits in range(1 << (N - 1)):
            vals = [1] + [1 if (bits >> (x - 1)) & 1 else -1
                          for x in range(1, N)]
            r = min_selector_residual(vals)
            if r != float("inf") and r > worst:
                worst, arg = r, bits
        out[str(n)] = {"worst_min_residual": worst,
                       "canonical_arg_index": arg,
                       "violates": worst > 1e-10}
    return out


def bent_values(m):
    # f(x)=(-1)^(x0*x1 + x2*x3 + ...), a standard bent quadratic phase.
    vals = []
    for x in range(1 << m):
        q = 0
        for k in range(0, m, 2):
            q ^= ((x >> k) & 1) & ((x >> (k + 1)) & 1)
        vals.append(1 if q == 0 else -1)
    return vals


def selector_parent(g, gp):
    return list(g) + list(gp)


def bent_selector():
    out = {}
    for m in (2, 4, 6, 8, 10, 12):
        g = bent_values(m)
        gp = list(g)
        gp[0] *= -1
        f = selector_parent(g, gp)
        H, _, _, _, inf = metrics(f)
        H0, _, _, P0, _ = metrics(g)
        H1, _, _, P1, _ = metrics(gp)
        az = inf[m]
        delta = H - 0.5 * (H0 + H1)
        residual = delta - C * az - 0.5 * (P0 + P1)
        out[str(m)] = {
            "selector_influence": az,
            "selector_delta_over_influence": delta / az,
            "selector_marginal_slack_residual": residual,
            "old_coordinate_influence_min": min(inf[:m]),
            "old_coordinate_influence_max": max(inf[:m]),
        }
    return out


if __name__ == "__main__":
    print(json.dumps({
        "candidate_C": C,
        "exhaustive_boolean_n_le_4": exhaustive(),
        "bent_selector": bent_selector(),
        "scope": "finite supporting checks only; full FEI remains open",
    }, indent=2, sort_keys=True))
