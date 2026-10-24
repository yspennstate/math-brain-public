#!/usr/bin/env python3
"""Exact finite certificate for NM13-07 / E0095, C_16 plus a perfect matching.

Claim checked:
  among all perfect matchings M of V(C_16) using only non-cycle edges,
  min_M lambda_2(A(C_16 union M)) = sqrt(3).
Hence the maximal Poincare spectral gap of simple random walk is
  1 - sqrt(3)/3.

The proof core is exact.  Floating-point eigensolvers are used only to SELECT
integer Rayleigh witnesses when a cheap integer Krylov witness is not found.
Every selected witness is then checked using Python integer arithmetic:
    sum(w)=0, N=w^T A w > 0, N^2 > 3 D^2, D=w^T w.
This implies lambda_2(A)>sqrt(3) by the Rayleigh principle.  The two equality
cases are checked by SymPy's exact characteristic polynomial.
"""

from functools import lru_cache
from itertools import combinations
import numpy as np
import sympy as sp

NVERT = 16
FULL = (1 << NVERT) - 1
CYCLE = {tuple(sorted((i, (i + 1) % NVERT))) for i in range(NVERT)}

M1 = tuple(sorted(((0, 5), (1, 12), (2, 7), (3, 14),
                   (4, 9), (6, 11), (8, 13), (10, 15))))
M2 = tuple(sorted(((0, 11), (1, 6), (2, 13), (3, 8),
                   (4, 15), (5, 10), (7, 12), (9, 14))))
EQUALITY = {M1, M2}
EXPECTED_COUNT = 673471


def norm_matching(pairs):
    return tuple(sorted(tuple(sorted(e)) for e in pairs))


def matchings(mask, pairs=()):
    if mask == 0:
        yield norm_matching(pairs)
        return
    i = (mask & -mask).bit_length() - 1
    rest = mask & ~(1 << i)
    for j in range(i + 1, NVERT):
        if ((rest >> j) & 1) and (i, j) not in CYCLE:
            yield from matchings(rest & ~(1 << j), pairs + ((i, j),))


@lru_cache(None)
def matching_count(mask):
    if mask == 0:
        return 1
    i = (mask & -mask).bit_length() - 1
    rest = mask & ~(1 << i)
    out = 0
    for j in range(i + 1, NVERT):
        if ((rest >> j) & 1) and (i, j) not in CYCLE:
            out += matching_count(rest & ~(1 << j))
    return out


def adjacency(matching, dtype=np.int64):
    A = np.zeros((NVERT, NVERT), dtype=dtype)
    for i in range(NVERT):
        j = (i + 1) % NVERT
        A[i, j] = A[j, i] = 1
    for i, j in matching:
        A[i, j] = A[j, i] = 1
    return A


def exact_rayleigh(A, w):
    # Inputs fit in int64 here; convert final scalars to arbitrary precision.
    w = np.asarray(w, dtype=np.int64)
    assert int(w.sum()) == 0
    D = int(w @ w)
    Q = A @ w
    R = int(w @ Q)
    return R, D, (D > 0 and R > 0 and R * R > 3 * D * D)


SEEDS = []
for j in range(1, 8):
    z = np.zeros(NVERT, dtype=np.int64)
    z[0], z[j] = 1, -1
    SEEDS.append(z)


def krylov_witness(A, steps=8):
    # B=A+3I is positive semidefinite and preserves the zero-sum subspace.
    B = A + 3 * np.eye(NVERT, dtype=np.int64)
    for seed in SEEDS[:3]:
        w = seed.copy()
        for _ in range(steps):
            w = B @ w
        R, D, ok = exact_rayleigh(A, w)
        if ok:
            return (R, D)
    return None


def rounded_witness(A):
    # Numerical diagonalization is ONLY a witness selector.  The returned
    # integer vector must pass exact_rayleigh, or this graph is not certified.
    _, vecs = np.linalg.eigh(A.astype(float))
    for col in (-2, -3, -4):
        v = vecs[:, col]
        for scale in (10_000, 100_000, 1_000_000, 10_000_000):
            w = np.rint(v * scale).astype(np.int64)
            w[-1] -= int(w.sum())  # exact orthogonality to the constant vector
            R, D, ok = exact_rayleigh(A, w)
            if ok:
                return (R, D)
    return None


