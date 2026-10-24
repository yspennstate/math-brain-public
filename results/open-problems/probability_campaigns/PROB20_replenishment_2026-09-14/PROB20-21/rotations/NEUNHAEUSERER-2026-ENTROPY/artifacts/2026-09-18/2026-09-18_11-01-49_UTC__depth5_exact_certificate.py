#!/usr/bin/env python3
"""Exact certificate for the depth-5 frontier of NEUNHAEUSERER-2026-ENTROPY.

This script uses exact Fraction arithmetic for every mathematical PASS decision.
It certifies:
  1. every realizable collision pattern for five arbitrary positive real weights
     is represented by one of 216 entropy signatures;
  2. H''(p)<0 for every one of those signatures on
     [1/2560000, 1/2] by rational Bernstein bounds and rigorous rational
     logarithm intervals.

The run report combines this with the already-proved arbitrary-depth endpoint
lemma on (0, 1/2560000] and complement symmetry, yielding global strict
concavity for all positive-real five-weight Bernoulli sums.

For runtime robustness the 216 signatures can be checked in shards, e.g.
  python depth5_exact_certificate.py --start 0 --stop 27
and then [27,54), ..., [189,216).
"""
from argparse import ArgumentParser
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, gcd
import hashlib

M = 5


def rref_key(rows):
    A = [[F(x) for x in row] for row in rows if any(F(x) != 0 for x in row)]
    if not A:
        return ()
    r = c = 0
    while r < len(A) and c < M:
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            c += 1
            continue
        A[r], A[piv] = A[piv], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                z = A[i][c]
                A[i] = [A[i][j] - z * A[r][j] for j in range(M)]
        r += 1
        c += 1
    nz = [tuple(row) for row in A if any(x != 0 for x in row)]
    nz.sort(key=lambda row: next(i for i, x in enumerate(row) if x != 0))
    return tuple(nz)


