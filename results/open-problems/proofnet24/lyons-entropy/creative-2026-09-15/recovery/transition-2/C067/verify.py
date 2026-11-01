#!/usr/bin/env python3
"""Reproduce C067's rational segment and exact finite entropy-gap identity.

Requirements: Python 3, sympy, mpmath. All mathematical certificate checks use
exact rational arithmetic or symbolic rational functions. Decimal entropy values
are illustrations, independently evaluated from the exact certificate.
"""
from collections import defaultdict
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

OUT = Path(__file__).resolve().parent
q = sp.Rational
t = sp.Symbol("t", real=True)
I2 = sp.eye(2)
I3 = sp.eye(3)
checks = []
atom_checks = 0


def check(name, condition):
    assert condition, name
    checks.append(name)


def zero_matrix(A):
    return all(sp.cancel(x) == 0 for x in A)


def det_principal(A, mask):
    idx = [i for i in range(A.rows) if mask & (1 << i)]
    return A.extract(idx, idx).det() if idx else sp.Integer(1)


def atoms(A):
    """Independent mixed-column determinants and inclusion Möbius inversion."""
    global atom_checks
    n = A.rows
    eye = sp.eye(n)
    moments = [det_principal(A, s) for s in range(1 << n)]
    result = []
    for s in range(1 << n):
        cols = [A[:, j] if s & (1 << j) else eye[:, j] - A[:, j]
                for j in range(n)]
        direct = sp.cancel(sp.Matrix.hstack(*cols).det())
        mobius = sp.cancel(sum(
            (-1) ** (u.bit_count() - s.bit_count()) * moments[u]
            for u in range(1 << n) if u & s == s
        ))
        assert sp.cancel(direct - mobius) == 0
        result.append(direct)
        atom_checks += 1
    assert sp.cancel(sum(result) - 1) == 0
    return result


def at_tau(P, tau):
    return [sp.cancel(p.subs(t, tau)) for p in P]


def gershgorin_lower(A):
    return min(A[i, i] - sum(abs(A[i, j]) for j in range(A.cols) if j != i)
               for i in range(A.rows))


def str_matrix(A):
    return [[str(sp.cancel(A[i, j])) for j in range(A.cols)]
            for i in range(A.rows)]


K0 = sp.Matrix([
    [q(2, 5), q(1, 5), q(3, 20)],
    [q(1, 5), q(51, 100), q(1, 200)],
    [q(3, 20), q(1, 200), q(51, 100)],
])
K1 = sp.Matrix([
    [q(3, 5), q(3, 20), q(1, 5)],
    [q(3, 20), q(49, 100), -q(1, 200)],
    [q(1, 5), -q(1, 200), q(49, 100)],
])
K = (1-t)*K0 + t*K1
direction = K1-K0
a = K[0, 0]
b = 1-a
z = K[1:, 0]
B = K[1:, 1:]
a0, a1 = K0[0, 0], K1[0, 0]
z0, z1 = K0[1:, 0], K1[1:, 0]
B0, B1 = K0[1:, 1:], K1[1:, 1:]
alpha, w, C = a1-a0, z1-z0, B1-B0
R = w*w.T-alpha*C
V = t*(1-t)*R

check("endpoint K0 spectral lower margin", gershgorin_lower(K0) == q(1, 20))
check("endpoint I-K0 spectral lower margin", gershgorin_lower(I3-K0) == q(1, 4))
check("endpoint K1 spectral lower margin", gershgorin_lower(K1) == q(1, 4))
check("endpoint I-K1 spectral lower margin", gershgorin_lower(I3-K1) == q(1, 20))
check("positive pivot slope", alpha == q(1, 5))
check("negative complementary block spectrum",
      set(C.eigenvals()) == {-q(3, 100), -q(1, 100)})
check("covariance matrix",
      R == sp.Matrix([[13, -1], [-1, 13]]) / 2000)
check("strict covariance spectrum",
      set(R.eigenvals()) == {q(3, 500), q(7, 1000)})
check("cross vectors not parallel", sp.Matrix.hstack(z0, z1).det() == q(7, 400))
check("full direction determinant", direction.det() == q(21, 100000))
check("positive Schur complement and inertia (1,2)",
      alpha-(w.T*C.inv()*w)[0] == q(7, 10))
check("every diagonal changes", all(direction[i, i] != 0 for i in range(3)))

G = {}
for j, Kj in enumerate([K0, K1]):
    aj, zj, Bj = Kj[0, 0], Kj[1:, 0], Kj[1:, 1:]
    G[j, 1] = Bj-zj*zj.T/aj
    G[j, 0] = Bj+zj*zj.T/(1-aj)
F = {1: B-z*z.T/a, 0: B+z*z.T/b}
weights = {
    1: [(1-t)*a0/a, t*a1/a],
    0: [(1-t)*(1-a0)/b, t*(1-a1)/b],
}
M = {i: weights[i][0]*G[0, i] + weights[i][1]*G[1, i]
     for i in [0, 1]}
