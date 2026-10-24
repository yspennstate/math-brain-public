"""Small independent CPU checks for the explicit P0162 boundary family.

No store access, no test bank, no third-party modules. All Fourier coefficients
in the truth-table checks are exact integers before entropy is evaluated.
"""
from __future__ import annotations

import json
import math
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent


def walsh(values: list[int]) -> list[int]:
    out = values.copy()
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2 * step):
            for index in range(start, start + step):
                left, right = out[index], out[index + step]
                out[index], out[index + step] = left + right, left - right
        step *= 2
    return out


def entropy(w: list[int]) -> float:
    denominator = len(w) ** 2
    return math.fsum(
        -(v * v / denominator) * math.log2(v * v / denominator)
        for v in w if v
    )


def binary(t: float) -> float:
    if t <= 0 or t >= 1:
        return 0.0
    return -t * math.log2(t) - (1 - t) * math.log2(1 - t)


def influence(w: list[int], bit: int | None = None) -> Fraction:
    return Fraction(sum(v * v * (i.bit_count() if bit is None else bool(i & (1 << bit)))
                        for i, v in enumerate(w)), len(w) ** 2)


def split_terms(a: list[int], b: list[int]) -> tuple[float, float, float]:
    norm = len(a)
    tilde, remainder = [], []
    for av, bv in zip(a, b):
        d = av * av + bv * bv
        if not d:
            continue
        weight = d / (2 * norm * norm)
        q = float(Fraction(av * av, d))
        r = float(Fraction((av - bv) ** 2, 2 * d))
        tilde.append(weight * binary(r))
        remainder.append(weight * (1 - binary(q)))
    return math.fsum(tilde), math.fsum(remainder), float(Fraction(sum((av-bv)**2 for av,bv in zip(a,b)), 4*norm*norm))


