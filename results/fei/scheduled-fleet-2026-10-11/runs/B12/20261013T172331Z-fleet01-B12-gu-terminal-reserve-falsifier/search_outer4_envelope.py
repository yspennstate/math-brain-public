#!/usr/bin/env python3
"""Exhaustive float64 scan of the endpoint-centered one-biased-child GU cocycle.

All 2^16 Boolean outer gates on four inputs are scanned, for each distinguished
coordinate, over an explicit bias grid.  The formulas are those proved in
B12-A056-GU-BIASED-CHILD-COCYCLE-v1.  This is candidate location, not a
rigorous interval certificate.
"""

import argparse
import json
import math
import numpy as np


def fwht_rows(x):
    x = x.copy().astype(np.float64)
    n = x.shape[1]
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            u = x[:, base:base + step].copy()
            v = x[:, base + step:base + 2 * step].copy()
            x[:, base:base + step] = u + v
            x[:, base + step:base + 2 * step] = u - v
        step *= 2
    return x / n


def upper_rows(x):
    out = x.copy()
    nbits = (x.shape[1]).bit_length() - 1
    for bit in range(nbits):
        stride = 1 << bit
        for base in range(0, 1 << nbits, 2 * stride):
            out[:, base:base + stride] += out[:, base + stride:base + 2 * stride]
    return out


def entropy_rows(atoms, caps):
    ratio = np.ones_like(atoms)
    np.divide(caps, atoms, out=ratio, where=atoms > 0)
    terms = np.zeros_like(atoms)
    np.multiply(atoms, np.log2(ratio), out=terms, where=atoms > 0)
    return terms.sum(axis=1)


def psi(mu):
    q = mu * mu
    return 0.0 if q == 0.0 else q * math.log2(1.0 / q)


def theta_rows(a, b, beta, b_entropy, mu):
    alpha2 = 1.0 - mu * mu
    c = a + mu * b
    c2 = c * c
    mixed = c2 + alpha2 * (b * b)
    caps = upper_rows(mixed)
    phi = entropy_rows(c2, caps) + alpha2 * b_entropy
    return phi - beta * psi(mu)


def truth_tables_4():
    ids = np.arange(1 << 16, dtype=np.uint32)[:, None]
    rows = np.arange(16, dtype=np.uint32)[None, :]
    return (2 * ((ids >> rows) & 1) - 1).astype(np.int8)


def split_coordinate(values, bit):
    minus_cols = [r for r in range(16) if not ((r >> bit) & 1)]
    plus_cols = [r | (1 << bit) for r in minus_cols]
    minus = values[:, minus_cols].astype(np.float64)
    plus = values[:, plus_cols].astype(np.float64)
    return (plus + minus) / 2.0, (plus - minus) / 2.0


def decode_gate(index):
    return [1 if (index >> r) & 1 else -1 for r in range(16)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid-denominator", type=int, default=512,
                    help="scan mu=k/d for -d<k<d")
    args = ap.parse_args()
    d = args.grid_denominator
    values = truth_tables_4()
    best = {"ratio": -math.inf}
    checked = 0

    for bit in range(4):
        av, bv = split_coordinate(values, bit)
        a = fwht_rows(av)
        b = fwht_rows(bv)
        b2 = b * b
        beta = b2.sum(axis=1)
        b_entropy = entropy_rows(b2, upper_rows(b2))
        tm = theta_rows(a, b, beta, b_entropy, -1.0)
        tp = theta_rows(a, b, beta, b_entropy, 1.0)
        active = beta > 0

        for k in range(-d + 1, d):
            mu = k / d
            centered = theta_rows(a, b, beta, b_entropy, mu)
            centered -= ((1.0 - mu) * tm + (1.0 + mu) * tp) / 2.0
            denom = beta * (1.0 - mu * mu)
            ratios = np.full(beta.shape, -math.inf)
            np.divide(centered, denom, out=ratios, where=active)
            idx = int(np.argmax(ratios))
            ratio = float(ratios[idx])
            checked += int(active.sum())
            if ratio > best["ratio"]:
                best = {
                    "ratio": ratio,
                    "outer_index": idx,
                    "outer_bit": bit,
                    "mu_numerator": k,
                    "mu_denominator": d,
                    "mu": mu,
                    "beta": float(beta[idx]),
                    "centered_theta": float(centered[idx]),
                    "truth_table_row_order": decode_gate(idx),
                }

    result = {
        "status": "NUMERICAL",
        "scope": "all 65536 four-input Boolean outer gates, all four coordinates",
        "bias_grid": f"mu=k/{d}, -{d}<k<{d}",
        "normalized_values_checked": checked,
        "best": best,
        "candidate_constant": 3.0,
        "margin": 3.0 - best["ratio"],
        "random_seed": None,
        "limitations": "float64 grid scan; not a continuum or interval proof",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
