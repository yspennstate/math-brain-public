"""Exact rational Bernstein certificate for the C010 scaling theorem.

No floating-point computation is used in any assertion.  Polynomials are
dictionaries from three-variable exponent tuples to Fraction coefficients.
"""
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path
import json


def add(p, q):
    ans = p.copy()
    for k, v in q.items():
        ans[k] = ans.get(k, F(0)) + v
    return ans


def mul(p, q):
    ans = {}
    for a, b in p.items():
        for c, d in q.items():
            k = tuple(x + y for x, y in zip(a, c))
            ans[k] = ans.get(k, F(0)) + b * d
    return ans


def power(p, n):
    ans = {(0, 0, 0): F(1)}
    for _ in range(n):
        ans = mul(ans, p)
    return ans


e = {
    (1, 0, 0): F(6, 5),
    (2, 0, 0): F(9, 25),
    (0, 1, 0): F(1),
    (1, 1, 0): F(6, 5),
    (2, 1, 0): F(9, 25),
}
penalty = mul(
    mul(
        power({(0, 0, 0): F(1), (0, 1, 0): F(1, 3)}, 3),
        power({(0, 0, 0): F(1), (1, 0, 0): F(1)}, 2),
    ),
    {(0, 0, 1): F(1)},
)
P = add(power(e, 2), penalty)


def bernstein(radius):
    homogeneous = {}
    unit_sum = {(1, 0, 0): F(1), (0, 1, 0): F(1), (0, 0, 1): F(1)}
    for k, v in P.items():
        degree = sum(k)
        for a, b in power(unit_sum, 6 - degree).items():
            ix = tuple(x + y for x, y in zip(k, a))
            homogeneous[ix] = homogeneous.get(ix, F(0)) + v * radius**degree * b
    # Include zero coefficients, if any.
    out = {}
    for i in range(7):
        for j in range(7 - i):
            k = (i, j, 6 - i - j)
            multinomial = F(factorial(6), prod(factorial(x) for x in k))
            out[k] = homogeneous.get(k, F(0)) / multinomial
    return out


def f(s):
    return s*s * (850 + 645*s + 207*s*s + 27*s*s*s) / 625


def main():
    half = bernstein(F(1, 2))
    two_thirds = bernstein(F(2, 3))
    cap = bernstein(F(27, 40))
    assert max(half.values()) == F(1, 2)
    assert max(two_thirds.values()) == F(368, 375)
    assert two_thirds[(5, 1, 0)] == f(F(2, 3))
    assert cap[(5, 1, 0)] == f(F(27, 40))
    assert f(F(2, 3)) < 1 < f(F(27, 40))
    others_cap = max(v for k, v in cap.items() if k != (5, 1, 0))
    assert others_cap == F(12787546405923, 12800000000000)
    assert others_cap < F(9991, 10000)
    alpha_margin = (1 - F(9991, 10000)) * (1 - F(5, 6)**5)
    assert alpha_margin > F(1, 2000)
    # Rational isolating interval for the single positive root f(alpha)=1.
    left, right = F(2, 3), F(27, 40)
    for _ in range(80):
        middle = (left + right) / 2
        if f(middle) < 1:
            left = middle
        else:
            right = middle
    output = {
        "all_assertions_passed": True,
        "polynomial_coefficients": {str(k): str(v) for k, v in sorted(P.items())},
        "bernstein_at_two_thirds": {str(k): str(v) for k, v in sorted(two_thirds.items())},
        "bernstein_at_27_over_40": {str(k): str(v) for k, v in sorted(cap.items())},
        "max_at_one_half": str(max(half.values())),
        "max_at_two_thirds": str(max(two_thirds.values())),
        "max_other_at_27_over_40": str(others_cap),
        "alpha_margin_lower": str(alpha_margin),
        "alpha_isolation": [str(left), str(right)],
        "alpha_approximation_not_used_in_proof": float((left + right) / 2),
    }
    destination = Path(__file__).with_name("scaling_results.json")
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k not in {
        "polynomial_coefficients", "bernstein_at_two_thirds", "bernstein_at_27_over_40"
    }}, indent=2))


if __name__ == "__main__":
    main()
