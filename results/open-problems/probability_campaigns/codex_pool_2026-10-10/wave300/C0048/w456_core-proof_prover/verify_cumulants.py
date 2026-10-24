"""Independent exact spin/FK enumeration, strictly bounded to <=4 vertices.

This is a finite identity check, not an infinite-volume or formal proof.
Run only immediately after a fresh, permitted compute-gate receipt.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
GRAPHS = [
    ("one-site", 1, []),
    ("edge", 2, [(0, 1)]),
    ("path3", 3, [(0, 1), (1, 2)]),
    ("triangle", 3, [(0, 1), (1, 2), (0, 2)]),
    ("square", 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
    ("complete4", 4, [(i, j) for i in range(4) for j in range(i + 1, 4)]),
]


def spin_cumulants(n: int, edges: list, q: int, t: int):
    z = 0
    totals = [0] * 5
    configurations = 0
    for sigma in product(range(q), repeat=n):
        weight = t ** sum(sigma[i] == sigma[j] for i, j in edges)
        scaled_x = q * sigma.count(0) - n
        z += weight
        for k in range(1, 5):
            totals[k] += weight * scaled_x ** k
        configurations += 1
    moments = [F(0)] + [F(totals[k], z * q ** k) for k in range(1, 5)]
    if moments[1] != 0:
        raise AssertionError("colour symmetry failed")
    return z, [moments[2], moments[3], moments[4] - 3 * moments[2] ** 2], configurations


def fk_moments(n: int, edges: list, q: int, t: int):
    z = 0
    sums = {2: 0, 3: 0, 4: 0, "s2_squared": 0}
    configurations = 0
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                parent[root(u)] = root(v)
        sizes = {}
        for x in range(n):
            r = root(x)
            sizes[r] = sizes.get(r, 0) + 1
        weight = (t - 1) ** mask.bit_count() * q ** len(sizes)
        powers = {k: sum(s ** k for s in sizes.values()) for k in (2, 3, 4)}
        z += weight
        for k in (2, 3, 4):
            sums[k] += weight * powers[k]
        sums["s2_squared"] += weight * powers[2] ** 2
        configurations += 1
    means = {k: F(sums[k], z) for k in (2, 3, 4)}
    variance = F(sums["s2_squared"], z) - means[2] ** 2
    return z, means, variance, configurations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate-receipt", type=Path, required=True)
    args = parser.parse_args()
    # Fresh official gate evidence is supplied by the worker, never fabricated here.
    receipt = args.gate_receipt.resolve()
    if receipt.parent != ROOT or not receipt.is_file():
        raise SystemExit("gate receipt must be a file in this worker folder")
    gate_data = json.loads(receipt.read_text(encoding="utf-8"))
    if gate_data.get("allowed") is not True:
        raise SystemExit("compute gate did not permit this run")
    gate_age = time.time() - receipt.stat().st_mtime
    if gate_age < 0 or gate_age > 300:
        raise SystemExit("fresh gate receipt required (<=300 seconds)")
    started = time.perf_counter()
    cpu_started = time.process_time()
    records = []
    total_spin = total_fk = 0
    corrected_failures = omission_failures = sign_differences = 0
    for name, n, edges in GRAPHS:
        assert n <= 4 and len(edges) <= 6
        for q in (2, 3, 4, 5):
            for t in (1, 2, 4):
                if time.process_time() - cpu_started > 5:
                    raise SystemExit("5 CPU-second bound exceeded")
                zs, spin, ns = spin_cumulants(n, edges, q, t)
                zf, means, variance, nf = fk_moments(n, edges, q, t)
                total_spin += ns
                total_fk += nf
                a2 = F(q - 1, q ** 2)
                a3 = F((q - 1) * (q - 2), q ** 3)
                a4 = F((q - 1) * (q ** 2 - 6 * q + 6), q ** 4)
                predicted = [a2 * means[2], a3 * means[3], a4 * means[4] + 3 * a2 ** 2 * variance]
                residuals = [s - f for s, f in zip(spin, predicted)]
                ok = zs == zf and all(r == 0 for r in residuals)
                corrected_failures += not ok
                omitted = a4 * means[4]
                omission_failures += spin[2] != omitted
                sign_differences += (spin[2] > 0) != (omitted > 0)
                assert means[3] * n >= means[2] ** 2
                records.append({
                    "graph": name, "vertices": n, "edges": len(edges), "q": q,
                    "exp_beta": t, "p": str(F(t - 1, t)), "partition_functions_equal": zs == zf,
                    "pressure_derivatives": [str(s / n) for s in spin],
                    "corrected_residuals": [str(r / n) for r in residuals],
                    "omission_residual_order4": str((spin[2] - omitted) / n),
                    "variance_S2": str(variance), "status": "PASS" if ok else "FAIL",
                })
    constants = {"q": 3, "r0": "1/2", "b": str(F(1, 3)), "K": str(F(64, 3)), "C": str(F(8, 9)), "exclusion_threshold": str(F(1, 3) / (6 * F(8, 9)))}
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Exact finite free-boundary spin/FK identities only; no parent theorem proof",
        "gate_receipt": str(receipt), "gate_age_seconds": gate_age,
        "hard_caps": {"vertices": 4, "edges": 6, "q": 5, "cases": 72, "cpu_seconds": 5},
        "cases": len(records), "spin_configurations": total_spin, "fk_configurations": total_fk,
        "corrected_identity_failures": corrected_failures,
        "incomplete_formula_failures": omission_failures,
        "incomplete_formula_description": "Diagnostic omission of 3 a2^2 Var(S2); not a deployed baseline",
        "quartic_sign_differences": sign_differences,
        "cpu_seconds": time.process_time() - cpu_started,
        "wall_seconds": time.perf_counter() - started,
        "scalar_entropy_constants": constants, "records": records,
    }
    (ROOT / "measurements.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with (ROOT / "measurements.jsonl").open("a", encoding="utf-8") as handle:
        for row in records:
            handle.write(json.dumps(row) + "\n")
    print(json.dumps({k: result[k] for k in ("cases", "spin_configurations", "fk_configurations", "corrected_identity_failures", "incomplete_formula_failures", "quartic_sign_differences", "cpu_seconds", "wall_seconds")}))
    return int(corrected_failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
