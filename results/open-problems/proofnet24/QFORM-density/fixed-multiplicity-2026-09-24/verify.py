#!/usr/bin/env python3
"""Finite reproducibility checks, added 2026-09-24; not a proof certificate.
This suite does not purport to reproduce the unavailable original self-audit suite.
Run: python verify.py --output checks.json
Dependencies: numpy, sympy. No network, credentials, or external processes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import numpy as np
import sympy as sp

EXPECTED = "9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69"

def run(root: Path) -> dict:
    source = (root / "manuscript.tex").read_bytes()
    source_sha = hashlib.sha256(source).hexdigest()
    if source_sha != EXPECTED:
        raise ValueError("Source differs from the pinned baseline; review before updating EXPECTED.")
    eta, eps = Fraction(1, 100), Fraction(1, 16)
    diagonal_lower = 1 - eps - eta
    row_upper = 4 * (Fraction(1, 7) + eps)
    slack = diagonal_lower - row_upper
    assert slack == Fraction(297, 2800) and slack > 0
    assert 2 * eta < Fraction(1, 49)
    assert 5 * Fraction(1, 80) == eps
    assert 6010 < 10000
    rng = np.random.default_rng(20260924)
    seeds = volume_tests = singular_extensions = 0
    for n in (4, 5, 6):
        for _ in range(3):
            raw = rng.integers(-3, 4, (n, n))
            A = sp.Matrix((raw + raw.T).tolist())
            def volume(r: int) -> sp.Expr:
                return sum((A.extract(S, T).det() ** 2
                            for S in combinations(range(n), r)
                            for T in combinations(range(n), r)
                            if set(S).isdisjoint(T)), sp.Integer(0))
            for r in (1, 2):
                vr = volume(r)
                if not vr:
                    continue
                weighted = sp.Integer(0)
                for S in combinations(range(n), r):
                    for T in combinations(range(n), r):
                        if not set(S).isdisjoint(T):
                            continue
                        B = A.extract(S, T)
                        det = B.det()
                        if not det:
                            continue
                        L = [i for i in range(n) if i not in S + T]
                        P = A[:, list(T)] * B.inv() * A[list(S), :]
                        E = sp.zeros(n)
                        D = sp.zeros(n)
                        for i in L:
                            D[i, i] = A[i, i] - P[i, i]
                            for j in L:
                                if i != j:
                                    E[i, j] = A[i, j] - P[i, j]
                                    rows, cols = sorted(S + (i,)), sorted(T + (j,))
                                    assert A.extract(rows, cols).det() ** 2 == det ** 2 * E[i, j] ** 2
                        R = A - D - E
                        assert P.rank() <= r and R.rank() <= 3 * r
                        assert R.extract(L, L) == P.extract(L, L)
                        assert R.extract(L, L).rank() <= r
                        assert all(D[i, i] == 0 for i in S + T)
                        assert all(E[i, i] == 0 for i in range(n))
                        weighted += det ** 2 * sum(x ** 2 for x in E)
                        seeds += 1
                upper = (r + 1) ** 2 * volume(r + 1)
                assert weighted <= upper
                singular_extensions += int(bool(weighted < upper))
                volume_tests += 1
    # Independent floating-point diagnostics, not rigorous universal certificates.
    schur_cases = graph_cases = 0
    for _ in range(30):
        n = 8
        raw = rng.normal(size=(n, n))
        A = (raw + raw.T) / 2
        for k in (1, 2):
            B, C = A[:k, :k], A[:k, k:]
            if abs(np.linalg.det(B)) < 1e-8:
                continue
            S = A[k:, k:] - C.T @ np.linalg.solve(B, C)
            eig_a = np.abs(np.linalg.eigvalsh(A))
            eig_s = np.abs(np.linalg.eigvalsh(S))
            for t in (0.2, 0.5, 1.0, 2.0):
                assert np.count_nonzero(eig_s >= t - 1e-9) >= np.count_nonzero(eig_a >= t) - k
                schur_cases += 1
        M = rng.normal(size=(6, 5))
        a = float(rng.uniform(0.1, 5))
        alpha = (2 * np.pi * np.e) ** 2
        H = alpha * np.eye(5) + a * a * (M.T @ M)
        inv = np.linalg.inv(H)
        c = alpha * np.diag(inv)
        d = a * a * np.einsum("ij,jk,ik->i", M, inv, M)
        assert c.min() > 0 and c.max() <= 1 + 1e-10
        assert d.min() >= -1e-10 and d.max() <= 1 + 1e-10
        assert abs(d.sum() - (1 - c).sum()) < 1e-10
        graph_cases += 1
    return {
        "suite": "delivery-reproducibility-2026-09-24-v1",
        "status": "PASS",
        "source_sha256": source_sha,
        "source_bytes": len(source),
        "source_lines": len(source.splitlines()),
        "exact": {"interpolation_seeds": seeds, "volume_sampling_cases": volume_tests,
                  "strict_sampling_cases": singular_extensions,
                  "diagonal_dominance_slack": str(slack)},
        "floating_diagnostics": {"schur_threshold_cases": schur_cases, "graph_weight_cases": graph_cases},
        "limitations": ["Not formal verification or an independent end-to-end mathematical audit.",
                        "Does not certify all dimensions or replace written analytic proofs.",
                        "New suite; does not reproduce all test counts historically reported in AUDIT.md."]
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("checks.json"))
    args = parser.parse_args()
    result = run(Path(__file__).resolve().parent)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
