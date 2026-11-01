"""Finite CPU-only checks of w505's restriction obstruction; no live brain access."""
from __future__ import annotations
import argparse
import json
import math
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def phi(p):
    return -p * math.log2(p) if p else 0.0

def entropy(spectrum):
    return math.fsum(phi(float(a * a)) for a in spectrum)

def walsh(values):
    """Exact integer transform followed by rational normalization."""
    out = list(values)
    stride = 1
    while stride < len(out):
        for start in range(0, len(out), 2 * stride):
            for j in range(start, start + stride):
                a, b = out[j], out[j + stride]
                out[j], out[j + stride] = a + b, a - b
        stride *= 2
    return [Fraction(a, len(values)) for a in out]

def direct_walsh(values):
    return [Fraction(sum(v * (-1 if (s & x).bit_count() % 2 else 1)
                         for x, v in enumerate(values)), len(values))
            for s in range(len(values))]

def influence(spectrum, coord=None):
    return sum(a * a * (s.bit_count() if coord is None else bool(s & (1 << coord)))
               for s, a in enumerate(spectrum))

def split(values, i):
    n = len(values).bit_length() - 1
    sides = [[], []]
    for k in range(1 << (n - 1)):
        low = k & ((1 << i) - 1)
        x = low | ((k >> i) << (i + 1))
        sides[0].append(values[x])
        sides[1].append(values[x | (1 << i)])
    return sides

def split_metrics(values, i):
    spectrum = walsh(values)
    left, right = split(values, i)
    ls, rs = walsh(left), walsh(right)
    delta = entropy(spectrum) - (entropy(ls) + entropy(rs)) / 2
    charge = influence(spectrum, i)
    assert influence(spectrum) == charge + (influence(ls) + influence(rs)) / 2
    increment_terms = []
    for p, q in zip(ls, rs):
        a, b = float((p + q) / 2), float((p - q) / 2)
        r = a*a + b*b
        if not r:
            continue
        w, t = b*b/r, 2*a*b/r
        h = phi(w) + phi(1-w)
        j = 1 - phi((1+t)/2) - phi((1-t)/2)
        increment_terms.append(r * (h + j))
    assert abs(delta - math.fsum(increment_terms)) < 1e-10
    assert delta >= -1e-10
    q = float(charge)
    assert delta <= phi(q) + phi(1-q) + 4*q*(1-q) + 1e-10
    return delta, charge

def analytic(m):
    a, n = 1 << m, 1 << (2*m)
    plus, minus = (n+a)//2, (n-a)//2
    hf = plus*phi((a-1)**2/n**2) + minus*phi((a+1)**2/n**2) + n*phi(1/n**2)
    hm = plus*phi((a-2)**2/n**2) + minus*phi((a+2)**2/n**2)
    delta = hf - (2*m+hm)/2
    rho, d = 1/n, 1/a
    psi = lambda u: u*u*math.log2(u)
    base_delta = 2-m*rho-(psi(1-d)+psi(1+d))/2
    return {"m": m, "base_dimension": 2*m, "dimension": 2*m+1,
            "N": n, "I_selector": 1/n, "H_full": hf, "H_minus": hm,
            "delta_selector": delta, "delta_over_selector_influence": delta*n,
            "proved_ratio_lower_bound": math.log2((a-1)**2+1),
            "I_full": m+(2*m+1)/n, "H_over_I": hf/(m+(2*m+1)/n),
            "base_coordinate_delta_formula": base_delta,
            "base_coordinate_delta_upper_bound": 2-m*rho,
            "base_coordinate_ratio_formula": base_delta/(0.5+rho)}

