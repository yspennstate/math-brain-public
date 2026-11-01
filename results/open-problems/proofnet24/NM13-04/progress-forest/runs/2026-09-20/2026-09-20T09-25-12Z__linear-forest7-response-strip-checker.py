from itertools import combinations, product
from functools import lru_cache
import collections
import math
import sympy as sp

# NM13-04 / T07 exact checker.
# The theorem certified here is:
#   G = K3 join H, where H is any disjoint union of paths P_l, 1<=l<=7,
# has strict pairwise negative edge correlation for the unit-weight uniform
# measure on all forests.
#
# The finite computation is only a local-response classification.  The
# all-parameter step is symbolic: all unmarked right components collapse to
# a 2D response strip (u,v), and every local Rayleigh polynomial is proved
# positive on that entire strip.


def canon(labels):
    mp = {}
    out = []
    nxt = 0
    for a in labels:
        if a not in mp:
            mp[a] = nxt
            nxt += 1
        out.append(mp[a])
    return tuple(out)


TERMINAL_STATES = [
    canon((0, 1, 2)), canon((0, 1, 1)), canon((0, 0, 1)),
    canon((0, 1, 0)), canon((0, 0, 0))
]


def union_part(labels, a, b):
    labels = list(labels)
    if labels[a] == labels[b]:
        return None
    la, lb = labels[a], labels[b]
    labels = [la if q == lb else q for q in labels]
    return canon(labels)


def introduce(labels):
    return canon(tuple(labels) + (max(labels, default=-1) + 1,))


def forget(labels, idx):
    return canon(tuple(q for i, q in enumerate(labels) if i != idx))


@lru_cache(None)
def transfer_path(length, required_tuple=()):
    """Five-terminal-partition transfer of one right P_length.

    Local edge IDs are ('s',i,t) for a spoke from path vertex i to terminal t,
    and ('i',i,i+1) for an internal path edge.  required_tuple means that all
    listed edges are forced present.
    """
    required = set(required_tuple)
    M = [[0] * 5 for _ in range(5)]
    for si, tstate in enumerate(TERMINAL_STATES):
        dp = {introduce(tstate): 1}
        stage = [(('s', 0, t), t, 3) for t in range(3)]
        nd = collections.defaultdict(int)
        for lab, cnt in dp.items():
            for bits in product([0, 1], repeat=3):
                if any((eid in required) and not bit
                       for bit, (eid, _, __) in zip(bits, stage)):
                    continue
                cur = lab
                ok = True
                for bit, (eid, a, b) in zip(bits, stage):
                    if bit:
                        cur2 = union_part(cur, a, b)
                        if cur2 is None:
                            ok = False
                            break
                        cur = cur2
                if ok:
                    nd[cur] += cnt
        dp = nd

        for i in range(1, length):
            nd = collections.defaultdict(int)
            stage = [(('i', i - 1, i), 3, 4)] + [
                (('s', i, t), t, 4) for t in range(3)
            ]
            for lab, cnt in dp.items():
                lab2 = introduce(lab)
                for bits in product([0, 1], repeat=4):
                    if any((eid in required) and not bit
                           for bit, (eid, _, __) in zip(bits, stage)):
                        continue
                    cur = lab2
                    ok = True
                    for bit, (eid, a, b) in zip(bits, stage):
                        if bit:
                            cur2 = union_part(cur, a, b)
                            if cur2 is None:
                                ok = False
                                break
                            cur = cur2
                    if ok:
                        nd[forget(cur, 3)] += cnt
            dp = nd

        for lab, cnt in dp.items():
            sj = TERMINAL_STATES.index(forget(lab, 3))
            M[si][sj] += cnt
    return sp.Matrix(M)


S = transfer_path(1)
N = S - 4 * sp.eye(5)
assert N**3 == sp.zeros(5)
assert N**2 != sp.zeros(5)

