from fractions import Fraction
import random


def mat_vec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def quad(A, x):
    return dot(x, mat_vec(A, x))


def check_translation_identity():
    rng = random.Random(20260922)
    trials = 1000
    for n in range(1, 8):
        for _ in range(trials // 7):
            A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    z = Fraction(rng.randrange(-7, 8), rng.randrange(1, 6))
                    A[i][j] = A[j][i] = z
            y = [Fraction(rng.randrange(-9, 10), rng.randrange(1, 6)) for _ in range(n)]
            m = [Fraction(rng.randrange(-9, 10), rng.randrange(1, 6)) for _ in range(n)]
            c = Fraction(rng.randrange(-9, 10), rng.randrange(1, 6))
            b = mat_vec(A, m)
            x = [y[i] + m[i] for i in range(n)]
            affine = quad(A, y) + 2 * dot(b, y) + c
            homogeneous_shifted = quad(A, x) + c - quad(A, m)
            assert affine == homogeneous_shifted
    return trials


def check_range_warning():
    # A=diag(1,0): translations produce vectors (m_1,0), never (0,1).
    A = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    for m1 in range(-10, 11):
        for m2 in range(-10, 11):
            assert mat_vec(A, [Fraction(m1), Fraction(m2)]) != [Fraction(0), Fraction(1)]


if __name__ == "__main__":
    trials = check_translation_identity()
    check_range_warning()
    print("STATUS=PASS")
    print(f"exact_translation_trials={trials}")
    print("singular_range_guard=PASS")

