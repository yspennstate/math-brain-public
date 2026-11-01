#!/usr/bin/env python3
"""Exact two-active-block Bernstein coupling and entropy-correction certificate.

No random sampling. Requires sympy. All sign certificates use rational arithmetic.
Run from any directory; outputs are placed alongside this script.
"""

from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parent
t, e = sp.symbols("t e", real=True)
R = sp.Rational
A = sp.Matrix([[R(1, 10), -R(1, 4)], [-R(1, 4), R(4, 5)]])
B = sp.Matrix([[R(1, 10), R(1, 4)], [R(1, 4), R(4, 5)]])
C = sp.Matrix([[R(1, 2), R(1, 8)], [R(1, 8), R(1, 2)]])
V = e * sp.eye(2)
K = A.row_join(V).col_join(V.row_join(C))
D = sp.diag(B, C)
L = D + t * (K - D)


def fraction(x):
    x = sp.Rational(x)
    return F(int(x.p), int(x.q))


def bernstein_coefficients(poly, degree):
    return [
        sp.expand(sum(poly.nth(j) * sp.binomial(k, j) / sp.binomial(degree, j)
                      for j in range(min(k, poly.degree()) + 1)))
        for k in range(degree + 1)
    ]


atoms = []
coeffs = []
for mask in range(16):
    absent = sp.diag(*[0 if mask & (1 << j) else 1 for j in range(4)])
    atom = sp.Poly(sp.expand((-1) ** (4 - mask.bit_count()) * (L - absent).det()), t)
    atoms.append(atom)
    row = bernstein_coefficients(atom, 5)
    coeffs.append(row)
    assert sp.expand(sum(sp.binomial(5, k) * t**k * (1-t)**(5-k) * row[k]
                         for k in range(6)) - atom.as_expr()) == 0
assert sp.expand(sum(p.as_expr() for p in atoms)) == 1
for k in range(6):
    assert sp.expand(sum(row[k] for row in coeffs)) == 1

# Check the compact closed formula stated in the report, not just a determinant
# implementation. This also gives the uniform positivity bound by inspection.
diagonal = [R(1,10), R(4,5), R(1,2), R(1,2)]
mu_u = [R(9,50), R(1,50), R(18,25), R(2,25)]
mu_c = [R(15,64), R(17,64), R(17,64), R(15,64)]
for mask in range(16):
    h = [diagonal[i] - (0 if mask & (1 << i) else 1) for i in range(4)]
    u = h[1]*h[3] + h[0]*h[2]
    sign = (-1)**mask.bit_count()
    sign_u = (-1)**(mask & 3).bit_count()
    for j in range(6):
        alpha, beta, gamma = sp.binomial(j,2)/10, sp.binomial(j,3)/10, sp.binomial(j,4)/5
        r = 1 - R(4,5)*j + 4*alpha
        formula = ((mu_u[mask & 3] - sign_u*r/16)*mu_c[mask >> 2]
                   + sign*(e*e*(-u*alpha+(2*beta-alpha)/16)+e**4*gamma))
        assert sp.expand(formula-coeffs[mask][j]) == 0

# The first-block event 10 has a negative degree-four Bernstein coefficient,
# independently of the rank-two cross-correlation strength e.
marginal = sp.Poly(sp.expand(sum(atoms[m].as_expr() for m in range(16)
                                  if m & 3 == 1)), t)
assert marginal.as_expr() == R(33, 400) - t/4 + t*t/4
marginal4 = bernstein_coefficients(marginal, 4)
assert marginal4 == [R(33, 400), R(1, 50), -R(1, 1200), R(1, 50), R(33, 400)]

# A uniform positivity certificate for the full five-bit coefficient laws.
triples = []
for row in coeffs:
    out = []
    for q in row:
        ep = sp.Poly(q, e)
        assert all(power[0] in (0, 2, 4) for power in ep.monoms())
        out.append([ep.nth(0), ep.nth(2), ep.nth(4)])
    triples.append(out)
min_base = min(v[0] for row in triples for v in row)
max_second = max(abs(v[1]) for row in triples for v in row)
max_fourth = max(abs(v[2]) for row in triples for v in row)
assert (min_base, max_second, max_fourth) == (R(9, 5120), R(73, 80), 1)
uniform_lower = min_base - max_second / 625 - max_fourth / 390625
assert uniform_lower == R(118101, 400000000) > 0

# Uniform strictness: lambda_min(A), lambda_min(B) > 7/360;
# lambda_min(I-A), lambda_min(I-B) > 47/440; lambda_min(C)=3/8.
# The Schur-complement loss is at most (8/3)e^2 <= 8/1875.
assert R(7, 360) - R(8, 1875) > 0
assert R(47, 440) - R(8, 1875) > 0
assert A * B != B * A


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(c, a):
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def minus(a, b):
    return plus(a, times(F(-1), b))


def atanh_log_interval(y, terms=28):
    """Rational enclosure of log(y), for 1 <= y <= 2."""
    assert F(1) <= y <= F(2)
    z = (y - 1) / (y + 1)
    partial = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    remainder = 2 * z**(2*terms+1) / ((2*terms+1) * (1-z*z))
    return partial, partial + remainder


LOG_TWO = atanh_log_interval(F(2))
LOG_CACHE = {}


