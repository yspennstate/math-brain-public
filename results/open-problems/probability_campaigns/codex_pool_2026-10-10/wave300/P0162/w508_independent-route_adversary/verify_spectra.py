"""Small CPU-only checks of explicit spectra; never a formal-proof receipt."""
import argparse
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fwht(values):
    out = list(values)
    stride = 1
    while stride < len(out):
        for start in range(0, len(out), stride * 2):
            for j in range(start, start + stride):
                a, b = out[j], out[j + stride]
                out[j], out[j + stride] = a + b, a - b
        stride *= 2
    return out


def entropy(transform):
    denominator = len(transform) ** 2
    return math.fsum(
        -(v * v / denominator) * math.log2(v * v / denominator)
        for v in transform if v
    )


def restrict(values, bit, value):
    return [v for y, v in enumerate(values) if (y >> bit) & 1 == value]


def checked_transform(values):
    assert all(v in (-1, 1) for v in values)
    transform = fwht(values)
    size = len(values)
    assert sum(v * v for v in transform) == size * size
    for bit in range(size.bit_length() - 1):
        edge_count = sum(v != values[y ^ (1 << bit)] for y, v in enumerate(values))
        spectral_sum = sum(v * v for s, v in enumerate(transform) if (s >> bit) & 1)
        assert spectral_sum == edge_count * size
    return transform


def bent_selector(m, flip_points=(0,)):
    size = 1 << m
    values = [(-1) ** sum(((y >> j) & 1) * ((y >> (j + 1)) & 1)
                         for j in range(0, m, 2)) for y in range(size)]
    flipped = list(values)
    for point in flip_points:
        flipped[point] = -flipped[point]
    k = len(flip_points)
    perturbation = [values[y] if y in flip_points else 0 for y in range(size)]
    wb = fwht(perturbation)
    combined = values + flipped
    ug = checked_transform(values)
    vh = checked_transform(flipped)
    wf = checked_transform(combined)
    root_size = math.isqrt(size)
    assert all(abs(v) == root_size for v in ug)
    assert sum(v > 0 for v in ug) == (size + root_size) // 2
    assert vh == [v - 2 * b for v, b in zip(ug, wb)]
    assert wf[:size] == [2 * v - 2 * b for v, b in zip(ug, wb)]
    assert wf[size:] == [2 * b for b in wb]
    influence = sum(v * v for v in wf[size:]) / (2 * size) ** 2
    assert influence == k / size
    hg, hh, hf = entropy(ug), entropy(vh), entropy(wf)
    defect = hf - (hg + hh) / 2
    ratio = defect / influence
    derivative_entropy = math.fsum(-(b * b / (k * size)) * math.log2(b * b / (k * size))
                                    for b in wb if b)
    theta = 2 * k / root_size
    assert theta < 1
    lower = derivative_entropy - math.log2(k) + 2 * math.log2(1 - theta) + 3 / math.log(2)
    upper = derivative_entropy - math.log2(k) + 2 * math.log2(1 + theta) + 3 / math.log(2)
    support_lower = m - 2 * math.log2(k) + 2 * math.log2(1 - theta) + 3 / math.log(2)
    assert derivative_entropy + 1e-9 >= m - math.log2(k)
    assert lower - 1e-9 <= ratio <= upper + 1e-9
    total_influence = sum(s.bit_count() * v * v for s, v in enumerate(wf)) / (2 * size) ** 2
    row = {"m": m, "flip_points": list(flip_points), "K": k, "dimension": m + 1, "truth_table_size": len(combined),
           "selector_influence": influence, "entropy_g": hg, "entropy_h": hh,
           "entropy_F": hf, "defect": defect, "defect_over_selector_influence": ratio,
           "analytic_lower": lower, "analytic_upper": upper,
           "support_size_lower": support_lower, "normalized_derivative_entropy": derivative_entropy,
           "global_entropy_over_influence": hf / total_influence,
           "false_local_C4_passes": ratio <= 4,
           "scoped_analytic_bounds_pass": True}
    if m == 4:
        row["coordinate_defect_ratios"] = []
        for bit in range(m + 1):
            left = checked_transform(restrict(combined, bit, 0))
            right = checked_transform(restrict(combined, bit, 1))
            inf_bit = sum(v * v for s, v in enumerate(wf) if (s >> bit) & 1) / (2 * size) ** 2
            delta_bit = hf - (entropy(left) + entropy(right)) / 2
            row["coordinate_defect_ratios"].append(delta_bit / inf_bit)
    return row


