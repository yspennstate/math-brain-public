"""Exact finite checks of the improved antichain rank lemma.

Enumerate every nonempty antichain in the N-cube and every +/- signing,
for 0 <= N <= 4.  The unnormalized Walsh transform is integral, so both
the noise-mask and harmonic-rank inequalities are checked by integer
cross-multiplication.  Floating point is used only for printed constants.
"""

from itertools import product
from math import comb, e, gcd, log, log2, pi
import json


def fwht_integer(values):
    result = list(values)
    half = 1
    while half < len(result):
        for start in range(0, len(result), 2 * half):
            for j in range(start, start + half):
                x, y = result[j], result[j + half]
                result[j], result[j + half] = x + y, x - y
        half *= 2
    return result


def nonempty_antichains(n):
    size = 1 << n
    comparable = []
    for x in range(size):
        comparable.append(sum(
            1 << y for y in range(size)
            if y != x and ((x & y) == x or (x & y) == y)
        ))
    for mask in range(1, 1 << size):
        work = mask
        support = []
        while work:
            bit = work & -work
            x = bit.bit_length() - 1
            if comparable[x] & mask:
                break
            support.append(x)
            work ^= bit
        else:
            yield support


def main():
    dimension_records = []
    cases = 0
    mask_checks = 0
    harmonic_checks = 0
    equality_cases = 0
    for n in range(5):
        size = 1 << n
        degree = [x.bit_count() for x in range(size)]
        lcm = 1
        for j in range(1, n + 1):
            lcm = lcm * j // gcd(lcm, j)
        harmonic_numerators = [0]
        for j in range(1, n + 1):
            harmonic_numerators.append(harmonic_numerators[-1] + lcm // j)
        # sum_{q=1}^n c_q/q, with common denominator 2^n*lcm.
        sperner_numerator = sum(
            comb(q, q // 2) * (1 << (n - q)) * (lcm // q)
            for q in range(1, n + 1)
        )
        count_supports = 0
        count_signings = 0
        for support in nonempty_antichains(n):
            count_supports += 1
            mass = len(support)
            for signs in product((-1, 1), repeat=mass):
                d = [0] * size
                for x, sign in zip(support, signs):
                    d[x] = sign
                walsh = fwht_integer(d)
                squares = [coefficient * coefficient for coefficient in walsh]
                assert sum(squares) == size * mass, (n, support, signs, "Parseval")

                for q in range(n + 1):
                    spectral_sum = sum(
                        value * comb(n - k, q)
                        for value, k in zip(squares, degree) if n - k >= q
                    )
                    lhs = (1 << q) * spectral_sum
                    rhs = size * mass * comb(n, q) * comb(q, q // 2)
                    assert lhs <= rhs, (n, support, signs, q, lhs, rhs)
                    mask_checks += 1

                cost_numerator = (
                    harmonic_numerators[n] * size * mass
                    - sum(value * harmonic_numerators[k]
                          for value, k in zip(squares, degree))
                )
                rhs = mass * sperner_numerator
                assert cost_numerator <= rhs, (
                    n, support, signs, cost_numerator, rhs
                )
                equality_cases += cost_numerator == rhs
                harmonic_checks += 1
                count_signings += 1
                cases += 1
        dimension_records.append({
            "predecessor_dimension": n,
            "nonempty_antichain_supports": count_supports,
            "signed_antichain_cases": count_signings,
        })
    result = {
        "arithmetic": "integer cross-multiplication; no numerical tolerance",
        "dimensions": dimension_records,
        "signed_antichain_cases": cases,
        "exact_noise_mask_checks": mask_checks,
        "exact_harmonic_rank_checks": harmonic_checks,
        "harmonic_equality_cases": equality_cases,
        "constants": {
            "single_rank": 1 + log(2),
            "level_entropy": log2(4 + e),
            "regular_fei": log2(4 + e) + 2 * log2(e * pi),
            "regular_variance_deficit": 4 * (log2(4 + e) + 2 * log2(e * pi)),
        },
        "status": "all exact checks passed",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
