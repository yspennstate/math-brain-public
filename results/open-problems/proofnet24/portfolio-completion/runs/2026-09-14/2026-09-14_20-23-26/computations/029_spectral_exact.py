"""Exact supporting checks for worker 029's two spectral claims.

Only the Python standard library is used.  The universal arguments are in
agents/029.md; this script checks radical identities, rational inequalities,
and one exact admissible example.  There is no random spectral search.
"""

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction as F
from itertools import permutations


@dataclass(frozen=True)
class Radical:
    """Q(sqrt(2), sqrt(5)), basis 1, sqrt(2), sqrt(5), sqrt(10)."""

    c: tuple

    def __post_init__(self):
        assert len(self.c) == 4
        object.__setattr__(self, "c", tuple(F(x) for x in self.c))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Radical) else Radical((value, 0, 0, 0))

    def __add__(self, other):
        other = self.coerce(other)
        return Radical(tuple(x + y for x, y in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Radical(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        out = [F(0)] * 4
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c):
                shared = i & j
                factor = (2 if shared & 1 else 1) * (5 if shared & 2 else 1)
                out[i ^ j] += factor * x * y
        return Radical(tuple(out))

    __rmul__ = __mul__

    def __truediv__(self, rational):
        assert not isinstance(rational, Radical)
        return self * (1 / F(rational))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = self.coerce(1)
        for _ in range(n):
            out = out * self
        return out

    def interval(self):
        """Certified rational interval, not a floating-point comparison."""
        bounds = [(F(1), F(1))]
        for radicand, digits in (
            (2, 1414213562373095048),
            (5, 2236067977499789696),
            (10, 3162277660168379331),
        ):
            lo = F(digits, 10**18)
            hi = lo + F(1, 10**18)
            assert lo * lo < radicand < hi * hi
            bounds.append((lo, hi))
        lo = hi = F(0)
        for coefficient, (left, right) in zip(self.c, bounds):
            if coefficient >= 0:
                lo += coefficient * left
                hi += coefficient * right
            else:
                lo += coefficient * right
                hi += coefficient * left
        return lo, hi

    def positive(self):
        assert self.interval()[0] > 0, self

    def decimal(self):
        roots = [Decimal(1), Decimal(2).sqrt(), Decimal(5).sqrt(), Decimal(10).sqrt()]
        return sum(Decimal(x.numerator) / Decimal(x.denominator) * root
                   for x, root in zip(self.c, roots))


one = Radical((1, 0, 0, 0))
L = Radical((0, 1, 0, 0))
sqrt5 = Radical((0, 0, 1, 0))
k = 3 - sqrt5
a = 1 - k
b = 1 + L
c0 = 5 - a - b
D = a * b * c0
eta0 = (18 - L) / 23
alpha0 = -1 + L / 2

assert D == 6 * sqrt5 + 7 * L * sqrt5 - 15 * L - 13
assert eta0 * (5 - L) == 4 - L
assert (L**2) == one * 2
assert (sqrt5**2) == one * 5

# The lower determinant polytope has exactly the stated vertex type.
for expression in (a, b - a, c0 - a, b - c0, a + 2*b - 5, 5 - 2*a - b):
    expression.positive()
(D - F(4, 3)).positive()

f_at_k = (1 - k) * (k + 4)**2 / 4
assert f_at_k == (41 * sqrt5 - 89) / 2
assert f_at_k - D == a * (b - (5-a)/2)**2
(f_at_k - D).positive()

# Averaging threshold: the upper quadratic reaches 1 exactly at eta0.
assert (5-L) * eta0**2 - (4-L) * eta0 == one * 0
eta0.positive()
(1-eta0).positive()
(2*(L-1)-eta0).positive()  # 2/(1+sqrt(2)) - eta0 > 0.
(-alpha0).positive()

# A short independent rational proof that D > 4/3.
assert F(2236,1000)**2 < 5 < F(2237,1000)**2
assert F(1414,1000)**2 < 2 < F(1415,1000)**2
rational_lower = F(59,250) * F(1207,500) * F(587,250)
assert rational_lower == F(41802031,31250000)
assert rational_lower > F(4,3)

# Exact admissible four-type operator with a boundary fixed point and
# nonreal tangent multipliers outside the unit circle for unaveraged V.
outputs = {
    (0,0): 1, (1,1): 2, (2,2): 0,
    (0,1): 2, (0,2): 1, (1,2): 0,
    (0,3): 1, (1,3): 2, (2,3): 0, (3,3): 0,
}
P = [[[F(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
for (i,j), child in outputs.items():
    P[i][j][child] = P[j][i][child] = F(1)
for i in range(4):
    for j in range(4):
        assert sum(P[i][j]) == 1
        assert P[i][j] == P[j][i]
        assert P[i][j][i] == P[i][j][j] == 0

p = [F(1,3), F(1,3), F(1,3), F(0)]
Vp = [sum(P[i][j][r]*p[i]*p[j] for i in range(4) for j in range(4))
      for r in range(4)]
assert Vp == p
J = [[2*sum(P[i][j][r]*p[i] for i in range(4)) for j in range(4)]
     for r in range(4)]
assert all(J[i][i] == 0 for i in range(4))
assert all(sum(J[i][j] for i in range(4)) == 2 for j in range(4))
assert [sum(J[i][j]*p[j] for j in range(4)) for i in range(4)] == [2*x for x in p]

# Matrix on E in the basis e_1-e_4, e_2-e_4, e_3-e_4.
M = [[J[i][j]-J[i][3] for j in range(3)] for i in range(3)]
assert M == [[F(-2,3), 0, F(2,3)],
             [F(2,3), F(-2,3), 0],
             [0, F(2,3), F(-2,3)]]


def poly_add(x, y):
    out = [F(0)] * max(len(x), len(y))
    for i, value in enumerate(x):
        out[i] += value
    for i, value in enumerate(y):
        out[i] += value
    return out


def poly_mul(x, y):
    out = [F(0)] * (len(x)+len(y)-1)
    for i, left in enumerate(x):
        for j, right in enumerate(y):
            out[i+j] += left*right
    return out


def charpoly(matrix):
    n = len(matrix)
    result = [F(0)] * (n+1)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = [F((-1)**inversions)]
        for i,j in enumerate(perm):
            term = poly_mul(term, [-matrix[i][j], F(i==j)])
        result = poly_add(result, term)
    return result


assert charpoly(M) == [0, F(4,3), 2, 1]
assert charpoly(J) == [0, F(-8,3), F(-8,3), 0, 1]
assert sum(charpoly(M)) == F(13,3)  # det(I - J|E).
assert F(1) + F(1,3) > 1  # |-1 +/- i/sqrt(3)|^2 = 4/3.

getcontext().prec = 50
print("All exact radical identities, interval inequalities, and example checks passed.")
print("determinant lower bound D =", D.decimal())
print("averaging threshold eta0 =", eta0.decimal())
print("tangent characteristic polynomial: t * (t^2 + 2*t + 4/3)")
print("The numerical displays above are explanatory only; all assertions were exact.")