ABC = {}
for L in range(1, 8):
    M = transfer_path(L)
    A = sp.Integer(M[0, 0])
    B = sp.Integer(M[0, 1])
    C = sp.Rational(M[0, 4] - B, 6)
    assert M == A * sp.eye(5) + B * N + C * N**2
    ABC[L] = (A, B, C)

EXPECTED_ABC = {
    1: (sp.Integer(4), sp.Integer(1), sp.Integer(0)),
    2: (sp.Integer(23), sp.Integer(12), sp.Rational(5, 3)),
    3: (sp.Integer(130), sp.Integer(103), sp.Rational(85, 3)),
    4: (sp.Integer(734), sp.Integer(780), sp.Rational(961, 3)),
    5: (sp.Integer(4144), sp.Integer(5524), sp.Rational(9050, 3)),
    6: (sp.Integer(23396), sp.Integer(37512), sp.Integer(25562)),
    7: (sp.Integer(132088), sp.Integer(247492), sp.Integer(202132)),
}
assert ABC == EXPECTED_ABC

# For normalized T_l/A_l = I + a_l N + c_l N^2, define
# rho_l = (a_l^2/2 - c_l)/a_l.  For a product of unmarked layers,
# u = sum a_i and v = sum c_i + sum_{i<j}a_i a_j, hence
# u^2/2 - v = sum rho_i a_i.  Therefore the physical response lies in
# v = u^2/2 - h u with h a weighted average of the rho_i.
rhos = {}
for L, (A, B, C) in ABC.items():
    a = sp.Rational(B, A)
    c = sp.Rational(C, A)
    rho = sp.factor((a*a/2 - c) / a)
    rhos[L] = rho

EXPECTED_RHOS = {
    1: sp.Rational(1, 8),
    2: sp.Rational(101, 828),
    3: sp.Rational(9727, 80340),
    4: sp.Rational(103613, 858780),
    5: sp.Rational(1033583, 8584296),
    6: sp.Rational(13190815, 109703844),
    7: sp.Rational(70123811, 583762916),
}
assert rhos == EXPECTED_RHOS
for L in range(1, 7):
    assert rhos[L] > rhos[L + 1] > 0
rho_min = rhos[7]
rho_max = rhos[1]

u, v, y = sp.symbols('u v y', nonnegative=True)
U = sp.eye(5) + u * N + v * N**2
one = sp.ones(5, 1)