check("included branch covariance identity for symbolic t",
      zero_matrix(F[1]-M[1]-V/a))
check("excluded branch covariance identity for symbolic t",
      zero_matrix(F[0]-M[0]+V/b))
for i in [0, 1]:
    check(f"branch {i} weights sum to one", sp.cancel(sum(weights[i])-1) == 0)

# Whole-interval analytic certificate: these affine or quadratic identities,
# together with 0 <= t <= 1, prove every inequality used in Section 4.
d, maxab, maxnorm, mincomponent = q(97, 200), q(3, 5), q(1, 16), q(9, 400)
vplus, vminus = sp.Matrix([1, 1]), sp.Matrix([1, -1])
check("complementary block plus-mode identity",
      zero_matrix((B-I2/2)*vplus - q(3, 200)*(1-2*t)*vplus))
check("complementary block minus-mode identity",
      zero_matrix((B-I2/2)*vminus - q(1, 200)*(1-2*t)*vminus))
check("spectral d bound", d == q(1, 2)-q(3, 200))
check("pivot and complementary pivot affine endpoint bounds",
      max(a0, a1, 1-a0, 1-a1) == maxab)
check("component affine endpoint lower bound",
      min(list(z0)+list(z1)) == q(3, 20))
check("squared norm identity on the entire interval",
      sp.expand((z.T*z)[0] - (q(1, 16)-t*(1-t)/200)) == 0)
inverse_bound = 1/d-mincomponent/(d*(maxab*d+maxnorm))
check("exact inverse diagonal bound", inverse_bound == q(132400, 68579))
check("strict uniform odds bound", inverse_bound < q(31, 16))
check("exact cross multiplication", 132400*16 == 2118400 and 68579*31 == 2125949)
r = q(15, 16)

laws = {"K": atoms(K)}
for i in [0, 1]:
    laws[f"F{i}"] = atoms(F[i])
    laws[f"M{i}"] = atoms(M[i])
    for j in [0, 1]:
        laws[f"G{j}{i}"] = atoms(G[j, i])
for i in [0, 1]:
    pivot_probability = a if i == 1 else b
    for s in range(4):
        check(f"symbolic conditional atom branch {i} atom {s}",
              sp.cancel(laws["K"][2*s+i] -
                        pivot_probability*laws[f"F{i}"][s]) == 0)

tau = q(1, 2)
P = {name: at_tau(law, tau) for name, law in laws.items()}
P["K0"], P["K1"] = at_tau(laws["K"], 0), at_tau(laws["K"], 1)
for name, law in P.items():
    check(f"positive midpoint or endpoint law {name}", all(p > 0 for p in law))
odds_diagonals = {}
for i in [0, 1]:
    Fi = F[i].subs(t, tau)
    odds = (I2-Fi).inv()-I2 if i == 1 else Fi.inv()-I2
    check(f"branch {i} actual midpoint odds below uniform bound",
          all(odds[k, k] <= r for k in range(2)))
    odds_diagonals[str(i)] = [str(odds[k, k]) for k in range(2)]
    for s in range(4):
        for k in range(2):
            if not s & (1 << k):
                smaller, larger = P[f"F{i}"][s], P[f"F{i}"][s | (1 << k)]
                check(f"branch {i} atom ratio {s} -> {s | (1 << k)}",
                      larger <= r*smaller if i == 1 else smaller <= r*larger)

# Canonical exact logarithmic expressions: factor rational arguments into
# primes, so every information quantity is a rational linear combination of
# log(prime). Equality is checked before any decimal evaluation.
def add(*terms):
    result = defaultdict(lambda: sp.Integer(0))
    for term in terms:
        for prime, coefficient in term.items():
            result[prime] += coefficient
    return {p: sp.cancel(c) for p, c in result.items() if c != 0}


def scale(c, term):
    return {p: sp.cancel(c*v) for p, v in term.items() if c*v != 0}


def logq(x):
    x = q(x)
    result = defaultdict(int)
    for prime, exponent in sp.factorint(x.p).items():
        result[int(prime)] += exponent
    for prime, exponent in sp.factorint(x.q).items():
        result[int(prime)] -= exponent
    return {p: q(e) for p, e in result.items() if e}


def entropy(law):
    return add(*(scale(-p, logq(p)) for p in law))


def binary(x):
    return entropy([x, 1-x])


def divergence(pm, pf):
    return add(*(scale(m, add(logq(m), scale(-1, logq(f))))
                 for m, f in zip(pm, pf)))


def order_cost(pm, pf):
    return add(*(scale(m-f, logq(f)) for m, f in zip(pm, pf)))


at = a.subs(t, tau)
bt = 1-at
gap = add(entropy(P["K"]), scale(-(1-tau), entropy(P["K0"])),
          scale(-tau, entropy(P["K1"])))
