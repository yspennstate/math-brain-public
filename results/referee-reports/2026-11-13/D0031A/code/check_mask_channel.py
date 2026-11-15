"""Exact finite checks for the masking-channel lemma in REPORT.md.

No process construction or numerical test of asymptotic mixing is claimed.
Standard library only; one thread; all probabilities use Fraction.
"""

from fractions import Fraction
from itertools import product
import json
from math import comb
import os
from pathlib import Path


def prod(values):
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def check(m, r):
    signs = list(product((-1, 1), repeat=m))
    # Distribution of D = V*U = Z*E, with Z a uniform sign.
    noise = {}
    error = Fraction(0)
    posterior_min = Fraction(1)
    for d in signs:
        plus = prod((1 + r * bit) / 2 for bit in d) / 2
        minus = prod((1 - r * bit) / 2 for bit in d) / 2
        noise[d] = plus + minus
        error += min(plus, minus)
        posterior_min = min(posterior_min, plus / (plus + minus), minus / (plus + minus))
    assert sum(noise.values()) == 1
    eigenvalues = []
    for mask in range(1 << m):
        eigenvalue = sum(
            (prob * prod(d[i] for i in range(m) if mask & (1 << i))
             for d, prob in noise.items()), Fraction(0)
        )
        degree = mask.bit_count()
        expected = r ** degree if degree % 2 == 0 else Fraction(0)
        assert eigenvalue == expected
        if mask:
            eigenvalues.append(abs(eigenvalue))
    rho = max(eigenvalues)
    assert rho == (r * r if m >= 2 else 0)
    assert 0 < error <= Fraction(1, 2)
    assert posterior_min > 0
    # Independent calculation: majority vote on the biased signs, with half
    # an error on ties. This does not use the joint-table enumeration above.
    wrong = (1 - r) / 2
    binomial_error = sum(
        (Fraction(comb(m, k)) * wrong ** k * (1 - wrong) ** (m - k)
         * (1 if 2 * k > m else Fraction(1, 2) if 2 * k == m else 0)
         for k in range(m + 1)), Fraction(0)
    )
    assert error == binomial_error
    return {
        "M": m, "r": str(r), "rho": str(rho),
        "Bayes_error": str(error), "smallest_posterior": str(posterior_min),
    }


if __name__ == "__main__":
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 10, priority
    results = [check(m, r) for r in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
               for m in range(1, 7)]
    output = {"nice": priority, "cases": len(results), "results": results}
    target = Path(__file__).resolve().parent / "mask_channel_results.json"
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Verified {len(results)} exact finite cases; nice={priority}.")
    for row in results:
        if row["r"] == "1/2":
            print(row)
