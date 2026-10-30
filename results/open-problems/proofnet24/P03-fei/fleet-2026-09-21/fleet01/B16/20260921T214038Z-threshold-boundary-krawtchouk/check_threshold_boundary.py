from fractions import Fraction
from math import comb
import json


def K(N, k, j):
    s = 0
    lo = max(0, j - (N - k))
    hi = min(k, j)
    for ell in range(lo, hi + 1):
        s += (-1) ** ell * comb(k, ell) * comb(N - k, j - ell)
    return s


def xlevel(N, a):
    return Fraction((N - 2 * a) ** 2, N * N)


def lam_direct(N, k, a):
    return Fraction(
        sum(K(N, k, j) for j in range(a + 1))
        + sum(K(N, k, j) for j in range(N - a, N + 1)),
        2 ** N,
    )


def lam_boundary(N, k, a):
    if k % 2:
        return Fraction(0)
    return Fraction(2 * K(N - 1, k - 1, a), 2 ** N)


partial = 0
threshold = 0
for N in range(2, 33):
    for k in range(1, N + 1):
        acc = 0
        for a in range(N + 1):
            acc += K(N, k, a)
            rhs = K(N - 1, k - 1, a) if a <= N - 1 else 0
            assert acc == rhs
            partial += 1
    if N % 2 == 0:
        for k in range(1, N + 1):
            for a in range(N // 2):
                assert lam_direct(N, k, a) == lam_boundary(N, k, a)
                threshold += 1


def energy_direct(N, coeff):
    ans = Fraction(0)
    for a in range(N // 2):
        F = sum(Fraction(c) * lam_direct(N, k, a) for k, c in coeff.items())
        ans += (xlevel(N, a) - xlevel(N, a + 1)) * F * F
    return ans


def pow2frac(e):
    return Fraction(2 ** e, 1) if e >= 0 else Fraction(1, 2 ** (-e))


def energy_full(N, coeff):
    factor = pow2frac(3 - 2 * N) / Fraction(N * N)
    ans = Fraction(0)
    for a in range(N):
        P = sum(
            Fraction(c) * K(N - 1, k - 1, a)
            for k, c in coeff.items()
            if k % 2 == 0
        )
        ans += factor * abs(N - 1 - 2 * a) * P * P
    return ans


tests = [
    (8, {4: 1}),
    (8, {4: 2, 6: -1, 8: 3}),
    (10, {2: 1, 4: 1, 6: 1, 8: 1, 10: 1}),
    (16, {4: 3, 8: -2, 12: 1}),
]
energies = []
for N, coeff in tests:
    lhs = energy_direct(N, coeff)
    rhs = energy_full(N, coeff)
    assert lhs == rhs
    energies.append(
        {
            "N": N,
            "coeff": coeff,
            "value": f"{lhs.numerator}/{lhs.denominator}",
        }
    )

assert K(7, 3, 0) == 1
assert K(7, 3, 2) == -3

out = {
    "status": "PASS",
    "partial_sum_integer_identities": partial,
    "threshold_boundary_identities": threshold,
    "energy_identities": energies,
    "sign_change": {
        "N": 8,
        "k": 4,
        "tail_radius_0_lambda": "1/128",
        "tail_radius_2_lambda": "-3/128",
    },
}
print(json.dumps(out, sort_keys=True, indent=2))
