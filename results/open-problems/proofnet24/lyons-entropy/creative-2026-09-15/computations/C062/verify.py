#!/usr/bin/env python3
"""Exact six-site satellite example and high-precision entropy illustrations.

Run from any directory: python computations/C062/verify.py
The general theorem is proved in agents/C062.md. Numerical inequalities here
illustrate that proof; exact assertions certify the stated finite example.
"""

from itertools import product
from pathlib import Path
import json

import mpmath as mp
import sympy as sp


OUT = Path(__file__).resolve().parent
Q = sp.Rational
I = sp.I
mp.mp.dps = 70

A0 = sp.Matrix([[Q(2, 5), Q(1, 25) + I / 50],
                [Q(1, 25) - I / 50, Q(1, 2)]])
A1 = sp.Matrix([[Q(11, 20), (1 - I) / 30],
                [(1 + I) / 30, Q(9, 20)]])
C = [sp.Matrix([[Q(2, 5), Q(1, 12)], [Q(1, 12), Q(3, 5)]]),
     sp.Matrix([[Q(9, 20), (1 + 2 * I) / 40],
                [(1 - 2 * I) / 40, Q(11, 20)]])]
B = [sp.Matrix([[Q(1, 20), I / 30], [(1 + I) / 40, Q(1, 25)]]),
     sp.Matrix([[Q(1, 30), (1 + I) / 50], [I / 40, -Q(1, 20)]])]
z0 = [sp.Integer(1), (1 + I) / 2]
z1 = [I / 2, 1 - I / 2]
t = Q(2, 5)


def clean(x):
    return sp.expand_complex(sp.cancel(x)).simplify()


def abs2(x):
    return clean(x * sp.conjugate(x))


def h2_law(M):
    p11 = clean(M.det())
    return {0: clean(1 - M.trace() + p11),
            1: clean(M[0, 0] - p11),
            2: clean(M[1, 1] - p11),
            3: p11}


q = [h2_law(Cj) for Cj in C]
D = []
for Cj, Bj in zip(C, B):
    Dj = {}
    for y in range(4):
        Qy = Cj - sp.diag(*[int(not (y >> k) & 1) for k in range(2)])
        Dj[y] = (Bj * Qy.inv() * Bj.H).applyfunc(clean)
    D.append(Dj)


def core(A, s, y):
    return (A - sum((s[j] * D[j][y[j]] for j in range(2)),
                    sp.zeros(2))).applyfunc(clean)


def conditional_law(A, s):
    result = {}
    for y in product(range(4), repeat=2):
        qy = q[0][y[0]] * q[1][y[1]]
        for x, p in h2_law(core(A, s, y)).items():
            result[x | (y[0] << 2) | (y[1] << 4)] = clean(qy * p)
    assert clean(sum(result.values())) == 1
    assert all(p > 0 for p in result.values())
    return result


def kernel(A, z):
    K = sp.zeros(6)
    K[:2, :2] = A
    for j in range(2):
        a = 2 + 2 * j
        K[a:a + 2, a:a + 2] = C[j]
        K[:2, a:a + 2] = z[j] * B[j]
        K[a:a + 2, :2] = sp.conjugate(z[j]) * B[j].H
    return K.applyfunc(clean)


def determinant_equivalent_kernel(A, s):
    """Principal-minor equivalent to Hermitian cross sqrt(s_j)*B_j.

    For positive strengths, conjugate that Hermitian kernel by the diagonal
    similarity diag(I_2, s_1^-1/2 I_2, s_2^-1/2 I_2). Zero follows polynomially.
    All entries here are rational complex numbers, avoiding radical arithmetic.
    """
    K = sp.zeros(6)
    K[:2, :2] = A
    for j in range(2):
        a = 2 + 2 * j
        K[a:a + 2, a:a + 2] = C[j]
        K[:2, a:a + 2] = s[j] * B[j]
        K[a:a + 2, :2] = B[j].H
    return K.applyfunc(clean)


def atom_law(K):
    result = {}
    for mask in range(64):
        absent = [int(not (mask >> k) & 1) for k in range(6)]
        atom_matrix = K - sp.diag(*absent)
        result[mask] = clean((-1) ** sum(absent)
                             * atom_matrix.det(method="domain-ge"))
    return result


def rational_abs_upper(x):
    re, im = clean(x).as_real_imag()
    return abs(re) + abs(im)


