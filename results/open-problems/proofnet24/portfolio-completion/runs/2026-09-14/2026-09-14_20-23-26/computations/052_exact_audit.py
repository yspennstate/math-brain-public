#!/usr/bin/env python3
"""Exact independent certificate for the archived W--E5 perturbation.

Only the Python standard library is required.  Sparse polynomials use exact
fractions.  Run from the research-session root; stdout is the certificate.
The inequalities and universal support lemma are proved in agents/052.md.
"""

from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform


NAMES = ("x1", "x2", "x3", "x4", "x5", "eps", "s", "t")
NV = len(NAMES)
ZERO_MONOMIAL = (0,) * NV
CHECKS = []


class Poly:
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {m: F(c) for m, c in value.items() if c}
        else:
            self.terms = {} if value == 0 else {ZERO_MONOMIAL: F(value)}

    @classmethod
    def variable(cls, index):
        monomial = list(ZERO_MONOMIAL)
        monomial[index] = 1
        return cls({tuple(monomial): F(1)})

    def __add__(self, other):
        terms = dict(self.terms)
        for m, c in Poly(other).terms.items():
            terms[m] = terms.get(m, F(0)) + c
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        terms = {}
        for m, c in self.terms.items():
            for n, d in Poly(other).terms.items():
                mn = tuple(a + b for a, b in zip(m, n))
                terms[mn] = terms.get(mn, F(0)) + c * d
        return Poly(terms)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (F(1) / F(scalar))

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        answer = Poly(1)
        for _ in range(exponent):
            answer = answer * self
        return answer

    def derivative(self, index):
        terms = {}
        for m, c in self.terms.items():
            if m[index]:
                n = list(m)
                n[index] -= 1
                terms[tuple(n)] = c * m[index]
        return Poly(terms)

    def coefficient(self, index, exponent):
        return Poly({tuple(0 if i == index else v for i, v in enumerate(m)): c
                     for m, c in self.terms.items() if m[index] == exponent})

    def substitute(self, substitutions):
        result = Poly(0)
        for m, c in self.terms.items():
            term = Poly(c)
            for i, power in enumerate(m):
                term *= Poly(substitutions.get(i, Poly.variable(i))) ** power
            result += term
        return result

    def constant(self):
        assert all(m == ZERO_MONOMIAL for m in self.terms)
        return self.terms.get(ZERO_MONOMIAL, F(0))

    def serialized(self):
        return [{"coefficient": str(c),
                 "powers": {name: power for name, power in zip(NAMES, m) if power}}
                for m, c in sorted(self.terms.items())]


def equal(actual, expected, name):
    difference = Poly(actual) - Poly(expected)
    assert not difference.terms, (name, difference.serialized())
    CHECKS.append(name)


