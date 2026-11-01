"""Bounded CPU-only verification of the P0162 restriction obstruction.

Run: python -X utf8 verify_obstruction.py
No live files or stores are written. Truth tables are generated from definitions.
"""
from __future__ import annotations

import ctypes
import json
import math
import time
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fresh_gate():
    class Memory(ctypes.Structure):
        _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong),
                    ("total_phys", ctypes.c_ulonglong), ("avail_phys", ctypes.c_ulonglong),
                    ("total_page", ctypes.c_ulonglong), ("avail_page", ctypes.c_ulonglong),
                    ("total_virtual", ctypes.c_ulonglong), ("avail_virtual", ctypes.c_ulonglong),
                    ("avail_extended", ctypes.c_ulonglong)]

    def cpu_ticks():
        values = [ctypes.c_ulonglong() for _ in range(3)]
        if not ctypes.windll.kernel32.GetSystemTimes(*(ctypes.byref(v) for v in values)):
            raise OSError("GetSystemTimes failed")
        return tuple(v.value for v in values)

    mem = Memory()
    mem.length = ctypes.sizeof(mem)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
        raise OSError("GlobalMemoryStatusEx failed")
    old = cpu_ticks()
    time.sleep(0.15)
    new = cpu_ticks()
    idle = new[0] - old[0]
    total = (new[1] - old[1]) + (new[2] - old[2])
    load = 1.0 - idle / total if total else 1.0
    gate = {"utc": datetime.now(timezone.utc).isoformat(), "cpu_fraction": load,
            "available_physical_bytes": mem.avail_phys,
            "limits": {"maximum_truth_table_atoms": 2048,
                       "maximum_exhaustive_dimension": 3, "maximum_seconds": 45,
                       "minimum_available_physical_bytes": 268435456,
                       "maximum_cpu_fraction": 0.95, "gpu": False,
                       "parallel_workers": 1, "network": False},
            "allowed": load <= 0.95 and mem.avail_phys >= 268435456}
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
    if not gate["allowed"]:
        raise RuntimeError("Fresh compute gate declined; no numerical experiment ran")
    return gate


def walsh_raw(values):
    a = list(values)
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2 * width):
            for j in range(start, start + width):
                x, y = a[j], a[j + width]
                a[j], a[j + width] = x + y, x - y
        width *= 2
    return a


def entropy(values):
    raw = walsh_raw(values)
    denominator = len(values) ** 2
    return math.fsum(-(c * c / denominator) * math.log2(c * c / denominator)
                     for c in raw if c)


