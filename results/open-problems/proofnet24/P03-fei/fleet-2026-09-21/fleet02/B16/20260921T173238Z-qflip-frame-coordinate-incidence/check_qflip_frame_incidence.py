#!/usr/bin/env python3
"""Exact self-check for B16 q-flip frame incidence theorem.

For deterministic nonnegative integer pivot weights lambda_u, exhaustively checks
27 * sum_u lambda_u E_u(f)^2 <= 4 D(lambda) J(f)
for every Boolean truth table through n=4, using integer arithmetic only.

It also checks the parity-switch witness exactly:
F_lambda((-1)^(x_i x_j)) = pair_load(i,j)/16, J=1.
"""
from itertools import combinations
import json

def truth_bit(mask, x):
    return (mask >> x) & 1

def disagreement_count(mask, n, u):
    N = 1 << n
    return sum(truth_bit(mask, x) ^ truth_bit(mask, x ^ u) for x in range(N))

def weight(u):
    # deterministic strictly positive integer weight, no randomness
    return ((37 * u + 11) % 17) + 1

def parity_switch_mask(n, i, j):
    N = 1 << n
    m = 0
    for x in range(N):
        bi = (x >> i) & 1
        bj = (x >> j) & 1
        if bi & bj:
            m |= 1 << x
    return m

def check_n(n):
    N = 1 << n
    lambdas = {u: weight(u) for u in range(1, N)}
    D = max(sum(lam for u, lam in lambdas.items() if (u >> i) & 1)
            for i in range(n))

    total_functions = 1 << N
    max_num = -1
    max_den = 1
    max_mask = None

    for mask in range(total_functions):
        dcoord = [disagreement_count(mask, n, 1 << i) for i in range(n)]
        J_num = sum(min(d, N - d) for d in dcoord)  # J = J_num/N

        # F = S/N^4
        S = 0
        for u, lam in lambdas.items():
            d = disagreement_count(mask, n, u)
            S += lam * d * d * (N - d) * (N - d)

        # Exact theorem: 27 S <= 4 D J_num N^3.
        rhs = 4 * D * J_num * (N ** 3)
        lhs = 27 * S
        if lhs > rhs:
            raise AssertionError(("frame bound failure", n, mask, lhs, rhs))

        # Track ratio F/(D J) = S/(D J_num N^3), excluding J=0.
        if J_num:
            num = S
            den = D * J_num * (N ** 3)
            if max_mask is None or num * max_den > max_num * den:
                max_num, max_den, max_mask = num, den, mask

    witness_checks = 0
    for i, j in combinations(range(n), 2):
        mask = parity_switch_mask(n, i, j)
        dcoord = [disagreement_count(mask, n, 1 << k) for k in range(n)]
        J_num = sum(min(d, N-d) for d in dcoord)
        if J_num != N:
            raise AssertionError(("parity switch J != 1", n, i, j, J_num, N))
        pair_load = sum(lam for u, lam in lambdas.items()
                        if ((u >> i) & 1) or ((u >> j) & 1))
        S = 0
        for u, lam in lambdas.items():
            d = disagreement_count(mask, n, u)
            S += lam * d * d * (N-d) * (N-d)
        # F=S/N^4 must equal pair_load/16.
        if 16 * S != pair_load * (N ** 4):
            raise AssertionError(("parity switch frame identity failure", n, i, j))
        witness_checks += 1

    return {
        "n": n,
        "functions": total_functions,
        "pivots": len(lambdas),
        "D": D,
        "witness_pairs": witness_checks,
        "max_observed_ratio_F_over_DJ": (
            f"{max_num}/{max_den}" if max_mask is not None else "0"
        ),
        "max_observed_ratio_float": (
            max_num / max_den if max_mask is not None else 0.0
        ),
        "theorem_constant_4_over_27": 4/27,
    }

def main():
    rows = [check_n(n) for n in range(2, 5)]
    out = {
        "status": "PASS",
        "arithmetic": "exact integers; displayed ratios additionally converted to float",
        "scope": "all Boolean truth tables for n=2,3,4 under one deterministic positive integer pivot-weight family; all parity-switch coordinate-pair witnesses",
        "rows": rows,
        "total_boolean_functions": sum(r["functions"] for r in rows),
        "total_witness_pairs": sum(r["witness_pairs"] for r in rows),
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
