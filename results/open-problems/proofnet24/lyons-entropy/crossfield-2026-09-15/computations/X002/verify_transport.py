"""Exact, deterministic checks for X002's signed cube transport identities."""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as s


def sub(M, rows, cols=None):
    return M.extract(rows, rows if cols is None else cols)


def conditioned(K, A, B, x):
    n = K.rows
    R = [i for i in range(n) if i not in B]
    M = sub(K, R) - s.diag(*[1 - x[i] for i in R])
    q = (-1) ** sum(1 - x[i] for i in R) * M.det()
    if R:
        C = sub(K, B) - sub(K, B, R) * M.inv() * sub(K, R, B)
        V = sub(A, B) - sub(A, B, R) * M.inv() * sub(K, R, B)
    else:
        C, V = sub(K, B), sub(A, B)
    return s.simplify(q), s.simplify(C), s.simplify(V)


def atom_jet(K, A, x):
    n = K.rows
    M = K - s.diag(*[1 - b for b in x])
    sign = (-1) ** sum(1 - b for b in x)
    p = sign * M.det()
    jet1 = 0
    jet2 = 0
    for i in range(n):
        Mi = M.copy()
        Mi[i, :] = A[i, :]
        jet1 += sign * Mi.det()
    for i, j in combinations(range(n), 2):
        Mij = M.copy()
        Mij[i, :] = A[i, :]
        Mij[j, :] = A[j, :]
        jet2 += 2 * sign * Mij.det()
    return tuple(s.simplify(v) for v in (p, jet1, jet2))


def check_case(K, A):
    n = K.rows
    atoms = list(product([0, 1], repeat=n))
    jets = {x: atom_jet(K, A, x) for x in atoms}
    assert all(v[0] > 0 for v in jets.values())
    assert sum(v[0] for v in jets.values()) == 1
    assert sum(v[1] for v in jets.values()) == 0
    assert sum(v[2] for v in jets.values()) == 0
    for x in atoms:
        div_J = 0
        div_Q = 0
        div_imag = 0
        for i in range(n):
            q, C, V = conditioned(K, A, [i], x)
            J = s.simplify(q * V[0, 0])
            hodge = A[i, i] * q
            gamma_div = 0
            for j in range(n):
                if j == i:
                    continue
                q2, C2, _ = conditioned(K, A, [i, j], x)
                Z = s.simplify(q2 * A[i, j] * C2[1, 0])
                hodge -= (2 * x[j] - 1) * Z
                gamma_div -= (2 * x[j] - 1) * s.im(Z)
            assert s.simplify(J - hodge) == 0
            assert s.simplify(s.im(J) - gamma_div) == 0
            div_J += (2 * x[i] - 1) * s.re(J)
            div_imag += (2 * x[i] - 1) * s.im(J)
        for i, j in combinations(range(n), 2):
            q, C, V = conditioned(K, A, [i, j], x)
            Q = s.simplify(q * s.re(V.det()))
            E = (V + V.conjugate().T) / 2
            G = (V - V.conjugate().T) / (2 * s.I)
            assert s.simplify(s.re(V.det()) - E.det() + G.det()) == 0
            div_Q += 2 * (2 * x[i] - 1) * (2 * x[j] - 1) * Q
            face = {}
            for a, b in product([0, 1], repeat=2):
                y = list(x)
                y[i], y[j] = a, b
                face[a, b] = jets[tuple(y)][0] / q
            assert s.simplify(face[0, 1] * face[1, 0]
                              - face[0, 0] * face[1, 1]
                              - C[0, 1] * C[1, 0]) == 0
        assert s.simplify(div_J - jets[x][1]) == 0
        assert s.simplify(div_Q - jets[x][2]) == 0
        assert s.simplify(div_imag) == 0
    I = sum(dp**2 / p for p, dp, _ in jets.values())
    direct = -I - sum(ddp * s.log(p) for p, _, ddp in jets.values())
    face_term = 0
    for i, j in combinations(range(n), 2):
        R = [r for r in range(n) if r not in (i, j)]
        for config in product([0, 1], repeat=len(R)):
            x = [0] * n
            for r, bit in zip(R, config):
                x[r] = bit
            q, _, V = conditioned(K, A, [i, j], x)
            ps = {}
            for a, b in product([0, 1], repeat=2):
                x[i], x[j] = a, b
                ps[a, b] = jets[tuple(x)][0]
            lam = s.log(ps[0, 1] * ps[1, 0] / (ps[0, 0] * ps[1, 1]))
            face_term += 2 * q * s.re(V.det()) * lam
    err = s.N(direct - (-I + face_term), 50)
    assert abs(float(s.re(err))) < 1e-45
    return {"n": n, "exact_atom_and_transport_checks": "PASS",
            "entropy_identity_error": str(err), "H_second": str(s.N(direct, 25))}


def obstruction():
    K = s.eye(3) / 2 + (s.ones(3) - s.eye(3)) / 10
    A = s.Matrix([[0, s.I, 10 * s.I], [-s.I, 0, 0], [-10 * s.I, 0, 0]])
    jets = {x: atom_jet(K, A, x) for x in product([0, 1], repeat=3)}
    assert all(dp == 0 for p, dp, ddp in jets.values())
    q, C, V = conditioned(K, A, [0, 1], [0, 0, 1])
    Q = s.simplify(q * s.re(V.det()))
    assert Q == s.Rational(1, 2)
    c = C[0, 1]
    assert c == s.Rational(2, 25)
    face = {ab: jets[(ab[0], ab[1], 1)][0] for ab in product([0, 1], repeat=2)}
    ratio = s.factor(face[0, 1] * face[1, 0] / (face[0, 0] * face[1, 1]))
    assert ratio > 1
    # Positive face acceleration despite every canonical real edge current vanishing.
    for x in product([0, 1], repeat=3):
        for i in range(3):
            qi, _, Vi = conditioned(K, A, [i], x)
            assert s.re(qi * Vi[0, 0]) == 0
    return {"K": str(K), "A": str(A), "positive_face_Q": str(Q),
            "face_log_ratio": str(ratio), "conditional_C": str(C),
            "conditional_V": str(V), "all_real_currents_and_scores_zero": True,
            "H_second": str(s.N(-sum(ddp * s.log(p) for p, dp, ddp in jets.values()), 25))}


if __name__ == "__main__":
    K = s.diag(s.Rational(2, 5), s.Rational(9, 20), s.Rational(11, 20), s.Rational(3, 5))
    A = s.diag(s.Rational(1, 7), s.Rational(-1, 5), s.Rational(1, 6), s.Rational(1, 9))
    for i, j in combinations(range(4), 2):
        K[i, j] = s.Rational(i + j + 1, 120) + s.I * s.Rational(i - j, 150)
        K[j, i] = s.conjugate(K[i, j])
        A[i, j] = s.Rational(2 * i - j + 1, 30) + s.I * s.Rational(i + j + 1, 35)
        A[j, i] = s.conjugate(A[i, j])
    results = {"dense_complex_case": check_case(K, A), "local_obstruction": obstruction()}
    out = Path(__file__).with_name("results.json")
    out.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
