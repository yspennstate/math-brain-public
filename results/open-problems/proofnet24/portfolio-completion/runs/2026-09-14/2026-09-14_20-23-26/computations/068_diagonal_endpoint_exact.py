#!/usr/bin/env python3
"""Exact audit certificates for the diagonal-endpoint entropy theorem.

Python standard library only.  No floating-point arithmetic, logarithm
evaluation, sampling, or optimization.  Formal log symbols verify their
coefficients; the logarithmic inequality is proved in agents/068.md.
"""

from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json


class Poly:
    """Sparse Laurent polynomials over Q, with the exact relation I^2=-1."""

    def __init__(self, value=0):
        self.c = dict(value.c) if isinstance(value, Poly) else ({(): Q(value)} if value else {})

    @staticmethod
    def mono(exponents, coefficient=1):
        out = Poly()
        exponents = dict(exponents)
        phase = exponents.pop("I", 0) % 4
        coefficient = Q(coefficient) * (-1 if phase >= 2 else 1)
        if phase % 2:
            exponents["I"] = 1
        key = tuple(sorted((v, e) for v, e in exponents.items() if e))
        if coefficient:
            out.c[key] = coefficient
        return out

    def __add__(self, other):
        other = Poly(other)
        out = Poly(self)
        for key, value in other.c.items():
            out.c[key] = out.c.get(key, Q(0)) + value
            if not out.c[key]:
                del out.c[key]
        return out

    __radd__ = __add__

    def __neg__(self):
        out = Poly()
        out.c = {key: -value for key, value in self.c.items()}
        return out

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        other = Poly(other)
        out = Poly()
        for left, lc in self.c.items():
            for right, rc in other.c.items():
                exponents = dict(left)
                for name, power in right:
                    exponents[name] = exponents.get(name, 0) + power
                out = out + Poly.mono(exponents, lc * rc)
        return out

    __rmul__ = __mul__

    def __pow__(self, power):
        if power < 0:
            assert len(self.c) == 1
            key, value = next(iter(self.c.items()))
            return Poly.mono({v: e * power for v, e in key}, value ** power)
        out = Poly(1)
        for _ in range(power):
            out = out * self
        return out

    def __truediv__(self, other):
        return self * (Poly(other) ** -1)

    def __eq__(self, other):
        return self.c == Poly(other).c

    def derivative(self, variable):
        out = Poly()
        for key, value in self.c.items():
            exponents = dict(key)
            power = exponents.get(variable, 0)
            if power:
                exponents[variable] = power - 1
                out = out + Poly.mono(exponents, value * power)
        return out

    def at(self, variable, value):
        out = Poly()
        for key, coefficient in self.c.items():
            exponents = dict(key)
            power = exponents.pop(variable, 0)
            out = out + Poly.mono(exponents, coefficient * Q(value) ** power)
        return out

    def rational(self):
        assert all(key == () for key in self.c)
        return self.c.get((), Q(0))

    def coefficients(self, variable):
        degree = max((dict(key).get(variable, 0) for key in self.c), default=0)
        coeffs = [Q(0)] * (degree + 1)
        for key, coefficient in self.c.items():
            exponents = dict(key)
            power = exponents.pop(variable, 0)
            assert not exponents and power >= 0
            coeffs[power] += coefficient
        return [str(x) for x in coeffs]


def V(name):
    return Poly.mono({name: 1})


def average(values, coordinate, parameter):
    out = []
    for mask in range(len(values)):
        absent = mask & ~(1 << coordinate)
        present = absent | (1 << coordinate)
        out.append((1 - parameter) * values[absent] + parameter * values[present])
    return out


def subtract(left, right):
    return [x - y for x, y in zip(left, right)]


def D(values, coordinate, parameter):
    return subtract(values, average(values, coordinate, parameter))


def L(values, parameters):
    terms = [D(values, i, d) for i, d in enumerate(parameters)]
    return [sum(term[mask] for term in terms) for mask in range(len(values))]


def determinant(matrix):
    n = len(matrix)
    total = Poly(0)
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n))
        term = Poly((-1) ** inversions)
        for i, j in enumerate(order):
            term = term * matrix[i][j]
        total = total + term
    return total


def atoms(kernel):
    n = len(kernel)
    return [determinant([
        [kernel[i][j] if mask & (1 << j) else Poly(int(i == j)) - kernel[i][j]
         for j in range(n)] for i in range(n)]) for mask in range(1 << n)]


def product_probability(mask, parameters):
    result = Q(1)
    for i, d in enumerate(parameters):
        result *= d if mask & (1 << i) else 1 - d
    return result


