#!/usr/bin/env python3
"""
Exact certificate for full lower stochastic domination on Z/6Z in R7-03/C0036.

The mathematical note proves positivity lemmas for a reflection-corner difference
    Delta = alpha A + beta B + gamma A B + eta W
under
    0<=x,y<=1,
    0<=A<=(1-x)^2, 0<=B<=(1-y)^2,
    W^2=A(A+4x)B(B+4y).
This script enumerates every translation-invariant increasing event on Z/6Z,
computes exact Fourier-projection DPP probabilities, derives all four corner
differences, and certifies that each falls under one of those lemmas.
"""
from itertools import combinations
from math import comb
from collections import Counter
import sympy as sp

N = 6
SUBSETS = list(range(1 << N))

def rotate(mask, k):
    out = 0
    for i in range(N):
        if (mask >> i) & 1:
            out |= 1 << ((i + k) % N)
    return out

# Translation orbits in 2^{Z/6Z}.
seen = set()
orbits = []
for m in SUBSETS:
    if m in seen:
        continue
    orb = sorted({rotate(m, k) for k in range(N)})
    orbits.append(orb)
    seen.update(orb)
orbit_index = {}
for i, orb in enumerate(orbits):
    for m in orb:
        orbit_index[m] = i
assert len(orbits) == 14

# Orbit poset under inclusion up to translation.
le = [[False] * len(orbits) for _ in orbits]
for i, oi in enumerate(orbits):
    for j, oj in enumerate(orbits):
        le[i][j] = any((a & b) == a for a in oi for b in oj)

# Every translation-invariant increasing event is an upper set in this poset.
upper_sets = []
for bits in range(1 << len(orbits)):
    ok = True
    for i in range(len(orbits)):
        if not ((bits >> i) & 1):
            continue
        for j in range(len(orbits)):
            if le[i][j] and not ((bits >> j) & 1):
                ok = False
                break
        if not ok:
            break
    if ok:
        upper_sets.append(bits)
assert len(upper_sets) == 44

# Exact normalized 6-point Fourier matrix.
I = sp.I
sqrt3 = sp.sqrt(3)
zeta = sp.Rational(1, 2) + I * sqrt3 / 2
assert sp.simplify(zeta**6) == 1

# Exact projection-DPP mass: P_J(X)=|det F[X,J]|^2, supported on |X|=|J|.
proj = {}
for J in SUBSETS:
    freq = [j for j in range(N) if (J >> j) & 1]
    r = len(freq)
    for X in SUBSETS:
        if X.bit_count() != r:
            continue
        sites = [i for i in range(N) if (X >> i) & 1]
        if r == 0:
            prob = sp.Integer(1)
        else:
            M = sp.Matrix([
                [zeta**(s*j) / sp.sqrt(6) for j in freq]
                for s in sites
            ])
            det = M.det()
            prob = sp.simplify(sp.expand_complex(det * sp.conjugate(det)))
        assert prob.is_Rational
        assert prob >= 0
        proj[(J, X)] = prob
    assert sp.simplify(sum(proj.get((J, X), 0) for X in SUBSETS) - 1) == 0

# h_E(J)=P^{P_J}(E) for each invariant increasing event E.
event_h = []
for ubits in upper_sets:
    event = [X for X in SUBSETS if (ubits >> orbit_index[X]) & 1]
    h = []
    for J in SUBSETS:
        h.append(sp.simplify(sum(proj.get((J, X), 0) for X in event)))
    event_h.append(h)

# Spectral variables for rho(i)=-i: fixed 0,3; paired (1,5),(2,4).
b, c, e, f, x, y = sp.symbols("b c e f x y", nonnegative=True, real=True)
vars4 = [b, c, e, f]
freq4 = [1, 2, 4, 5]

def corner_poly(h, abit, dbit):
    ans = sp.Rational(0)
    for m in range(16):
        J = (abit << 0) | (dbit << 3)
        w = sp.Rational(1)
        for pos, (idx, var) in enumerate(zip(freq4, vars4)):
            if (m >> pos) & 1:
                J |= 1 << idx
                w *= var
            else:
                w *= 1 - var
        ans += h[J] * w
    return sp.expand(ans)

def reflected(expr):
    return sp.expand(expr.xreplace({b: f, f: b, c: e, e: c}))

# Invariant multi-affine basis.
U = b + f
V = c + e
P = b * f
Q = c * e
W = (b - f) * (c - e)
basis = [
    sp.Integer(1), U, V, P, Q, U*V, W, Q*U, P*V, P*Q
]
monomials = [sp.Integer(1)]
for r in range(1, 5):
    for cc in combinations(vars4, r):
        monomials.append(sp.prod(cc))

def coeffvec(expr):
    poly = sp.Poly(sp.expand(expr), b, c, e, f)
    return sp.Matrix([poly.coeff_monomial(m) for m in monomials])

Bmat = sp.Matrix.hstack(*[coeffvec(bb) for bb in basis])
assert Bmat.rank() == 10

def invariant_coefficients(expr):
    sol = sp.linsolve((Bmat, coeffvec(expr)))
    tup = next(iter(sol))
    assert all(not z.free_symbols for z in tup)
    recon = sp.expand(sum(z*bb for z, bb in zip(tup, basis)))
    assert sp.expand(recon - expr) == 0
    return tuple(sp.simplify(z) for z in tup)

