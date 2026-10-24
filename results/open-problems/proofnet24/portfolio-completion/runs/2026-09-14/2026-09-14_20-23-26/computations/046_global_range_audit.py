#!/usr/bin/env python3
"""Exact arithmetic certificate for worker046's independent QSO audit.

Uses only Python's standard library.  No random sampling, numerical optimizer,
external service, or floating-point comparison is used.  The analytic report
supplies the universal inequalities and geometric arguments; this script
certifies the expansions, rational constants, local transfer polytope, and
exhaustive classification of all 192 ordered column/cut choices.

Run from any directory: python computations/046_global_range_audit.py
The initial invocation freezes the source texts. Subsequent invocations retain
that snapshot and print hashes of any live files that differ from the snapshot.
"""

from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "computations/046_inputs.json"
OUT = ROOT / "computations/046_exact_certificate.json"
SOURCES = (
    "SESSION.md",
    "repository-policy.md",
    "QSO_GLOBAL_051.md",
    "QSO_AVERAGING_RANGE.md",
    "FOUR_TYPE_UNIQUENESS.md",
    "QSO_HALF_STEP_EXPLICIT.md",
)
EXPECTED_INITIAL_HASHES = {
    "SESSION.md": "6281283ec5344796e80c58027e60209d6fd78b83201c43156b705a5a93b1349c",
    "repository-policy.md": "f485859d8a19bc831493a1bf495fc4706c7356eb59e9664bae1702658485be6a",
    "QSO_GLOBAL_051.md": "395951b0722fa0e5dd0345f619182b80047b1d3c8d4b8bbc742cfa0cb30f222e",
    "QSO_AVERAGING_RANGE.md": "19e0baa68562f1732fb7942b076669e47ffc84abe7be7cf6d4c1445e92e259ac",
    "FOUR_TYPE_UNIQUENESS.md": "1d9e00b127318c24f599f4790264699ba85311ff998bca79ab85dc01f80f8ca4",
    "QSO_HALF_STEP_EXPLICIT.md": "55bcc63ea54c4ff2df867816d9d46b4812e37fbec3deabaab0db0c43e66cb681",
}

if not SNAPSHOT.exists():
    inputs = {}
    for name in SOURCES:
        raw = (ROOT / name).read_bytes()
        digest = sha256(raw).hexdigest()
        assert digest == EXPECTED_INITIAL_HASHES[name], (name, digest)
        inputs[name] = {"sha256": digest, "text": raw.decode()}
    snapshot = {
        "snapshot_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": inputs,
    }
    with SNAPSHOT.open("x") as f:
        json.dump(snapshot, f, indent=2)
        f.write("\n")
else:
    snapshot = json.loads(SNAPSHOT.read_text())
    for name in SOURCES:
        entry = snapshot["inputs"][name]
        assert sha256(entry["text"].encode()).hexdigest() == entry["sha256"]
        assert entry["sha256"] == EXPECTED_INITIAL_HASHES[name]