def main():
    checks = []
    a, b, c, d, p, q, t = (V(x) for x in ("a", "b", "c", "d", "p", "q", "t"))
    la, lb, lc, ld = (V(x) for x in ("log_a", "log_b", "log_c", "log_d"))
    # Bit 0 is coordinate i, bit 1 is coordinate j: 00,10,01,11.
    g = [a, c, b, d]
    logs = [la, lc, lb, ld]
    weights = [(1-p)*(1-q), p*(1-q), (1-p)*q, p*q]
    di, dj = D(g, 0, p), D(g, 1, q)
    didj = D(dj, 0, p)
    assert didj == D(di, 1, q)
    assert D(di, 0, p) == di and D(dj, 1, q) == dj
    checks.append("symbolic biased binary projections: idempotence and commutation")

    cross = sum(w * u * v / value for w, u, v, value in zip(weights, di, dj, g))
    mixed_log = sum(w * v * ell for w, v, ell in zip(weights, didj, logs))
    weight = p*(1-p)*q*(1-q)
    fraction_part = b*c/a + a*d/b + a*d/c + b*c/d - a-b-c-d
    log_part = (a+d-b-c)*(la+ld-lb-lc)
    assert cross == weight*fraction_part
    assert mixed_log == weight*log_part
    checks.append("universal 2x2 fiber rational term and formal logarithm coefficients")

    r, X, Y, logr = a*d/(b*c), a+d, b+c, la+ld-lb-lc
    certificate = X*(r**-1-1+logr) + Y*(r-1-logr)
    assert fraction_part + log_part == certificate
    checks.append("universal Laurent identity X(1/r-1+log r)+Y(r-1-log r)")

    # Reversibility with respect to an arbitrary biased Bernoulli marginal.
    mu = [1-p, p]
    transition = [[t*int(x == y)+(1-t)*mu[y] for y in range(2)] for x in range(2)]
    for x in range(2):
        for y in range(2):
            assert mu[x]*transition[x][y] == mu[y]*transition[y][x]
    checks.append("symbolic detailed balance for the coordinate resampling transition")

    imaginary = V("I")
    z12, z13, z23 = (1+2*imaginary)/40, (2-imaginary)/50, (1+imaginary)/30
    interior = [[Poly(Q(2,5)), z12, z13],
                [(1-2*imaginary)/40, Poly(Q(1,2)), z23],
                [(2+imaginary)/50, (1-imaginary)/30, Poly(Q(3,5))]]
    # |Re z|+|Im z| bounds prove strict diagonal dominance of K and I-K.
    row_bounds = [Q(3,40)+Q(3,50), Q(3,40)+Q(2,30), Q(3,50)+Q(2,30)]
    for bound, diagonal in zip(row_bounds, (Q(2,5), Q(1,2), Q(3,5))):
        assert bound < diagonal and bound < 1-diagonal
    projection = [[Poly(Q(1,3)), -imaginary/3, Poly(Q(1,3))],
                  [imaginary/3, Poly(Q(1,3)), imaginary/3],
                  [Poly(Q(1,3)), -imaginary/3, Poly(Q(1,3))]]
    for i in range(3):
        for j in range(3):
            assert sum(projection[i][k]*projection[k][j] for k in range(3)) == projection[i][j]
    checks.append("exact feasibility certificates for a complex interior kernel and a rank-one projection")

    cases = []
    for name, kernel, parameters in [
        ("complex_interior_changing_diagonal", interior, [Q(1,3), Q(3,7), Q(2,3)]),
        ("complex_projection_complement_line", projection, [Q(1,2)]*3),
    ]:
        n = len(kernel)
        endpoint = atoms(kernel)
        assert sum(endpoint) == 1
        assert all(value.rational() >= 0 for value in endpoint)
        mu = [product_probability(mask, parameters) for mask in range(1 << n)]
        interpolated = [[(1-t)*parameters[i]*int(i == j)+t*kernel[i][j]
                         for j in range(n)] for i in range(n)]
        direct = atoms(interpolated)
        channel = []
        for y in range(1 << n):
            probability = Poly(0)
            for x in range(1 << n):
                term = endpoint[x]
                for i, parameter in enumerate(parameters):
                    yi, xi = (y >> i) & 1, (x >> i) & 1
                    term = term * (t*int(xi == yi)+(1-t)*(parameter if yi else 1-parameter))
                probability = probability + term
            channel.append(probability)
        assert direct == channel
        assert sum(direct) == 1
        for i, parameter in enumerate(parameters):
            marginal = sum(direct[mask] for mask in range(1 << n) if mask & (1 << i))
            assert marginal == parameter + t*(kernel[i][i]-parameter)

        density = [value / weight for value, weight in zip(endpoint, mu)]
        for i, parameter in enumerate(parameters):
            averaged = average(density, i, parameter)
            density = [v+t*(u-v) for u, v in zip(density, averaged)]
        assert density == [value / weight for value, weight in zip(direct, mu)]
        lg = L(density, parameters)
        llg = L(lg, parameters)
        assert [t*v.derivative("t") for v in density] == lg
        assert [t*t*v.derivative("t").derivative("t") for v in density] == subtract(llg, lg)

        if name == "complex_projection_complement_line":
            complement = [[int(i == j)-kernel[i][j] for j in range(n)] for i in range(n)]
            assert [value.at("t", -1) for value in direct] == atoms(complement)
        cases.append({
            "name": name,
            "reference_marginals": [str(x) for x in parameters],
            "endpoint_atoms_mask_order": [str(x.rational()) for x in endpoint],
            "atom_polynomials_ascending_t": [x.coefficients("t") for x in direct],
            "identities": ["channel=direct mixed-column determinant, all t coefficients",
                           "density=N_t(endpoint density), all t coefficients",
                           "t g'=Lg and t^2 g''=(L^2-L)g, all t coefficients",
                           "normalization and affine marginals, all t coefficients"],
        })
    checks.append("full polynomial complex-kernel resampling and density identities in two independent examples")

    result = {"status": "ALL EXACT ASSERTIONS PASSED", "arithmetic": "rational Laurent polynomials, I^2=-1",
              "numeric_sampling": False, "logarithm_evaluation": False,
              "universal_checks": checks, "finite_examples": cases,
              "limitations": "The logarithmic nonnegativity, arbitrary-dimensional argument, strictness, and endpoint gluing are analytic proofs in agents/068.md. The finite examples establish their listed identities only."}
    target = Path(__file__).with_name("068_diagonal_endpoint_exact_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "universal_check_groups": len(checks),
                      "finite_examples": len(cases), "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
