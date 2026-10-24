"""Exact self-checks for X018. Requires SymPy; no LP or floating arithmetic."""
from itertools import combinations
from pathlib import Path
import json
import sympy as s

E = tuple(range(6))
pairs = list(combinations(E, 2))
triples = list(combinations(E, 3))
pidx = {p: i for i, p in enumerate(pairs)}
tidx = {t: i for i, t in enumerate(triples)}
edges = []
for A in pairs:
    for J in pairs:
        if not set(A) & set(J):
            B = tuple(i for i in E if i not in A + J)
            edges.append((A, J, B))
eidx = {e: i for i, e in enumerate(edges)}

def clean(z):
    return s.expand(z)

def clean_matrix(M):
    return M.applyfunc(clean)

def zero_matrix(M):
    assert clean_matrix(M) == s.zeros(M.rows, M.cols)

def middle(A, J):
    return [tuple(sorted(A + (j,))) for j in J]

L = s.Matrix([[int(set(J) <= set(M)) for M in triples] for J in pairs])
P = s.zeros(45, 90)
G = s.zeros(20, 90)
for j, (A, J, B) in enumerate(edges):
    for color, pair in enumerate((A, J, B)):
        P[15 * color + pidx[pair], j] = 1
    for M in middle(A, J):
        G[tidx[M], j] = 1

values = {0: -s.Rational(1, 4), 1: s.Rational(1, 12),
          2: -s.Rational(1, 12), 3: s.Rational(1, 4)}
Pi = s.Matrix([[values[len(set(M) & set(N))] for N in triples]
               for M in triples])
zero_matrix(L * Pi)
zero_matrix(Pi * Pi - Pi)
assert s.trace(Pi) == 5
zero_matrix(P * G.T * Pi)
zero_matrix(G * G.T * Pi - 6 * Pi)
R = G.T * Pi / 6
zero_matrix(G * R - Pi)
for _, (A, J, B) in enumerate(edges):
    v = s.zeros(20, 1)
    for M in middle(A, J):
        v[tidx[M]] = 1
    assert (v.T * Pi * v)[0] == s.Rational(1, 3)
sharp_delta = Pi * G[:, 0]
assert (R * sharp_delta)[0] ** 2 == (sharp_delta.T * sharp_delta)[0] / 108
assert ((R * sharp_delta).T * (R * sharp_delta))[0] == (
    sharp_delta.T * sharp_delta)[0] / 6

def matchings(xs):
    if not xs:
        yield ()
        return
    for b in xs[1:]:
        for tail in matchings(tuple(x for x in xs if x not in (xs[0], b))):
            yield ((xs[0], b),) + tail

def cube(m):
    return s.Matrix([
        (-1) ** sum(p[1] in M for p in m)
        if all(len(set(p) & set(M)) == 1 for p in m) else 0
        for M in triples
    ])

all_matchings = list(matchings(E))
basis_matchings = [
    ((0, 1), (2, 3), (4, 5)),
    ((0, 1), (2, 4), (3, 5)),
    ((0, 2), (1, 3), (4, 5)),
    ((0, 2), (1, 4), (3, 5)),
    ((0, 3), (1, 4), (2, 5)),
]
basis = [cube(m) for m in basis_matchings]
assert s.Matrix.hstack(*basis).rank() == 5
for m in all_matchings:
    q = cube(m)
    zero_matrix(L * q)
    for A, J, B in edges:
        cost = sum(q[tidx[M]] for M in middle(A, J))
        alternate = -sum(q[tidx[tuple(sorted(J + (a,)))]] for a in A)
        assert cost == alternate

def householder(h):
    h = s.Matrix(h)
    return s.eye(6) - 2 * h * h.T / (h.T * h)[0]

D = s.diag((3 + 4*s.I)/5, 1, 1, (5 + 12*s.I)/13, 1, 1)
Q = clean_matrix(householder([1, 2, 3, 4, 5, 6])
                 * D * householder([2, -1, 3, -2, 1, 4]))
zero_matrix(Q.H * Q - s.eye(6))
W, U, Z = Q[:, :2], Q[:, 2:4], Q[:, 4:6]
PW, PU, PZ = [clean_matrix(V * V.H) for V in (W, U, Z)]

def minor(F, rows):
    return clean(F.extract(list(rows), list(range(F.cols))).det())

def abs2(z):
    return clean(z * s.conjugate(z))

def pair_law(F):
    return s.Matrix([abs2(minor(F, J)) for J in pairs])

def aggregate(F, H):
    return s.Matrix([
        sum(abs2(minor(F.row_join(H[:, j]), M)) for j in range(2))
        for M in triples
    ])

a, h, c = [pair_law(F) for F in (W, U, Z)]
assert all(x > 0 for v in (a, h, c) for x in v)
for law in (a, h, c):
    assert sum(law) == 1
