"""Exact certificates for C003; Python 3 standard library only.

The general proof is in agents/C003.md. Finite evaluations independently check
the atom/Fisher formulas. Polynomial arithmetic verifies the determinant
factorization used in the positive matrix integral. No floating point is used.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def determinant(a):
    if not a:
        return Q(1)
    return sum(((-1) ** j) * a[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in a[1:]])
        for j in range(len(a)))


def inverse(a):
    n = len(a)
    b = [list(row) + [Q(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j])
        b[j], b[k] = b[k], b[j]
        d = b[j][j]
        b[j] = [v / d for v in b[j]]
        for i in range(n):
            if i != j:
                d = b[i][j]
                b[i] = [v - d * w for v, w in zip(b[i], b[j])]
    return [row[n:] for row in b]


def atoms(s):
    K = [[Q(1, 2), s, Q(0)], [s, Q(1, 2), s],
         [Q(0), s, Q(1, 2)]]
    p = []
    for mask in range(8):
        x = [(mask >> i) & 1 for i in range(3)]
        a = [[K[i][j] - Q(i == j and not x[i])
              for j in range(3)] for i in range(3)]
        p.append((-1) ** (3 - sum(x)) * determinant(a))
    return K, p


samples = [Q(0), Q(1, 10), Q(1, 5), Q(1, 3), Q(7, 20), Q(707, 2000)]
for s in samples:
    x = 8 * s * s
    check(0 <= x < 1)
    K, p = atoms(s)
    expected = [Q(1, 8)] * 8
    expected[0] = expected[7] = (1 - x) / 8
    expected[2] = expected[5] = (1 + x) / 8
    check(p == expected)
    check(sum(p) == 1 and min(p) > 0)
    deriv = [[(2 * ((mask >> i) & 1) - 1) *
              (p[mask] + p[mask ^ (1 << i)])
              for i in range(3)] for mask in range(8)]
    J = [[sum(deriv[m][i] * deriv[m][j] / p[m] for m in range(8))
          for j in range(3)] for i in range(3)]
    B = x * x * (2 - x * x) / (2 * (1 - x * x))
    f = x * (2 - x * x) / (1 - x * x)
    D = 2 * x * x / (1 - x * x)
    expected_J = [[4 + B, f, B], [f, 4 + D, f], [B, f, 4 + B]]
    for i in range(3):
        for j in range(3):
            check(J[i][j] == expected_J[i][j])
    for i, j in [(0, 1), (1, 2), (0, 2)]:
        other = 3 - i - j
        for bit in [0, 1]:
            m = bit << other
            d, b, c, e = (p[m], p[m | (1 << i)],
                          p[m | (1 << j)], p[m | (1 << i) | (1 << j)])
            check(d + b + c + e == Q(1, 2))
            target = 1 / (1 - x * x) if (i, j) == (0, 2) else (1 + x) / (1 - x)
            check(b * c / (d * e) == target)
    Sigma = [[Q(1, 4) if i == j else -K[i][j] ** 2
              for j in range(3)] for i in range(3)]
    invSigma = inverse(Sigma)
    check(sum(sum(row) for row in invSigma) == 8 * (3 + 2 * x) / (2 - x * x))
    ImK = [[Q(i == j) - K[i][j] for j in range(3)] for i in range(3)]
    inv = inverse(ImK)
    L = [[inv[i][j] - Q(i == j) for j in range(3)] for i in range(3)]
    expected_L = [[1, 4 * s, x], [4 * s, 1 + x, 4 * s], [x, 4 * s, 1]]
    for i in range(3):
        for j in range(3):
            check(L[i][j] == expected_L[i][j] / (1 - x))


# Polynomial coefficients in ascending order, exact arithmetic.
def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(n)])


def scale(a, c):
    return trim([c * v for v in a])


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return trim(c)


def diff(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


X = [0, 1]
X2 = mul(X, X)
X4 = mul(X2, X2)
den = add([1], scale(X2, -1))
den2 = mul(den, den)

# Derivative numerators of P, D and q, all over (1-x^2)^2.
# P=x^2+x^2/(1-x^2)+log(1-x^2).
Pprime = add(add(mul(diff(X2), den2),
                  add(mul(diff(X2), den), scale(mul(X2, diff(den)), -1))),
             mul(diff(den), den))
Ptarget = scale(mul(X, add(add([1], scale(X2, -1)), X4)), 2)
check(Pprime == Ptarget)
# D=2x^2/(1-x^2).
Dprime = scale(add(mul(diff(X2), den), scale(mul(X2, diff(den)), -1)), 2)
check(Dprime == scale(X, 4))
# q=x+x/(1-x^2)-log((1+x)/(1-x)); log derivative=2/(1-x^2).
qprime = add(add(den2, add(den, scale(mul(X, diff(den)), -1))), scale(den, -2))
check(qprime == mul(X2, add([1], X2)))
det_numerator = add(mul(Pprime, Dprime), scale(mul(qprime, qprime), -2))
det_target = scale(mul(mul(X2, den), add(add(X4, scale(X2, -1)), [4])), 2)
check(det_numerator == det_target)
# x^4-x^2+4=(x^2-1/2)^2+15/4.
check(add(add(X4, scale(X2, -1)), [4]) ==
      add(mul(add(X2, [Q(-1, 2)]), add(X2, [Q(-1, 2)])), [Q(15, 4)]))

# Exact obstruction.  Its off-diagonal kernel entry is sqrt(2047)/128;
# every expression below depends only on its rational square.
x = Q(2047, 2048)
c_argument = (1 + x) / (1 - x)
e_argument = 1 / (1 - x * x)
check(c_argument == 4095)
check(e_argument == Q(4194304, 4095))
check(c_argument > 2 ** 11)
check(e_argument > 2 ** 10)
covariance_quadratic = 8 * (3 + 2 * x) / (2 - x * x)
check(covariance_quadratic < 40)
check(64 * Q(2, 3) - 40 == Q(8, 3))
# log(2)>2/3 is proved analytically by log(z)>2(z-1)/(z+1), z>1.

result = {
    "status": "passed",
    "exact_assertions": checks,
    "rational_s_samples": [str(s) for s in samples],
    "obstruction_x": str(x),
    "covariance_quadratic": str(covariance_quadratic),
    "odds_arguments": [str(c_argument), str(e_argument)],
    "strict_obstruction_upper_bound": "-8/3",
    "matrix_integral_determinant": "2*x^2*(x^4-x^2+4)/(1-x^2)^3",
}
Path(__file__).with_name("certificate_result.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
