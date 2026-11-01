"""Exact combinatorial coefficients and numeric entropy for the obstruction."""
import json
import math
from fractions import Fraction
from pathlib import Path
from decimal import Decimal, getcontext

getcontext().prec = 100
LN2 = Decimal(2).ln()


def exact_float(fraction):
    return Decimal(fraction.numerator) / fraction.denominator


def binary_entropy_exact(prob):
    if prob == 0 or prob == 1:
        return Decimal(0)
    x = exact_float(prob)
    return -(x * x.ln() + (1 - x) * (1 - x).ln()) / LN2


def entropy_term(prob):
    return -float(prob) * math.log2(float(prob)) if prob else 0.


results = []
direct_checks = 0
for N in range(3, 82, 2):
    d = (N - 1) // 2
    alpha = Fraction(1, 2 ** N)
    full_entropy = minus_entropy = plus_entropy = 0.
    minimum_coefficient = None
    if N <= 11:
        majority = [1 if 2 * i.bit_count() > N else -1 for i in range(1 << N)]
        walsh = majority.copy()
        step = 1
        while step < len(walsh):
            for offset in range(0, len(walsh), 2 * step):
                for j in range(step):
                    a, b = walsh[offset + j], walsh[offset + j + step]
                    walsh[offset + j], walsh[offset + j + step] = a + b, a - b
            step *= 2
        for subset, value in enumerate(walsh):
            k = subset.bit_count()
            ell = (k - 1) // 2
            formula = ((-1) ** ell * Fraction(math.comb(2 * d, d), 4 ** d) * Fraction(math.comb(d, ell), math.comb(2 * d, 2 * ell))) if k % 2 else Fraction(0)
            assert Fraction((-1) ** k * value, 1 << N) == formula
        w = N + 1
        for z in [-1, 1]:
            for i, g_value in enumerate(majority):
                score = w * z + 2 * i.bit_count() - N
                encoded = -1 if score < -w else 1 if score < 2 else -1 if score < w else 1
                expected = 1 if z == 1 and i == 0 else g_value
                assert encoded == expected
                direct_checks += 1
    for k in range(N + 1):
        if k % 2:
            ell = (k - 1) // 2
            g = (-1) ** ell * Fraction(math.comb(2 * d, d), 4 ** d) * Fraction(math.comb(d, ell), math.comb(2 * d, 2 * ell))
            minimum_coefficient = min(abs(g), minimum_coefficient) if minimum_coefficient is not None else abs(g)
        else:
            g = Fraction(0)
        b = (-1) ** k * alpha
        a = g + b
        multiplicity = math.comb(N, k)
        full_entropy += multiplicity * (entropy_term(a * a) + entropy_term(b * b))
        minus_entropy += multiplicity * entropy_term(g * g)
        plus_entropy += multiplicity * entropy_term((g + 2 * b) ** 2)
    # Avoid catastrophic cancellation of whole-function entropies when alpha
    # is tiny: sum the exact local coefficient-pair entropy increments.
    local_delta = Decimal(0)
    for k in range(N + 1):
        ell = (k - 1) // 2
        g = ((-1) ** ell * Fraction(math.comb(2 * d, d), 4 ** d) * Fraction(math.comb(d, ell), math.comb(2 * d, 2 * ell))) if k % 2 else Fraction(0)
        b = (-1) ** k * alpha
        a = g + b
        P = a * a + b * b
        q, r = b * b / P, (a + b) ** 2 / (2 * P)
        local_delta += math.comb(N, k) * exact_float(P) * (1 + binary_entropy_exact(q) - binary_entropy_exact(r))
    lower_coefficient = Fraction(1, 2 ** d * N * (d + 1))
    assert minimum_coefficient >= lower_coefficient
    if N >= 15:
        assert minimum_coefficient >= 2 * alpha
    ratio = float(local_delta / exact_float(alpha))
    lower_ratio = (N + 3) / 2 - math.log2(N * (N + 1) / 2)
    upper_ratio = 2 * (N + math.log2(math.e))
    if N >= 15:
        assert ratio >= lower_ratio - 1e-8, (N, ratio, lower_ratio)
    assert ratio <= upper_ratio + 1e-8
    if N <= 25:
        assert abs(full_entropy - (minus_entropy + plus_entropy) / 2 - float(local_delta)) < 1e-12
    results.append({"N": N, "alpha": float(alpha), "split_increment_over_alpha": ratio,
                    "proved_lower_ratio": lower_ratio, "proved_upper_ratio": upper_ratio})

report = {"status": "all assertions passed", "scope": "finite check of exact coefficient formulas; analytic asymptotic proof separate",
          "cases": len(results), "direct_encoded_truth_checks": direct_checks, "results": results}
Path(__file__).with_name("three_crossing_obstruction_checks.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": report["status"], "cases": len(results), "first": results[0], "last": results[-1]}, indent=2))
