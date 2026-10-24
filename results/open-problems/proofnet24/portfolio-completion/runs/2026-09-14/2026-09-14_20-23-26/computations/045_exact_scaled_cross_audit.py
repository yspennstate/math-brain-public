#!/usr/bin/env python3
"""Exact illustrative audit of the scaled-cross-block conditioning identities.

Standard library only. Gaussian rationals and quadratic Taylor jets verify all
32 atoms of one genuinely complex five-site example with a 2-by-3 cross block.
The universal theorem is proved analytically in agents/045.md; this finite
calculation is a reproducible sign/factor check, not a universal certificate.
"""

from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def cast(x):
        return x if isinstance(x, G) else G(x)

    def __add__(self, other):
        if isinstance(other, J):
            return NotImplemented
        q = G.cast(other)
        return G(self.re + q.re, self.im + q.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) + (-self)

    def __mul__(self, other):
        if isinstance(other, J):
            return NotImplemented
        q = G.cast(other)
        return G(self.re * q.re - self.im * q.im,
                 self.re * q.im + self.im * q.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = G.cast(other)
        d = q.re * q.re + q.im * q.im
        assert d
        return self * G(q.re / d, -q.im / d)

    def conjugate(self):
        return G(self.re, -self.im)

    def real(self):
        assert self.im == 0
        return self.re

    def norm2(self):
        return self.re * self.re + self.im * self.im


@dataclass(frozen=True)
class J:
    """Taylor coefficients through t^2; the second derivative is 2*c2."""
    c0: G = G()
    c1: G = G()
    c2: G = G()

    def __post_init__(self):
        for key in ("c0", "c1", "c2"):
            object.__setattr__(self, key, G.cast(getattr(self, key)))

    @staticmethod
    def cast(x):
        return x if isinstance(x, J) else J(x)

    def __add__(self, other):
        q = J.cast(other)
        return J(self.c0 + q.c0, self.c1 + q.c1, self.c2 + q.c2)

    __radd__ = __add__

    def __neg__(self):
        return J(-self.c0, -self.c1, -self.c2)

    def __sub__(self, other):
        return self + (-J.cast(other))

    def __rsub__(self, other):
        return J.cast(other) + (-self)

    def __mul__(self, other):
        q = J.cast(other)
        return J(self.c0 * q.c0,
                 self.c0 * q.c1 + self.c1 * q.c0,
                 self.c0 * q.c2 + self.c1 * q.c1 + self.c2 * q.c0)

    __rmul__ = __mul__


def g(a=0, b=0, d=1):
    return G(F(a, d), F(b, d))


def determinant(a):
    if not a:
        return G(1)
    if len(a) == 1:
        return a[0][0]
    return sum(((-1) ** j) * a[0][j] * determinant(
        [[a[i][h] for h in range(len(a)) if h != j]
         for i in range(1, len(a))]) for j in range(len(a)))


def inverse(a):
    d = determinant(a)
    n = len(a)
    return [[((-1) ** (i + j)) * determinant(
        [[a[u][v] for v in range(n) if v != i]
         for u in range(n) if u != j]) / d
             for j in range(n)] for i in range(n)]


def adjoint(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def multiply(a, b):
    return [[sum(a[i][h] * b[h][j] for h in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def identity_minus(a):
    return [[G(int(i == j)) - a[i][j] for j in range(len(a))]
            for i in range(len(a))]


def strict_minors(a):
    assert a == adjoint(a)
    return [determinant([row[:k] for row in a[:k]]).real()
            for k in range(1, len(a) + 1)]


def assert_strict_contraction(a):
    p = strict_minors(a)
    q = strict_minors(identity_minus(a))
    assert all(x > 0 for x in p + q)
    return p, q


def atom(a, mask):
    n = len(a)
    return determinant([[a[i][j] if ((mask >> j) & 1)
                         else 1 - a[i][j] if i == j else -a[i][j]
                         for j in range(n)] for i in range(n)])


def block(a, b, c, z):
    k, r = len(a), len(c)
    upper = [[z * b[i][j] for j in range(r)] for i in range(k)]
    lower = adjoint(upper)
    return [a[i] + upper[i] for i in range(k)] + [
        lower[i] + c[i] for i in range(r)]


def main():
    a = [[g(3, d=8), g(1, 2, 32)],
         [g(1, -2, 32), g(9, d=16)]]
    c = [[g(1, d=2), g(1, 1, 32), g(-1, d=64)],
         [g(1, -1, 32), g(5, d=8), g(1, -2, 64)],
         [g(-1, d=64), g(1, 2, 64), g(7, d=16)]]
    b = [[g(1, 1, 32), g(2, -1, 32), g(1, d=64)],
         [g(-1, 2, 32), g(1, -2, 32), g(0, 1, 32)]]
    e = [[g(1, d=7), g(1, -3, 11)],
         [g(1, 3, 11), g(-2, d=9)]]
    z, v = g(3, 2, 4), g(-1, 3, 5)
    k, r, n = 2, 3, 5
    kernel = block(a, b, c, z)
    direction = block(e, b, [[G() for _ in range(r)] for _ in range(r)], v)
    kernel_minors = assert_strict_contraction(kernel)
    assert_strict_contraction(c)
    assert determinant(multiply(b, adjoint(b))).real() > 0
    kernel_jet = [[J(kernel[i][j], direction[i][j]) for j in range(n)]
                  for i in range(n)]
    direct = [atom(kernel_jet, m) for m in range(1 << n)]
    assert sum(direct) == J(1)
    s0, s1, s2 = z.norm2(), 2 * (z.conjugate() * v).re, v.norm2()
    s_jet = J(s0, s1, s2)
    sum_qr = [[G() for _ in range(r)] for _ in range(r)]
    sum_qd = [[G() for _ in range(k)] for _ in range(k)]
    outside_weights = []
    indefinite_d = 0
    derivative_factorizations = 0
    radial_checks = 0

    for y in range(1 << r):
        absent = r - y.bit_count()
        q_matrix = [[c[i][j] - G(int(i == j and not ((y >> j) & 1)))
                     for j in range(r)] for i in range(r)]
        q = ((-1) ** absent) * determinant(q_matrix)
        assert q.real() > 0
        assert q == atom(c, y)
        outside_weights.append(q.real())
        resolvent = inverse(q_matrix)
        d = multiply(multiply(b, resolvent), adjoint(b))
        assert d == adjoint(d)
        if determinant(d).real() < 0:
            indefinite_d += 1
        for i in range(r):
            for j in range(r):
                sum_qr[i][j] += q * resolvent[i][j]
        for i in range(k):
            for j in range(k):
                sum_qd[i][j] += q * d[i][j]

        for radial_fraction in (F(0), F(1, 3), F(2, 3), F(1)):
            conditioned = [[a[i][j] - s0 * radial_fraction * d[i][j]
                            for j in range(k)] for i in range(k)]
            assert_strict_contraction(conditioned)
            radial_checks += 1

        conditioned_jet = [[J(a[i][j], e[i][j]) - s_jet * d[i][j]
                            for j in range(k)] for i in range(k)]
        for w in range(1 << k):
            conditional_probability = atom(conditioned_jet, w)
            assert isinstance(conditional_probability, J)
            assert conditional_probability.c0.real() > 0
            assert direct[w | (y << k)] == q * conditional_probability
            derivative_factorizations += 1

    assert sum(outside_weights) == 1
    assert sum_qr == [[G() for _ in range(r)] for _ in range(r)]
    assert sum_qd == [[G() for _ in range(k)] for _ in range(k)]
    assert indefinite_d > 0
    result = {
        "arithmetic": "exact Gaussian rational and degree-two Taylor coefficients",
        "inside_sites": k,
        "outside_sites": r,
        "cross_matrix_rank": 2,
        "kernel_and_complement_leading_minors": [[str(x) for x in row]
                                                for row in kernel_minors],
        "outside_atom_weights_in_bit_order": [str(x) for x in outside_weights],
        "outside_weights_sum_exactly_one": True,
        "weighted_resolvent_sum_exactly_zero": True,
        "weighted_conditional_shift_sum_exactly_zero": True,
        "indefinite_conditional_shifts": indefinite_d,
        "conditional_kernel_strict_contraction_checks": radial_checks,
        "atom_factorizations_verified_through_t_squared": derivative_factorizations,
        "joint_probability_jet_sum": ["1", "0", "0"],
        "s_jet_coefficients": [str(s0), str(s1), str(s2)],
        "second_conditional_kernel_derivative_factor": "-2 * |v|^2 * D_Y",
        "scope": "One exact example; the general theorem is analytic, not inferred from this check.",
        "all_assertions_passed": True,
    }
    output = Path(__file__).with_name("045_exact_scaled_cross_audit_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
