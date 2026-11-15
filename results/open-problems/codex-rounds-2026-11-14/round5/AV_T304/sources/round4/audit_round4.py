"""Small exact-arithmetic checks for PROOF.md; Python standard library only."""

from fractions import Fraction as F
from itertools import product


def solve(matrix, rhs):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(matrix, rhs)]
    n = len(a)
    for col in range(n):
        pivot = next(row for row in range(col, n) if a[row][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for row in range(n):
            if row != col:
                scale = a[row][col]
                a[row] = [x - scale * y for x, y in zip(a[row], a[col])]
    return [row[-1] for row in a]


def old_recurrence():
    # New Gaussian completion data: norm(a)=7/25, s=24/25.
    a, s = [F(21, 125), F(28, 125)], F(24, 25)
    p = [[F(i == j) - a[i] * a[j] / (1 + s) for j in range(2)] for i in range(2)]
    for i, j in product(range(2), repeat=2):
        assert sum(p[i][k] * p[j][k] for k in range(2)) + a[i] * a[j] == F(i == j)
    for alpha, expected in [(F(1, 2), F(33, 32)), (F(1, 3), F(73, 72))]:
        residual = 1 - alpha**2 / 2
        by_independent_seeds = alpha**2 / 4 + 3 * alpha**2 / 8 + residual
        by_cross_covariance = 1 + alpha**2 / 8
        assert by_independent_seeds == by_cross_covariance == expected

    # Heterogeneous intrinsic errors on ternary trees; compare exact path sums
    # with a bottom-up evaluation that visits nodes in a different order.
    af, bound_a, k, n, upper_s, dbar = map(F, ['3/4', '2/3', '1/11', '1', '2/5', '7/3'])
    delta_p, loss = F(1, 625), F(5)  # delta=1/625, p=1.
    for height in range(1, 6):
        records = {}

        def grow(path, level):
            coeff = af if level == 1 else bound_a
            weights = [-coeff / 4, coeff / 4, coeff / 2]
            terms = []
            for index, weight in enumerate(weights):
                next_path = path + (index,)
                sigma = n / (2 * af) if level == 1 else upper_s * F(index + 1, 3)
                d_i = dbar * F(index + 1, 3)
                intrinsic = sigma * d_i * delta_p * (1 if level == 1 else loss)
                continues = level < height and (index != 0 or level % 2)
                terms.append((weight, intrinsic, next_path if continues else None))
                if continues:
                    grow(next_path, level + 1)
            records[path] = terms

        grow((), 1)
        bottom_up = {}
        for path in sorted(records, key=len, reverse=True):
            bottom_up[path] = sum(abs(w) * (intrinsic + (k * bottom_up[child] if child is not None else 0))
                                  for w, intrinsic, child in records[path])
        stack, expanded = [((), F(1))], F(0)
        while stack:
            path, scale = stack.pop()
            for weight, intrinsic, child in reversed(records[path]):
                expanded += scale * abs(weight) * intrinsic
                if child is not None:
                    stack.append((child, scale * abs(weight) * k))
        upper = dbar * delta_p * (n / 2 + af * upper_s * loss * sum((k * bound_a)**j for j in range(1, height)))
        assert bottom_up[()] == expanded <= upper
    print('Inherited recheck: new Gaussian data; 33/32 and 73/72 by two methods; unequal ternary trees, heights 1..5: PASS')


def endpoint_quadrature():
    for order in range(3, 9):
        nodes = [F(i, order - 2) for i in range(order - 1)]
        matrix = [[node**j for j in range(order)] for node in nodes]
        matrix.append([F(j == 1) for j in range(order)])
        # Construct every Hermite value-basis polynomial explicitly.
        basis_weights = []
        for column in range(order - 1):
            coeff = solve(matrix, [F(i == column) for i in range(order - 1)] + [F(0)])
            assert coeff[1] == 0
            basis_weights.append(sum(F(j, j - 1) * coeff[j] for j in range(2, order)))
        # Independently solve the moment equations for all admissible monomials.
        powers = [0] + list(range(2, order))
        moment_weights = solve([[node**j for node in nodes] for j in powers],
                               [F(0)] + [F(j, j - 1) for j in powers[1:]])
        assert basis_weights == moment_weights
        assert sum(basis_weights) == 0
        for ell in [F(1, 8), F(1, 32)]:
            for j in range(2, order):
                # Physical integral of derivative(rho^j)/rho on [0,ell].
                direct = F(j, j - 1) * ell**(j - 1)
                quadrature = sum((weight / ell) * (ell * node)**j
                                 for weight, node in zip(basis_weights, nodes))
                assert direct == quadrature
        print(f'Hermite endpoint order {order}: two exact constructions agree; unit weight l1={sum(map(abs, basis_weights))}')


def angle_and_cancellation():
    for order in range(2, 9):
        nodes = list(map(F, range(order)))
        unit = solve([[node**j for node in nodes] for j in range(order)],
                     [F(j == 1) for j in range(order)])
        for psi in [F(1, 16), F(1, 1024)]:
            weights = [value / psi for value in unit]
            for power in range(order):
                assert sum(weight * (psi * node)**power for weight, node in zip(weights, nodes)) == F(power == 1)
    # Expand correction coefficients through either order of scalar operations.
    q, d, w = [F(-2), F(5, 3)], [F(-3), F(3)], [F(7, 5), F(-2, 5)]
    sigma = F(3, 7)
    results = []
    for r in [F(1), F(1, 10**6), F(1, 10**30)]:
        raw = [-F(2, 1) / (r * sigma) * qi * dj * (-r * wk)
               for qi, dj, wk in product(q, d, w)]
        canceled = [F(2, 1) / sigma * qi * dj * wk for qi, dj, wk in product(q, d, w)]
        assert raw == canceled
        results.append(raw)
    assert results[0] == results[1] == results[2]
    print('Angle stencil orders 2..8 exact; coefficient cancellation at r=1, 10^-6, 10^-30: PASS')


def scale_and_exponents():
    for eta in [F(1, 1000), F(1, 10), F(1, 2), F(1)]:
        # Square identities avoid rounding square roots.
        rho_sq = 4 / (4 + eta**2)
        tau_sq = 1 - rho_sq
        assert tau_sq == eta**2 / (4 + eta**2)
        assert tau_sq / rho_sq == eta**2 / 4
        assert tau_sq >= eta**2 / 5
    for k0 in [2, 3, 8, 20]:
        t = F(1, 320 * (k0 + 2))
        w = t / 20
        b = F(1, 2)
        gain = b - 4*t - 10*w
        assert gain > F(63, 128) > F(1, 3)
        assert (b - 6*t - 10*w) - (b - 10*t) > 3*t
        assert (b - 2*t) - (b - 10*t) == 8*t
        assert (b - t) - (b - 10*t) == 9*t
    assert F(1, 2) - 5 * F(1, 640) == F(63, 128)
    assert F(1, 3) - F(1, 4) == F(1, 12)
    print('Scale square identities and lower bounds: PASS')
    print('Exponent checks: 63/128 > 1/3; label slack >3t, 8t, 9t; 1/3-1/4=1/12: PASS')


if __name__ == '__main__':
    old_recurrence()
    endpoint_quadrature()
    angle_and_cancellation()
    scale_and_exponents()
