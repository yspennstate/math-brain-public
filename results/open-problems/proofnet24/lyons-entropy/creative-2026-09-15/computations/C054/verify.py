"""Exact C054 certificates. Run from the campaign root with Python + SymPy."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s

OUT = Path(__file__).resolve().parent
n = 6
Id = s.eye(n)
T = s.diag(*([2] * n))
for i in range(n - 1):
    T[i, i + 1] = T[i + 1, i] = -1


def q(x):
    x = s.cancel(x)
    assert x.is_Rational, x
    return Q(int(x.p), int(x.q))


def log_unit(x, terms=48):
    """Outward rational log bounds, for 1 <= x <= 2."""
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    out = Q(0)
    zp = z
    for j in range(terms):
        out += 2 * zp / (2 * j + 1)
        zp *= z * z
    tail = 2 * zp / ((2 * terms + 1) * (1 - z * z))
    return out, out + tail


L2 = log_unit(Q(2))


def log_bounds(x):
    x = Q(x)
    assert x > 0
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return -hi, -lo
    k = 0
    while x > 2:
        x /= 2
        k += 1
    lo, hi = log_unit(x)
    lo, hi = lo + k * L2[0], hi + k * L2[1]
    scale = 10 ** 32
    return Q((lo * scale).__floor__(), scale), Q((hi * scale).__ceil__(), scale)


def linear_logs(terms):
    lo = hi = Q(0)
    for coeff, arg in terms:
        coeff = q(coeff) if not isinstance(coeff, Q) else coeff
        a, b = log_bounds(q(arg) if not isinstance(arg, Q) else arg)
        lo += coeff * (a if coeff >= 0 else b)
        hi += coeff * (b if coeff >= 0 else a)
    return lo, hi


def interval_json(ab):
    return {"lower": str(ab[0]), "upper": str(ab[1]),
            "decimal_display": float((ab[0] + ab[1]) / 2)}


def mat_json(M):
    return [[str(s.re(M[i, j])) + (" + i*(" + str(s.im(M[i, j])) + ")"
            if s.im(M[i, j]) else "") for j in range(M.cols)]
            for i in range(M.rows)]


def sub(M, inds):
    return M.extract(inds, inds)


def jets(K, A):
    atoms = []
    for mask in range(1 << n):
        inds = [i for i in range(n) if mask >> i & 1]
        N = K - s.diag(*[0 if mask >> i & 1 else 1 for i in range(n)])
        p = s.cancel((-1) ** (n - len(inds)) * N.det())
        R = N.inv() * A
        g = s.cancel(p * s.trace(R))
        h = s.cancel(p * (s.trace(R) ** 2 - s.trace(R * R)))
        p, g, h = map(q, (p, g, h))
        assert p > 0
        atoms.append((mask, p, g, h))
    assert sum(v[1] for v in atoms) == 1
    assert sum(v[2] for v in atoms) == 0
    assert sum(v[3] for v in atoms) == 0
    for i in range(n):
        assert sum(v[3] for v in atoms if v[0] >> i & 1) == 0
    return atoms


def case(name, L, A, path_scale=None, split=None):
    K = L * (Id + L).inv()
    atoms = jets(K, A)
    Z = (Id + L).det()
    for mask, p, g, h in atoms:
        inds = [i for i in range(n) if mask >> i & 1]
        assert p == q(sub(L, inds).det() / Z)
    FI = sum(g * g / p for _, p, g, _ in atoms)
    frozen = linear_logs([(-h, p) for _, p, _, h in atoms])
    entropy = frozen[0] - FI, frozen[1] - FI
    assert entropy[1] < 0
    neighbor = linear_logs([(1 - K[i, i], L[i, i] * L.inv()[i, i])
                            for i in range(n)])
    result = {"name": name, "L": mat_json(L), "K": mat_json(K),
              "A": mat_json(A), "FI": str(FI),
              "frozen": interval_json(frozen),
              "entropy": interval_json(entropy),
              "neighbor_budget": interval_json(neighbor),
              "atoms": [{"mask": mask, "p": str(p), "g": str(g), "h": str(h)}
                        for mask, p, g, h in atoms]}
    if path_scale is not None:
        intervals = []
        frozen_terms, budget_terms, imaginary_terms = [], [], []
        for length in range(2, n + 1):
            ratio = s.Rational(length * length, length * length - 1)
            for start in range(n - length + 1):
                inds = list(range(start, start + length))
                mask = sum(1 << i for i in inds)
                G = sub(K, inds).det()
                R = sub(K, inds).inv() * sub(A, inds)
                Gp = s.cancel(G * s.trace(R))
                Gpp = s.cancel(G * (s.trace(R) ** 2 - s.trace(R * R)))
                assert q(G) == sum(p for m, p, _, _ in atoms if m & mask == mask)
                assert q(Gp) == sum(g for m, _, g, _ in atoms if m & mask == mask)
                assert q(Gpp) == sum(h for m, _, _, h in atoms if m & mask == mask)
                frozen_terms.append((Gpp, ratio))
                budget_terms.append((1 - G, ratio))
                intervals.append({"sites": inds, "ratio": str(ratio),
                                  "probability": str(G), "second_jet": str(Gpp)})
                if split is not None:
                    X, B = split
                    RX = sub(K, inds).inv() * sub(X, inds)
                    RB = sub(K, inds).inv() * sub(B, inds)
                    imag_cost = s.cancel(-G * s.trace(RB * RB))
                    real_cost = s.cancel(G * (s.trace(RX * RX) - s.trace(RX) ** 2))
                    assert imag_cost >= 0 and real_cost >= 0
                    assert Gpp == -imag_cost - real_cost
                    imaginary_terms.append((imag_cost, ratio))
        for mask, _, _, _ in atoms:
            inds = [i for i in range(n) if mask >> i & 1]
            expected = s.Integer(2 * path_scale) ** len(inds)
            for row in intervals:
                if all(mask >> i & 1 for i in row["sites"]):
                    expected /= s.Rational(row["ratio"])
            assert sub(L, inds).det() == expected
        ff = linear_logs(frozen_terms)
        assert max(ff[0], frozen[0]) <= min(ff[1], frozen[1])
        budget = linear_logs(budget_terms)
        assert budget[1] < neighbor[0]
        result["exact_event_budget"] = interval_json(budget)
        result["intervals"] = intervals
        if split is not None:
            ja = jets(K, split[0])
            jb = jets(K, s.I * split[1])
            for f, x, b in zip(atoms, ja, jb):
                assert f[2] == x[2] and b[2] == 0
                assert f[3] == x[3] + b[3]
            result["imaginary_cost"] = interval_json(linear_logs(imaginary_terms))
    print(name, "FI", float(FI), "F''", result["frozen"]["decimal_display"],
          "H''", result["entropy"]["decimal_display"], flush=True)
    return result


# Exact neighboring Schur-complement resolvent identity; the two blocks do not commute.
S, J, i = [0, 1], [2, 3], 4
C = sub(T, J) - T.extract(J, S) * sub(T, S).inv() * T.extract(S, J)
b = T.extract(J, [i]) - T.extract(J, S) * sub(T, S).inv() * T.extract(S, [i])
c = T[i, i] - (T.extract([i], S) * sub(T, S).inv() * T.extract(S, [i]))[0]
D = C - b * b.T / c
assert C * D != D * C
for t in (s.Integer(0), s.Rational(1, 3), s.Integer(2)):
    R = (C + t * s.eye(len(J))).inv()
    denominator = c - (b.T * R * b)[0]
    assert denominator > 0
    assert (D + t * s.eye(len(J))).inv() - R == R * b * b.T * R / denominator
assert C.det() / D.det() > 1

# A full-rank (3,3) direction whose real part has inertia (1,1).
B = s.zeros(n)
for i in range(n):
    for j in range(i + 1, n):
        B[i, j], B[j, i] = 1, -1
X = s.diag(s.Rational(1, 10), 0, 0, 0, 0, -s.Rational(1, 10))
assert B.det() == 1
assert sum(x * x for x in B.inv()) == 30
assert s.Rational(1, 100) * 30 < 1
low = case("unrestricted_phase_with_rank_two_real_part", T, X + s.I * B,
           path_scale=1, split=(X, B))
assert Q(low["exact_event_budget"]["lower"]) > Q(3, 2)

# High-rank positive frozen curvature compensated by the neighboring-minor budget.
V = s.eye(n)
for i in range(n - 1):
    V[i + 1, i] = s.Rational(1, 5)
A = V * s.diag(1, 2, 3, 4, 5, 6) * V.T
high = case("full_hessian_saturation", 8 * T, A, path_scale=8)
assert Q(high["frozen"]["lower"]) > 0
assert Q(high["neighbor_budget"]["upper"]) < Q(3, 4)
assert Q(high["neighbor_budget"]["lower"]) > Q("0.72082363926848")
assert Q(high["neighbor_budget"]["upper"]) < Q("0.72082363926850")
assert Q(high["entropy"]["upper"]) < -Q(3, 8) * Q(high["FI"])
assert log_bounds(Q(64, 7))[0] > 2

# A connected, genuinely rank-six indefinite finite segment in the convex theorem.
L0 = 120 * T
L1 = 60 * T + 120 * Id
K0 = L0 * (Id + L0).inv()
K1 = L1 * (Id + L1).inv()
Aseg = K1 - K0
Adj = 2 * Id - T
Sign = s.diag(*[(-1) ** i for i in range(n)])
assert Sign * Adj * Sign == -Adj
assert Adj.det() == -1
assert Aseg == 60 * Adj * (Id + L0).inv() * (Id + L1).inv()
assert Aseg.det() != 0
assert max(sum(abs(T.inv()[i, j]) for j in range(n)) for i in range(n)) == 6
assert max(sum(abs(T[i, j]) for j in range(n)) for i in range(n)) == 4
assert log_bounds(Q(625, 96))[1] < 2
checks = []
for t in (s.Integer(0), s.Rational(1, 4), s.Rational(1, 2), s.Rational(3, 4), s.Integer(1)):
    Kt = (1 - t) * K0 + t * K1
    Lt = (Id - Kt).inv() - Id
    assert all(Lt[i, j] <= 0 for i in range(n) for j in range(n) if i != j)
    assert all(sub(Lt, list(range(k))).det() > 0 for k in range(1, n + 1))
    checks.append({"t": str(t), "L": mat_json(Lt)})
Lmid = (Id - (K0 + K1) / 2).inv() - Id
mid = case("rank_six_indefinite_segment_midpoint", Lmid, Aseg)
assert Q(mid["frozen"]["lower"]) > 0
assert Q(mid["entropy"]["upper"]) < -Q(11, 21) * Q(mid["FI"])

result = {"status": "PASS", "operator_neighbor": {"C": mat_json(C), "D": mat_json(D),
          "determinant_ratio": str(C.det() / D.det())},
          "cases": [low, high, mid], "segment": {"T": mat_json(T), "K0": mat_json(K0),
          "K1": mat_json(K1), "A": mat_json(Aseg), "inertia": [3, 3],
          "minimum_eigenvalue_lower_bound_T": "1/6", "condition_upper_bound_T": "24",
          "full_hessian_FI_gap_lower_bound": "11/21", "odds_checks": checks}}
(OUT / "certificate.json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS: 192 exact atoms; neighboring operator resolvents; high-rank phase squares; "
      "positive frozen curvature paid by Fisher; connected rank-six indefinite segment.")