def restriction(values, bit, value):
    lowmask = (1 << bit) - 1
    return [values[(x & lowmask) | ((x & ~lowmask) << 1) | (value << bit)]
            for x in range(len(values) // 2)]


def direct_influence(values, bit):
    return Fraction(sum(v != values[x ^ (1 << bit)] for x, v in enumerate(values)), len(values))


def binary_entropy(q):
    if q in (0.0, 1.0):
        return 0.0
    return -q * math.log2(q) - (1 - q) * math.log2(1 - q)


def check_ledger(values, bit):
    plus, minus = restriction(values, bit, 0), restriction(values, bit, 1)
    n = len(plus)
    u, v = walsh_raw(plus), walsh_raw(minus)
    r = [(x * x + y * y) / (2 * n * n) for x, y in zip(u, v)]
    hr = math.fsum(-p * math.log2(p) for p in r if p)
    child_h = (entropy(plus) + entropy(minus)) / 2
    js = hr - child_h
    conditional = math.fsum(p * binary_entropy((x - y) ** 2 / (2 * (x * x + y * y)))
                            for p, x, y in zip(r, u, v) if p)
    delta = entropy(values) - child_h
    influence = Fraction(sum((x - y) ** 2 for x, y in zip(u, v)), 4 * n * n)
    assert influence == direct_influence(values, bit)
    residual = abs(delta - (js + conditional))
    assert residual < 2e-12, (residual, len(values), bit)
    assert js >= -2e-12 and delta >= -2e-12
    return delta, js, conditional, residual


def closed_form(m):
    with localcontext() as ctx:
        ctx.prec = 180
        n = Decimal(1 << m)
        root = Decimal(1 << (m // 2))
        kp, km = (n + root) / 2, (n - root) / 2
        ln2 = Decimal(2).ln()

        def term(p):
            return -p * p.ln() / ln2 if p else Decimal(0)

        hf = kp * term((root - 1) ** 2 / n ** 2) + km * term((root + 1) ** 2 / n ** 2)
        hf += n * term(1 / n ** 2)
        hh = kp * term((root - 2) ** 2 / n ** 2) + km * term((root + 2) ** 2 / n ** 2)
        delta = hf - (Decimal(m) + hh) / 2
        lower = (n - 2 * root + 2).ln() / ln2
        return {"m": m, "selector_ratio": str(delta * n),
                "analytic_lower_bound": str(lower), "H": str(hf),
                "I": str(Decimal(m) / 2 + (m + 1) / n),
                "H_over_I": str(hf / (Decimal(m) / 2 + (m + 1) / n)),
                "evaluation": "180-digit decimal evaluation of proved two-sign multiplicities"}


def main():
    gate = fresh_gate()
    started = time.perf_counter()

    def deadline():
        if time.perf_counter() - started > 45:
            raise RuntimeError("Bounded verification deadline exceeded")

    ledger_checks = 0
    max_residual = 0.0
    count_functions = 0
    for dimension in range(4):
        size = 1 << dimension
        for code in range(1 << size):
            deadline()
            values = [1 - 2 * ((code >> x) & 1) for x in range(size)]
            raw = walsh_raw(values)
            assert sum(c * c for c in raw) == size ** 2
            spectral_i = Fraction(sum(mask.bit_count() * c * c for mask, c in enumerate(raw)), size ** 2)
            assert spectral_i == sum((direct_influence(values, j) for j in range(dimension)), Fraction())
            for bit in range(dimension):
                *_, residual = check_ledger(values, bit)
                max_residual = max(max_residual, residual)
                ledger_checks += 1
            count_functions += 1

    family_rows = []
    for m in (2, 4, 6, 8, 10):
        deadline()
        size = 1 << m
        g = [1 - 2 * (sum(((z >> (2*j)) & 1) * ((z >> (2*j+1)) & 1)
                          for j in range(m // 2)) % 2) for z in range(size)]
        h = list(g)
        h[0] = -1
        f = g + h
        gr, hr, fr = walsh_raw(g), walsh_raw(h), walsh_raw(f)
        root = 1 << (m // 2)
        assert set(gr) == {-root, root}
        assert hr == [a - 2 for a in gr]
        assert fr[:size] == [2 * a - 2 for a in gr]
        assert fr[size:] == [2] * size
        iy = direct_influence(f, m)
        assert iy == Fraction(1, size)
        others = [direct_influence(f, j) for j in range(m)]
        assert all(p == Fraction(1, 2) + Fraction(1, size) and p > iy for p in others)
        delta, js, conditional, residual = check_ledger(f, m)
        ratio = delta / float(iy)
        lower = math.log2(size - 2 * root + 2)
        assert ratio >= lower - 2e-10
        total_i = sum(others, iy)
        assert total_i == Fraction(m, 2) + Fraction(m + 1, size)
        hf = entropy(f)
        assert hf <= 3 * float(total_i) + 1e-12
        computed = closed_form(m)
        assert abs(ratio - float(computed["selector_ratio"])) < 2e-9
        coordinate_ratios = []
        for bit in range(m + 1):
            d, _, _, coordinate_residual = check_ledger(f, bit)
            max_residual = max(max_residual, coordinate_residual)
            coordinate_ratios.append(d / float(direct_influence(f, bit)))
        family_rows.append({"m": m, "n": m + 1, "table_atoms": len(f), "H": hf,
                            "I": str(total_i), "I_selector": str(iy), "Delta_selector": delta,
                            "selector_ratio": ratio, "lower_bound": lower,
                            "JS_over_I_selector": js / float(iy),
                            "conditional_entropy_over_I_selector": conditional / float(iy),
                            "coordinate_ratios": coordinate_ratios, "H_over_I": hf / float(total_i)})
        ledger_checks += m + 2
        max_residual = max(max_residual, residual)

    # A separate construction changes every affine phase and flip location at m=4.
    # It tests the claimed bent-base/vertex invariance, including both signs of
    # the changes in the other coordinate influences.
    splice_variants = 0
    variant_max_ratio_error = 0.0
    m, size = 4, 16
    quadratic = [1 - 2 * ((((z >> 0) & 1) * ((z >> 1) & 1)
                          + ((z >> 2) & 1) * ((z >> 3) & 1)) % 2) for z in range(size)]
    reference = float(closed_form(m)["selector_ratio"])
    for phase in range(size):
        for vertex in range(size):
            deadline()
            g = [v * (1 - 2 * ((phase & z).bit_count() % 2)) for z, v in enumerate(quadratic)]
            h = list(g)
            h[vertex] *= -1
            f = g + h
            iy = direct_influence(f, m)
            assert iy == Fraction(1, size)
            other_i = [direct_influence(f, j) for j in range(m)]
            assert all(i in (Fraction(1, 2) - iy, Fraction(1, 2) + iy) and i > iy for i in other_i)
            delta, _, _, variant_residual = check_ledger(f, m)
            max_residual = max(max_residual, variant_residual)
            ratio_error = abs(delta / float(iy) - reference)
            assert ratio_error < 2e-11
            variant_max_ratio_error = max(variant_max_ratio_error, ratio_error)
            assert entropy(f) <= 3 * float(sum(other_i, iy)) + 2e-12
            splice_variants += 1
            ledger_checks += 1

    extended = [closed_form(m) for m in (16, 32, 64, 128, 256)]
    deadline()
    result = {"status": "PASS", "command": "python -X utf8 verify_obstruction.py", "compute_gate": gate,
              "elapsed_seconds": time.perf_counter() - started,
              "all_boolean_functions_checked": count_functions, "exhaustive_dimensions": [0, 1, 2, 3],
              "restriction_ledger_checks": ledger_checks, "maximum_float_ledger_residual": max_residual,
              "family_truth_table_checks": family_rows, "extended_closed_form_evaluations": extended,
              "affine_phase_and_flip_vertex_checks": splice_variants,
              "maximum_variant_selector_ratio_error": variant_max_ratio_error,
              "policy_comparison": [{"m": r["m"], "minimum_influence_split_ratio": r["selector_ratio"],
                                     "best_observed_split_ratio": min(r["coordinate_ratios"])} for r in family_rows],
              "scope": "Independent exact truth-table/FWHT arithmetic plus floating entropy checks; no formal proof receipt and no independent agent review."}
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "functions": count_functions,
                      "ledger_checks": ledger_checks, "max_residual": max_residual,
                      "elapsed_seconds": result["elapsed_seconds"], "splice_variants": splice_variants,
                      "selector_ratios": [round(r["selector_ratio"], 9) for r in family_rows],
                      "extended_selector_ratios": [float(r["selector_ratio"]) for r in extended]}))


if __name__ == "__main__":
    main()
