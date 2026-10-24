#!/usr/bin/env python3
"""Exact finite checks for worker 042; the universal proof is agents/042.md.

Uses only Fraction arithmetic for the certificates. Decimal Hessians are
illustrations; zero/nonzero curvature is separately certified exactly.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def cast(z):
        return z if isinstance(z, G) else G(F(z))

    def __add__(self, other):
        z = G.cast(other)
        return G(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) + (-self)

    def __mul__(self, other):
        z = G.cast(other)
        return G(self.re*z.re - self.im*z.im,
                 self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def __truediv__(self, other):
        z = G.cast(other)
        numerator = self*z.conj()
        d = z.norm2()
        return G(numerator.re/d, numerator.im/d)

    def real(self):
        assert self.im == 0
        return self.re


def vec(*entries):
    return [G.cast(z) for z in entries]


def determinant(m):
    if not m:
        return G(F(1))
    return sum(((-1)**j)*m[0][j]*determinant(
        [[row[k] for k in range(len(m)) if k != j] for row in m[1:]])
        for j in range(len(m)))


def outer(u):
    return [[x*y.conj() for y in u] for x in u]


def square(m):
    n = len(m)
    return [[sum(m[i][k]*m[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def exact_data(u, v, t):
    n = len(u)
    a = [z.norm2() for z in u]
    b = [z.norm2() for z in v]
    assert sum(a) == sum(b) == 1
    w = {(i, j): (u[i]*v[j]-v[i]*u[j]).norm2()
         for i, j in combinations(range(n), 2)}
    gamma = sum(w.values())
    c = sum(x.conj()*y for x, y in zip(u, v))
    assert gamma == 1-c.norm2()
    d = [sum(value for edge, value in w.items() if i in edge)
         for i in range(n)]
    s = t*(1-t)
    probs = {(): s*gamma}
    deriv = {(): (1-2*t)*gamma}
    delta = {(): -gamma}
    for i in range(n):
        probs[(i,)] = (1-t)*a[i]+t*b[i]-s*d[i]
        deriv[(i,)] = b[i]-a[i]-(1-2*t)*d[i]
        delta[(i,)] = d[i]
    for edge, value in w.items():
        probs[edge] = s*value
        deriv[edge] = (1-2*t)*value
        delta[edge] = -value
    assert sum(probs.values()) == 1
    assert sum(deriv.values()) == sum(delta.values()) == 0
    ku, kv = outer(u), outer(v)
    k = [[(1-t)*ku[i][j]+t*kv[i][j] for j in range(n)]
         for i in range(n)]
    for mask in range(1 << n):
        subset = tuple(i for i in range(n) if mask & (1 << i))
        mixed = [[k[i][j] if mask & (1 << j)
                  else G.cast(int(i == j))-k[i][j]
                  for j in range(n)] for i in range(n)]
        atom = determinant(mixed).real()
        assert atom == probs.get(subset, F(0))
        assert atom >= 0
    for i in range(n):
        assert sum(value for subset, value in probs.items() if i in subset) == k[i][i].real()
    if 0 < t < 1 and gamma:
        k2 = square(k)
        ell = [[z/(s*gamma) for z in row] for row in k2]
        for i in range(n):
            assert probs[(i,)] == probs[()]*ell[i][i].real()
        for i, j in w:
            minor = ell[i][i].real()*ell[j][j].real()-ell[i][j].norm2()
            assert probs[(i, j)] == probs[()]*minor
            gap = probs[(i,)]*probs[(j,)]-probs[()]*probs[(i, j)]
            assert gap == probs[()]**2*ell[i][j].norm2()
            assert gap >= 0
    return a, b, w, gamma, probs, deriv, delta


def signs_relation(u, v):
    if any(x.norm2() != y.norm2() for x, y in zip(u, v)):
        return None
    active = [i for i, x in enumerate(u) if x.norm2()]
    z0 = v[active[0]]/u[active[0]]
    plus = []
    minus = []
    for i in active:
        ratio = (v[i]/u[i])/z0
        if ratio == G(F(1)):
            plus.append(i)
        elif ratio == G(F(-1)):
            minus.append(i)
        else:
            return None
    if not minus:
        return None
    return sum(u[i].norm2() for i in plus)


def check_case(name, u, v):
    output = {"name": name, "n": len(u), "checks": []}
    mass = signs_relation(u, v)
    for t in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        a, b, w, gamma, probs, deriv, delta = exact_data(u, v, t)
        output["gamma"] = str(gamma)
        if not (0 < t < 1):
            continue
        if gamma == 0:
            assert all(value == 0 for value in deriv.values())
            output["checks"].append({"t": str(t), "constant_path": True})
            continue
        positive = [key for key, value in probs.items() if value > 0]
        fi = sum(deriv[key]**2/probs[key] for key in positive)
        ratios = {edge: probs[(edge[0],)]*probs[(edge[1],)] /
                  (probs[()]*probs[edge])
                  for edge, value in w.items() if value > 0}
        assert all(value >= 1 for value in ratios.values())
        zero = fi == 0 and all(value == 1 for value in ratios.values())
        assert zero == (t == F(1, 2) and mass is not None)
        hessian = -float(fi)-2*sum(float(w[edge])*math.log(float(ratio))
                                 for edge, ratio in ratios.items())
        output["checks"].append({
            "t": str(t), "fisher_exact": str(fi), "zero_exact": zero,
            "positive_log_ratios": [str(x) for x in ratios.values() if x > 1],
            "hessian_decimal_only": hessian,
        })
        if zero:
            c4 = -sum(delta[key]**2/probs[key] for key in positive)/2
            c6 = sum(delta[key]**3/probs[key]**2 for key in positive)/6
            assert c4 == -8
            expected6 = F(32, 3)*(2*mass-1)**2/(mass*(1-mass))
            assert c6 == expected6
            output["midpoint_coefficients_exact"] = {
                "plus_mass": str(mass), "x4": str(c4), "x6": str(c6)}
    return output


def main():
    third = F(1, 3)
    base = vec(third, 2*third, 2*third)
    cases = [
        ("generic_complex", base, vec(G(0, 2*third), 2*third, third)),
        ("zeros_and_disjoint_support", vec(1, 0, 0),
         vec(0, F(3, 5), G(0, F(4, 5)))),
        ("two_nonopposite_phases", base,
         vec(third, G(0, 2*third), G(0, 2*third))),
        ("three_phases", base, vec(third, G(0, 2*third), -2*third)),
        ("signs_with_inactive_coordinate", base+vec(0),
         vec(third, 2*third, -2*third, 0)),
        ("unbalanced_signs", base, vec(third, -2*third, -2*third)),
        ("balanced_signs", vec(*([F(1, 2)]*4)),
         vec(F(1, 2), F(1, 2), F(-1, 2), F(-1, 2))),
        ("proportional_with_phase_and_zero", base+vec(0),
         [G(0, 1)*z for z in base]+vec(0)),
    ]
    result = {"status": "all exact checks passed",
              "arithmetic": "Fractions and Gaussian rationals",
              "limitations": "Finite consistency certificates; the all-dimensional theorem is analytic.",
              "cases": [check_case(*case) for case in cases]}
    path = Path(__file__).with_name("042_projection_flatness_exact_output.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