def binary_entropy(p):
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p) if 0 < p < 1 else 0.0


def and_marginals(n):
    size = 1 << n
    c = 1 - 2 / size
    p_empty = c * c
    p_nonempty = 4 / (size * size)
    h = -(p_empty * math.log2(p_empty) if p_empty else 0) \
        - (size - 1) * p_nonempty * math.log2(p_nonempty)
    influence = n * 2 / size
    marginals = n * binary_entropy(2 / size)
    if n <= 8:
        spectrum = checked_transform([-1] + [1] * (size - 1))
        assert abs(entropy(spectrum) - h) < 1e-12
    return {"n": n, "entropy": h, "influence": influence,
            "true_entropy_over_influence": h / influence,
            "marginal_entropy_over_influence": marginals / influence,
            "marginal_bound_over_true_entropy": marginals / h}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "MEASUREMENTS.json")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.parent != ROOT:
        raise SystemExit("Output must be in this worker's folder")
    gate = json.loads(args.gate.read_text(encoding="utf-8-sig"))
    age = time.time() - gate["checked_epoch"]
    if not gate.get("bounded_cpu_check_allowed") or not 0 <= age <= 120:
        raise SystemExit("Fresh passing compute receipt required; no experiment run")
    start = time.perf_counter()
    # New multi-point families; the paired prover measured the one-point family.
    rows = []
    for m, points in ((6, (0, 1)), (8, (0, 1, 2)), (8, (0, 1, 3)), (10, (0, 1, 3, 7))):
        if time.perf_counter() - start >= 45:
            raise SystemExit("Bounded verification deadline reached")
        rows.append(bent_selector(m, points))
    # Formula-only rows above n=8 avoid allocating large truth tables.
    marginals = [and_marginals(n) for n in (4, 8, 16, 32)]
    controls = []
    for name, values, expected_h, expected_i in (
        ("constant", [1] * 16, 0, 0),
        ("dictator", [(-1) ** (y & 1) for y in range(16)], 0, 1),
        ("parity", [(-1) ** y.bit_count() for y in range(16)], 0, 4),
        ("two_bit_bent", [1, 1, 1, -1], 2, 1),
    ):
        transform = checked_transform(values)
        h = entropy(transform)
        influence = sum(s.bit_count() * v * v for s, v in enumerate(transform)) / len(values) ** 2
        assert h == expected_h and influence == expected_i
        controls.append({"name": name, "entropy": h, "influence": influence, "pass": True})
    result = {"generated_utc": datetime.now(timezone.utc).isoformat(),
              "command": "python -X utf8 verify_spectra.py --gate COMPUTE_GATE.json",
              "gate_age_at_start_seconds": age, "gate_receipt": str(args.gate.resolve()),
              "max_transform_size": 2048, "gpu_used": False, "formal_proof": False,
              "elapsed_seconds": time.perf_counter() - start,
              "bent_selector": rows, "and_marginal_diagnostic": marginals,
              "canonical_controls": controls,
              "before_false_C4_pass_count": sum(r["false_local_C4_passes"] for r in rows),
              "after_scoped_analytic_bound_pass_count": sum(r["scoped_analytic_bounds_pass"] for r in rows),
              "experiment_count": len(rows)}
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": str(output), "ratios": [r["defect_over_selector_influence"] for r in rows],
                      "controls_passed": len(controls), "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
