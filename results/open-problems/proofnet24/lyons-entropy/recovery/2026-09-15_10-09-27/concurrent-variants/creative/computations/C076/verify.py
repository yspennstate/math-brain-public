#!/usr/bin/env python3
"""Exact reproducer for C076. Requires sympy and mpmath.

The interval theorem is proved analytically in agents/C076.md. This script
verifies the exact block/channel laws, finite gap, all example hypotheses,
rank-three data, and rational lower bound. Logarithmic signs use rational
atanh-series enclosures; decimal evaluations are separate illustrations.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

OUT = Path(__file__).resolve().parent
q = sp.Rational
I = sp.I
p, zr, zi = sp.symbols("p zr zi", real=True)
t = sp.Symbol("t", real=True)
z = zr+I*zi
Pplus = sp.Matrix([[1, 1], [1, 1]])/2
Pminus = sp.eye(2)-Pplus
x, y = q(1, 2)-p/5, q(13, 20)-p/10
B = y*Pplus+x*Pminus
T = Pplus/10+Pminus/5
checks = []
atom_count = 0


def check(name, condition):
    assert condition, name
    checks.append(name)


def simplify_matrix(A):
    return A.applyfunc(sp.cancel)


def zero(A):
    return all(sp.cancel(v) == 0 for v in A)


def principal_det(A, mask):
    ix = [i for i in range(A.rows) if mask & (1 << i)]
    return A.extract(ix, ix).det() if ix else sp.Integer(1)


def atoms(A):
    global atom_count
    n = A.rows
    eye = sp.eye(n)
    moments = [principal_det(A, s) for s in range(1 << n)]
    result = []
    for s in range(1 << n):
        cols = [A[:, j] if s & (1 << j) else eye[:, j]-A[:, j]
                for j in range(n)]
        det_atom = sp.cancel(sp.Matrix.hstack(*cols).det())
        inversion = sp.cancel(sum(
            (-1)**(u.bit_count()-s.bit_count())*moments[u]
            for u in range(1 << n) if u & s == s))
        assert sp.cancel(det_atom-inversion) == 0
        atom_count += 1
        result.append(det_atom)
    assert sp.cancel(sum(result)-1) == 0
    return result


def at(law, replacements):
    return [sp.cancel(v.subs(replacements)) for v in law]


def str_matrix(A):
    return [[str(sp.cancel(A[i, j])) for j in range(A.cols)]
            for i in range(A.rows)]


D = sp.Matrix([[q(1, 2), q(1, 3)], [q(1, 3), q(1, 3)]])
u = sp.Matrix([1, 0])
alpha = 1/(u.T*D.inv()*u)[0]
beta = 1/(u.T*(sp.eye(2)-D).inv()*u)[0]
ell = alpha+beta
check("normalization constants", (alpha, beta, ell) == (q(1, 6), q(1, 3), q(1, 2)))
check("guide is not a reservoir eigenvector", sp.Matrix.hstack(u, D*u).det() != 0)
check("reservoir strict", D.det() > 0 and (sp.eye(2)-D).det() > 0
      and 0 < D[0, 0] < 1)
Q0, Q1 = D-alpha*u*u.T, D+beta*u*u.T
check("channel endpoint spectra",
      set(Q0.eigenvals()) == {0, q(2, 3)} and set(Q1.eigenvals()) == {q(1, 6), 1})
C0, C1 = atoms(Q0), atoms(Q1)
check("exact endpoint channel columns",
      C0 == [q(1, 3), q(1, 3), q(1, 3), 0]
      and C1 == [0, q(2, 3), q(1, 6), q(1, 6)])
tauC = sum(abs(b-a) for a, b in zip(C0, C1))/2
groups = [
    {"name": "A", "weight": q(2, 3), "r": q(1, 2), "s": q(1, 2)},
    {"name": "B", "weight": q(1, 3), "r": 0, "s": q(1, 2)},
]
muC = sum(g["weight"]*g["s"]**2 for g in groups)
check("channel TV and second moment", tauC == q(1, 2) and muC == q(1, 4))
check("balanced refinement slope sum",
      sum(g["weight"]*g["s"] for g in groups) == tauC)

# Physical four-site kernel has rational complex entries. The seed's sqrt(2)
# cancels in all atom laws; refined seed matrices are rational directly.
K = sp.zeros(4)
K[:2, :2] = D+(ell*p-alpha)*u*u.T
K[2:, 2:] = B
for j in [2, 3]:
    K[0, j] = sp.conjugate(z)/2
    K[j, 0] = z/2
N = sp.zeros(3)
N[0, 0] = p
N[1:, 1:] = B
for j in [1, 2]:
    N[0, j] = sp.conjugate(z)/sp.sqrt(2)
    N[j, 0] = z/sp.sqrt(2)
Pg = []
Ng = []
for g in groups:
    A = sp.zeros(3)
    A[0, 0] = g["r"]+g["s"]*p
    A[1:, 1:] = B
    for j in [1, 2]:
        A[0, j] = sp.conjugate(z)/2
        A[j, 0] = z/2
    Ng.append(A)
    Pg.append(atoms(A))
PK, PN = atoms(K), atoms(N)

for bottom in range(4):
    for left in range(4):
        full = PK[left+4*bottom]
        check(f"generic block-channel atom {left},{bottom}",
              sp.cancel(full-C0[left]*PN[2*bottom]-C1[left]*PN[2*bottom+1]) == 0)
        group_index, bit = (0, left) if left < 2 else (1, left-2)
        check(f"generic two-group atom {left},{bottom}",
              sp.cancel(full-groups[group_index]["weight"] *
                        Pg[group_index][2*bottom+bit]) == 0)

p0, p1 = q(1, 3), q(2, 3)
z0, z1 = (1+I)/10, (2-I)/12
replacements = [
    {p: p0, zr: sp.re(z0), zi: sp.im(z0)},
    {p: p1, zr: sp.re(z1), zi: sp.im(z1)},
]
K0, K1 = [simplify_matrix(K.subs(s)) for s in replacements]
direction = K1-K0
active = direction.extract([0, 2, 3], [0, 2, 3])
check("active rank-three determinant", active.det() == q(59, 36000))
check("rank-three physical direction", direction.rank() == 3)
check("negative two-mode complementary direction",
      set((B.subs(p, p1)-B.subs(p, p0)).eigenvals()) == {-q(1, 30), -q(1, 15)})
check("noncommuting physical endpoints",
      (K0*K1-K1*K0)[1, 2] == (4+11*I)/360)
for j, Kj in enumerate([K0, K1]):
    check(f"endpoint {j} rank-one nonzero cross block", Kj[:2, 2:].rank() == 1)
    check(f"endpoint {j} coherent reservoir blocks",
          Kj[0, 1] != 0 and Kj[2, 3] != 0)
lmi_margins = []
for j, (pj, zj) in enumerate([(p0, z0), (p1, z1)]):
    xj, yj = x.subs(p, pj), y.subs(p, pj)
    nz = sp.expand(zj*sp.conjugate(zj))
    margins = [pj*(yj-q(1, 4))-nz, (1-pj)*(q(3, 4)-yj)-nz]
    check(f"endpoint {j} convex domain margins",
          q(1, 4) <= pj <= q(3, 4) and q(1, 4) <= xj <= q(3, 4)
          and all(m > 0 for m in margins))
    lmi_margins.append(margins)
check("stated exact LMI margins",
      lmi_margins == [[q(23, 225), q(31, 450)], [q(3, 16), q(1, 48)]])
centerB = B.subs(p, q(1, 2))
check("older atom criterion fails in new domain",
      all(((sp.eye(2)-centerB).inv()-sp.eye(2))[i, i] == q(13, 12)
          and (centerB.inv()-sp.eye(2))[i, i] == q(13, 12) for i in [0, 1]))

pt, zt = (1-t)*p0+t*p1, (1-t)*z0+t*z1
line = {p: pt, zr: sp.re(zt), zi: sp.im(zt)}
dp, dz = p1-p0, z1-z0
ndz = sp.expand(dz*sp.conjugate(dz))
R = ndz*Pplus+dp**2*T
V = t*(1-t)*R
mid = q(1, 2)
pm, zm = pt.subs(t, mid), zt.subs(t, mid)
traceV = sp.trace(V).subs(t, mid)
nzm = sp.expand(zm*sp.conjugate(zm))
check("midpoint exact strength and covariance trace",
      traceV == q(257, 14400) and nzm == traceV)
bound = muC*(2*mid*(1-mid)*dp**2+
              q(16, 15)*traceV*nzm+q(8, 15)*traceV**2)
check("exact stated finite lower bound", bound == q(7266049, 518400000))

# Rational prime-log expressions certify finite entropy identities exactly.
def add(*terms):
    result = defaultdict(lambda: sp.Integer(0))
    for term in terms:
        for prime, coefficient in term.items():
            result[prime] += coefficient
    return {prime: sp.cancel(c) for prime, c in result.items() if c != 0}


def scale(c, term):
    return {prime: sp.cancel(c*v) for prime, v in term.items() if c*v != 0}


@lru_cache(None)
def logq(x):
    x = q(x)
    result = defaultdict(int)
    for prime, exponent in sp.factorint(x.p).items():
        result[int(prime)] += exponent
    for prime, exponent in sp.factorint(x.q).items():
        result[int(prime)] -= exponent
    return {prime: q(e) for prime, e in result.items() if e}


def entropy(law):
    return add(*(scale(-v, logq(v)) for v in law if v != 0))


def h(a):
    return entropy([a, 1-a])


def gap(laws):
    return add(entropy(laws[1]), scale(-q(1, 2), entropy(laws[0])),
               scale(-q(1, 2), entropy(laws[2])))


def conditional(A, i):
    a, zz, BB = A[0, 0], A[1:, 0], A[1:, 1:]
    return simplify_matrix(BB-zz*zz.conjugate().T/a if i
                           else BB+zz*zz.conjugate().T/(1-a))


def modes(A):
    return [sp.cancel(sp.trace(Pplus*A)), sp.cancel(sp.trace(Pminus*A))]


def balanced(A):
    values = modes(A)
    return zero(A-values[0]*Pplus-values[1]*Pminus) and all(
        q(1, 4) <= v <= q(3, 4) for v in values)


group_certificates = []
group_gaps = []
group_formal = []
for g_index, g in enumerate(groups):
    Aline = simplify_matrix(Ng[g_index].subs(line))
    a = Aline[0, 0]
    b = 1-a
    Vg = g["s"]*V
    check(f"group {g['name']} scaled covariance",
          zero(t*(1-t)*(
              (Aline[1:, 0].subs(t, 1)-Aline[1:, 0].subs(t, 0)) *
              (Aline[1:, 0].subs(t, 1)-Aline[1:, 0].subs(t, 0)).conjugate().T
              -(a.subs(t, 1)-a.subs(t, 0)) *
              (Aline[1:, 1:].subs(t, 1)-Aline[1:, 1:].subs(t, 0))
          )-Vg))
    F = {i: conditional(Aline, i) for i in [0, 1]}
    G = {(j, i): conditional(Aline.subs(t, j), i)
         for j in [0, 1] for i in [0, 1]}
    ws = {}
    M = {}
    for i in [0, 1]:
        pivot = a if i else b
        ws[i] = [(1-t)*pivot.subs(t, 0)/pivot, t*pivot.subs(t, 1)/pivot]
        M[i] = simplify_matrix(ws[i][0]*G[0, i]+ws[i][1]*G[1, i])
        check(f"group {g['name']} branch {i} symbolic covariance identity",
              zero(F[i]-M[i]-(Vg/a if i else -Vg/b)))
    check(f"group {g['name']} ordered correction path identity",
          zero(F[0]-F[1] -
               (Aline[1:, 0]*Aline[1:, 0].conjugate().T)/(a*b)))
    matrices = {f"G{j}{i}": G[j, i] for j in [0, 1] for i in [0, 1]}
    matrices.update({f"F{i}": F[i].subs(t, mid) for i in [0, 1]})
    matrices.update({f"M{i}": M[i].subs(t, mid) for i in [0, 1]})
    for name, Q in matrices.items():
        check(f"group {g['name']} balanced matrix {name}", balanced(Q))
    laws = {name: atoms(Q) for name, Q in matrices.items()}
    Pl = [at(Pg[g_index], {**replacements[0]}),
          at(Pg[g_index], {p: pm, zr: sp.re(zm), zi: sp.im(zm)}),
          at(Pg[g_index], {**replacements[1]})]
    group_gap = gap(Pl)
    am, bm = a.subs(t, mid), b.subs(t, mid)
    Jh = add(h(am), scale(-q(1, 2), h(a.subs(t, 0))),
             scale(-q(1, 2), h(a.subs(t, 1))))
    terms = {"J_h": Jh}
    correction = {}
    for i, prob in [(1, am), (0, bm)]:
        Ji = add(entropy(laws[f"M{i}"]),
                 *(scale(-ws[i][j].subs(t, mid), entropy(laws[f"G{j}{i}"]))
                   for j in [0, 1]))
        terms[f"{'a' if i else 'b'}_J{i}"] = scale(prob, Ji)
        correction[i] = scale(prob, add(entropy(laws[f"F{i}"]),
                                       scale(-1, entropy(laws[f"M{i}"]))))
    combined = add(correction[0], correction[1])
    terms["paired_correction"] = combined
    check(f"group {g['name']} exact finite entropy decomposition",
          add(group_gap, scale(-1, add(*terms.values()))) == {})
    vgtrace = g["s"]*traceV
    zgnorm = g["s"]*nzm
    correction_lower = (q(4, 15)*vgtrace*zgnorm+q(2, 15)*vgtrace**2)/(am*bm)
    group_gaps.append(group_gap)
    group_formal.append({"gap": group_gap, **terms,
                         "included_correction": correction[1],
                         "excluded_correction": correction[0]})
    group_certificates.append({
        "name": g["name"], "weight": str(g["weight"]),
        "r": str(g["r"]), "s": str(g["s"]),
        "conditional_matrices": {name: str_matrix(Q) for name, Q in matrices.items()},
        "conditional_mode_values": {name: list(map(str, modes(Q))) for name, Q in matrices.items()},
        "atom_probabilities": {name: list(map(str, law)) for name, law in laws.items()},
        "exact_paired_correction_lower_bound": str(correction_lower),
    })

physical_laws = [
    at(PK, replacements[0]),
    at(PK, {p: pm, zr: sp.re(zm), zi: sp.im(zm)}),
    at(PK, replacements[1]),
]
physical_gap = gap(physical_laws)
weighted_group_gap = add(*(scale(g["weight"], expr)
                           for g, expr in zip(groups, group_gaps)))
check("exact physical gap equals fixed group average",
      add(physical_gap, scale(-1, weighted_group_gap)) == {})

# Rigorous log intervals: log x = 2 atanh((x-1)/(x+1)).
# Reduce each prime by a power of two so the series ratio is at most 1/3.
def series_log_interval(x, terms=40):
    zeta = (x-1)/(x+1)
    partial = sum(2*zeta**(2*k+1)/q(2*k+1) for k in range(terms))
    tail = 2*zeta**(2*terms+1)/(q(2*terms+1)*(1-zeta*zeta))
    return partial, partial+tail


@lru_cache(None)
def prime_log_interval(prime):
    exponent = int(prime).bit_length()-1
    normalized = q(prime, 2**exponent)
    lo, hi = series_log_interval(normalized)
    lo2, hi2 = series_log_interval(q(2))
    lo, hi = lo+exponent*lo2, hi+exponent*hi2
    unit = 10**30
    lower = (lo*unit).p//(lo*unit).q
    upper = -((-hi*unit).p//(-hi*unit).q)
    return q(lower, unit), q(upper, unit)


def expression_interval(expr):
    low, high = sp.Integer(0), sp.Integer(0)
    for prime, c in expr.items():
        lo, hi = prime_log_interval(prime)
        low += c*(lo if c >= 0 else hi)
        high += c*(hi if c >= 0 else lo)
    return sp.cancel(low), sp.cancel(high)


intervals = []
for index, (g, forms) in enumerate(zip(groups, group_formal)):
    enclosed = {name: expression_interval(expr) for name, expr in forms.items()}
    check(f"group {g['name']} paired correction rigorous positivity",
          enclosed["paired_correction"][0] > 0)
    check(f"group {g['name']} paired correction rigorous quantitative bound",
          enclosed["paired_correction"][0] >
          q(group_certificates[index]["exact_paired_correction_lower_bound"]))
    intervals.append(enclosed)
check("an individual included correction is rigorously negative",
      any(values["included_correction"][1] < 0 for values in intervals))
physical_interval = expression_interval(physical_gap)
check("physical entropy gap rigorously exceeds rational lower bound",
      physical_interval[0] > bound)

def serialize_expr(expr):
    return {str(prime): str(c) for prime, c in sorted(expr.items())}


def serialize_intervals(values):
    return {name: [str(lo), str(hi)] for name, (lo, hi) in values.items()}


certificate = {
    "status": "all exact checks passed",
    "exact_atom_determinant_mobius_equalities": atom_count,
    "named_exact_check_count": len(checks), "named_exact_checks": checks,
    "K0": str_matrix(K0), "K1": str_matrix(K1),
    "physical_direction": str_matrix(direction),
    "active_direction_minor": str(active.det()),
    "physical_direction_inertia": [1, 2, 1],
    "noncommutator_entry_2_3": str((K0*K1-K1*K0)[1, 2]),
    "endpoint_LMI_margins": [[str(v) for v in row] for row in lmi_margins],
    "channel_columns": [list(map(str, C0)), list(map(str, C1))],
    "channel_TV": str(tauC), "channel_second_moment": str(muC),
    "midpoint_traceV": str(traceV), "midpoint_coupling_strength": str(nzm),
    "rational_gap_lower_bound": str(bound),
    "physical_atom_laws": [list(map(str, law)) for law in physical_laws],
    "groups": group_certificates,
    "exact_physical_gap_prime_logs": serialize_expr(physical_gap),
    "exact_group_gap_prime_logs": [
        {name: serialize_expr(expr) for name, expr in forms.items()}
        for forms in group_formal],
    "rigorous_group_logarithmic_enclosures": [serialize_intervals(v) for v in intervals],
    "rigorous_physical_gap_enclosure": list(map(str, physical_interval)),
    "exact_fixed_group_gap_residual": {},
}
mp.mp.dps = 70
def dec(x):
    x = q(x)
    return mp.mpf(int(x.p))/mp.mpf(int(x.q))


def evaluate(expr):
    return mp.fsum(dec(c)*mp.log(prime) for prime, c in expr.items())


def output_number(x):
    return mp.nstr(x, 55)


numeric_groups = [{name: output_number(evaluate(expr)) for name, expr in forms.items()}
                  for forms in group_formal]
numerical_gap = evaluate(physical_gap)
numeric_residual = numerical_gap-mp.fsum(
    dec(g["weight"])*evaluate(expr) for g, expr in zip(groups, group_gaps))
results = {
    "decimal_precision": mp.mp.dps,
    "physical_midpoint_entropy_gap": output_number(numerical_gap),
    "proved_rational_lower_bound": str(bound),
    "proved_lower_bound_decimal": output_number(dec(bound)),
    "group_terms_before_weighting": numeric_groups,
    "numerical_fixed_group_residual": output_number(numeric_residual),
    "individual_included_correction_negative": [
        values["included_correction"][1] < 0 for values in intervals
    ],
    "note": "All identities and signs above have exact rational certificates; decimals are illustrations.",
}
(OUT/"exact_certificate.json").write_text(json.dumps(certificate, indent=2)+"\n")
(OUT/"results.json").write_text(json.dumps(results, indent=2, default=bool)+"\n")
print(f"PASS: {atom_count} exact atom equalities and {len(checks)} named exact checks.")
print("Exact gap identities pass; rational logarithm enclosures certify signs.")
print(json.dumps(results, indent=2, default=bool))