def family_values(m):
    n, mask = 1 << (2*m), (1 << m)-1
    base = [-1 if (((x & mask) & (x >> m)).bit_count() % 2) else 1 for x in range(n)]
    flipped = base.copy()
    flipped[0] = -1
    return base, flipped, base+flipped

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True, choices=["cpu20s-n9"])
    args = ap.parse_args()
    started = time.monotonic()
    gate = {"gate": args.gate, "max_seconds": 20, "max_truth_table_points": 512,
            "enumeration_max_dimension": 3, "gpu": False, "training": False,
            "live_store_access": False}
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2)+"\n", encoding="utf-8")
    def deadline():
        if time.monotonic()-started > 20:
            raise TimeoutError("CPU gate expired; no additional cases permitted")
    rows = []
    truth_checks = []
    for m in range(1, 9):
        deadline()
        row = analytic(m)
        assert row["delta_over_selector_influence"] + 1e-9 >= row["proved_ratio_lower_bound"]
        assert row["H_full"] <= 2*row["I_full"] + 1e-10
        assert row["base_coordinate_delta_formula"] <= row["base_coordinate_delta_upper_bound"] + 1e-10
        assert row["base_coordinate_ratio_formula"] < 4
        rows.append(row)
        if m <= 4:
            base, flipped, full = family_values(m)
            assert set(full) <= {-1, 1}
            bs, fs, fulls = walsh(base), walsh(flipped), walsh(full)
            assert sum(t*t for t in fulls) == 1
            n = len(base)
            assert all(abs(t) == Fraction(1, 1 << m) for t in bs)
            assert sum(t > 0 for t in bs) == (n+(1 << m))//2
            assert fs == [t-Fraction(2, n) for t in bs]
            assert fulls[:n] == [t-Fraction(1, n) for t in bs]
            assert fulls[n:] == [Fraction(1, n)]*n
            assert influence(fulls, 2*m) == Fraction(1, n)
            assert influence(fulls) == Fraction(m) + Fraction(2*m+1, n)
            if m <= 3:
                assert fulls == direct_walsh(full)
            delta, charge = split_metrics(full, 2*m)
            assert abs(delta-row["delta_selector"]) < 1e-10
            coords = [split_metrics(full, i) for i in range(2*m+1)]
            for d, q in coords[:2*m]:
                assert q == Fraction(1, 2)+Fraction(1, n)
                assert abs(d-row["base_coordinate_delta_formula"]) < 1e-10
            truth_checks.append({"m": m, "points": len(full), "exact_walsh_and_influence": True,
                                 "direct_character_sum_checked": m <= 3,
                                 "best_coordinate_ratio": min(d/float(q) for d, q in coords if q),
                                 "selector_ratio": delta/float(charge)})
        (ROOT/"measurements.json").write_text(json.dumps({"gate": gate, "family": rows,
            "truth_table_checks": truth_checks, "complete": False}, indent=2)+"\n", encoding="utf-8")
    worst_best = -1.0
    checked = 0
    for n in range(1, 4):
        for truth in range(1 << (1 << n)):
            deadline()
            values = [1 if truth & (1 << x) else -1 for x in range(1 << n)]
            metrics = [split_metrics(values, i) for i in range(n)]
            candidates = [d/float(q) for d, q in metrics if q]
            if candidates:
                worst_best = max(worst_best, min(candidates))
            checked += 1
    result = {"gate": gate, "family": rows, "truth_table_checks": truth_checks,
              "exhaustive_boolean_functions_checked": checked,
              "max_best_coordinate_ratio_n_le_3": worst_best,
              "seconds": time.monotonic()-started, "complete": True,
              "interpretation": "Finite corroboration only; analytic proof is in ATTEMPT.md; no FEI proof."}
    (ROOT/"measurements.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"complete": True, "truth_table_families": len(truth_checks),
          "functions_checked": checked, "m1_ratio": rows[0]["delta_over_selector_influence"],
          "m8_ratio": rows[-1]["delta_over_selector_influence"],
          "max_best_coordinate_ratio_n_le_3": worst_best, "seconds": result["seconds"]}))

if __name__ == "__main__":
    main()
