#!/usr/bin/env python3
"""Exact certificates for C035's rank-one phase / Householder diamond theorem.

Standard-library only.  This verifies actual Gaussian-rational unitary minors,
every marginal of the constructed joint law, its forced added-pair marginal,
and the universal signed exterior lift on a product of two real reflectors.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def lift(x):
        return x if isinstance(x, G) else G(F(x))

    def __add__(self, other):
        y = G.lift(other)
        return G(self.re + y.re, self.im + y.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -G.lift(other)

    def __rsub__(self, other):
        return G.lift(other) + -self

    def __mul__(self, other):
        y = G.lift(other)
        return G(self.re * y.re - self.im * y.im,
                 self.re * y.im + self.im * y.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        y = G.lift(other)
        assert y.norm() != 0
        z = self * y.conj()
        return G(z.re / y.norm(), z.im / y.norm())

    def conj(self):
        return G(self.re, -self.im)

    def norm(self):
        return self.re * self.re + self.im * self.im

    def __bool__(self):
        return bool(self.re or self.im)


def det(matrix):
    a = [[G.lift(x) for x in row] for row in matrix]
    n = len(a)
    result = G(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return G()
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        p = a[k][k]
        result *= p
        for i in range(k + 1, n):
            scale = a[i][k] / p
            for j in range(k + 1, n):
                a[i][j] -= scale * a[k][j]
    return result


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), G())
             for j in range(len(b[0]))] for i in range(len(a))]


def phase_matrix(z, phase):
    z = [G.lift(x) for x in z]
    norm = sum(x.norm() for x in z)
    assert norm > 0 and phase.norm() == 1
    rho = phase - 1
    q = [[G(int(i == j)) + rho * z[i] * z[j].conj() / norm
          for j in range(len(z))] for i in range(len(z))]
    return q, [x.norm() / norm for x in z], rho.norm()


def check_unitary(q):
    n = len(q)
    for i in range(n):
        for j in range(n):
            assert sum((q[k][i].conj() * q[k][j] for k in range(n)), G()) == G(int(i == j))


def projection_law(q, cols):
    return {s: det([[q[i][j] for j in cols] for i in s]).norm()
            for s in combinations(range(len(q)), len(cols))}


def swapped(s, i, j):
    return tuple(sorted(j if x == i else i if x == j else x for x in s))


def add_weight(table, bottom, top, weight):
    key = (tuple(sorted(bottom)), tuple(sorted(top)))
    table[key] = table.get(key, F(0)) + weight


def phase_coupling(masses, gamma, r):
    """Return the full sparse unlabeled diamond coupling, using only rationals."""
    n = len(masses)
    assert 0 <= r <= n - 2 and sum(masses) == 1 and 0 <= gamma <= 4
    a = tuple(range(r))
    p = (r, r + 1)
    c = tuple(range(r + 2, n))
    h = a + p
    alpha = sum((masses[i] for i in a), F(0))
    beta = sum((masses[i] for i in p), F(0))
    eta = sum((masses[i] for i in c), F(0))
    central = 1 - gamma * (alpha * beta + alpha * eta + beta * eta)
    deficit = max(F(0), -central)
    result = {(a, h): central}
    for left, right in ((a, p), (a, c), (p, c)):
        for i in left:
            for j in right:
                add_weight(result, swapped(a, i, j), swapped(h, i, j),
                           gamma * masses[i] * masses[j])
    if deficit:
        assert alpha * beta * eta > 0
        assert deficit <= gamma * min(alpha * beta, alpha * eta, beta * eta)
        for i in a:
            for k in p:
                for j in c:
                    amount = deficit * masses[i] * masses[k] * masses[j] / (alpha * beta * eta)
                    # The embedded oriented triangle a -> c -> p -> a.
                    add_weight(result, a, h, amount)
                    add_weight(result, swapped(a, i, j), swapped(h, k, j), amount)
                    add_weight(result, swapped(a, i, k), swapped(h, i, j), amount)
                    add_weight(result, swapped(a, i, j), swapped(h, i, j), -amount)
                    add_weight(result, swapped(a, i, k), h, -amount)
                    add_weight(result, a, swapped(h, k, j), -amount)
    assert min(result.values()) >= 0
    return {key: val for key, val in result.items() if val}, {
        "alpha": alpha, "beta": beta, "eta": eta,
        "gamma": gamma, "central_before": central, "repair_mass": deficit,
    }


def marginals(table, n, r):
    bottom = {s: F(0) for s in combinations(range(n), r)}
    top = {s: F(0) for s in combinations(range(n), r + 2)}
    middle = {s: F(0) for s in combinations(range(n), r + 1)}
    pair = {s: F(0) for s in combinations(range(n), 2)}
    for (s, t), weight in table.items():
        assert set(s) < set(t) and len(t) - len(s) == 2
        j = tuple(sorted(set(t) - set(s)))
        bottom[s] += weight
        top[t] += weight
        pair[j] += weight
        for i in j:
            middle[tuple(sorted(s + (i,)))] += weight
    return bottom, middle, top, pair


def signed_exterior(q, r):
    n = len(q)
    acols = tuple(range(r))
    ccols = tuple(range(r + 2))
    dcols = (r, r + 1)
    aa = {s: det([[q[i][j] for j in acols] for i in s])
          for s in combinations(range(n), r)}
    cc = {s: det([[q[i][j] for j in ccols] for i in s])
          for s in combinations(range(n), r + 2)}
    dd = {s: det([[q[i][j] for j in dcols] for i in s])
          for s in combinations(range(n), 2)}
    result = {}
    for s, av in aa.items():
        for j in combinations(sorted(set(range(n)) - set(s)), 2):
            t = tuple(sorted(s + j))
            sign = (-1) ** sum(x > y for x in s for y in j)
            result[s, t] = (av * cc[t].conj() * dd[j] * sign).re
    return result


def check_marginals(q, r, table):
    n = len(q)
    a = tuple(range(r))
    ucols, vcols, h = a + (r,), a + (r + 1,), tuple(range(r + 2))
    mu0, muu, muv, mu2 = (projection_law(q, cols) for cols in (a, ucols, vcols, h))
    added = projection_law(q, (r, r + 1))
    b, m, t, pair = marginals(table, n, r)
    assert b == mu0 and t == mu2 and pair == added
    assert all(m[x] == muu[x] + muv[x] for x in m)
    assert sum(table.values()) == 1
    return mu0, muu, muv, mu2


def fraction_text(value):
    return str(value)


def table_records(table):
    return [{"bottom": list(s), "top": list(t), "weight": fraction_text(w)}
            for (s, t), w in sorted(table.items())]


def law_records(law):
    return [{"set": list(s), "mass": fraction_text(w)} for s, w in law.items()]


def verify_case(name, z, phase, r, save=False):
    q, masses, gamma = phase_matrix(z, phase)
    check_unitary(q)
    table, parameters = phase_coupling(masses, gamma, r)
    laws = check_marginals(q, r, table)
    # Fair labels give the equalized real-frame middle marginals exactly.
    if phase == G(-1) and all(not G.lift(x).im for x in z):
        fair = {s: F(0) for s in laws[1]}
        for (s, t), weight in table.items():
            for i in sorted(set(t) - set(s)):
                fair[tuple(sorted(s + (i,)))] += weight / 2
        assert all(fair[s] == (laws[1][s] + laws[2][s]) / 2 for s in fair)
        a = tuple(range(r))
        for s in fair:
            au = det([[q[i][j] for j in a + (r,)] for i in s])
            av = det([[q[i][j] for j in a + (r + 1,)] for i in s])
            assert not au.im and not av.im
            # The missing sqrt(2) is accounted for by dividing squared modulus by 2.
            assert (au + G(0, 1) * av).norm() / 2 == fair[s]
            assert (au - G(0, 1) * av).norm() / 2 == fair[s]
    signed = signed_exterior(q, r)
    check_marginals(q, r, signed)
    summary = {"name": name, "n": len(q), "r": r,
               "positive_atoms": len(table), "minimum_positive_weight": str(min(table.values())),
               "signed_exterior_minimum": str(min(signed.values())),
               **{k: str(v) for k, v in parameters.items()}}
    if save:
        artifact = {
            "case": summary,
            "matrix": [[[str(v.re), str(v.im)] for v in row] for row in q],
            "coupling": table_records(table),
            "bottom": law_records(laws[0]), "middle_u": law_records(laws[1]),
            "middle_v": law_records(laws[2]), "top": law_records(laws[3]),
            "fair_middle": law_records({s: (laws[1][s] + laws[2][s]) / 2 for s in laws[1]}),
        }
        (Path(__file__).parent / (name + "_certificate.json")).write_text(json.dumps(artifact, indent=2) + "\n")
    return summary


def main():
    cases = [
        ("flat_six_reflection", [1] * 6, G(-1), 2, True),
        ("nonuniform_eight_reflection", [1, 2, 1, 1, 2, 2, 1, 2], G(-1), 3, True),
        ("complex_six_phase", [1, 1, 1, 1, 1, 1], G(F(-3, 5), F(4, 5)), 2, True),
        ("complex_ten_phase", [1] * 10, G(F(-99, 101), F(20, 101)), 4, False),
        ("coordinate_phases", [1, G(0, 2), 1, G(0, -1), 2, 2, G(0, 1), 2], G(F(-3, 5), F(4, 5)), 3, False),
        ("bottom_rank_zero", [1, 2, 1, 3, 2], G(-1), 0, False),
        ("top_full_rank", [1, 2, 1, 3, 2], G(-1), 3, False),
        ("zero_update_mass", [1, 2, 0, 0, 3, 2], G(-1), 2, False),
        ("zero_bottom_mass", [0, 0, 1, 2, 3, 2], G(-1), 2, False),
        ("identity_phase", [1, 2, 3, 4, 5, 6], G(1), 2, False),
    ]
    summaries = [verify_case(*case) for case in cases]
    # Non-Householder real frame: the exterior identity is rank-uniform, but
    # its weights can be negative and are not asserted to be a coupling.
    q1, _, _ = phase_matrix([1, 2, 1, 3, 1, 2], G(-1))
    q2, _, _ = phase_matrix([2, -1, 3, 1, 2, 1], G(-1))
    product = matmul(q1, q2)
    check_unitary(product)
    signed = signed_exterior(product, 2)
    check_marginals(product, 2, signed)
    assert min(signed.values()) < 0
    exterior_record = {"matrix": [[[str(v.re), str(v.im)] for v in row] for row in product],
                       "signed_weights": table_records(signed),
                       "minimum": str(min(signed.values()))}
    (Path(__file__).parent / "signed_exterior_example.json").write_text(json.dumps(exterior_record, indent=2) + "\n")
    # Equalizing all middle minors by one U(2) basis change would require one
    # nonzero real normal orthogonal to all these Bloch vectors.  Their exact
    # determinant is nonzero, so no such basis exists for this complex phase.
    qcomplex, _, _ = phase_matrix([1] * 6, G(F(-3, 5), F(4, 5)))
    bloch_rows, bloch_records = [], []
    for s in ((0, 2, 4), (0, 1, 4), (0, 1, 2)):
        au = det([[qcomplex[i][j] for j in (0, 1, 2)] for i in s])
        av = det([[qcomplex[i][j] for j in (0, 1, 3)] for i in s])
        cross = au * av.conj()
        row = [2 * cross.re, 2 * cross.im, au.norm() - av.norm()]
        bloch_rows.append(row)
        bloch_records.append({"set": list(s), "u_amplitude": [str(au.re), str(au.im)],
                              "v_amplitude": [str(av.re), str(av.im)],
                              "bloch_vector": [str(v) for v in row]})
    bloch_det = det(bloch_rows)
    assert bloch_det and not bloch_det.im
    bloch_output = {"rows": bloch_records, "determinant": str(bloch_det.re)}
    (Path(__file__).parent / "equalization_obstruction.json").write_text(json.dumps(bloch_output, indent=2) + "\n")
    output = {"status": "PASS", "exact_cases": summaries,
              "universal_signed_exterior_product_test": {"n": 6, "r": 2,
                                                        "minimum": str(min(signed.values()))},
              "complex_equalization_bloch_determinant": str(bloch_det.re)}
    (Path(__file__).parent / "verified_output.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