Jh = add(binary(at), scale(-(1-tau), binary(a0)), scale(-tau, binary(a1)))
terms = {"J_h": Jh}
for i, branch_probability in [(1, at), (0, bt)]:
    ws = [sp.cancel(x.subs(t, tau)) for x in weights[i]]
    Ji = add(entropy(P[f"M{i}"]),
             scale(-ws[0], entropy(P[f"G0{i}"])),
             scale(-ws[1], entropy(P[f"G1{i}"])))
    Di = divergence(P[f"M{i}"], P[f"F{i}"])
    Oi = order_cost(P[f"M{i}"], P[f"F{i}"])
    correction = add(entropy(P[f"F{i}"]), scale(-1, entropy(P[f"M{i}"])))
    check(f"exact branch {i} KL plus order identity",
          add(correction, scale(-1, Di), scale(-1, Oi)) == {})
    terms[f"{'a' if i else 'b'}_J{i}"] = scale(branch_probability, Ji)
    terms[f"{'a' if i else 'b'}_D{i}"] = scale(branch_probability, Di)
    terms[f"{'a' if i else 'b'}_O{i}"] = scale(branch_probability, Oi)
exact_residual = add(gap, scale(-1, add(*terms.values())))
check("exact seven-term gap identity as prime logarithms", exact_residual == {})

def rational_text(x):
    return str(sp.cancel(x))


def log_expression(expr):
    return {str(p): rational_text(c) for p, c in sorted(expr.items())}


certificate = {
    "status": "all exact checks passed",
    "exact_atom_determinant_mobius_equalities": atom_checks,
    "named_exact_check_count": len(checks),
    "named_exact_checks": checks,
    "K0": str_matrix(K0), "K1": str_matrix(K1),
    "direction": str_matrix(direction), "R": str_matrix(R),
    "direction_determinant": str(direction.det()),
    "direction_inertia": [1, 2, 0],
    "uniform_certificate": {
        "parameter_interval": ["0", "1"], "d": str(d), "A": str(maxab),
        "Q": str(maxnorm), "mu": str(mincomponent),
        "inverse_diagonal_upper_bound": str(inverse_bound),
        "odds_diagonal_upper_bound": str(r),
        "squared_norm_identity": str(q(1, 16)-t*(1-t)/200),
    },
    "symbolic_conditional_kernels": {f"F{i}": str_matrix(F[i]) for i in [0, 1]},
    "symbolic_conditional_barycenters": {f"M{i}": str_matrix(M[i]) for i in [0, 1]},
    "symbolic_full_atoms": [str(p) for p in laws["K"]],
    "illustration_parameter": str(tau),
    "exact_illustration_atom_probabilities": {
        name: [str(p) for p in law] for name, law in P.items()
    },
    "illustration_conditional_odds_diagonals": odds_diagonals,
    "exact_logarithmic_gap": log_expression(gap),
    "exact_logarithmic_terms": {name: log_expression(x) for name, x in terms.items()},
    "exact_seven_term_residual": log_expression(exact_residual),
}

mp.mp.dps = 80
def dec(x):
    x = q(x)
    return mp.mpf(int(x.p))/mp.mpf(int(x.q))


def evaluate(expr):
    return mp.fsum(dec(c)*mp.log(p) for p, c in expr.items())


def outnum(x):
    return mp.nstr(x, 65)


numeric_terms = {name: evaluate(expr) for name, expr in terms.items()}
numeric_gap = evaluate(gap)
numeric_residual = numeric_gap-mp.fsum(numeric_terms.values())
binary_order_bound = dec(tau*(1-tau)) * (dec(q(2, 25)) +
                         dec(q(13, 500))*mp.log(dec(q(16, 15))))
pinsker_extra = dec(q(169, 500000)*tau**2*(1-tau)**2)
# These are sanity checks on numerical illustrations, not proofs of signs.
assert all(value > 0 for value in numeric_terms.values())
assert abs(numeric_residual) < mp.mpf("1e-70")
assert numeric_gap > binary_order_bound+pinsker_extra
results = {
    "precision_decimal_digits": mp.mp.dps,
    "entropy_gap": outnum(numeric_gap),
    "seven_weighted_terms": {name: outnum(x) for name, x in numeric_terms.items()},
    "numerical_identity_residual": outnum(numeric_residual),
    "binary_plus_order_lower_bound": outnum(binary_order_bound),
    "additional_pinsker_lower_bound": outnum(pinsker_extra),
    "combined_explicit_lower_bound": outnum(binary_order_bound+pinsker_extra),
    "note": "Decimals illustrate exact proved identities; no sampled interval sign is used.",
}
(OUT/"exact_certificate.json").write_text(json.dumps(certificate, indent=2)+"\n")
(OUT/"results.json").write_text(json.dumps(results, indent=2)+"\n")
print(f"PASS: {atom_checks} exact atom equalities, {len(checks)} named exact checks.")
print("Seven-term entropy identity: exact zero residual in prime logarithms.")
print(json.dumps(results, indent=2))