def solve(matrix, vector):
    n = len(vector)
    rows = [[F(v) for v in matrix[i]] + [F(vector[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        denominator = rows[j][j]
        rows[j] = [v / denominator for v in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def determinant(matrix):
    rows = [[F(v) for v in row] for row in matrix]
    result = F(1)
    for j in range(len(rows)):
        possible = [i for i in range(j, len(rows)) if rows[i][j]]
        if not possible:
            return F(0)
        pivot = possible[0]
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            result *= -1
        value = rows[j][j]
        result *= value
        for i in range(j + 1, len(rows)):
            factor = rows[i][j] / value
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[j])]
    return result


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def tensor():
    return [[[F(0) for _ in range(5)] for _ in range(5)] for _ in range(5)]


P, H = tensor(), tensor()


def setp(i, j, k, value):
    P[i][j][k] = P[j][i][k] = F(value)


for i in range(3):
    for k in range(3):
        if k != i:
            setp(i, i, k, F(1, 2))
    for j in range(i + 1, 3):
        k = next(k for k in range(3) if k not in {i, j})
        setp(i, j, k, 1)
    setp(i, 3, 4, 1)
    setp(i, 4, 3, 1)
setp(3, 3, 4, 1)
setp(4, 4, 3, 1)
for k in range(3):
    setp(3, 4, k, F(1, 3))
for i in range(5):
    for j in range(5):
        allowed = [k for k in range(5) if k not in {i, j}]
        for k in allowed:
            H[i][j][k] = F(1, len(allowed))
for i in range(5):
    for j in range(5):
        allowed = [k for k in range(5) if k not in {i, j}]
        for array in [P, H]:
            assert sum(array[i][j]) == 1
            assert all(array[i][j][k] >= 0 for k in range(5))
            assert all(array[i][j][k] == array[j][i][k] for k in range(5))
            assert all(array[i][j][k] == 0 for k in {i, j})
        assert all(H[i][j][k] > 0 for k in allowed)
CHECKS.append("All 25 ordered coefficient rows: stochastic, symmetric, nonnegative, strictly non-Volterra; E positive on allowed entries")

x = [Poly.variable(i) for i in range(5)]
eps, s, t = [Poly.variable(i) for i in range(5, 8)]
total = sum(x)
W = [sum(P[i][j][k] * x[i] * x[j] for i in range(5) for j in range(5)) for k in range(5)]
E = [sum(H[i][j][k] * x[i] * x[j] for i in range(5) for j in range(5)) for k in range(5)]
V = [(1 - eps) * w + eps * e for w, e in zip(W, E)]
for k in range(3):
    a, b = [i for i in range(3) if i != k]
    equal(W[k], (x[a] ** 2 + x[b] ** 2) / 2 + 2 * x[a] * x[b] + F(2, 3) * x[3] * x[4], f"W_{k+1} from tensor")
equal(W[3], x[4] * (2 * sum(x[:3]) + x[4]), "W_4 from tensor")
equal(W[4], x[3] * (2 * sum(x[:3]) + x[3]), "W_5 from tensor")
for i in range(5):
    equal(E[i], (total - x[i]) ** 2 / 3 - sum(x[j] ** 2 for j in range(5) if j != i) / 12, f"E_{i+1} formula")
    for j in range(i + 1, 5):
        equal(E[i] - E[j], -(x[i] - x[j]) * (F(2, 3) * total - F(5, 12) * (x[i] + x[j])), f"E difference {i+1},{j+1}")
for i in range(3):
    for j in range(i + 1, 3):
        k = next(k for k in range(3) if k not in {i, j})
        equal(W[i] - W[j], -(x[i] - x[j]) * ((x[i] + x[j]) / 2 + 2 * x[k]), f"W first-group difference {i+1},{j+1}")
equal(W[3] - W[4], -(x[3] - x[4]) * (2 * total - x[3] - x[4]), "W last-group difference")
equal(sum(W), total ** 2, "W homogeneous stochastic sum")
equal(sum(E), total ** 2, "E homogeneous stochastic sum")
equal(sum(V), total ** 2, "V homogeneous stochastic sum")

r = (1 - 2 * s) / 3
symmetric = {0: r, 1: r, 2: r, 3: s, 4: s}
ws = [v.substitute(symmetric) for v in W]
es = [v.substitute(symmetric) for v in E]
vs = [v.substitute(symmetric) for v in V]
for k in range(3):
    equal(ws[k], (1 - 4 * s + 6 * s ** 2) / 3, f"symmetric W_{k+1}")
    equal(es[k], (7 + 20 * s - 5 * s ** 2) / 54, f"symmetric E_{k+1}")
for k in (3, 4):
    equal(ws[k], s * (2 - 3 * s), f"symmetric W_{k+1}")
    equal(es[k], (11 - 20 * s + 5 * s ** 2) / 36, f"symmetric E_{k+1}")
Q = 36 * (vs[3] - s)
A, B, C = [Q.coefficient(6, power) for power in (2, 1, 0)]
equal(Q, (-108 + 113 * eps) * s ** 2 + (36 - 92 * eps) * s + 11 * eps, "scalar fixed-point polynomial")
for value, expected in [(0, 11 * eps), (F(1, 2), -9 - F(27, 4) * eps), (F(1, 5), F(72, 25) * (1 - eps)), (F(1, 3), -F(64, 9) * eps)]:
    equal(Q.substitute({6: value}), expected, f"Q endpoint s={value}")
discriminant = B ** 2 - 4 * A * C
equal(discriminant, 36 * (36 - 52 * eps + 97 * eps ** 2), "discriminant")
equal(discriminant / 36, 97 * (eps - F(26, 97)) ** 2 + F(2816, 97), "positive completed-square discriminant")
d = -B + t
equal(4 * A * C ** 2 + 2 * B * C * d + C * d ** 2, C * (t ** 2 - discriminant), "rationalized root after denominator clearing")
equal(4 * A * C + (B + t) * d, t ** 2 - discriminant, "physical Q_s equals negative square root")
equal(Q.substitute({5: F(108, 113), 6: F(33, 163)}), 0, "linear-case root 33/163")
equal(Q.substitute({5: 1}), (5 * s - 1) * (s - 11), "equiprobable endpoint roots")
for sval, expected in [(0, F(-11, 36)), (F(1, 3), F(-16, 81))]:
    dqde = Q.derivative(5).substitute({5: 0, 6: sval}).constant()
    dqds = Q.derivative(6).substitute({5: 0, 6: sval}).constant()
    assert -dqde / dqds == expected
CHECKS.append("Both implicit scalar derivatives at eps=0")

JV = [[v.derivative(j).substitute(symmetric) for j in range(5)] for v in V]
mu_F = -((1 - eps) * (1 - 2 * s) + eps * (7 + 10 * s) / 18)
mu_last = -((1 - eps) * (2 - 2 * s) + eps * (F(2, 3) - F(5, 6) * s))
nu = vs[3].derivative(6)
vectors = [([1, -1, 0, 0, 0], mu_F), ([1, 0, -1, 0, 0], mu_F),
           ([0, 0, 0, 1, -1], mu_last), ([F(-2, 3)] * 3 + [1, 1], nu)]
for number, (vector, eigenvalue) in enumerate(vectors):
    assert sum(vector) == 0
    for k, output in enumerate(matvec(JV, vector)):
        equal(output, eigenvalue * vector[k], f"tangent eigenvector {number+1}, coordinate {k+1}")
equal(nu, 1 + Q.derivative(6) / 36, "symmetric-line eigenvalue identity")
equal((1 - eps) * F(4, 3) + eps * F(7, 18), F(4, 3) - F(17, 18) * eps, "instability lower bound")
equal((F(4, 3) - F(17, 18) * eps).substitute({5: F(6, 17)}), 1, "instability interval endpoint")

points = {}
JW = [[v.derivative(j) for j in range(5)] for v in W]
for label, point, expected_derivative, expected_det in [
    ("p", [F(1, 3)] * 3 + [F(0), F(0)], [F(11, 54)] * 3 + [F(-11, 36)] * 2, F(-12)),
    ("q", [F(1, 9)] * 3 + [F(1, 3)] * 2, [F(32, 243)] * 3 + [F(-16, 81)] * 2, F(112, 27)),
]:
    sub = dict(enumerate(point))
    for i in range(5):
        equal(W[i].substitute(sub), point[i], f"archived fixed point {label}, coordinate {i+1}")
    J = [[entry.substitute(sub).constant() for entry in row] for row in JW]
    forcing = [(E[i] - W[i]).substitute(sub).constant() for i in range(5)]
    tangent = [[J[i][j] - J[i][4] for j in range(4)] for i in range(4)]
    I_minus = [[F(i == j) - tangent[i][j] for j in range(4)] for i in range(4)]
    det = determinant(I_minus)
    assert det == expected_det
    derivative = solve(I_minus, forcing[:4])
    derivative.append(-sum(derivative))
    assert derivative == expected_derivative
    assert [derivative[i] - v for i, v in enumerate(matvec(J, derivative))] == forcing
    CHECKS.append(f"Full affine implicit derivative and nondegeneracy at {label}")
    points[label] = {"point": list(map(str, point)), "DW": [[str(v) for v in row] for row in J],
                     "forcing_E_minus_W": list(map(str, forcing)),
                     "branch_derivative": list(map(str, derivative)),
                     "det_I_minus_DW_tangent": str(det)}
assert [[points["p"]["DW"][i][j] for j in (3, 4)] for i in (3, 4)] == [["0", "2"], ["2", "0"]]
for basis, expected in [([1, 0], [F(-1, 3), F(-2, 3)]), ([0, 1], [F(-2, 3), F(-1, 3)])]:
    assert solve([[1, -2], [-2, 1]], basis) == expected
CHECKS.append("Negative inverse of I minus boundary transverse Jacobian")

snapshot = Path(__file__).resolve().parent / "052_snapshot_20260914T223847.733197Z"
manifest = json.loads((snapshot / "manifest.json").read_text())
for item in manifest["files"]:
    data = (snapshot / item["path"]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item["sha256"]
    assert len(data) == item["bytes"]
CHECKS.append("All six input snapshot SHA256 hashes and byte counts")
source_data = (snapshot / "sources/qso_fixed_points.tex").read_bytes()
git_blob = hashlib.sha1(b"blob " + str(len(source_data)).encode() + b"\0" + source_data).hexdigest()
assert git_blob == "424677e34bc27529aa21d8254a278b4e8b375ea9"
assert source_data.endswith(b"\n\n")
canonical_bytes = source_data[:-1]
canonical_blob = hashlib.sha1(b"blob " + str(len(canonical_bytes)).encode() + b"\0" + canonical_bytes).hexdigest()
assert canonical_blob == "87ba2b2a6d0747c942dba830a98082b6705d2664"
CHECKS.append("Local manuscript has exactly one extra terminal LF relative to recorded archival Git blob")

print(json.dumps({
    "status": "PASS", "python": platform.python_version(),
    "arithmetic": "fractions.Fraction; sparse polynomial identities; exact Gaussian elimination",
    "check_count": len(CHECKS), "checks": CHECKS,
    "Q": Q.serialized(), "discriminant": discriminant.serialized(),
    "points": points, "local_source_git_blob_sha1": git_blob,
    "canonical_source_after_removing_one_final_LF": {
        "bytes": len(canonical_bytes), "git_blob_sha1": canonical_blob,
        "sha256": hashlib.sha256(canonical_bytes).hexdigest()},
    "source_snapshot": str(snapshot.relative_to(snapshot.parent.parent)),
    "source_manifest": manifest,
    "scope": "Finite identities are checked here. Sign/interval arguments, the support lemma, and four-type uniqueness are proved in agents/052.md. No floating-point root count or formal proof-assistant verification is claimed."
}, indent=2))
