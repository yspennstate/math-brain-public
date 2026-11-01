from fractions import Fraction
from itertools import product

PERMS = [
    (0, 1, 2),  # e
    (1, 0, 2),  # (12)
    (2, 1, 0),  # (13)
    (0, 2, 1),  # (23)
    (1, 2, 0),  # (123)
    (2, 0, 1),  # (132)
]


def matrix_from_weights(weights):
    R = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    for w, p in zip(weights, PERMS):
        for i, j in enumerate(p):
            R[i][j] += w
    return R


def interval(R):
    L = max(Fraction(0), R[2][2] - R[0][1], R[1][1] - R[0][2])
    U = min(R[0][0], R[1][1], R[2][2])
    return L, U


def weights_at(R, t):
    return [
        t,
        R[2][2] - t,
        R[1][1] - t,
        R[0][0] - t,
        R[0][1] - R[2][2] + t,
        R[0][2] - R[1][1] + t,
    ]


def m_values(K):
    answer = []
    for p in PERMS:
        xs = [K[i][p[i]] for i in range(3)]
        prod_x = xs[0] * xs[1] * xs[2]
        answer.append(Fraction(0) if prod_x >= 0 else min(abs(x) for x in xs))
    return answer


def payment(R, m, t):
    return sum(w * x for w, x in zip(weights_at(R, t), m))


def check_reconstruction():
    cases = [
        [Fraction(1, 6)] * 6,
        [Fraction(3, 10), Fraction(1, 10), Fraction(1, 5), Fraction(1, 10), Fraction(1, 10), Fraction(1, 5)],
        [Fraction(4, 5), Fraction(0), Fraction(0), Fraction(0), Fraction(1, 5), Fraction(0)],
    ]
    for original in cases:
        R = matrix_from_weights(original)
        L, U = interval(R)
        assert L <= U
        for t in (L, U, (L + U) / 2):
            recovered = weights_at(R, t)
            assert all(x >= 0 for x in recovered)
            assert sum(recovered) == 1
            assert matrix_from_weights(recovered) == R
    return cases


def check_endpoint_minimum(cases):
    K = [
        [Fraction(2), Fraction(-3), Fraction(5)],
        [Fraction(7), Fraction(11), Fraction(-13)],
        [Fraction(-17), Fraction(19), Fraction(23)],
    ]
    m = m_values(K)
    for original in cases:
        R = matrix_from_weights(original)
        L, U = interval(R)
        endpoint_min = min(payment(R, m, L), payment(R, m, U))
        grid_min = min(payment(R, m, L + (U - L) * Fraction(k, 100)) for k in range(101))
        assert endpoint_min == grid_min


def check_sign_parity():
    counts = set()
    for signs in product((1, -1), repeat=9):
        S = [signs[3 * i:3 * i + 3] for i in range(3)]
        negative = 0
        total_product = 1
        for p in PERMS:
            s = 1
            for i, j in enumerate(p):
                s *= S[i][j]
            total_product *= s
            negative += int(s < 0)
        assert total_product == 1
        counts.add(negative)
    assert counts == {0, 2, 4, 6}
    return counts


if __name__ == "__main__":
    cases = check_reconstruction()
    check_endpoint_minimum(cases)
    counts = check_sign_parity()
    print("PASS: exact 3x3 Birkhoff interval reconstruction")
    print("PASS: parity-payment minimum occurs at an endpoint")
    print("PASS: nonzero transversal negative counts =", sorted(counts))