def primitive_int(v):
    den = 1
    for x in v:
        den = den * x.denominator // gcd(den, x.denominator)
    z = [int(x * den) for x in v]
    g = 0
    for x in z:
        g = gcd(g, abs(x))
    if g:
        z = [x // g for x in z]
    for x in z:
        if x:
            if x < 0:
                z = [-y for y in z]
            break
    return tuple(z)


def nullspace_basis(key):
    piv = [next(i for i, x in enumerate(row) if x != 0) for row in key]
    free = [j for j in range(M) if j not in piv]
    out = []
    for f in free:
        v = [F(0)] * M
        v[f] = F(1)
        for row, p in reversed(list(zip(key, piv))):
            v[p] = -sum(row[j] * v[j] for j in free)
        out.append(tuple(v))
    return out


# Primitive subset-difference normals. Equality of two subset sums, after
# cancellation, has normal in {-1,0,1}^5 with at least one +1 and one -1.
# Quotient by epsilon ~ -epsilon.
RELS = []
for v in product((-1, 0, 1), repeat=M):
    if 1 not in v or -1 not in v:
        continue
    first = next(x for x in v if x)
    if first < 0:
        v = tuple(-x for x in v)
    if v not in RELS:
        RELS.append(v)
assert len(RELS) == 90

# Exhaust all relation spans through rank 3. Rank 4 is reconstructed later
# from positive rank-3 subspaces plus one additional primitive relation.
levels = [{()}]
for target_rank in (1, 2, 3):
    nxt = set()
    for key in levels[-1]:
        for rel in RELS:
            nk = rref_key(list(key) + [rel])
            if len(nk) == target_rank:
                nxt.add(nk)
    levels.append(nxt)
assert [len(x) for x in levels] == [1, 90, 2780, 29955]


def span2_has_nonnegative_row_vector(key):
    """Exact Gordan obstruction for a 2-dimensional row space in R^5.

    A strictly positive vector exists in ker(key) iff the row space contains
    no nonzero componentwise-nonnegative vector.  For a 2D row space, write
    y = u + t v after normalizing a nonzero coefficient to 1 (and also -u+t v).
    Intersect the exact half-line constraints in t.
    """
    u, v = key

    def feasible(sign):
        lo = None  # strict/weak endpoints are harmless: we only need y>=0
        hi = None
        for j in range(M):
            a = sign * u[j]
            b = v[j]
            if b == 0:
                if a < 0:
                    return False
                continue
            t0 = -a / b
            if b > 0:
                lo = t0 if lo is None or t0 > lo else lo
            else:
                hi = t0 if hi is None or t0 < hi else hi
        return not (lo is not None and hi is not None and lo > hi)

    # Also allow coefficient of u to be zero, i.e. +/-v itself.
    if all(x >= 0 for x in v) and any(x > 0 for x in v):
        return True
    if all(x <= 0 for x in v) and any(x < 0 for x in v):
        return True
    return feasible(F(1)) or feasible(F(-1))


positive_rank2 = []
for key in levels[2]:
    if not span2_has_nonnegative_row_vector(key):
        positive_rank2.append(key)
assert len(positive_rank2) == 1985


def positive_rank3_basis(key):
    """Return a 2D nullspace basis iff ker(key) contains a strictly positive vector.

    Any vector is alpha*u + beta*v. Strict positivity is an open cone, so if it
    is nonempty we may normalize alpha to +1 or -1 (the alpha=0 case can be
    perturbed inside the open cone). Exact rational interval intersection in
    beta decides feasibility.
    """
    basis = nullspace_basis(key)
    assert len(basis) == 2
    u, v = basis
    for s in (F(1), F(-1)):
        lo = None
        hi = None
        ok = True
        for j in range(M):
            a = s * u[j]
            b = v[j]
            if b == 0:
                if a <= 0:
                    ok = False
                    break
                continue
            t0 = -a / b
            if b > 0:
                lo = t0 if lo is None or t0 > lo else lo
            else:
                hi = t0 if hi is None or t0 < hi else hi
        if ok and not (lo is not None and hi is not None and lo >= hi):
            return basis
    return None


positive_rank3 = {}
for key in levels[3]:
    b = positive_rank3_basis(key)
    if b is not None:
        positive_rank3[key] = b
assert len(positive_rank3) == 10765

# Every positive rank-4 relation span has a one-dimensional positive kernel.
# Since that span is generated by primitive relations, three independent
# generators give a positive rank-3 subspace already enumerated above. Add a
# fourth primitive relation. If u,v span the rank-3 kernel, imposing r.w=0
# leaves the ray (r.v)u-(r.u)v. Collect every strictly positive primitive ray.
positive_rank4_rays = set()
for basis in positive_rank3.values():
    u, v = basis
    for rel in RELS:
        ru = sum(F(rel[j]) * u[j] for j in range(M))
        rv = sum(F(rel[j]) * v[j] for j in range(M))
        if ru == 0 and rv == 0:
            continue
        w = [rv * u[j] - ru * v[j] for j in range(M)]
        if all(x > 0 for x in w) or all(x < 0 for x in w):
            if all(x < 0 for x in w):
                w = [-x for x in w]
            positive_rank4_rays.add(primitive_int(w))
assert len(positive_rank4_rays) == 8376


def collision_signature_from_basis(basis):
    """Exact Boolean-cube collision signature for the relation subspace.

    A primitive normal is active iff it annihilates the whole kernel. Union all
    subset pairs realizing active normals; transitive closure gives exactly the
    equal-subset-sum fibers. Return each fiber by counts at Boolean ranks 0..5.
    """
    parent = list(range(1 << M))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    active = []
    for rel in RELS:
        if all(sum(F(rel[j]) * b[j] for j in range(M)) == 0 for b in basis):
            active.append(rel)
    for rel in active:
        pos = [j for j, x in enumerate(rel) if x == 1]
        neg = [j for j, x in enumerate(rel) if x == -1]
        zero = [j for j, x in enumerate(rel) if x == 0]
        p0 = sum(1 << j for j in pos)
        n0 = sum(1 << j for j in neg)
        for zmask in range(1 << len(zero)):
            common = 0
            for t, j in enumerate(zero):
                if (zmask >> t) & 1:
                    common |= 1 << j
            union(p0 | common, n0 | common)

    classes = {}
    for mask in range(1 << M):
        root = find(mask)
        if root not in classes:
            classes[root] = [0] * (M + 1)
        classes[root][mask.bit_count()] += 1
    return tuple(sorted(tuple(v) for v in classes.values()))


SIGS = set()
SIGS.add(collision_signature_from_basis([tuple(F(int(i == j)) for i in range(M)) for j in range(M)]))
for key in levels[1]:
    SIGS.add(collision_signature_from_basis(nullspace_basis(key)))
for key in positive_rank2:
    SIGS.add(collision_signature_from_basis(nullspace_basis(key)))
for key, basis in positive_rank3.items():
    SIGS.add(collision_signature_from_basis(basis))
for w in positive_rank4_rays:
    SIGS.add(collision_signature_from_basis([tuple(F(x) for x in w)]))
SIGS = tuple(sorted(SIGS))
assert len(SIGS) == 216
SIG_DIGEST = hashlib.sha256(repr(SIGS).encode("utf-8")).hexdigest()
assert SIG_DIGEST == "67d49101d56b827f4c557ab31775b90b97abddad2d8386e75f38ab13aec9339b"

# ---------- Exact entropy-curvature interval certificate ----------

def q_poly(c):
    # Q_C(p)=sum_k c_k p^k(1-p)^(M-k), returned in power basis.
    out = [F(0)] * (M + 1)
    for k, ck in enumerate(c):
        if not ck:
            continue
        for j in range(M - k + 1):
            out[k + j] += F(ck * comb(M - k, j) * ((-1) ** j))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def deriv(a):
    return (F(0),) if len(a) == 1 else tuple(F(i) * a[i] for i in range(1, len(a)))


POLY = {}
for c in {c for sig in SIGS for c in sig}:
    q0 = q_poly(c)
    POLY[c] = (q0, deriv(q0), deriv(deriv(q0)))


def bernstein_bounds(coeff, a, b):
    d = len(coeff) - 1
    if d == 0:
        return coeff[0], coeff[0]
    h = b - a
    power = [F(0)] * (d + 1)
    for j, cj in enumerate(coeff):
        for r in range(j + 1):
            power[r] += cj * comb(j, r) * (a ** (j - r)) * (h ** r)
    beta = []
    for k in range(d + 1):
        beta.append(sum((power[j] * F(comb(k, j), comb(d, j)) for j in range(k + 1)), F(0)))
    return min(beta), max(beta)


def iadd(I, J):
    return I[0] + J[0], I[1] + J[1]


def imul(I, J):
    vals = (I[0] * J[0], I[0] * J[1], I[1] * J[0], I[1] * J[1])
    return min(vals), max(vals)


def isquare(I):
    a, b = I
    if a <= 0 <= b:
        return F(0), max(a * a, b * b)
    return min(a * a, b * b), max(a * a, b * b)


def idiv_pos(I, J):
    assert J[0] > 0
    return imul(I, (1 / J[1], 1 / J[0]))


def iscale(I, k):
    return (I[0] * k, I[1] * k) if k >= 0 else (I[1] * k, I[0] * k)


def floor_log2(x):
    n, d = x.numerator, x.denominator
    k = n.bit_length() - d.bit_length()
    while F(2) ** k > x:
        k -= 1
    while F(2) ** (k + 1) <= x:
        k += 1
    return k


def log2_bounds(N=10):
    # log 2 = 2 atanh(1/3), with an exact positive-tail bound.
    z = F(1, 3)
    zz = z * z
    term = z
    s = F(0)
    for j in range(N):
        s += term / F(2 * j + 1)
        term *= zz
    lo = 2 * s
    tail = 2 * term / (F(2 * N + 1) * (1 - zz))
    return lo, lo + tail


LOG2 = log2_bounds()


@lru_cache(maxsize=None)
def log_unit_bounds(y, N=8):
    # y in [1,2): log y = 2 atanh((y-1)/(y+1)); z in [0,1/3).
    assert F(1) <= y < F(2)
    z = (y - 1) / (y + 1)
    zz = z * z
    term = z
    s = F(0)
    for j in range(N):
        s += term / F(2 * j + 1)
        term *= zz
    lo = 2 * s
    tail = 2 * term / (F(2 * N + 1) * (1 - zz))
    return lo, lo + tail


@lru_cache(maxsize=None)
def log_bounds(x):
    assert x > 0
    k = floor_log2(x)
    y = x / (F(2) ** k)
    return iadd(iscale(LOG2, k), log_unit_bounds(y))


def S_interval(sig, a, b):
    # H'' = -S, where
    # S=sum_C [Q_C'' log Q_C + (Q_C')^2/Q_C].
    S = (F(0), F(0))
    for c in sig:
        q0, q1, q2 = POLY[c]
        Q = bernstein_bounds(q0, a, b)
        Q1 = bernstein_bounds(q1, a, b)
        Q2 = bernstein_bounds(q2, a, b)
        assert Q[0] > 0
        L = (log_bounds(Q[0])[0], log_bounds(Q[1])[1])
        S = iadd(S, iadd(imul(Q2, L), idiv_pos(isquare(Q1), Q)))
    return S


def certify(sig, a, b, depth=0, maxdepth=16, records=None):
    if records is None:
        records = []
    S = S_interval(sig, a, b)
    if S[0] > 0:
        records.append((a, b, S[0], S[1], depth))
        return True, records
    if depth >= maxdepth:
        records.append((a, b, S[0], S[1], depth))
        return False, records
    mid = (a + b) / 2
    ok, records = certify(sig, a, mid, depth + 1, maxdepth, records)
    if not ok:
        return False, records
    return certify(sig, mid, b, depth + 1, maxdepth, records)


def main():
    ap = ArgumentParser()
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--stop", type=int, default=216)
    args = ap.parse_args()
    assert 0 <= args.start < args.stop <= len(SIGS)

    LO, HI = F(1, 2560000), F(1, 2)
    summaries = []
    for idx in range(args.start, args.stop):
        ok, recs = certify(SIGS[idx], LO, HI)
        assert ok
        summaries.append((len(recs), max(r[4] for r in recs), min(r[2] for r in recs)))
    global_min = min(x[2] for x in summaries)
    assert global_min > 0

    print("PASS")
    print("relation_normals =", len(RELS))
    print("spans_rank_0_3 =", [len(x) for x in levels])
    print("positive_rank2_spans =", len(positive_rank2))
    print("positive_rank3_spans =", len(positive_rank3))
    print("positive_rank4_rays =", len(positive_rank4_rays))
    print("entropy_signatures =", len(SIGS))
    print("signatures_sha256 =", SIG_DIGEST)
    print("certified_signature_range = [%d,%d)" % (args.start, args.stop))
    print("certified_interval = [1/2560000,1/2]")
    print("terminal_rational_intervals =", sum(x[0] for x in summaries))
    print("max_bisection_depth =", max(x[1] for x in summaries))
    print("minimum_exact_lower_bound_positive =", global_min > 0)
    print("minimum_lower_bound_float_diagnostic =", float(global_min))


if __name__ == "__main__":
    main()