def q_core(required_edges):
    """Triangle forest response, with required core edges forced present."""
    req = set(required_edges)
    tri = [(0, 1), (0, 2), (1, 2)]
    counts = [0] * 5
    for bits in product([0, 1], repeat=3):
        chosen = [tri[i] for i, b in enumerate(bits) if b]
        if not req.issubset(set(chosen)):
            continue
        if len(chosen) == 3:
            continue
        parent = list(range(3))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def join(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        for a, b in chosen:
            join(a, b)
        part = canon(tuple(find(i) for i in range(3)))
        counts[TERMINAL_STATES.index(part)] += 1
    return sp.Matrix([counts])

assert q_core([]) == sp.Matrix([[1, 1, 1, 1, 3]])
assert q_core([(0, 1)]) == sp.Matrix([[0, 0, 1, 0, 2]])
assert q_core([(0, 1), (0, 2)]) == sp.Matrix([[0, 0, 0, 0, 1]])

# Universal local witness: triangle plus two copies of every P_l, 1<=l<=7.
# Any marked edge pair in any target graph meets at most two right components,
# so after labelling those components it occurs here.
edges = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    edges.append(('core', a, b))
for L in range(1, 8):
    for copy in range(2):
        for i in range(L):
            for t in range(3):
                edges.append(('right', L, copy, 's', i, t))
        for i in range(L - 1):
            edges.append(('right', L, copy, 'i', i, i + 1))
assert len(edges) == 213
assert math.comb(len(edges), 2) == 22578


def local_edge(e):
    assert e[0] == 'right'
    _, L, copy, kind, a, b = e
    return (kind, a, b)


def quantity_coeffs(pair, required):
    """Return alpha,beta,gamma with I_required=alpha+beta*u+gamma*v."""
    core_req = []
    comps = {}
    for e in pair:
        if e[0] == 'core':
            if e in required:
                _, a, b = e
                core_req.append(tuple(sorted((a, b))))
        else:
            _, L, copy, kind, a, b = e
            comps.setdefault((L, copy), []).append(e)

    row = q_core(core_req)
    for (L, copy), comp_edges in sorted(comps.items()):
        req = [local_edge(e) for e in comp_edges if e in required]
        M = transfer_path(L, tuple(sorted(req, key=repr))) if req else transfer_path(L)
        row = row * M

    return (
        sp.Integer((row * one)[0]),
        sp.Integer((row * N * one)[0]),
        sp.Integer((row * (N**2) * one)[0]),
    )


def affine(c):
    a0, b0, c0 = c
    return a0 + b0 * u + c0 * v


def rayleigh_uv(pair):
    e, f = pair
    I = affine(quantity_coeffs(pair, set()))
    Ie = affine(quantity_coeffs(pair, {e}))
    If = affine(quantity_coeffs(pair, {f}))
    Ief = affine(quantity_coeffs(pair, {e, f}))
    return sp.Poly(sp.expand(Ie * If - I * Ief), u, v, domain=sp.QQ)


def edesc(e):
    if e[0] == 'core':
        return f'C{e[1]}{e[2]}'
    _, L, copy, kind, a, b = e
    return f'P{L}.{copy}:{kind}{a}-{b}'


def bernstein_deg2(poly_y):
    """Degree-2 Bernstein coefficients on y in [0,1]."""
    p = sp.Poly(sp.expand(poly_y), y, domain=sp.QQ)
    assert p.degree() <= 2
    c0 = p.coeff_monomial(1)
    c1 = p.coeff_monomial(y)
    c2 = p.coeff_monomial(y**2)
    return [sp.factor(c0), sp.factor(c0 + c1 / 2), sp.factor(c0 + c1 + c2)]


# Parameterize the exact response strip by
# h = rho_min + y(rho_max-rho_min), 0<=y<=1,
# v = u^2/2 - h u.
h = rho_min + y * (rho_max - rho_min)
vstrip = u**2 / 2 - h * u

# Deduplicate exact Q(u,v) polynomials only for reporting; positivity is checked
# once per distinct Q.  Every one of the 22,578 witness pairs is mapped to one.
unique = {}
for pair in combinations(edges, 2):
    P = rayleigh_uv(pair)
    key = tuple(P.terms())
    if key not in unique:
        unique[key] = (pair, P)
assert len(unique) == 749

regular = []
exceptional = []
min_regular_constant = None
min_regular_bernstein = None

for pair, P in unique.values():
    R = sp.Poly(sp.expand(P.as_expr().subs(v, vstrip)), u, y, domain=sp.QQ)
    # Write R=sum_i r_i(y) u^i and certify each r_i by its degree-2
    # Bernstein coefficients.  If this succeeds and r_0>0, R>0.
    Pu = sp.Poly(R.as_expr(), u, domain=sp.QQ[y])
    all_b = []
    for i in range(5):
        ri = sp.expand(Pu.coeff_monomial(u**i))
        if ri != 0:
            all_b.extend(bernstein_deg2(ri))
    const = sp.factor(R.as_expr().subs({u: 0, y: 0}))
    if all(b >= 0 for b in all_b) and const > 0:
        regular.append((pair, P, R))
        pos = [b for b in all_b if b > 0]
        if pos:
            m = min(pos)
            min_regular_bernstein = m if min_regular_bernstein is None else min(min_regular_bernstein, m)
        min_regular_constant = const if min_regular_constant is None else min(min_regular_constant, const)
    else:
        exceptional.append((pair, P, R))

assert len(regular) == 736
assert len(exceptional) == 13
assert min_regular_constant == 2
assert min_regular_bernstein == 1

expected_exception_desc = [
    ('P4.0:s0-0', 'P4.0:s3-1'),
    ('P5.0:s0-0', 'P5.0:s3-1'),
    ('P5.0:s0-0', 'P5.0:s4-1'),
    ('P6.0:s0-0', 'P6.0:s3-1'),
    ('P6.0:s0-0', 'P6.0:s4-1'),
    ('P6.0:s0-0', 'P6.0:s5-1'),
    ('P6.0:s1-0', 'P6.0:s4-1'),
    ('P7.0:s0-0', 'P7.0:s3-1'),
    ('P7.0:s0-0', 'P7.0:s4-1'),
    ('P7.0:s0-0', 'P7.0:s5-1'),
    ('P7.0:s0-0', 'P7.0:s6-1'),
    ('P7.0:s1-0', 'P7.0:s4-1'),
    ('P7.0:s1-0', 'P7.0:s5-1'),
]
actual_exception_desc = [(edesc(pair[0]), edesc(pair[1])) for pair, _, _ in exceptional]
assert actual_exception_desc == expected_exception_desc

# Each exceptional strip polynomial has the special shape
#   a4 u^4 - b3(y)u^3 + a2(y)u^2 + a1(y)u + a0,
# with a4,a2,a1,a0 positive on [0,1], b3 positive, and
#   4 a4 a2(y) - b3(y)^2 = D > 0.
# Hence u^2(a4 u^2-b3 u+a2)>0 for u>0 by negative discriminant,
# while the lower terms are positive.  At u=0 the constant is positive.
exception_discriminants = []
for pair, P, R in exceptional:
    Pu = sp.Poly(R.as_expr(), u, domain=sp.QQ[y])
    coeff = {i: sp.factor(Pu.coeff_monomial(u**i)) for i in range(5)}
    a4 = coeff[4]
    b3 = -coeff[3]
    a2 = coeff[2]
    a1 = coeff[1]
    a0 = coeff[0]
    assert a4 > 0 and a0 > 0
    assert all(z > 0 for z in bernstein_deg2(a2))
    assert all(z > 0 for z in bernstein_deg2(a1))
    assert all(z > 0 for z in bernstein_deg2(b3))
    D = sp.factor(4 * a4 * a2 - b3**2)
    assert sp.degree(D, y) == 0
    assert D > 0
    exception_discriminants.append((edesc(pair[0]), edesc(pair[1]), D))

EXPECTED_D = [
    16476912,
    12901593600,
    1156460544,
    12802993007616,
    907023960000,
    76503301056,
    10096206840000,
    12954731194211328,
    902212338069504,
    60028920979200,
    4954651893504,
    10019454655795200,
    710839190880000,
]
assert [int(D) for _, _, D in exception_discriminants] == EXPECTED_D

print('T07 triangle + right linear forest (component order <=7) exact sign checker')
print('N^3=0 and N^2!=0: PASS')
print('unmarked path transfers T_l=A_l I+B_l N+C_l N^2:')
for L in range(1, 8):
    print(f'  P{L}: A,B,C={ABC[L]} rho={rhos[L]}')
print('strict rho ordering rho1>...>rho7>0: PASS')
print('response strip: v=u^2/2-hu, h in [rho7,1/8]: PASS')
print('universal local witness: 213 edges, 22578 unordered pairs: PASS')
print('distinct exact local Rayleigh Q(u,v) polynomials:', len(unique))
print('regular strip-Bernstein certificates: 736/749 PASS')
print('minimum regular constant =', min_regular_constant)
print('minimum positive regular Bernstein coefficient =', min_regular_bernstein)
print('exceptional exact discriminant certificates:')
for a, b, D in exception_discriminants:
    print(f'  {a} | {b} : D={D}')
print('exceptional count 13/749; all D>0 and all lower coefficients positive: PASS')
print('THEOREM CERTIFIED: K3 join any disjoint union of P_l, 1<=l<=7, is strictly unit-p-NC')
print('ALL_EXACT_CHECKS_PASS')