def grouped(n: int) -> dict:
    with localcontext() as ctx:
        ctx.prec = 110
        two = Decimal(2)
        p = two ** (-n)
        s = two ** (-(n // 2))
        log_two = two.ln()
        counts = [(1 / p + 1 / s) / 2, (1 / p - 1 / s) / 2]

        def phi(value: Decimal) -> Decimal:
            return -value * value.ln() / log_two if value else Decimal(0)

        hf = sum(count * phi((sign * s - p) ** 2)
                 for count, sign in zip(counts, [1, -1])) + phi(p * p) / p
        hh = sum(count * phi((sign * s - 2 * p) ** 2)
                 for count, sign in zip(counts, [1, -1]))
        delta = hf - (Decimal(n) + hh) / 2
        total = Decimal(n) / 2 + (n + 1) * p
        ratio = delta / p
        lower = Decimal(n) - 4 / log_two
        assert ratio >= lower
        h_binary = phi(p) + phi(1-p)
        sharp_remainder = (delta-h_binary)/p
        assert sharp_remainder <= 2/log_two
        return {"base_n": n, "selector_influence": str(p),
                "split_ratio": str(ratio), "proved_lower_bound": str(lower),
                "squared_spectrum_l1_ratio": str(4 * (1-p) / s),
                "global_H_over_I": str(hf / total),
                "split_ratio_minus_n": str(ratio - n),
                "delta_minus_binary_entropy_over_influence": str(sharp_remainder),
                "sharp_additive_bound": str(2/log_two)}


def main() -> None:
    started = time.perf_counter()
    gate = json.loads((BASE / "COMPUTE_GATE.json").read_text(encoding="utf-8-sig"))
    assert gate["max_base_dimension_enumerated"] == 10
    rows, max_error = [], 0.0
    for n in [2, 4, 6, 8, 10]:
        assert time.perf_counter() - started < gate["max_runtime_seconds"]
        count = 1 << n
        g = [(-1 if sum(((t >> (2*j)) & 1) * ((t >> (2*j+1)) & 1)
                       for j in range(n // 2)) % 2 else 1) for t in range(count)]
        h = g.copy()
        h[0] = -1
        f = g + h
        wg, wh, wf = walsh(g), walsh(h), walsh(f)
        assert all(abs(v) == 1 << (n // 2) for v in wg)
        assert wh == [v - 2 for v in wg]
        assert wf == [2*v - 2 for v in wg] + [2]*count
        p = Fraction(1, count)
        assert influence(wf, n) == p
        assert influence(wf) == Fraction(n, 2) + (n+1)*p
        for bit in range(n):
            assert influence(wg, bit) == Fraction(1, 2)
            assert influence(wh, bit) == Fraction(1, 2) + 2*p
            assert influence(wf, bit) == Fraction(1, 2) + p
            original_plus = [f[t] for t in range(len(f)) if not (t & (1 << bit))]
            original_minus = [f[t] for t in range(len(f)) if t & (1 << bit)]
            other_delta = entropy(wf) - (entropy(walsh(original_plus)) + entropy(walsh(original_minus))) / 2
            assert -1e-12 <= other_delta <= 2 + 1e-12
            assert other_delta / float(influence(wf, bit)) < 4
        delta = entropy(wf) - (entropy(wg) + entropy(wh)) / 2
        tilde, remainder, inf = split_terms(wg, wh)
        error = abs(delta - tilde - remainder)
        max_error = max(max_error, error)
        assert error < 1e-11
        l1 = Fraction(sum(abs(av*av-bv*bv) for av,bv in zip(wg,wh)), count*count)
        assert l1/p == 4*(1-p)*(1 << (n//2))
        exact = grouped(n)
        assert abs(delta / float(p) - float(exact["split_ratio"])) < 1e-8
        # Independent dictator balances the function and both restrictions.
        balanced = f + [-v for v in f]
        wb = walsh(balanced)
        assert sum(balanced) == 0 and sum(g + [-v for v in g]) == 0
        assert entropy(wb) == entropy(wf)
        assert influence(wb, n) == p and influence(wb) == influence(wf)+1
        rows.append({"base_n": n, "truth_table_size": len(f),
                     "H_F": entropy(wf), "H_g": entropy(wg), "H_h": entropy(wh),
                     "delta": delta, "selector_influence": float(p),
                     "split_ratio": delta/float(p), "tilde": tilde,
                     "remainder": remainder, "global_H_over_I": entropy(wf)/float(influence(wf)),
                     "exact_coefficients_and_influences": "PASS", "balanced_wrapper": "PASS"})

    # Exhaustively test all pairs of 2-variable Boolean restrictions (256 splits).
    worst_bridge_error = 0.0
    max_increment, attained = 0.0, False
    for code_a in range(16):
        a = [1 if code_a & (1 << t) else -1 for t in range(4)]
        wa = walsh(a)
        for code_b in range(16):
            b = [1 if code_b & (1 << t) else -1 for t in range(4)]
            wb = walsh(b)
            d = entropy(walsh(a+b)) - (entropy(wa)+entropy(wb))/2
            t, r, inf = split_terms(wa, wb)
            assert -1e-12 <= d <= 2 + 1e-12
            assert abs(d-t-r) < 1e-12
            assert d <= binary(inf)+(2/math.log(2))*inf+1e-12
            assert r <= (2/math.log(2))*inf+1e-12
            max_increment = max(max_increment, d)
            worst_bridge_error = max(worst_bridge_error, abs(d-t-r))
            attained = attained or (abs(d-2)<1e-12 and abs(inf-.5)<1e-12)
    assert attained and max_increment == 2
    grouped_rows = [grouped(n) for n in [16, 32, 64, 128]]
    elapsed = time.perf_counter() - started
    assert elapsed < gate["max_runtime_seconds"]
    result = {"command": "python -X utf8 verify_boundary.py", "wall_seconds": elapsed,
              "gate": gate, "enumerated_family": rows,
              "grouped_family": grouped_rows,
              "max_family_identity_error": max_error,
              "all_two_variable_restriction_pairs": {"count": 256, "passed": 256,
                "max_identity_error": worst_bridge_error, "sharp_max_increment_bits": max_increment},
              "formal_verification": False, "independent_referee_status": "pending w512"}
    (BASE/"measurements.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    lines = ["Small CPU boundary verification: PASS", f"Runtime: {elapsed:.6f} seconds",
             "n, specified-split ratio, global H/I"]
    lines += [f'{r["base_n"]}, {r["split_ratio"]:.10f}, {r["global_H_over_I"]:.10f}' for r in rows]
    lines += [f'{r["base_n"]}, {float(r["split_ratio"]):.10f}, {float(r["global_H_over_I"]):.10f}'
              for r in result["grouped_family"]]
    lines += [f"Exact Fourier/influence checks: {len(rows)}/{len(rows)} dimensions passed",
              "All 256 Boolean restriction pairs passed the exact identity, [0,2] bound and sharp binary-entropy envelope.",
              f"Maximum entropy identity error: {max(max_error,worst_bridge_error):.3g}",
              "These are mathematical sanity checks, not a proof of full FEI or a novelty certificate."]
    (BASE/"measurements.txt").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
