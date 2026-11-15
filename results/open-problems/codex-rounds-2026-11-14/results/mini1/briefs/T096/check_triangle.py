#!/usr/bin/env python3
"""Enumerate a frustrated triangle and independently check the symbolic claims."""
import os

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"

import csv
import itertools
import json
import math
import platform
from pathlib import Path
import resource

# The problem is eight states; prohibit an accidentally enlarged calculation.
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
STATES = list(itertools.product((-1, 1), repeat=3))
INDEX = {x: i for i, x in enumerate(STATES)}


def chain(k, h):
    # Construct rates using differences of full Gibbs log weights, rather than
    # the conditional-mean formulas used in PROOF.md.
    logs = np.array([-k * (x[0]*x[1] + x[0]*x[2] + x[1]*x[2])
                     + h * sum(x) for x in STATES])
    weights = np.exp(logs - logs.max())
    pi = weights / weights.sum()
    q = np.zeros((8, 8))
    for a, x in enumerate(STATES):
        for i in range(3):
            y = list(x)
            y[i] *= -1
            b = INDEX[tuple(y)]
            q[a, b] = 1 / (1 + math.exp(float(logs[a] - logs[b])))
        q[a, a] = -q[a].sum()
    symmetric = -(np.sqrt(pi)[:, None] * q / np.sqrt(pi)[None, :])
    assert np.max(np.abs(symmetric - symmetric.T)) < 2e-13
    eigenvalues = np.linalg.eigvalsh(symmetric)
    assert abs(eigenvalues[0]) < 2e-13
    assert np.max(np.abs(pi @ q)) < 2e-13
    assert np.max(np.abs(q.sum(axis=1))) < 2e-13
    return pi, q, eigenvalues


def exact_audit():
    # At K=log(2), every unnormalized weight is a rational power of 2.
    out = {}
    for field in (0, 1):
        weights = [sp.Integer(2) ** (-(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])
                                    + field*sum(x)) for x in STATES]
        q = sp.zeros(8)
        for a, x in enumerate(STATES):
            for i in range(3):
                y = list(x)
                y[i] *= -1
                b = INDEX[tuple(y)]
                q[a, b] = weights[b] / (weights[a] + weights[b])
            q[a, a] = -sum(q[a, b] for b in range(8) if b != a)
        factors = sp.factor((-q).charpoly().as_expr())
        out["field_K" if field else "field_zero"] = str(factors)
    q = sp.Symbol("q", nonnegative=True)
    u = (1-q)/(1+q)
    v = (1-q**3)/(1+q**3)
    a = (u+v)/4
    c = (v-3*u)/4
    lam = (3-2*a-sp.sqrt(1+4*c*(-a+2*c)))/2
    out["field_gap_series_q_exp_minus_2K"] = str(sp.series(lam, q, 0, 3))
    return out


def main():
    rows = []
    residual = 0.0
    for k in (0.0, 0.1, 0.25, 0.5, math.log(2), 1.0, 2.0, 3.0, 5.0):
        pi0, q0, ev0 = chain(k, 0)
        pih, qh, evh = chain(k, k)
        z = 3*math.exp(2*k) + 4 + math.exp(-6*k)
        mass = math.exp(2*k) / z
        exit_rate = 3 / (1 + math.exp(2*k))
        a = (math.tanh(k) + math.tanh(3*k)) / 4
        c = (math.tanh(3*k) - 3*math.tanh(k)) / 4
        lam = (3 - 2*a - math.sqrt(1 + 4*c*(-a + 2*c))) / 2
        expected = sorted([0, 1+math.tanh(2*k),
                           1-math.tanh(2*k)/2, 1-math.tanh(2*k)/2,
                           2+math.tanh(2*k), 2-math.tanh(2*k)/2,
                           2-math.tanh(2*k)/2, 3])
        residual = max(residual, float(np.max(np.abs(ev0 - expected))))
        assert min(abs(evh-lam)) < 2e-13
        nu_minus = (3+4*a-math.sqrt(1+8*c*(a+c))) / 2
        nu_plus = (3+4*a+math.sqrt(1+8*c*(a+c))) / 2
        lam_plus = (3-2*a+math.sqrt(1+4*c*(-a+2*c))) / 2
        expected_field = sorted([0, 3, lam, lam, lam_plus, lam_plus,
                                 nu_minus, nu_plus])
        residual = max(residual, float(np.max(np.abs(evh-expected_field))))
        assert abs(evh[1]-lam) < 2e-13
        state = INDEX[(1, 1, -1)]
        assert abs(pih[state] - mass) < 2e-13
        assert abs(-qh[state, state] - exit_rate) < 2e-13
        indicator = np.zeros(8)
        indicator[state] = 1
        variance = float(pih @ (indicator - pih @ indicator)**2)
        energy = float(-pih @ (indicator * (qh @ indicator)))
        rayleigh = energy / variance
        assert abs(rayleigh-exit_rate/(1-mass)) < 2e-13
        assert evh[1] <= rayleigh + 2e-13
        # The d,e invariant subspace is checked in the full generator.
        d = np.array([x[0]-x[1] for x in STATES], dtype=float)
        e = np.array([x[2]*(x[0]-x[1]) for x in STATES], dtype=float)
        assert np.max(abs(qh @ d - (-(1-a)*d-c*e))) < 2e-13
        assert np.max(abs(qh @ e - ((a-2*c)*d-(2-a)*e))) < 2e-13
        rows.append(dict(K=k, zero_gap=float(ev0[1]),
                         zero_formula=1-math.tanh(2*k)/2,
                         field_gap=float(evh[1]), field_eigenvalue=lam,
                         rayleigh_bound=rayleigh, singleton_mass=mass,
                         exit_rate=exit_rate))
    assert residual < 2e-13
    exact = exact_audit()
    exact["expected_field_small_eigenvalue"] = "(72-sqrt(1765))/65"
    exact["expected_zero_gap"] = "19/34"
    exact["max_full_spectrum_residual"] = residual
    with (ROOT / "triangle_data.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / "triangle_exact.json").write_text(json.dumps(exact, indent=2)+"\n")
    print("effective nice:", os.getpriority(os.PRIO_PROCESS, 0))
    print("K                 zero gap       field gap      Rayleigh upper")
    for r in rows:
        print(f"{r['K']:17.12f} {r['zero_gap']:.12f} "
              f"{r['field_gap']:.12f} {r['rayleigh_bound']:.12f}")
    print("Exact characteristic polynomials at K=log(2):")
    for key, val in exact.items():
        print(key + ":", val)
    print("PASS: full spectra, invariant subspaces, stationary laws, and exit rates")
    print("Data: triangle_data.csv; triangle_exact.json")
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if platform.system() == "Darwin" else peak*1024
    assert peak_bytes < 1_000_000_000
    print("peak RSS bytes:", peak_bytes)


if __name__ == "__main__":
    main()
