#!/usr/bin/env python3
"""Exact certificates for C056. Python standard library only."""
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        if not isinstance(other, G):
            other = G(F(other))
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other if isinstance(other, G) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, G):
            other = G(F(other))
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, other):
        if not isinstance(other, G):
            other = G(F(other))
        z = self * other.conj()
        d = other.norm2()
        return G(z.re / d, z.im / d)

    def __bool__(self):
        return bool(self.re or self.im)


ZERO, ONE = G(), G(F(1))


def determinant(matrix):
    a = [row[:] for row in matrix]
    det = ONE
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        d = a[j][j]
        det = det * d
        for i in range(j + 1, len(a)):
            if a[i][j]:
                ratio = a[i][j] / d
                for k in range(j + 1, len(a)):
                    a[i][k] = a[i][k] - ratio * a[j][k]
                a[i][j] = ZERO
    return det


def make_frame(weights, phase):
    norm = sum(w * w for w in weights)
    s = [F(w * w, norm) for w in weights]
    q = [[(ONE if i == j else ZERO)
          + (phase - ONE) * F(weights[i] * weights[j], norm)
          for j in range(len(weights))] for i in range(len(weights))]
    for i in range(len(q)):
        for j in range(len(q)):
            dot = sum((q[k][i].conj() * q[k][j]
                       for k in range(len(q))), ZERO)
            assert dot == (ONE if i == j else ZERO)
    return q, s, (phase - ONE).norm2()


def projection_law(q, columns):
    columns = tuple(sorted(columns))
    law = {}
    count = 0
    for rows in combinations(range(len(q)), len(columns)):
        p = determinant([[q[i][j] for j in columns] for i in rows]).norm2()
        count += 1
        if p:
            law[rows] = p
    assert sum(law.values()) == 1
    return law, count


def formula_law(s, gamma, columns):
    columns = set(columns)
    mass = sum((s[i] for i in columns), F(0))
    out = {}
    unchanged = 1 - gamma * mass * (1 - mass)
    if unchanged:
        out[tuple(sorted(columns))] = unchanged
    for i in columns:
        for j in range(len(s)):
            if j not in columns and gamma * s[i] * s[j]:
                out[tuple(sorted((columns - {i}) | {j}))] = gamma * s[i] * s[j]
    return out


@lru_cache(None)
def factor_integer(n):
    out = {}
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            out[prime] = out.get(prime, 0) + 1
            n //= prime
        prime += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def add_log(out, multiplier, argument):
    if not multiplier or not argument:
        return
    assert argument > 0
    for integer, sign in ((argument.numerator, 1),
                          (argument.denominator, -1)):
        for prime, power in factor_integer(integer).items():
            out[prime] = out.get(prime, F(0)) + multiplier * sign * power
            if not out[prime]:
                del out[prime]


def entropy_terms(law):
    out = {}
    for p in law.values():
        add_log(out, -p, p)
    return out


def combine_terms(*weighted):
    out = {}
    for scale, terms in weighted:
        for prime, coefficient in terms.items():
            out[prime] = out.get(prime, F(0)) + scale * coefficient
            if not out[prime]:
                del out[prime]
    return out


def lower_terms(x, y, d):
    out = {}
    for multiplier, value in ((2, x), (-2, y), (-2, d)):
        add_log(out, multiplier * value, value)
    return out


def scalar_beta_terms(base, a, b, gamma):
    if not gamma or not a or not b:
        return {}
    out = {}
    for sign, mass in ((1, base), (1, base + a + b),
                       (-1, base + a), (-1, base + b)):
        k = 1 - gamma * mass * (1 - mass)
        add_log(out, sign * k, k)
    add_log(out, -2 * gamma * a * b, gamma * a * b)
    return out


def reduced_log_interval(x, terms=60):
    """x in [1,2]; rigorous positive-tail atanh-series enclosure."""
    assert 1 <= x <= 2
    y = (x - 1) / (x + 1)
    partial = sum((2 * y ** (2*j + 1) / (2*j + 1)
                   for j in range(terms)), F(0))
    tail = 2 * y ** (2*terms + 1) / ((2*terms + 1) * (1 - y*y))
    return partial, partial + tail


@lru_cache(None)
def log_prime_interval(prime):
    x, shift = F(prime), 0
    while x > 2:
        x /= 2
        shift += 1
    low, high = reduced_log_interval(x)
    two_low, two_high = reduced_log_interval(F(2))
    return low + shift * two_low, high + shift * two_high