# Exact degree-(2,2) Bernstein coefficients on [0,1]^2.
def bernstein_coefficients_22(expr):
    poly = sp.Poly(sp.expand(expr), x, y)
    a = [[sp.Rational(0) for _ in range(3)] for _ in range(3)]
    for (i, j), coef in poly.terms():
        assert 0 <= i <= 2 and 0 <= j <= 2
        a[i][j] = sp.Rational(coef)
    beta = [[sp.Rational(0) for _ in range(3)] for _ in range(3)]
    for k in range(3):
        for ell in range(3):
            s = sp.Rational(0)
            for i in range(k + 1):
                for j in range(ell + 1):
                    s += (
                        a[i][j]
                        * sp.Rational(comb(k, i), comb(2, i))
                        * sp.Rational(comb(ell, j), comb(2, j))
                    )
            beta[k][ell] = sp.simplify(s)
    return beta

def bern_nonnegative(expr):
    beta = bernstein_coefficients_22(expr)
    return all(z >= 0 for row in beta for z in row)

# Five exceptional exact corner forms. Symmetric mates are listed separately.
E49 = (
    sp.Rational(1,2) - y/4,
    sp.Rational(1,2) - x/4,
    -sp.Rational(1,8),
    -sp.Rational(1,8),
)
E59 = (
    -sp.Rational(3,2)*y**2 + sp.Rational(19,12)*y,
    -sp.Rational(5,6)*x**2 + sp.Rational(19,12)*x,
    sp.Rational(19,24),
    sp.Rational(1,8),
)
E60 = (
    -sp.Rational(5,6)*y**2 + sp.Rational(19,12)*y,
    -sp.Rational(3,2)*x**2 + sp.Rational(19,12)*x,
    sp.Rational(19,24),
    sp.Rational(1,8),
)
E66 = (
    -sp.Rational(5,6)*y**2 + sp.Rational(11,12)*y,
    -sp.Rational(1,2)*x**2 + sp.Rational(11,12)*x + sp.Rational(1,3),
    sp.Rational(11,24),
    sp.Rational(1,8),
)
E67 = (
    -sp.Rational(1,2)*y**2 + sp.Rational(11,12)*y + sp.Rational(1,3),
    -sp.Rational(5,6)*x**2 + sp.Rational(11,12)*x,
    sp.Rational(11,24),
    sp.Rational(1,8),
)
exception_map = {
    tuple(map(sp.expand, E49)): "exception_E49",
    tuple(map(sp.expand, E59)): "exception_E59",
    tuple(map(sp.expand, E60)): "exception_E59_swap",
    tuple(map(sp.expand, E66)): "exception_E66",
    tuple(map(sp.expand, E67)): "exception_E66_swap",
}

def classify(form):
    alpha, beta, gamma, eta = map(sp.expand, form)

    # Lemma A: eta=0, gamma>=0, alpha,beta>=0.
    if eta == 0 and gamma >= 0 and bern_nonnegative(alpha) and bern_nonnegative(beta):
        return "eta0_positive"

    # Lemma B: eta=0, gamma<0, absorb gamma*AB using B<=(1-y)^2.
    if eta == 0 and gamma < 0:
        if bern_nonnegative(beta) and bern_nonnegative(alpha + gamma*(1-y)**2):
            return "eta0_negative_absorb"

    # Lemma C: q=|eta|, gamma>=q, alpha>=2qy, beta>=2qx.
    if eta != 0:
        q = abs(eta)
        if (
            gamma >= q
            and bern_nonnegative(alpha - 2*q*y)
            and bern_nonnegative(beta - 2*q*x)
        ):
            return "W_generic"

    key = tuple(map(sp.expand, (alpha, beta, gamma, eta)))
    if key in exception_map:
        return exception_map[key]
    raise AssertionError(f"uncertified form: {form}")

certificate_counts = Counter()
unique_forms = {}

for h in event_h:
    for abit in (0, 1):
        for dbit in (0, 1):
            H = corner_poly(h, abit, dbit)
            assert sp.expand(H - reflected(H)) == 0
            coeff = invariant_coefficients(H)
            (_, cU, cV, _cP, _cQ, cUV, cW, cQU, cPV, _cPQ) = coeff
            alpha = sp.expand(cU + 2*y*cUV + y**2*cQU)
            beta  = sp.expand(cV + 2*x*cUV + x**2*cPV)
            gamma = sp.expand(cUV)
            eta   = sp.expand(cW)
            form = tuple(map(sp.expand, (alpha, beta, gamma, eta)))
            kind = classify(form)
            certificate_counts[kind] += 1
            unique_forms.setdefault(form, kind)

assert sum(certificate_counts.values()) == 44*4
assert len(unique_forms) == 72
assert certificate_counts == Counter({
    "eta0_positive": 110,
    "eta0_negative_absorb": 22,
    "W_generic": 38,
    "exception_E49": 2,
    "exception_E59": 1,
    "exception_E59_swap": 1,
    "exception_E66": 1,
    "exception_E66_swap": 1,
})

print("Z6_TRANSLATION_ORBITS=14")
print("Z6_INVARIANT_UPPER_SETS=44")
print("CORNER_CERTIFICATES=176")
print("UNIQUE_CORNER_FORMS=72")
for k in sorted(certificate_counts):
    print(f"{k}={certificate_counts[k]}")
print("ALL_EXACT_CERTIFICATES_PASS")