def gershgorin(K):
    lower, upper = [], []
    for i in range(K.rows):
        radius = sum(rational_abs_upper(K[i, j])
                     for j in range(K.cols) if i != j)
        lower.append(clean(K[i, i] - radius))
        upper.append(clean(1 - K[i, i] - radius))
    assert min(lower) > 0 and min(upper) > 0
    return {"lower_margins": list(map(str, lower)),
            "upper_margins": list(map(str, upper)),
            "uniform_margin": str(min(lower + upper))}


def marginal(p, coordinates):
    result = {}
    for mask, value in p.items():
        key = sum(((mask >> k) & 1) << j
                  for j, k in enumerate(coordinates))
        result[key] = result.get(key, sp.S.Zero) + value
    return {key: clean(value) for key, value in result.items()}


def number(x):
    return mp.mpf(str(sp.N(x, 80)))


def entropy(p):
    return -mp.fsum(number(v) * mp.log(number(v)) for v in p.values() if v)


def mutual_information(p, left, right):
    return (entropy(marginal(p, left)) + entropy(marginal(p, right))
            - entropy(marginal(p, list(left) + list(right))))


def finite(x):
    return mp.nstr(x, 55)


At = ((1 - t) * A0 + t * A1).applyfunc(clean)
zt = [clean((1 - t) * z0[j] + t * z1[j]) for j in range(2)]
s0 = list(map(abs2, z0))
s1 = list(map(abs2, z1))
sbar = [clean((1 - t) * s0[j] + t * s1[j]) for j in range(2)]
st = list(map(abs2, zt))
delta = [clean(t * (1 - t) * abs2(z1[j] - z0[j])) for j in range(2)]
lam = [clean(delta[j] / sbar[j]) for j in range(2)]
assert all(clean(sbar[j] - delta[j] - st[j]) == 0 for j in range(2))

states = {"endpoint_0": (A0, s0), "endpoint_1": (A1, s1),
          "target": (At, st), "auxiliary": (At, sbar)}
weights = {}
for R in range(4):
    weights[R] = clean(sp.prod(lam[j] if (R >> j) & 1 else 1 - lam[j]
                               for j in range(2)))
    if R:
        states[f"remove_{R}"] = (At, [0 if (R >> j) & 1 else sbar[j]
                                      for j in range(2)])
assert sum(weights.values()) == 1

laws = {}
checked_atoms = 0
for name, (A, s) in states.items():
    p = conditional_law(A, s)
    direct = atom_law(determinant_equivalent_kernel(A, s))
    assert p == direct, name
    checked_atoms += 64
    laws[name] = p

for name, A, z in [("endpoint_0", A0, z0),
                   ("endpoint_1", A1, z1), ("target", At, zt)]:
    assert atom_law(kernel(A, z)) == laws[name], name
    checked_atoms += 64

# Check every conditional matrix identity exactly, not only its entropy.
checked_conditional_identities = 0
for y in product(range(4), repeat=2):
    Mbar = core(At, sbar, y)
    assert Mbar == ((1 - t) * core(A0, s0, y)
                   + t * core(A1, s1, y)).applyfunc(clean)
    MR_mean = sp.zeros(2)
    for R, w in weights.items():
        sr = [0 if (R >> j) & 1 else sbar[j] for j in range(2)]
        MR_mean += w * core(At, sr, y)
    assert core(At, st, y) == MR_mean.applyfunc(clean)
    checked_conditional_identities += 2

Llaw = laws["auxiliary"]
H = {name: entropy(p) for name, p in laws.items()}
gamma = H["target"] - number(1 - t) * H["endpoint_0"] - number(t) * H["endpoint_1"]
Jend = H["auxiliary"] - number(1 - t) * H["endpoint_0"] - number(t) * H["endpoint_1"]
Jremove = H["target"] - mp.fsum(number(w) * H["auxiliary" if R == 0 else f"remove_{R}"]
                                for R, w in weights.items())
information_by_R = {}
for R in range(4):
    left = [2 + 2 * j + k for j in range(2) if (R >> j) & 1 for k in range(2)]
    right = [0, 1] + [2 + 2 * j + k for j in range(2) if not (R >> j) & 1
                     for k in range(2)]
    information_by_R[R] = mutual_information(Llaw, left, right)
    expected_difference = H["auxiliary" if R == 0 else f"remove_{R}"] - H["auxiliary"]
    assert abs(information_by_R[R] - expected_difference) < mp.mpf("1e-65")