# Sparse exact polynomials in (lambda, s, v, u).
class P:
    n = 4

    def __init__(self, terms=0):
        if isinstance(terms, P):
            self.terms = terms.terms.copy()
        elif isinstance(terms, dict):
            self.terms = {e: Q(c) for e, c in terms.items() if c}
        else:
            self.terms = {(0,) * self.n: Q(terms)} if terms else {}

    @classmethod
    def variable(cls, j):
        e = [0] * cls.n
        e[j] = 1
        return cls({tuple(e): 1})

    def __add__(self, other):
        other = P(other)
        terms = self.terms.copy()
        for e, c in other.terms.items():
            terms[e] = terms.get(e, 0) + c
        return P(terms)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        other = P(other)
        terms = {}
        for e, c in self.terms.items():
            for f, d in other.terms.items():
                g = tuple(ei + fi for ei, fi in zip(e, f))
                terms[g] = terms.get(g, 0) + c * d
        return P(terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (Q(1) / Q(other))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = P(1)
        for _ in range(n):
            out *= self
        return out

    def __eq__(self, other):
        return self.terms == P(other).terms

    def sub(self, replacements):
        out = P()
        for e, c in self.terms.items():
            term = P(c)
            for j, power in enumerate(e):
                term *= P(replacements.get(j, self.variable(j))) ** power
            out += term
        return out

    def deriv(self, j):
        terms = {}
        for e, c in self.terms.items():
            if e[j]:
                f = list(e)
                f[j] -= 1
                terms[tuple(f)] = c * e[j]
        return P(terms)

    def eval(self, **kwargs):
        variables = {"l": 0, "s": 1, "v": 2, "u": 3}
        out = self.sub({variables[k]: P(v) for k, v in kwargs.items()})
        assert all(not any(e) for e in out.terms), out.terms
        return out.terms.get((0,) * self.n, Q(0))

    def uni_coeffs(self, j, degree):
        assert all(all(p == 0 for k, p in enumerate(e) if k != j)
                   for e in self.terms)
        assert all(e[j] <= degree for e in self.terms)
        return [self.terms.get(tuple(i if k == j else 0 for k in range(self.n)), Q(0))
                for i in range(degree + 1)]


def bernstein_from_power(coeffs):
    n = len(coeffs) - 1
    return [sum((coeffs[j] * Q(comb(k, j), comb(n, j))
                 for j in range(k + 1)), Q(0)) for k in range(n + 1)]


def string_fractions(xs):
    return [str(x) for x in xs]


l, s, v, u = [P.variable(j) for j in range(4)]
a = 1 - l
lo, hi = Q(1, 2), Q(51, 100)
q, d, eps = Q(2, 5), Q(1, 5), Q(1, 50)
cert = {"snapshot_utc": snapshot["snapshot_utc"], "source_hashes": EXPECTED_INITIAL_HASHES}

# T_lambda^2's nonnegative bilinear envelope and endpoint reductions.
envelope = a*a*s + l*a*(1+a)*v + 2*l*l*a*(1-s)*(1-v) + l**3*(1-v)**2
endpoint_zero = l*l*(2-l) + a*(a-2*l*l)*s
assert envelope.sub({2: 0}) == endpoint_zero
F = a*a*(1-u) + l*a*(1+a)*u*u + 2*l*l*a*u*(1-u*u) + l**3*(1-u*u)**2
assert envelope.sub({1: 1-u, 2: u*u}) == F
assert envelope.deriv(2).deriv(2) == 2*l**3

# Independently obtain Bernstein coefficients from the power polynomial.
c_u = []
for j in range(5):
    terms = {}
    for e, c in F.terms.items():
        if e[3] == j:
            f = list(e)
            f[3] = 0
            terms[tuple(f)] = c
    c_u.append(P(terms))
b = [sum((c_u[j] * Q(comb(k, j), comb(4, j))
          for j in range(k+1)), P(0)) for k in range(5)]
claimed = [
    1-2*l+l*l+l**3,
    Q(3,4)-Q(3,2)*l+Q(5,4)*l*l+Q(1,2)*l**3,
    Q(1,6)*(3-4*l+6*l*l-l**3),
    Q(1,4)+Q(1,2)*l-Q(1,4)*l*l-Q(1,2)*l**3,
    2*l-3*l*l+l**3,
]
assert b == claimed
rebuilt = sum((b[k] * comb(4,k) * u**k * (1-u)**(4-k)
               for k in range(5)), P(0))
assert rebuilt == F

# Derivative signs on the full lambda interval are certified by Bernstein
# coefficients after lambda = 1/2 + t/100, where the variable u holds t.
signs = [-1, +1, +1, -1, -1]
upper_bounds = [Q(3,8), Q(752901,2000000), Q(795983,2000000), Q(3,8), Q(3,8)]
derivative_cert = []
for k, (bk, sign, bound) in enumerate(zip(b, signs, upper_bounds)):
    der = bk.deriv(0).sub({0: lo + (hi-lo)*u})
    bern = bernstein_from_power(der.uni_coeffs(3, 2))
    assert all(sign*x > 0 for x in bern)
    at = hi if sign > 0 else lo
    assert bk.eval(l=at) == bound
    assert bound < q
    derivative_cert.append({
        "k": k, "derivative_bernstein_on_lambda_interval": string_fractions(bern),
        "derivative_sign": sign, "max_at_lambda": str(at),
        "maximum": str(bound), "gap_below_2_over_5": str(q-bound),
    })

# For v=0: a-2lambda^2 is decreasing and zero at lambda=1/2.
assert (a-2*l*l).eval(l=lo) == 0
assert all(x < 0 for x in bernstein_from_power(
    (a-2*l*l).deriv(0).sub({0: lo+(hi-lo)*u}).uni_coeffs(3, 1)))
base = l*l*(2-l)
base_der_bern = bernstein_from_power(base.deriv(0).sub({0: lo+(hi-lo)*u}).uni_coeffs(3, 2))
assert all(x > 0 for x in base_der_bern)
assert base.eval(l=hi) == Q(387549,1000000) < q
cert["two_step_cap"] = {
    "bernstein_coefficients_checked": 5,
    "derivative_certificates": derivative_cert,
    "v_zero_maximum": str(base.eval(l=hi)),
    "v_zero_gap_below_cap": str(q-base.eval(l=hi)),
    "upper_envelope_convex_v_second_derivative": "2 lambda^3 > 0",
    "common_scalar_bound": str(max(upper_bounds + [base.eval(l=hi)])),
}

# Uniform overlap arithmetic. Analytic monotonicity is certified by
# theta'(t)=(d+c*t)/(d-c*t)^3 > 0 on this denominator-positive interval.
c = Q(100,49)
denom = d-c*eps
theta = eps/denom**2
h = (d-eps)*(1-theta)
assert denom == Q(39,245) > 0
assert theta == Q(2401,3042) < 1
assert h == Q(641,16900) > eps
assert d-eps > eps
cert["overlap"] = {
    "q": str(q), "d": str(d), "epsilon": str(eps),
    "minimum_preimage_other_coordinate": str(denom),
    "theta_at_epsilon": str(theta), "h_at_epsilon": str(h),
    "h_minus_epsilon": str(h-eps),
    "other_midpoint_mass_minus_epsilon": str(d-2*eps),
}

# The transfer expression's extrema in its five independent probability
# variables occur at 0/1. Their relaxed cube is realizable by allowed parental
# rows for a fixed two-pair cut. Enumerate every cube vertex and every capped
# midpoint vertex. Convexity extends the check to the entire product polytope.
mass_vertices = sorted(set(permutations((Q(2,5), Q(2,5), Q(1,5), Q(0)))))
assert len(mass_vertices) == 12
transfer_cases = 0
max_transfer = Q(-1)
for mi, mj, mk, ml in mass_vertices:
    for pii, pij, pjj, pkj, pli in product((Q(0), Q(1)), repeat=5):
        D = mi*(pii-pij) + mj*(pij-pjj) - mk*pkj + ml*(pli-1)
        assert D <= max(mi,mj) <= q
        max_transfer = max(max_transfer, D)
        transfer_cases += 1
assert transfer_cases == 384 and max_transfer == q
cert["transfer_polytope"] = {
    "capped_mass_vertices": len(mass_vertices), "probability_cube_vertices": 32,
    "exact_vertex_checks": transfer_cases, "attained_maximum": str(max_transfer),
    "limitation": "This certifies the two-pair transfer inequality; it does not replace the third-image overlap proof.",
}

# Exhaust all ordered column pairs and all row subsets. In particular zero
# sign supports do not remove any cases from the operator norm argument.
cut_counts = Counter()
for i in range(4):
    for j in range(4):
        if i == j:
            continue
        for mask in range(16):
            G = {r for r in range(4) if mask & (1 << r)}
            identity_sign = int(i in G)-int(j in G)
            if not G or len(G) == 4:
                category = "empty_or_full"
                assert identity_sign == 0
            elif identity_sign == 0:
                category = "same_side"
            elif identity_sign == -1:
                category = "reverse_separating"
            else:
                category = {1:"forward_singleton", 2:"forward_pair", 3:"forward_triple"}[len(G)]
            cut_counts[category] += 1
assert dict(cut_counts) == {
    "empty_or_full":24, "forward_singleton":12, "reverse_separating":48,
    "same_side":72, "forward_pair":24, "forward_triple":12,
}
assert sum(cut_counts.values()) == 192
global_terms = [2*hi*(1-eps), 1-lo/5, 3*hi-1]
assert global_terms == [Q(2499,2500), Q(9,10), Q(53,100)]
assert max(global_terms) < 1
cert["zero_sum_cut_norm"] = {
    "ordered_column_pairs":12, "subsets_per_pair":16, "category_counts":dict(cut_counts),
    "uniform_bounds_same_side_forward_pair_reverse":string_fractions(global_terms),
    "uniform_rate":str(max(global_terms)), "gap_from_one":str(1-max(global_terms)),
}

# Below-half scalar entry: polynomial identities plus the minimum at q=2/5.
f = (1-l)*u + l*(1-u)**2
assert u-f == l*(3*u-u*u-1)
entry_poly = 3*u-u*u-1
entry_der_bern = bernstein_from_power(entry_poly.deriv(3).sub({3:q+(1-q)*u}).uni_coeffs(3,1))
assert all(x > 0 for x in entry_der_bern)
assert entry_poly.eval(u=q) == Q(1,25)
assert (1-u)*(1-2*u) == 1-3*u+2*u*u
cert["below_half"] = {
    "entry_polynomial_minimum_on_q_to_one": "1/25",
    "entry_polynomial_derivative_bernstein_on_2_over_5_to_one": string_fractions(entry_der_bern),
    "entry_bound": "d=lambda*(3*q-q^2-1); N=ceil((1-q)/d)",
    "cap": "q=max(2/5,lambda), 0<lambda<1/2",
    "rate": "L=1-lambda*(1-2*q)",
}

# Independent verification of the half-step dependency used only by the
# distinct 0.502 perturbative method.
half_envelope = Q(1,2)*((s+v)/2) + Q(1,2)*(1-(s+v)/2)**2 - Q(1,8)*((1-s)**2-v)
half_claim = Q(1,8)*(3+(2*s-1)*v+v*v)
assert half_envelope == half_claim
assert half_claim.sub({2:(1-s)**2}) == Q(1,8)*(3+s*s*(1-s)**2)
qh, dh = Q(49,128), Q(15,64)
eh = dh*dh/2
Rh = 1-eh
thetah = eh/(dh-2*eh)**2
hh = (dh-eh)*(1-thetah)
assert eh == Q(225,8192)
assert Rh == Q(7967,8192)
assert thetah == Q(2048,2401) < 1
assert hh == Q(598335,19668992) > eh
assert Q(1,2)+qh == Q(113,128) < Rh
cert["half_step_dependency"] = {
    "cap":str(qh), "d":str(dh), "epsilon":str(eh),
    "theta_at_epsilon":str(thetah), "h_at_epsilon":str(hh),
    "h_minus_epsilon":str(hh-eh), "R":str(Rh),
}

ep = Q(1,500)
lp = Q(251,500)
rp = 1+lp
comparison_coefficient = 3+2*(1+rp+rp*rp)
rate = Rh+13*ep
assert comparison_coefficient == Q(1564501,125000) < 13
assert rate == Q(1022499,1024000) < 1
assert 1-rate == Q(1501,1024000)
cert["distinct_0502_perturbative_method"] = {
    "lambda_upper":str(lp), "e_upper":str(ep),
    "exact_error_coefficient_upper":str(comparison_coefficient),
    "rounded_coefficient":13, "R":str(Rh),
    "uniform_rate":str(rate), "gap_from_one":str(1-rate),
}

live_changes = {}
for name in SOURCES:
    current = sha256((ROOT / name).read_bytes()).hexdigest()
    if current != EXPECTED_INITIAL_HASHES[name]:
        live_changes[name] = current
cert["live_source_hashes_differing_at_run"] = live_changes
cert["all_assertions_passed"] = True
OUT.write_text(json.dumps(cert, indent=2) + "\n")
print(json.dumps(cert, indent=2))
