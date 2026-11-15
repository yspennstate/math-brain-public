#!/usr/bin/env python3
"""Audit exhaustive outputs with integer arithmetic and a third small-n method."""
import csv
import json
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def subsequences(word, n):
    """Literal set of all subsequences, with no LCS recurrence."""
    result = {()}
    for i in range(n):
        bit = (word >> i) & 1
        result |= {s + (bit,) for s in result}
    return result


def main():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    primary = [json.loads(s) for s in (ROOT / "results_bits.jsonl").read_text().splitlines()]
    secondary = [json.loads(s) for s in (ROOT / "results_dp.jsonl").read_text().splitlines()]
    assert primary == secondary, "independent enumerations disagree"
    assert [r["n"] for r in primary] == list(range(1, 13))
    summaries, spectra, quadratic = [], [], []
    for r in primary:
        n, total = r["n"], r["pairs"]
        den = total * total
        hist, masses = r["hist"], r["masses"]
        assert total == 4**n == sum(hist)
        sum1 = sum(k * count for k, count in enumerate(hist))
        sum2 = sum(k * k * count for k, count in enumerate(hist))
        assert (sum1, sum2) == (r["sum"], r["sum2"])
        mean = Q(sum1, total)
        # First: raw moments. Second: centered sum over the whole histogram.
        variance = Q(sum2, total) - mean * mean
        centered = sum(count * (Q(k) - mean)**2 for k, count in enumerate(hist)) / total
        assert variance == centered
        assert sum(masses) == total * sum2
        assert all(not masses[k] for k in range(1, 2*n + 1, 2))
        assert variance == Q(sum(masses[1:]), den)
        energy = Q(r["edges"], 2 * total)
        assert energy == Q(sum(k * s for k, s in enumerate(masses)), den)
        remainder = sum(Q(k, 2) * masses[k] - masses[k] for k in range(4, 2*n + 1, 2)) / den
        assert variance == energy / 2 - remainder
        assert variance <= Q(n, 4)
        coeffs = {(i, j): c for i, j, c in r["quadratic"]}
        assert len(coeffs) == n * (2*n - 1)
        assert sum(c*c for c in coeffs.values()) == masses[2]
        assert masses[2] == 2 * r["same_mass"] + r["cross_mass"]
        adjacent = 2 * sum(coeffs[i, i+1] for i in range(n - 1))
        assert adjacent == r["adjacent"]
        derivative = Q(adjacent, total)
        markov_lower = Q(adjacent * adjacent, 2 * (n - 1) * den) if n > 1 else Q(0)
        same_lower = Q(2 * r["same_mass"], den)
        word_lower = 2 * (Q(r["conditional_sum_squares"], 2**(3*n)) - mean*mean)
        w2 = Q(masses[2], den)
        assert 0 <= markov_lower <= same_lower <= word_lower <= variance
        assert same_lower <= w2 <= variance
        # Small-n independent check: literal subsequence intersection and direct
        # character sums, with no dynamic programming or fast Walsh transform.
        if n <= 5:
            words = 2**n
            sets = [subsequences(x, n) for x in range(words)]
            scores = [max(map(len, sets[x] & sets[y]))
                      for y in range(words) for x in range(words)]
            hist3 = [scores.count(k) for k in range(n + 1)]
            assert hist3 == hist
            direct_masses = [0] * (2*n + 1)
            for mask in range(total):
                coefficient = sum(score * (-1 if (z & mask).bit_count() % 2 else 1)
                                  for z, score in enumerate(scores))
                direct_masses[mask.bit_count()] += coefficient * coefficient
                if mask.bit_count() == 2:
                    i, j = [k for k in range(2*n) if mask >> k & 1]
                    assert coefficient == coeffs[i, j]
            assert direct_masses == masses
        summaries.append(dict(n=n, pairs=total, mean=str(mean), variance=str(variance),
                              variance_over_n=str(variance/n), W2=str(w2),
                              W2_fraction_of_variance=str(w2/variance),
                              same_word_quadratic_lower=str(same_lower),
                              conditional_word_lower=str(word_lower),
                              markov_derivative=str(derivative),
                              markov_lower=str(markov_lower), energy=str(energy)))
        for k, mass in enumerate(masses):
            spectra.append(dict(n=n, degree=k, square_sum=mass,
                                denominator=den, mass=str(Q(mass, den))))
        for (i, j), c in coeffs.items():
            quadratic.append(dict(n=n, i=i+1, j=j+1, numerator=c,
                                  denominator=total, coefficient=str(Q(c, total))))
        print(f"n={n:2d} pairs={total:8d} variance={float(variance):.10f} "
              f"W2/variance={float(w2/variance):.8f} "
              f"Markov_derivative/n={float(derivative/n):.8f} PASS")
    for filename, rows in [("summary.csv", summaries), ("spectrum.csv", spectra),
                           ("quadratic.csv", quadratic)]:
        with (ROOT / filename).open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    report = dict(verdict="PASS", exhaustive_independent_methods_max_n=12,
                  direct_subsequence_and_character_sums_max_n=5,
                  total_pairs_per_method=sum(r["pairs"] for r in primary),
                  checks=["identical independent enumeration outputs", "histogram moments",
                          "centered moments", "Parseval", "zero odd Walsh degrees",
                          "direct cube edges vs spectral energy", "exact remainder",
                          "n/4 upper bound", "all quadratic coefficients",
                          "direct adjacent statistic vs Walsh coefficients",
                          "conditional-word lower bound", "Markov lower bound"])
    (ROOT / "audit.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