def exact_charpoly(matching):
    A = sp.zeros(NVERT)
    for i in range(NVERT):
        j = (i + 1) % NVERT
        A[i, j] = A[j, i] = 1
    for i, j in matching:
        A[i, j] = A[j, i] = 1
    x = sp.symbols("x")
    return sp.factor(A.charpoly(x).as_expr())


def dihedral_image(matching, shift, reflect):
    out = []
    for a, b in matching:
        if reflect:
            a, b = (-a) % NVERT, (-b) % NVERT
        a, b = (a + shift) % NVERT, (b + shift) % NVERT
        out.append((a, b))
    return norm_matching(out)


def valid_two_switches(matching):
    m = list(matching)
    out = set()
    for p, q in combinations(range(len(m)), 2):
        a, b = m[p]
        c, d = m[q]
        rest = [e for r, e in enumerate(m) if r not in (p, q)]
        for pair2 in (((a, c), (b, d)), ((a, d), (b, c))):
            pair2 = [tuple(sorted(e)) for e in pair2]
            if any(u == v or (u, v) in CYCLE for u, v in pair2):
                continue
            nm = norm_matching(rest + pair2)
            if len(nm) == NVERT // 2:
                out.add(nm)
    return out


def main():
    assert matching_count(FULL) == EXPECTED_COUNT

    expected_poly = (sp.Symbol("x") - 3) * (sp.Symbol("x") - 1) ** 3 \
        * (sp.Symbol("x") + 1) ** 3 * (sp.Symbol("x") + 3) \
        * (sp.Symbol("x") ** 2 - 3) ** 4
    p1 = exact_charpoly(M1)
    p2 = exact_charpoly(M2)
    assert sp.expand(p1 - expected_poly) == 0
    assert sp.expand(p2 - expected_poly) == 0

    orbit = {
        dihedral_image(M1, shift, reflect)
        for reflect in (False, True)
        for shift in range(NVERT)
    }
    assert orbit == EQUALITY

    total = strict = equality = krylov_ok = fallback_ok = 0
    smallest_fallback_margin = None

    for m in matchings(FULL):
        total += 1
        A = adjacency(m)
        assert np.all(A.sum(axis=0) == 3)
        if m in EQUALITY:
            equality += 1
            continue
        cert = krylov_witness(A)
        if cert is not None:
            strict += 1
            krylov_ok += 1
            continue
        cert = rounded_witness(A)
        if cert is None:
            raise AssertionError(f"uncertified matching: {m}")
        R, D = cert
        margin = R * R - 3 * D * D
        assert R > 0 and margin > 0
        strict += 1
        fallback_ok += 1
        if smallest_fallback_margin is None or margin < smallest_fallback_margin:
            smallest_fallback_margin = margin

    assert total == EXPECTED_COUNT
    assert equality == 2
    assert strict == EXPECTED_COUNT - 2

    switches = valid_two_switches(M1)
    assert len(switches) == 40
    for m in switches:
        assert m not in EQUALITY
        A = adjacency(m)
        cert = krylov_witness(A) or rounded_witness(A)
        assert cert is not None

    print("E0095 C16 exact certificate")
    print(f"matchings_exhausted={total}")
    print(f"strictly_above_sqrt3={strict}")
    print(f"equality_matchings={equality}")
    print(f"krylov_exact_witnesses={krylov_ok}")
    print(f"fallback_integer_witnesses={fallback_ok}")
    print(f"smallest_fallback_integer_margin={smallest_fallback_margin}")
    print(f"dihedral_orbit_size_of_M1={len(orbit)}")
    print(f"valid_two_switch_perturbations={len(switches)}")
    print(f"M1={M1}")
    print(f"M2={M2}")
    print(f"candidate_charpoly={p1}")
    print("lambda2_min=sqrt(3)")
    print("poincare_gap_max=1-sqrt(3)/3")
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
