#!/usr/bin/env python3
"""Search endpoint reserve ratios for Boolean outer gates.

The distinguished coordinate separates two arbitrary Boolean slices
u=g(-1,.) and v=g(+1,.).  We exhaust all u and all v obtained by flipping at
most `--max-flips` truth-table points, and optionally add a seeded random
sample of unrestricted pairs.  Float64 locates candidates; exact certification
belongs in a separate script.
"""

import argparse
import itertools
import json
import math
import numpy as np


def fwht_rows(x):
    x = x.copy().astype(np.float64)
    n = x.shape[1]
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            a = x[:, base:base + step].copy()
            b = x[:, base + step:base + 2 * step].copy()
            x[:, base:base + step] = a + b
            x[:, base + step:base + 2 * step] = a - b
        step *= 2
    return x / n


def upper_rows(x):
    out = x.copy()
    nbits = x.shape[1].bit_length() - 1
    for bit in range(nbits):
        step = 1 << bit
        for base in range(0, 1 << nbits, 2 * step):
            out[:, base:base + step] += out[:, base + step:base + 2 * step]
    return out


def entropy_rows(atoms, caps=None):
    if caps is None:
        caps = upper_rows(atoms)
    ratio = np.ones_like(atoms)
    np.divide(caps, atoms, out=ratio, where=atoms > 0)
    terms = np.zeros_like(atoms)
    np.multiply(atoms, np.log2(ratio), out=terms, where=atoms > 0)
    return terms.sum(axis=1)


def endpoint_ratio(u_hat, v_hat):
    a = (u_hat + v_hat) / 2.0
    b = (v_hat - u_hat) / 2.0
    b2 = b*b
    beta = b2.sum(axis=1)
    eb = entropy_rows(b2)
    u2 = u_hat*u_hat
    caps = upper_rows(u2)
    cap_primes = upper_rows(2*a*b)

    qprime = np.zeros(beta.shape)
    mask = u2 > 0
    logratio = np.zeros_like(u2)
    np.log2(np.divide(caps, u2, out=np.ones_like(u2), where=mask),
            out=logratio, where=mask)
    qprime += (2*u_hat*b*logratio).sum(axis=1)
    rational = np.zeros_like(u2)
    np.divide(cap_primes, caps, out=rational, where=mask)
    second = np.zeros_like(u2)
    np.divide(2*b, u_hat, out=second, where=mask)
    qprime += (u2*(rational-second)).sum(axis=1)/math.log(2)
    theta_prime = qprime + 2*eb - 2*beta/math.log(2)
    theta_minus = entropy_rows(u2, caps)
    theta_plus = entropy_rows(v_hat*v_hat)
    slope = theta_prime + (theta_minus-theta_plus)/2.0
    ratios = np.full(beta.shape, -math.inf)
    np.divide(slope, 2*beta, out=ratios, where=beta > 0)
    return ratios, beta


def all_truth_tables(bits):
    nrows = 1 << bits
    ids = np.arange(1 << nrows, dtype=np.uint32)[:, None]
    rows = np.arange(nrows, dtype=np.uint32)[None, :]
    return (2*((ids >> rows) & 1)-1).astype(np.int8)


def table_index(row):
    ans = 0
    for k, x in enumerate(row):
        if x == 1:
            ans |= 1 << k
    return ans


def update(best, ratios, beta, u_rows, v_rows, family, extra):
    idx = int(np.argmax(ratios))
    if float(ratios[idx]) > best["ratio"]:
        best.clear()
        best.update({
            "ratio": float(ratios[idx]),
            "beta": float(beta[idx]),
            "u_index": table_index(u_rows[idx]),
            "v_index": table_index(v_rows[idx]),
            "u_truth_table": [int(x) for x in u_rows[idx]],
            "v_truth_table": [int(x) for x in v_rows[idx]],
            "family": family,
            **extra,
        })


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-flips", type=int, default=2)
    ap.add_argument("--slice-bits", type=int, default=4)
    ap.add_argument("--random-pairs", type=int, default=250000)
    ap.add_argument("--batch", type=int, default=32768)
    ap.add_argument("--seed", type=int, default=20261013)
    args = ap.parse_args()

    best = {"ratio": -math.inf}
    checked = 0

    nrows = 1 << args.slice_bits
    if args.max_flips and args.slice_bits <= 4:
        all_u = all_truth_tables(args.slice_bits)
        u_hat_all = fwht_rows(all_u)
        for k in range(1, args.max_flips+1):
            for subset in itertools.combinations(range(nrows), k):
                signs = np.ones(nrows, dtype=np.int8)
                signs[list(subset)] = -1
                v_rows = all_u*signs
                v_hat = fwht_rows(v_rows)
                ratios, beta = endpoint_ratio(u_hat_all, v_hat)
                update(best, ratios, beta, all_u, v_rows,
                       "all_u_fixed_flip_subset", {"flip_subset": list(subset)})
                checked += len(all_u)

    rng = np.random.default_rng(args.seed)
    left = args.random_pairs
    while left:
        m = min(left, args.batch)
        u = rng.choice(np.array([-1, 1], dtype=np.int8), size=(m, nrows))
        v = rng.choice(np.array([-1, 1], dtype=np.int8), size=(m, nrows))
        ratios, beta = endpoint_ratio(fwht_rows(u), fwht_rows(v))
        update(best, ratios, beta, u, v, "seeded_random_pairs", {})
        checked += m
        left -= m

    out = {
        "status": "NUMERICAL_CANDIDATE_SEARCH",
        "outer_arity": args.slice_bits+1,
        "distinguished_coordinate": 0,
        "exhaustive_family": (f"all {args.slice_bits}-bit u and v differing at 1..{args.max_flips} truth-table points"
                              if args.max_flips and args.slice_bits <= 4 else "none"),
        "random_pairs": args.random_pairs,
        "seed": args.seed,
        "pairs_checked": checked,
        "best": best,
        "candidate_constant": 4,
        "margin": 4-best["ratio"],
        "limitations": "float64; exhaustive only in stated small-symmetric-difference family",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
