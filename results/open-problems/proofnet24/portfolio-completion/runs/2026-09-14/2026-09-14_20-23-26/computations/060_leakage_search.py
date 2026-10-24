"""Exploratory linear-programming search for two fixed points of a four-type QSO.

This is finite floating-point exploration, not a uniqueness proof. Parent rows
are indexed by unordered pairs, so P_ii,i is counted once in parental leakage.
For x=m+t*z and y=m-t*z, impose the midpoint and divided-difference equations
directly to avoid cancellation as t tends to zero.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog

PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
N = 4 * len(PAIRS)


def minimum_leakage(m, z, t):
    eq, rhs = [], []
    for a, (i, j) in enumerate(PAIRS):
        row = np.zeros(N + 1)
        row[4*a:4*a+4] = 1
        eq.append(row)
        rhs.append(1)
    for k in range(4):
        row = np.zeros(N + 1)
        derivative = np.zeros(N + 1)
        for a, (i, j) in enumerate(PAIRS):
            multiplicity = 1 if i == j else 2
            row[4*a+k] = multiplicity * (m[i]*m[j] + t*t*z[i]*z[j])
            derivative[4*a+k] = multiplicity * (m[i]*z[j] + m[j]*z[i])
        eq.extend([row, derivative])
        rhs.extend([m[k], z[k]])
    ub = []
    for a, (i, j) in enumerate(PAIRS):
        row = np.zeros(N + 1)
        for k in {i, j}:
            row[4*a+k] = 1
        row[-1] = -1
        ub.append(row)
    objective = np.zeros(N + 1)
    objective[-1] = 1
    fit = linprog(objective, A_eq=eq, b_eq=rhs, A_ub=ub,
                  b_ub=np.zeros(len(ub)), bounds=(0, 1), method="highs")
    if not fit.success:
        return None
    return {"delta": float(fit.fun), "m": list(m), "z": list(z),
            "t": float(t), "x": list(m+t*z), "y": list(m-t*z),
            "rows": [list(fit.x[4*a:4*a+4]) for a in range(len(PAIRS))]}


def decode(v):
    # Stick breaking parametrizes every simplex midpoint.
    m = np.array([v[0], (1-v[0])*v[1],
                  (1-v[0])*(1-v[1])*v[2],
                  (1-v[0])*(1-v[1])*(1-v[2])])
    z = np.array([v[3], 1-v[3], -v[4], v[4]-1])
    tmax = min(m[i] / abs(z[i]) for i in range(4) if z[i] != 0)
    return m, z, v[5] * tmax


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maxiter", type=int, default=100)
    parser.add_argument("--seed", type=int, default=60)
    parser.add_argument("--output", default="computations/060_leakage_search_output.json")
    args = parser.parse_args()
    best = {"delta": float("inf")}
    calls = 0

    def objective(v):
        nonlocal best, calls
        calls += 1
        cert = minimum_leakage(*decode(v))
        if cert is None:
            return 2
        if cert["delta"] < best["delta"]:
            best = cert
        return cert["delta"]

    fit = differential_evolution(objective, [(0.00001, .99999)]*6,
                                 maxiter=args.maxiter, popsize=12,
                                 seed=args.seed, polish=False, tol=1e-9)
    best.update({"solver": "scipy.optimize.linprog(method='highs')",
                 "search": "differential_evolution", "seed": args.seed,
                 "maxiter": args.maxiter, "calls": calls,
                 "pairs_zero_based": PAIRS,
                 "parameters": list(fit.x),
                 "warning": "Exploratory floating-point search, not an exact certificate or proof."})
    Path(args.output).write_text(json.dumps(best, indent=2) + "\n")
    print(json.dumps({"delta": best["delta"], "m": best["m"], "z": best["z"],
                      "t": best["t"], "calls": calls, "output": args.output}))


if __name__ == "__main__":
    main()
