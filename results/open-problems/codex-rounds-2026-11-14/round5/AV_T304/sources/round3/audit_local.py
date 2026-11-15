"""Exact arithmetic checks for the local identities in PROOF.md."""
from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def gaussian_completion():
    # ||a||=5/13, sqrt(1-||a||^2)=12/13: all entries are rational.
    a = [F(3, 13), F(4, 13)]
    s = F(12, 13)
    p = [[F(i == j) - a[i] * a[j] / (1 + s) for j in range(2)] for i in range(2)]
    u = [p[i] + [-a[i]] for i in range(2)] + [a + [s]]
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    assert multiply(u, transpose(u)) == identity
    pp = multiply(p, transpose(p))
    assert all(
        pp[i][j] + a[i] * a[j] == F(i == j) for i in range(2) for j in range(2)
    )
    print('Gaussian completion: U U^T = I_3; P P^T + aa^T = I_2 (exact)')


def shared_center():
    # Each output is represented by squared contributions of independent Z,G1,G2,R.
    residual = 1 - 2 * F(1, 2) ** 2 * F(1, 2) ** 2
    direct = F(1, 4) ** 2 + 2 * F(3, 64) + residual
    covariance = F(1, 4) ** 2
    second = 1 + 2 * F(1, 2) ** 2 * covariance
    assert residual == F(7, 8)
    assert direct == second == F(33, 32)
    print(f'Shared-center counterexample: residual={residual}; variance={direct} by both methods')


def finite_tree():
    # Compare bottom-up recurrence to explicit path expansion on nonuniform trees.
    af, a, k = F(2, 3), F(3, 5), F(1, 7)
    n, sigma, deeper_sigma = F(1), F(3, 4), F(2, 5)
    delta_p, loss = F(1, 256), F(2)  # delta=1/16, p=2, delta^(-1/4)=2.

    def terms(level, maximum, path):
        bound = af if level == 1 else a
        weights = [bound / 3, -2 * bound / 3]
        for index, weight in enumerate(weights):
            child_path = path + (index,)
            # Unequal branch lengths, retaining a deepest branch.
            continues = level < maximum and not (index == 0 and level % 2 == 0)
            yield weight, child_path, continues

    def recurse(level, maximum, path):
        intrinsic = delta_p * (sigma if level == 1 else deeper_sigma * loss)
        return sum(abs(weight) * (intrinsic + (k * recurse(level + 1, maximum, child_path) if cont else 0))
                   for weight, child_path, cont in terms(level, maximum, path))

    for height in range(1, 7):
        direct = recurse(1, height, ())
        stack, expanded = [(1, (), F(1))], F(0)
        while stack:
            level, path, scale = stack.pop()
            intrinsic = delta_p * (sigma if level == 1 else deeper_sigma * loss)
            for weight, child_path, cont in terms(level, height, path):
                expanded += scale * abs(weight) * intrinsic
                if cont:
                    stack.append((level + 1, child_path, scale * abs(weight) * k))
        bound = delta_p * (n / 2 + af * deeper_sigma * loss * sum((k * a) ** j for j in range(1, height)))
        assert direct == expanded
        assert direct <= bound
    assert F(1, 3) - F(1, 4) == F(1, 12)
    print('Finite-tree recurrence: bottom-up = path expansion <= bound for heights 1 through 6')
    print('Exponent margin: 1/3 - 1/4 = 1/12 (exact)')


if __name__ == '__main__':
    gaussian_completion()
    shared_center()
    finite_tree()