information_term = mp.fsum(number(weights[R]) * information_by_R[R] for R in range(4))
single_MI = [mutual_information(Llaw, [2 + 2*j, 3 + 2*j], [0, 1]) for j in range(2)]
additive_MI = mp.fsum(number(lam[j]) * single_MI[j] for j in range(2))
max_B4 = [max(abs2(x) ** 2 for x in Bj) for Bj in B]
explicit_bound = clean(8 * t * (1 - t)
                       * sum(abs2(z1[j] - z0[j]) * sbar[j] * max_B4[j]
                             for j in range(2)))
assert abs(gamma - Jend - Jremove - information_term) < mp.mpf("1e-65")
assert Jend >= 0 and Jremove >= 0
assert information_term >= additive_MI >= number(explicit_bound) > 0

# Exact nonlinearity: coefficient of s_1^2 in the all-occupied atom.
# With two sites in each reservoir, it is det(C_2) * |det(B_1)|^2.
reset_obstruction_coefficient = clean(C[1].det() * abs2(B[0].det()))
sx = sp.Symbol("sx", real=True)
all_present = clean(q[0][3] * q[1][3] * core(At, [sx, sbar[1]], (3, 3)).det())
assert sp.Poly(all_present, sx).coeff_monomial(sx ** 2) == reset_obstruction_coefficient > 0

certificate = {
    "status": "exact assertions passed; entropy evaluations are numerical illustrations",
    "n": 6, "reservoir_sizes": [2, 2],
    "A0": [[str(x) for x in row] for row in A0.tolist()],
    "A1": [[str(x) for x in row] for row in A1.tolist()],
    "C": [[[str(x) for x in row] for row in Cj.tolist()] for Cj in C],
    "B": [[[str(x) for x in row] for row in Bj.tolist()] for Bj in B],
    "z0": list(map(str, z0)), "z1": list(map(str, z1)), "t": str(t),
    "s0": list(map(str, s0)), "s1": list(map(str, s1)),
    "sbar": list(map(str, sbar)), "target_strengths": list(map(str, st)),
    "delta": list(map(str, delta)), "lambda": list(map(str, lam)),
    "removal_weights": {str(R): str(w) for R, w in weights.items()},
    "det_B": [str(clean(Bj.det())) for Bj in B],
    "det_C": [str(clean(Cj.det())) for Cj in C],
    "det_B_ranks": [Bj.rank() for Bj in B],
    "max_abs_B_to_fourth": list(map(str, max_B4)),
    "explicit_bound": str(explicit_bound),
    "quadratic_strength_coefficient_in_all_occupied_atom": str(reset_obstruction_coefficient),
    "gershgorin_endpoint_0": gershgorin(kernel(A0, z0)),
    "gershgorin_endpoint_1": gershgorin(kernel(A1, z1)),
    "gershgorin_target": gershgorin(kernel(At, zt)),
    "gershgorin_auxiliary_with_strength_amplitudes_bounded_by_one": gershgorin(kernel(At, [1, 1])),
    "exact_atom_equalities": checked_atoms,
    "exact_conditional_matrix_equalities": checked_conditional_identities,
    "minimum_atom_by_state": {name: str(min(p.values())) for name, p in laws.items()},
    "reservoir_atom_probabilities": [{str(y): str(v) for y, v in qj.items()} for qj in q],
}

results = {
    "precision_decimal_digits": mp.mp.dps,
    "entropy_values": {name: finite(value) for name, value in H.items()},
    "actual_jensen_gap": finite(gamma),
    "endpoint_conditional_Jensen_gap": finite(Jend),
    "removal_conditional_Jensen_gap": finite(Jremove),
    "expected_removal_information": finite(information_term),
    "identity_residual": finite(gamma - Jend - Jremove - information_term),
    "information_by_removed_set_bitmask": {str(R): finite(value) for R, value in information_by_R.items()},
    "single_block_core_information": list(map(finite, single_MI)),
    "additive_information_lower_bound": finite(additive_MI),
    "extra_conditional_information": finite(information_term - additive_MI),
    "explicit_quartic_lower_bound": finite(number(explicit_bound)),
}

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "exact_certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
(OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps({"exact_atom_equalities": checked_atoms,
                  "exact_conditional_matrix_equalities": checked_conditional_identities,
                  "actual_gap": finite(gamma),
                  "gap_components": [finite(Jend), finite(Jremove), finite(information_term)],
                  "additive_information_bound": finite(additive_MI),
                  "explicit_bound": str(explicit_bound),
                  "identity_residual": results["identity_residual"]}, indent=2))