gWU, gUW, gUZ = aggregate(W, U), aggregate(U, W), aggregate(U, Z)
zero_matrix(gUW + gUZ - L.T * h)
ds = [minor(U, J) for J in pairs]
rs = []
for M in triples:
    r = s.zeros(6, 1)
    for k, i in enumerate(M):
        J = tuple(j for j in M if j != i)
        r[i] = (-1)**k * s.conjugate(ds[pidx[J]])
    rs.append(r)
    adj = PU.extract(list(M), list(M)).adjugate()
    zero_matrix(r.extract(list(M), [0]) * r.extract(list(M), [0]).H - adj)
    zero_matrix(U.H * r)
zero_matrix(sum((r*r.H for r in rs), s.zeros(6)) - (s.eye(6) - PU))

def cofactor_observable(q):
    return clean_matrix(sum((q[i]*r*r.H for i, r in enumerate(rs)),
                            s.zeros(6)))

def verify_slack(q):
    beta = sum(h[j] * sum(max(q[i], 0) for i, M in enumerate(triples)
                         if set(J) <= set(M)) for j, J in enumerate(pairs))
    t = clean((q.T * gWU)[0])
    minus = clean(sum(max(q[i], 0)*gUW[i] + max(-q[i], 0)*gUZ[i]
                      for i in range(20)))
    plus = clean(sum(max(q[i], 0)*gUZ[i] + max(-q[i], 0)*gUW[i]
                     for i in range(20)))
    assert clean(beta-t-minus) == 0
    assert clean(beta+t-plus) == 0
    assert minus >= 0 and plus >= 0
    return beta, t, minus, plus

for q in basis:
    C = cofactor_observable(q)
    zero_matrix(C * U)
    assert clean(s.trace(C)) == 0
    assert clean((q.T * (gWU + gUW))[0]) == 0
    assert clean((q.T * gWU)[0] + s.trace(PW * C)) == 0
    verify_slack(q)

# Two additional combinations have nontrivial mixed signs.
for coefficients in ((1, -2, 3, -4, 5), (2, 1, -3, 4, -2)):
    q = sum((z*b for z, b in zip(coefficients, basis)), s.zeros(20, 1))
    verify_slack(q)

cube_slacks = []
for m in all_matchings:
    q = cube(m)
    beta, t, minus, plus = verify_slack(q)
    assert beta == sum(h[pidx[J]] for J in pairs if J not in m)
    x = s.zeros(90, 1)
    for J in pairs:
        outside = tuple(r for r in E if r not in J)
        if J in m:
            A = outside[:2]
            B = outside[2:]
            x[eidx[(A, J, B)]] = h[pidx[J]]
        elif beta != 0:
            vals = {r: q[tidx[tuple(sorted(J + (r,)))]] for r in outside}
            z = min(r for r in outside if vals[r] == 0)
            for sign in (1, -1):
                r = next(r for r in outside if vals[r] == -sign)
                A = tuple(sorted((z, r)))
                B = tuple(r for r in outside if r not in A)
                x[eidx[(A, J, B)]] = h[pidx[J]]*(beta+sign*t)/(2*beta)
    assert all(v >= 0 for v in x)
    zero_matrix(P[15:30, :] * x - h)
    assert clean((q.T * G * x)[0] - t) == 0
    cube_slacks.append({"matching": m, "beta": str(beta), "t": str(t),
                        "minus_slack": str(minus), "plus_slack": str(plus),
                        "flow_support": sum(v != 0 for v in x)})

# Determinantal sharpness certificate.
I = s.eye(6)
W0, U0 = I[:, [1, 5]], I[:, [0, 2]]
q0 = cube(basis_matchings[0])
assert (q0.T * aggregate(W0, U0))[0] == 1
assert sum(pair_law(U0)[pidx[J]] for J in pairs
           if J not in basis_matchings[0]) == 1

result = {
    "status": "all exact checks passed",
    "arithmetic": "exact rational complex (SymPy), no LP",
    "harmonic_projector_rank": 5,
    "right_inverse_factor": 6,
    "sharp_infinity_norm_squared": "1/108",
    "full_support_pair_laws": 3,
    "harmonic_basis_trace_and_reciprocity_checks": 5,
    "general_signed_combination_slack_checks": 2,
    "cube_slack_and_explicit_addition_flow_checks": 15,
    "sharp_projection_flag": {"W": [1, 5], "U": [0, 2], "Z": [3, 4],
                              "cube_value": 1, "off_matching_mass": 1},
    "frame": [[str(Q[i, j]) for j in E] for i in E],
    "cube_certificates": cube_slacks,
}
dest = Path(__file__).with_name("verified_output.json")
dest.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items()
                  if k not in ("frame", "cube_certificates")}, indent=2))