def log_interval(x):
    """Exact log enclosure, rounded outward to denominator 10^24."""
    assert x > 0
    if x in LOG_CACHE:
        return LOG_CACHE[x]
    y, shift = x, 0
    while y < 1:
        y *= 2
        shift -= 1
    while y >= 2:
        y /= 2
        shift += 1
    lo, hi = plus(atanh_log_interval(y), times(F(shift), LOG_TWO))
    grid = 10**24
    lo_grid = F((lo.numerator * grid) // lo.denominator, grid)
    hi_grid = F(-((-hi.numerator * grid) // hi.denominator), grid)
    assert lo_grid <= lo <= hi <= hi_grid
    LOG_CACHE[x] = lo_grid, hi_grid
    return LOG_CACHE[x]


def entropy_interval(p):
    out = (F(0), F(0))
    for x in p:
        out = plus(out, times(-x, log_interval(x)))
    return out


# One fixed, full-rank member. No search is used to obtain these signs.
epsilon, midpoint = R(1, 100), R(1, 2)
pv, p1, p2 = [], [], []
for p in atoms:
    expr = p.as_expr().subs(e, epsilon)
    pv.append(fraction(expr.subs(t, midpoint)))
    p1.append(fraction(sp.diff(expr, t).subs(t, midpoint)))
    p2.append(fraction(sp.diff(expr, t, 2).subs(t, midpoint)))
qv = [[fraction(coeffs[m][k].subs(e, epsilon)) for m in range(16)] for k in range(6)]
assert all(x > 0 for row in qv for x in row)
weights2 = [fraction(sp.diff(sp.binomial(5,k)*t**k*(1-t)**(5-k), t, 2).subs(t, midpoint))
            for k in range(6)]
assert weights2 == [F(5,2), F(5,2), F(-5), F(-5), F(5,2), F(5,2)]

fisher = sum((v*v/p for p,v in zip(pv,p1)), F(0))
h2 = (-fisher, -fisher)
for p, derivative2 in zip(pv,p2):
    h2 = plus(h2, times(-derivative2, log_interval(p)))
average2 = (F(0), F(0))
for w2, row in zip(weights2, qv):
    average2 = plus(average2, times(w2, entropy_interval(row)))
mutual2 = minus(h2, average2)
hidden_conditional2 = plus((F(-20), F(-20)), minus(average2, h2))

assert F(-11,10**7) < h2[0] <= h2[1] < F(-1,10**6)
assert F(-4850,10000) < average2[0] <= average2[1] < F(-4849,10000)
assert F(4849,10000) < mutual2[0] <= mutual2[1] < F(4850,10000)
assert F(-204850,10000) < hidden_conditional2[0] <= hidden_conditional2[1] < F(-204849,10000)

example_minors = {}
for label, matrix in [("K", K.subs(e,epsilon)), ("I-K", sp.eye(4)-K.subs(e,epsilon)),
                      ("D",D), ("I-D",sp.eye(4)-D)]:
    values = [matrix[:j,:j].det() for j in range(1,5)]
    assert all(v > 0 for v in values)
    example_minors[label] = [str(v) for v in values]

def interval_json(pair):
    return {"lower": str(pair[0]), "upper": str(pair[1]),
            "decimal_summary": [float(pair[0]),float(pair[1])]}

results = {
    "family": {"epsilon_range": "0 < abs(epsilon) <= 1/25",
               "minimum_number_of_iid_retention_bits": 5,
               "min_fifth_degree_base_coefficient":str(min_base),
               "max_abs_epsilon_squared_coefficient":str(max_second),
               "max_abs_epsilon_fourth_coefficient":str(max_fourth),
               "uniform_positive_lower_bound":str(uniform_lower)},
    "four_bit_obstruction": {"event": "X1=1,X2=0", "polynomial":str(marginal.as_expr()),
                              "degree_four_bernstein_coefficients":[str(v) for v in marginal4]},
    "fixed_example": {"epsilon":"1/100", "eta":"1/2", "strictness_minors":example_minors,
                      "actual_entropy_second_derivative":interval_json(h2),
                      "conditional_component_entropy_second_derivative":interval_json(average2),
                      "mutual_information_second_derivative":interval_json(mutual2),
                      "hidden_conditional_entropy_second_derivative":interval_json(hidden_conditional2)},
    "proof_method":"Symbolic determinants and rational Bernstein coefficients; log intervals from 28-term atanh series and outward rational rounding. No floating-point sign inference."
}
table = {
    "atom_order":"mask bit 0 is site 1; displayed strings run sites 1,2,3,4",
    "coefficient_convention":"Q_j(atom)=a+b*epsilon^2+c*epsilon^4",
    "rows":[{"mask":m, "atom":"".join(str((m>>i)&1) for i in range(4)),
             "Q0_through_Q5":[[str(v) for v in triple] for triple in triples[m]]}
            for m in range(16)]
}
(ROOT / "exact_certificate.json").write_text(json.dumps(results, indent=2)+"\n")
(ROOT / "coefficient_table.json").write_text(json.dumps(table, indent=2)+"\n")
print(json.dumps({"uniform_positive_lower_bound":str(uniform_lower),
                  "minimum_retention_bits":5,
                  "H_second":[float(v) for v in h2],
                  "component_entropy_second":[float(v) for v in average2],
                  "mutual_information_second":[float(v) for v in mutual2]}, indent=2))
