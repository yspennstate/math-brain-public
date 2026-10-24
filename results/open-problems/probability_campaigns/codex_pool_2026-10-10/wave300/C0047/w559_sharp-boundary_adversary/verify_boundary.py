"""Exact finite checks for the independent C0047 boundary packet (no simulation)."""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent


def offspring(config: tuple[int, ...]) -> int:
    # Edges 0,1,2 form a triangle; edges 3,4 leave vertices 1,2.
    reached = {0}
    triangle = ((0, 1), (0, 2), (1, 2))
    while True:
        old = set(reached)
        for is_open, (u, v) in zip(config[:3], triangle):
            if is_open and (u in reached or v in reached):
                reached.update((u, v))
        if old == reached:
            break
    return int(1 in reached and config[3]) + int(2 in reached and config[4])


def enumeration(p: F) -> list[F]:
    probs = [F(0), F(0), F(0)]
    for config in product((0, 1), repeat=5):
        opened = sum(config)
        probs[offspring(config)] += p**opened * (1-p)**(5-opened)
    return probs


def main() -> None:
    started = time.perf_counter()
    # Fresh compute gate: 32 configurations, 7 rational parameters, 180
    # decimal bisections; stdlib CPU only; no model load, GPU, or network.
    configs = list(product((0, 1), repeat=5))
    # Compare the complete symbolic mean, derived from configuration counts.
    coeffs = [0] * 6
    for config in configs:
        opened = sum(config)
        count = offspring(config)
        for j in range(5-opened+1):
            coeffs[opened+j] += count * comb(5-opened, j) * (-1)**j
    assert coeffs == [0, 0, 2, 2, -2, 0], coeffs
    samples = []
    for p in (F(0), F(1, 2), F(63, 100), F(64, 100), F(2, 3), F(9, 10), F(1)):
        probs = enumeration(p)
        assert sum(probs) == 1
        mean = probs[1] + 2*probs[2]
        analytic_mean = 2*p**2+2*p**3-2*p**4
        assert mean == analytic_mean
        assert probs[2] == 3*p**4-2*p**5
        samples.append({"p": str(p), "offspring_distribution": list(map(str, probs)),
                        "mean": str(mean), "supercritical": mean > 1})
    lo, hi = F(63, 100), F(64, 100)
    assert 2*lo**2+2*lo**3-2*lo**4 < 1 < 2*hi**2+2*hi**3-2*hi**4
    probs = enumeration(F(2, 3))
    extinction = probs[0]/probs[2]
    assert probs[0] + probs[1]*extinction + probs[2]*extinction**2 == extinction
    assert 1-extinction == F(21, 80)
    assert (1-F(2, 3))*(1-extinction) == F(7, 80)
    with localcontext() as ctx:
        ctx.prec = 60
        dl, dh = Decimal("0.63"), Decimal("0.64")
        for _ in range(180):
            dm = (dl+dh)/2
            if 2*dm**2+2*dm**3-2*dm**4 < 1:
                dl = dm
            else:
                dh = dm
        pc_display = str((dl+dh)/2)
    # The old SRW-rho criterion is automatically satisfied when rho<1.
    # The corrected criterion fails since ||A||>=2 and p_c>63/100.
    result = {
        "status": "PASS",
        "command": "python -X utf8 ~/brain_workers/w559/verify_boundary.py",
        "compute_gate": {"configurations": 32, "rational_parameters": 7,
                         "decimal_bisections": 180, "GPU": False},
        "mean_polynomial_coefficients": coeffs,
        "rational_bracket": ["63/100", "64/100"],
        "pc_decimal_display_only": pc_display,
        "forward_survival_at_two_thirds": "21/80",
        "isolated_branch_probability_at_two_thirds": "7/80",
        "corrected_spectral_product_strict_lower_bound": "63/50 = 1.26",
        "before_after": {"old_unscaled_criterion_accepts_witness": True,
                         "corrected_criterion_accepts_witness": False,
                         "false_positive_on_this_witness_before": 1,
                         "false_positive_on_this_witness_after": 0},
        "samples": samples,
        "elapsed_seconds": round(time.perf_counter()-started, 6),
        "limits": "Finite exact algebra check, not an independent proof of the infinite block-tree reduction, p_u, or the parent conjecture. Decimal root is display only."
    }
    (ROOT/"MEASUREMENTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
