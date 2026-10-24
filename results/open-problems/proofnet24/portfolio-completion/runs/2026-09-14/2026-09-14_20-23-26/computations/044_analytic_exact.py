#!/usr/bin/env python3
"""Exact companion checks for agents/044.md; Python standard library only.

The universal analytic-continuation and norm arguments are proved in the report.
This certificate checks radical identities, the 14 coefficient coordinates,
and exact first/second derivatives in a feasible boundary-activation example.
"""

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as F


@dataclass(frozen=True)
class Q5:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def lift(x):
        return x if isinstance(x, Q5) else Q5(F(x))

    def __add__(self, other):
        other = Q5.lift(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q5.lift(other))

    def __rsub__(self, other):
        return Q5.lift(other) - self

    def __mul__(self, other):
        other = Q5.lift(other)
        return Q5(self.a * other.a + 5 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Q5.lift(other)
        den = other.a * other.a - 5 * other.b * other.b
        assert den != 0
        return self * Q5(other.a / den, -other.b / den)

    def __rtruediv__(self, other):
        return Q5.lift(other) / self

    def interval(self):
        lo, hi = F(2236, 1000), F(2237, 1000)
        assert lo * lo < 5 < hi * hi
        if self.b >= 0:
            return self.a + self.b * lo, self.a + self.b * hi
        return self.a + self.b * hi, self.a + self.b * lo

    def decimal(self):
        with localcontext() as ctx:
            ctx.prec = 45
            a = Decimal(self.a.numerator) / Decimal(self.a.denominator)
            b = Decimal(self.b.numerator) / Decimal(self.b.denominator)
            return a + b * Decimal(5).sqrt()


s = Q5(F(0), F(1))
a = s - 2
c = (3 - s) / 2
C = 1 / a
D = 2 * s - 1
r = a / 4
epsilon = a * a / 9
gamma = a - 2 * r - 2 * epsilon * (1 + r)
assert a * a + 4 * a == Q5(F(1))
assert c * c - 3 * c + 1 == Q5()
assert C == s + 2
assert D == C - 2 * c
assert D * (D + 2) == Q5(F(19))
assert gamma == 4 * a / 9
assert gamma * r == epsilon
assert 1 + 2 * r * (1 + r) == Q5(F(9, 8))
assert 2 * C * c * c == s - 1
assert a.interval()[0] > 0
assert c.interval()[0] > 0 and c.interval()[1] < F(1, 2)
assert epsilon.interval()[0] > 0


def zeros():
    return [[[F(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]


def check_array(P, stochastic):
    for i in range(4):
        for j in range(4):
            assert P[i][j] == P[j][i]
            assert P[i][j][i] == P[i][j][j] == 0
            assert sum(P[i][j]) == int(stochastic)
            if stochastic:
                assert min(P[i][j]) >= 0


def bilinear(P, u, v):
    return [sum(P[i][j][k] * u[i] * v[j]
                for i in range(4) for j in range(4)) for k in range(4)]


def solve(M, b):
    A = [list(row) + [rhs] for row, rhs in zip(M, b)]
    n = len(M)
    for j in range(n):
        pivot = next(i for i in range(j, n) if A[i][j])
        A[j], A[pivot] = A[pivot], A[j]
        q = A[j][j]
        A[j] = [x / q for x in A[j]]
        for i in range(n):
            if i != j:
                q = A[i][j]
                A[i] = [x - q * y for x, y in zip(A[i], A[j])]
    return [row[-1] for row in A]


def transfer(i, j, receiving, giving):
    H = zeros()
    for u, v in {(i, j), (j, i)}:
        H[u][v][receiving] = F(1)
        H[u][v][giving] = F(-1)
    check_array(H, stochastic=False)
    return H


directions = []
for i in range(4):
    for j in range(i, 4):
        allowed = [k for k in range(4) if k not in {i, j}]
        for k in allowed[:-1]:
            directions.append(transfer(i, j, k, allowed[-1]))
assert len(directions) == 14
# The missing-output face loses one coordinate for each unordered pair in S.
assert len([(i, j) for i in range(3) for j in range(i, 3)]) == 6
assert 14 - 6 == 8

P = zeros()
offspring = {
    (0, 0): 1, (1, 1): 2, (2, 2): 0,
    (0, 1): 2, (0, 2): 1, (1, 2): 0,
    (0, 3): 1, (1, 3): 2, (2, 3): 0, (3, 3): 0,
}
for (i, j), k in offspring.items():
    P[i][j][k] = P[j][i][k] = F(1)
check_array(P, stochastic=True)
p = [F(1, 3), F(1, 3), F(1, 3), F(0)]
assert bilinear(P, p, p) == p
J = [[2 * sum(P[i][j][k] * p[i] for i in range(4))
      for j in range(4)] for k in range(4)]
assert J == [
    [F(0), F(2, 3), F(4, 3), F(2, 3)],
    [F(4, 3), F(0), F(2, 3), F(2, 3)],
    [F(2, 3), F(4, 3), F(0), F(2, 3)],
    [F(0)] * 4,
]
assert all(sum(J[i][j] for i in range(4)) == 2 for j in range(4))
M = [[F(i == j) - J[i][j] for j in range(4)] for i in range(4)]

H = transfer(0, 0, receiving=3, giving=1)
assert all(H[i][j][k] >= 0 for i in range(4) for j in range(4)
           for k in range(4) if P[i][j][k] == 0)
g = bilinear(H, p, p)
assert g == [F(0), F(-1, 9), F(0), F(1, 9)]
v = solve(M, g)
assert v == [F(-4, 351), F(-25, 351), F(-10, 351), F(1, 9)]
assert sum(v) == 0
Pvv, Hpv = bilinear(P, v, v), bilinear(H, p, v)
w = solve(M, [2 * x + 4 * y for x, y in zip(Pvv, Hpv)])
assert sum(w) == 0
assert w[3] == F(-16, 1053)

# Direct substitution of p + t*v + (t^2/2)*w into x - V_(P+tH)(x):
# check all residual coefficients through second order independently.
xcoeff = [p, v, [z / 2 for z in w]]
for degree in range(3):
    rhs = [F(0)] * 4
    for parameter_degree, array in enumerate([P, H]):
        for first in range(3):
            second = degree - parameter_degree - first
            if 0 <= second < 3:
                term = bilinear(array, xcoeff[first], xcoeff[second])
                rhs = [u + z for u, z in zip(rhs, term)]
    assert rhs == xcoeff[degree]

# A within-face direction has no missing output at any parameter value.
Hface = transfer(0, 0, receiving=2, giving=1)
assert all(Hface[i][j][3] == 0 for i in range(4) for j in range(4))
assert solve(M, bilinear(Hface, p, p))[3] == 0
# An off-diagonal perturbation carries the ordered-pair factor of two.
Hoff = transfer(0, 1, receiving=3, giving=2)
assert bilinear(Hoff, p, p)[3] == F(2, 9)
assert solve(M, bilinear(Hoff, p, p))[3] == F(2, 9)

print('PASS: exact radical identities, 14 coordinates, and boundary-face codimension.')
print('PASS: admissible boundary example; exact derivative and quadratic residual.')
print('PASS: invariant-face and off-diagonal activation checks.')
print('epsilon =', epsilon.decimal())
print('tube radius =', r.decimal())
print('tube contraction bound =', (1 - c * gamma).decimal())
print('derivative bound D =', D.decimal())
print('Hessian bound =', (38 * C).decimal())
print('quadratic remainder bound =', (19 * C).decimal())
print('activation derivative =', ', '.join(map(str, v)))
print('activation second derivative =', ', '.join(map(str, w)))
