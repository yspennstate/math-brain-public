"""Reproducible diagnostics for worker 051's Gaussian risk envelope.

Standard library only. Rational identities are exact. Decimal roots are
high-precision diagnostics, not a substitute for the analytic proof.
"""

from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def odd_double_factorial(m):
    answer = 1
    for k in range(1, m + 1, 2):
        answer *= k
    return answer


def centered_square_moment(k):
    from math import comb
    return sum(
        comb(k, j) * (-1) ** (k - j) * odd_double_factorial(2 * j - 1)
        for j in range(k + 1)
    )


def partitions(n, upper=None):
    if n == 0:
        yield ()
        return
    if upper is None:
        upper = n
    for first in range(min(n, upper), 1 - 1, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def polynomial_product(weights):
    coefficients = [Fraction(1)]
    for weight in weights:
        enlarged = [Fraction(0)] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            enlarged[i] += coefficient
            enlarged[i + 1] += 2 * weight * coefficient
        coefficients = enlarged
    return coefficients


def laplace_quantile(delta):
    # Unique theta in (0,1) with theta exp(1-theta) = delta**2.
    # Bisection chooses the principal Lambert-W branch without evaluating W.
    lower, upper = Decimal(0), Decimal(1)
    for _ in range(260):
        middle = (lower + upper) / 2
        if middle * (1 - middle).exp() < delta * delta:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def main():
    root = Path(__file__).resolve().parents[1]
    source_hashes = {
        name: sha256((root / name).read_bytes()).hexdigest()
        for name in ("agents/003.md", "computations/003_sources/P23.md")
    }
    moment2 = centered_square_moment(2)
    moment4 = centered_square_moment(4)
    assert (moment2, moment4) == (2, 60)
    count = 0
    for denominator in range(1, 17):
        for parts in partitions(denominator):
            weights = [Fraction(part, denominator) for part in parts]
            coefficients = polynomial_product(weights)
            assert coefficients[:2] == [1, 2]
            assert all(coefficient >= 0 for coefficient in coefficients[2:])
            s2 = sum(weight**2 for weight in weights)
            s4 = sum(weight**4 for weight in weights)
            # Independently expand the fourth centered moment using independence.
            expanded_fourth = 60 * s4 + 24 * sum(
                weights[i]**2 * weights[j]**2
                for i in range(len(weights))
                for j in range(i)
            )
            assert expanded_fourth == 12 * s2**2 + 48 * s4
            assert expanded_fourth <= 60 * s2**2
            assert max(weights)**2 <= s2 <= max(weights)
            count += 1
    rows = []
    with localcontext() as context:
        context.prec = 80
        constant = Decimal(12103) / 50000
        for delta_text in ("0.5", "0.2", "0.1", "0.05", "0.01"):
            delta = Decimal(delta_text)
            theta = laplace_quantile(delta)
            residual = theta * (1 - theta).exp() - delta**2
            assert abs(residual) < Decimal("1e-74")
            optimizer = (1 / theta - 1) / 2
            # Check both the stationary point and optimized objective numerically.
            assert abs(theta - 1 / (1 + 2 * optimizer)) < Decimal("1e-74")
            objective = (optimizer * theta).exp() / (1 + 2 * optimizer).sqrt()
            assert abs(objective - delta) < Decimal("1e-70")
            rows.append({
                "failure_probability": delta_text,
                "theta_delta": format(theta, ".20f"),
                "c_times_theta_delta": format(constant * theta, ".20f"),
                "simple_c_delta_squared_over_e": format(
                    constant * delta**2 / Decimal(1).exp(), ".20f"
                ),
                "absolute_root_residual": str(abs(residual)),
            })
        theta = Decimal("0.5")
        laplace_failure_at_half_mean = (theta * (1 - theta).exp()).sqrt()
        cantelli_failure_at_half_mean = 2 / (2 + (1 - theta)**2)
    data = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_sha256": source_hashes,
        "exact_centered_chi_square_moments": {"second": moment2, "fourth": moment4},
        "exact_normalized_rational_spectra_checked": count,
        "quantile_rows_diagnostic_only": rows,
        "half_mean_failure_bounds": {
            "laplace": str(laplace_failure_at_half_mean),
            "cantelli": str(cantelli_failure_at_half_mean),
        },
        "exact_95_percent_simple_threshold": str(Fraction(12103, 60000000)),
        "limitations": [
            "No actual P23 kernel matrices are sampled or spectrally estimated.",
            "Finite rational checks do not prove the all-spectra inequality.",
            "The analytic report supplies the all-spectra proofs.",
            "The optimized Chernoff envelope is not asserted to be the exact extremal CDF.",
        ],
    }
    output = root / "computations/051_quantile_checks.json"
    output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