def linear_interval(terms):
    low = high = F(0)
    for prime, coefficient in terms.items():
        lo, hi = log_prime_interval(prime)
        if coefficient > 0:
            low += coefficient * lo
            high += coefficient * hi
        else:
            low += coefficient * hi
            high += coefficient * lo
    return low, high


def decimal(x):
    with localcontext() as ctx:
        ctx.prec = 45
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def dump_terms(terms):
    return {str(prime): str(value) for prime, value in sorted(terms.items())}


def dump_law(law):
    return [{"set": list(key), "probability": str(value)}
            for key, value in sorted(law.items())]


CASES = [
    ("flat_six_reflection", [1]*6, G(F(-1)), [0, 1], 2, 3, True),
    ("flat_six_complex", [1]*6, G(F(-3, 5), F(4, 5)), [0, 1], 2, 3, True),
    ("nonuniform_eight_reflection", [1, 2, 1, 1, 2, 2, 1, 2],
     G(F(-1)), [0, 1, 2], 3, 4, False),
    ("empty_bottom", [1, 2, 1, 1], G(F(-3, 5), F(4, 5)),
     [], 0, 1, False),
    ("full_top", [1, 2, 1, 1], G(F(-1)), [0, 1], 2, 3, False),
    ("zero_update_mass", [1, 2, 0, 1, 2], G(F(-1)), [0, 1], 2, 3, True),
    ("identity_phase", [1, 2, 1, 1, 2], G(F(1)), [0, 1], 2, 3, True),
]


def main():
    certificates, summary = [], []
    total_minors = 0
    for name, weights, phase, r, p, q, equality_expected in CASES:
        matrix, s, gamma = make_frame(weights, phase)
        sets = [r, r + [p], r + [q], r + [p, q]]
        laws = []
        for columns in sets:
            law, count = projection_law(matrix, columns)
            total_minors += count
            assert law == formula_law(s, gamma, columns)
            laws.append(law)
        entropy = [entropy_terms(law) for law in laws]
        beta = combine_terms((1, entropy[1]), (1, entropy[2]),
                             (-1, entropy[0]), (-1, entropy[3]))
        base, a, b = sum((s[i] for i in r), F(0)), s[p], s[q]
        assert beta == scalar_beta_terms(base, a, b, gamma)
        x = 1 - gamma / 4 + gamma * (a + b)**2 / 4
        y = 1 - gamma / 4 + gamma * (a - b)**2 / 4
        d = gamma * a * b
        assert x == y + d and min(x, y, d) >= 0
        lower = lower_terms(x, y, d)
        gap = combine_terms((1, beta), (-1, lower))
        assert bool(gap) != equality_expected
        beta_interval = linear_interval(beta)
        lower_interval = linear_interval(lower)
        gap_interval = linear_interval(gap)
        assert beta_interval[0] >= 0
        assert lower_interval[0] >= 0
        assert gap_interval[0] >= 0
        if not equality_expected:
            assert gap_interval[0] > 0
        if name == "flat_six_reflection":
            assert all(len(law) == 9 and set(law.values()) == {F(1, 9)}
                       for law in laws)
            assert beta == {}
        certificates.append({
            "name": name,
            "matrix": [[{"real": str(z.re), "imag": str(z.im)} for z in row]
                       for row in matrix],
            "weights": [str(value) for value in s],
            "gamma": str(gamma),
            "R": r, "p": p, "q": q,
            "projection_laws": [dump_law(law) for law in laws],
            "entropy_prime_log_coefficients": [dump_terms(v) for v in entropy],
            "beta_prime_log_coefficients": dump_terms(beta),
            "lower_bound_prime_log_coefficients": dump_terms(lower),
            "gap_prime_log_coefficients": dump_terms(gap),
            "X": str(x), "Y": str(y), "D": str(d),
            "beta_exact_interval": [str(v) for v in beta_interval],
            "lower_bound_exact_interval": [str(v) for v in lower_interval],
            "gap_exact_interval": [str(v) for v in gap_interval],
            "sharp_equality_verified": equality_expected,
        })
        summary.append({
            "name": name,
            "beta_approximation": decimal(sum(beta_interval) / 2),
            "lower_bound_approximation": decimal(sum(lower_interval) / 2),
            "gap_approximation": decimal(sum(gap_interval) / 2),
            "gap_exactly_zero": not gap,
            "projection_law_support_sizes": [len(law) for law in laws],
        })
    here = Path(__file__).resolve().parent
    result = {"status": "PASS", "examples": len(CASES),
              "exact_minors_checked": total_minors,
              "log_series_terms": 60, "results": summary}
    (here / "certificate.json").write_text(json.dumps(certificates, indent=2) + "\n")
    (here / "verified_output.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
