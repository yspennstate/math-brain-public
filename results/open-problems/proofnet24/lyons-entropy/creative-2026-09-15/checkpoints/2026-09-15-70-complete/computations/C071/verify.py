#!/usr/bin/env python3
"""Exact certificate for C071. Python 3 + SymPy; no numerical sign tests."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import json
import sympy as s

N = 6
R = s.Rational
ii = s.I
C = s.zeros(N)
for i in range(N):
    for j in range(i + 1, N):
        C[i, j] = (12 + ii) / 72
        C[j, i] = s.conjugate(C[i, j])
L = s.eye(N) - C
K = (s.eye(N) - (s.eye(N) + L).inv(method="DM")).applyfunc(s.cancel)
u = s.ones(N, 1)
v = s.Matrix([1, -1, 1, -1, 1, -1])
A = u * u.T - v * v.T
assert (u.T * v)[0] == 0 and (u.T * u)[0] == (v.T * v)[0] == 6
assert A.rank() == 2

def simp(x):
    return s.cancel(s.expand_complex(x))

def real(x):
    z = simp(x)
    assert s.im(z) == 0, z
    return s.re(z)

def frac(x):
    x = real(x)
    return F(int(s.numer(x)), int(s.denom(x)))

def ids(mask):
    return [i for i in range(N) if mask >> i & 1]

def sub(M, mask):
    q = ids(mask)
    return M.extract(q, q)

def det(M):
    return real(M.det(method="domain-ge")) if M.rows else s.Integer(1)

def subsets(mask):
    t = mask
    while True:
        yield t
        if not t:
            break
        t = (t - 1) & mask

def ser_matrix(M):
    return [[[str(s.re(simp(M[i, j]))), str(s.im(simp(M[i, j])))]
             for j in range(M.cols)] for i in range(M.rows)]

# Every unoriented simple cycle is enumerated exactly once.
polymers = []
for i, j in combinations(range(N), 2):
    polymers.append({"vertices": [i, j], "mask": (1 << i) | (1 << j),
                     "activity": real(C[i, j] * C[j, i])})
for k in range(3, N + 1):
    for vertices in combinations(range(N), k):
        first = vertices[0]
        for rest in permutations(vertices[1:]):
            if rest[0] > rest[-1]:
                continue
            cycle = (first,) + rest
            z = s.Integer(1)
            for a, b in zip(cycle, cycle[1:] + cycle[:1]):
                z *= C[a, b]
            activity = 2 * s.re(simp(z))
            assert activity > 0
            polymers.append({"vertices": list(cycle),
                             "mask": sum(1 << x for x in cycle),
                             "activity": activity})
assert len(polymers) == 212  # 15 edges + 197 longer unoriented cycles.

# Direct determinant coefficients, versus the disjoint-polymer recursion.
@lru_cache(None)
def polymer_poly(mask):
    if not mask:
        return (s.Integer(1),) + (s.Integer(0),) * N
    low = mask & -mask
    ans = list(polymer_poly(mask ^ low))
    for p in polymers:
        pm = p["mask"]
        if pm & low and pm & mask == pm:
            rest = polymer_poly(mask ^ pm)
            degree = pm.bit_count()
            for j in range(N + 1 - degree):
                ans[j + degree] -= p["activity"] * rest[j]
    return tuple(s.cancel(x) for x in ans)

dL = {}
dC = {}
for mask in range(1 << N):
    dL[mask] = det(sub(L, mask))
    dC[mask] = det(sub(C, mask))
    assert dL[mask] > 0
for mask in range(1 << N):
    coefficients = [s.Integer(0)] * (N + 1)
    for t in subsets(mask):
        coefficients[t.bit_count()] += (-1) ** t.bit_count() * dC[t]
    assert tuple(coefficients) == polymer_poly(mask)

# Exact Boolean log coefficients are logarithms of exact rational ratios.
mobius = []
for mask in range(1 << N):
    if mask.bit_count() < 2:
        continue
    ratio = s.Integer(1)
    for t in subsets(mask):
        exponent = -(-1) ** ((mask ^ t).bit_count())
        ratio *= dL[t] ** exponent
    ratio = s.cancel(ratio)
    assert ratio > 1
    mobius.append({"mask": mask, "ratio": str(ratio)})

# Exact full atom derivatives from the rank-two determinant lemma.
# Q_S (I+L) has rows L on S and rows -I on the complement.
Z = det(s.eye(N) + L)
atoms = []
for mask in range(1 << N):
    inside, outside = ids(mask), ids(((1 << N) - 1) ^ mask)
    Lss = L.extract(inside, inside)
    inv = Lss.inv(method="DM") if inside else s.zeros(0)
    def qsolve(w):
        y = s.zeros(N, 1)
        for j in outside:
            y[j] = -w[j]
        if inside:
            rhs = w.extract(inside, [0])
            if outside:
                rhs += L.extract(inside, outside) * w.extract(outside, [0])
            ys = inv * rhs
            for index, j in enumerate(inside):
                y[j] = ys[index]
        return ((s.eye(N) + L) * y).applyfunc(simp)
    qu, qv = qsolve(u), qsolve(v)
    # Independently check the two solves against Q itself.
    Q = K - s.diag(*[0 if j in inside else 1 for j in range(N)])
    assert (Q * qu - u).applyfunc(simp) == s.zeros(N, 1)
    assert (Q * qv - v).applyfunc(simp) == s.zeros(N, 1)
    aa, bb = real((u.T * qu)[0]), real((v.T * qv)[0])
    cc = simp((u.T * qv)[0])
    p0 = s.cancel(dL[mask] / Z)
    p1 = s.cancel(p0 * (aa - bb))
    p2 = real(-2 * p0 * (aa * bb - cc * s.conjugate(cc)))
    atoms.append({"mask": mask, "p": p0, "dp": p1, "ddp": p2})
assert sum(a["p"] for a in atoms) == 1
assert sum(a["dp"] for a in atoms) == 0
assert sum(a["ddp"] for a in atoms) == 0

# Every inclusion second derivative is nonpositive; this is the exact
# finite-example version of the rank-two mixed Gram determinant identity.
inclusion_dd = {}
for mask in range(1 << N):
    gdd = s.cancel(sum(a["ddp"] for a in atoms if a["mask"] & mask == mask))
    inclusion_dd[mask] = gdd
    assert gdd <= 0
for mask in range(1 << N):
    inversion = sum((-1) ** ((t ^ mask).bit_count()) * inclusion_dd[t]
                    for t in range(1 << N) if t & mask == mask)
    assert s.cancel(inversion) == atoms[mask]["ddp"]

# Exact logarithm enclosures, using outward integer fixed-point arithmetic.
BITS, TERMS = 200, 64
BASE = 1 << BITS
def ceildiv(a, b):
    return -(-a // b)

def log_reduced(y):
    assert F(1) <= y <= F(2)
    z = (y - 1) / (y + 1)
    zl, zh = z.numerator * BASE // z.denominator, ceildiv(z.numerator * BASE, z.denominator)
    z2l, z2h = zl * zl // BASE, ceildiv(zh * zh, BASE)
    pl, ph = zl, zh
    lo = hi = 0
    for k in range(TERMS):
        denominator = 2 * k + 1
        lo += 2 * (pl // denominator)
        hi += 2 * ceildiv(ph, denominator)
        pl, ph = pl * z2l // BASE, ceildiv(ph * z2h, BASE)
    # log y = 2 sum z^(2k+1)/(2k+1), and 0 <= z <= 1/3.
    tail = F(2, (2 * TERMS + 1) * 3 ** (2 * TERMS + 1)) / F(8, 9)
    hi += ceildiv(tail.numerator * BASE, tail.denominator)
    return lo, hi

LOG2 = log_reduced(F(2))
def log_interval(x):
    x = frac(x)
    assert x > 0
    power = 0
    while x < 1:
        x *= 2
        power -= 1
    while x >= 2:
        x /= 2
        power += 1
    lo, hi = log_reduced(x)
    if power >= 0:
        lo, hi = lo + power * LOG2[0], hi + power * LOG2[1]
    else:
        lo, hi = lo + power * LOG2[1], hi + power * LOG2[0]
    return F(lo, BASE), F(hi, BASE)

fisher = sum(frac(a["dp"]) ** 2 / frac(a["p"]) for a in atoms)
frozen_lo = frozen_hi = F(0)
for a in atoms:
    lo, hi = log_interval(a["p"])
    c = -frac(a["ddp"])
    if c >= 0:
        frozen_lo, frozen_hi = frozen_lo + c * lo, frozen_hi + c * hi
    else:
        frozen_lo, frozen_hi = frozen_lo + c * hi, frozen_hi + c * lo
hessian_lo, hessian_hi = frozen_lo - fisher, frozen_hi - fisher
assert fisher > 0 and frozen_hi < 0 and hessian_hi < 0

# The complete affine interval is certified analytically in the report.
# Retain exact endpoint principal-minor and odds-sector checks as well.
endpoint_data = []
for t in [R(-1, 6000), R(0), R(1, 6000)]:
    J = (K + t * A).applyfunc(simp)
    odds = ((s.eye(N) - J).inv(method="DM") - s.eye(N)).applyfunc(simp)
    pd = []
    for j in range(1, N + 1):
        jm = (1 << j) - 1
        kj, ikj = det(sub(J, jm)), det(sub(s.eye(N) - J, jm))
        assert kj > 0 and ikj > 0
        pd.append([str(kj), str(ikj)])
    for i in range(N):
        for j in range(i + 1, N):
            z = -odds[i, j]
            assert s.re(z) > 0
            assert 6 * abs(s.im(z)) < s.re(z)
    endpoint_data.append({"t": str(t), "positive_leading_minors": pd})

cycle_L = simp(L[0, 1] * L[1, 2] * L[2, 0])
invL = L.inv(method="DM").applyfunc(simp)
cycle_invL = simp(invL[0, 1] * invL[1, 2] * invL[2, 0])
assert s.im(cycle_L) != 0 and s.im(cycle_invL) != 0
commutator = (K * A - A * K).applyfunc(simp)
noncommuting = next((i, j, commutator[i, j]) for i in range(N) for j in range(N)
                     if commutator[i, j] != 0)
assert A[0, 2] == 0 and K[0, 2] != 0  # The line never reaches a diagonal kernel.

def interval_record(lo, hi):
    return {"lower": str(lo), "upper": str(hi),
            "display_lower": float(lo), "display_upper": float(hi)}

result = {
    "status": "PASS",
    "scope": "One exact six-site example and interval; the all-dimensional theorem is analytic.",
    "matrix_encoding": "Each complex entry is [real rational, imaginary rational].",
    "L": ser_matrix(L), "K": ser_matrix(K), "A": ser_matrix(A),
    "polymers": [{"vertices_1based": [x + 1 for x in p["vertices"]],
                  "activity": str(p["activity"])} for p in polymers],
    "positive_mobius_log_ratios": mobius,
    "atoms": [{k: str(x) if k != "mask" else x for k, x in a.items()} for a in atoms],
    "inclusion_second_derivatives": {str(k): str(v) for k, v in inclusion_dd.items()},
    "fisher": str(fisher),
    "frozen_curvature": interval_record(frozen_lo, frozen_hi),
    "entropy_hessian": interval_record(hessian_lo, hessian_hi),
    "endpoint_checks": endpoint_data,
    "obstructions": {
        "odds_triangle_imaginary_part": str(s.im(cycle_L)),
        "inverse_odds_triangle_imaginary_part": str(s.im(cycle_invL)),
        "nonzero_commutator_entry_1based": [noncommuting[0] + 1, noncommuting[1] + 1,
                                            str(noncommuting[2])],
        "A_13": str(A[0, 2]), "K_13": str(K[0, 2]),
    },
    "checks": {
        "all_principal_odds_minors_positive": 64,
        "determinant_polymer_polynomial_identities": 64,
        "positive_long_cycle_activities": 197,
        "positive_nonmodular_mobius_coefficients": 57,
        "exact_atom_probabilities_and_first_second_derivatives": 64,
        "nonpositive_inclusion_second_derivatives": 64,
        "strict_odds_sector_endpoint_checks": 45,
    },
}
output = Path(__file__).with_name("certificate.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print("PASS: 197 complex cycle activities; 64 polymer determinant identities; 57 positive log-Mobius ratios;")
print("      64 exact atoms and derivatives; full Fisher/frozen/Hessian enclosures; 3 exact interval endpoints.")
print(f"Fisher = {float(fisher):.12f}; frozen = [{float(frozen_lo):.12f}, {float(frozen_hi):.12f}]")
print(f"Hessian = [{float(hessian_lo):.12f}, {float(hessian_hi):.12f}]")
print("The interval-wide conclusion uses the analytic resolvent and sector bound, not endpoint sampling.")
print(f"Certificate: {output}")
