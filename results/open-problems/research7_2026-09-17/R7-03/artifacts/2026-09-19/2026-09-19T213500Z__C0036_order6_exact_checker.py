#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations, product


def cyclic_orbits(n):
    seen = set()
    out = []
    for mask in range(1 << n):
        if mask in seen:
            continue
        orb = set()
        for sh in range(n):
            m = 0
            for i in range(n):
                if (mask >> i) & 1:
                    m |= 1 << ((i + sh) % n)
            orb.add(m)
        seen |= orb
        out.append(sorted(orb))
    return out


def compose(g, h):
    return tuple(g[h[i]] for i in range(len(g)))


def s3_left_perms():
    elts = list(permutations(range(3)))
    idx = {g: i for i, g in enumerate(elts)}
    return [[idx[compose(g, h)] for h in elts] for g in elts]


def subset_orbits(perms, n):
    seen = set()
    out = []
    for mask in range(1 << n):
        if mask in seen:
            continue
        orb = set()
        for perm in perms:
            m = 0
            for i in range(n):
                if (mask >> i) & 1:
                    m |= 1 << perm[i]
            orb.add(m)
        seen |= orb
        out.append(sorted(orb))
    return out


def orbit_leq(A, B):
    return any((a & ~b) == 0 for a in A for b in B)


def upper_sets(orbits):
    m = len(orbits)
    leq = [[orbit_leq(orbits[i], orbits[j]) for j in range(m)] for i in range(m)]
    ans = []
    for um in range(1 << m):
        ok = True
        for i in range(m):
            if (um >> i) & 1:
                for j in range(m):
                    if leq[i][j] and not ((um >> j) & 1):
                        ok = False
                        break
            if not ok:
                break
        if ok:
            ans.append(um)
    return ans


def det_frac(mat):
    n = len(mat)
    if n == 0:
        return Fraction(1)
    A = [row[:] for row in mat]
    det = Fraction(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if A[r][i]), None)
        if piv is None:
            return Fraction(0)
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            det = -det
        pv = A[i][i]
        det *= pv
        for j in range(i + 1, n):
            A[i][j] /= pv
        for r in range(i + 1, n):
            f = A[r][i]
            if f:
                for j in range(i + 1, n):
                    A[r][j] -= f * A[i][j]
            A[r][i] = Fraction(0)
    return det


COS1 = [Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2)]
COS2 = [Fraction(1), Fraction(-1, 2), Fraction(-1, 2), Fraction(1), Fraction(-1, 2), Fraction(-1, 2)]


def qrow_sym(a, b, c, d):
    return [(a + d * ((-1) ** j) + 2 * b * COS1[j] + 2 * c * COS2[j]) / 6 for j in range(6)]


def exact_probs(a, b, c, d):
    row = qrow_sym(a, b, c, d)
    Q = [[row[(i - j) % 6] for j in range(6)] for i in range(6)]
    inc = [Fraction(0)] * 64
    inc[0] = Fraction(1)
    for mask in range(1, 64):
        ids = [i for i in range(6) if (mask >> i) & 1]
        inc[mask] = det_frac([[Q[i][j] for j in ids] for i in ids])
    probs = inc[:]
    for bit in range(6):
        for mask in range(64):
            if not ((mask >> bit) & 1):
                probs[mask] -= probs[mask | (1 << bit)]
    assert sum(probs, Fraction(0)) == 1
    assert min(probs) >= 0
    return probs


def edge_union_coeff(edges):
    coeff = {}
    for fm in range(1, 1 << len(edges)):
        vm = 0
        k = 0
        for j, (u, v) in enumerate(edges):
            if (fm >> j) & 1:
                k += 1
                vm |= (1 << u) | (1 << v)
        coeff[vm] = coeff.get(vm, 0) + (1 if k & 1 else -1)
    return {m: c for m, c in coeff.items() if c}


z6 = cyclic_orbits(6)
s3 = subset_orbits(s3_left_perms(), 6)
uz6 = upper_sets(z6)
us3 = upper_sets(s3)
assert len(z6) == 14 and len(uz6) == 44
assert len(s3) == 16 and len(us3) == 76

orbit_of = {}
for oi, orb in enumerate(z6):
    for cfg in orb:
        orbit_of[cfg] = oi

adj = edge_union_coeff([(i, (i + 1) % 6) for i in range(6)])
d2 = edge_union_coeff(sorted({tuple(sorted((i, (i + 2) % 6))) for i in range(6)}))
opp = edge_union_coeff([(i, i + 3) for i in range(3)])


def patt(mask):
    return ''.join('1' if (mask >> i) & 1 else '0' for i in range(6))


def orbit_signature(coeff):
    out = {}
    for mask, c in coeff.items():
        oi = orbit_of[mask]
        key = (patt(min(z6[oi])), len(z6[oi]))
        out.setdefault(key, set()).add(c)
    return sorted((k[0], k[1], next(iter(v))) for k, v in out.items())


assert orbit_signature(adj) == [
    ('110000', 6, 1), ('110110', 3, -1), ('111000', 6, -1), ('111110', 6, 1), ('111111', 1, -2)
]
assert orbit_signature(d2) == [
    ('101000', 6, 1), ('101010', 2, -2), ('110110', 3, -1), ('111100', 6, -1), ('111110', 6, 2), ('111111', 1, -4)
]
assert orbit_signature(opp) == [
    ('100100', 3, 1), ('110110', 3, -1), ('111111', 1, 1)
]

# Exact negation search on reflection-symmetric sixth-power spectra
# lambda=(t0^6,t1^6,t2^6,t3^6,t2^6,t1^6), t_i in {1/3,2/3,1}.
grid = [Fraction(1, 3), Fraction(2, 3), Fraction(1)]
min_positive = None
checks = 0
for t0, t1, t2, t3 in product(grid, repeat=4):
    probs = exact_probs(t0 ** 6, t1 ** 6, t2 ** 6, t3 ** 6)
    p = t0 * t3 * t1 * t1 * t2 * t2
    bern = [p ** m.bit_count() * (1 - p) ** (6 - m.bit_count()) for m in range(64)]
    delta = [probs[m] - bern[m] for m in range(64)]
    for um in uz6:
        gap = sum((delta[m] for m in range(64) if (um >> orbit_of[m]) & 1), Fraction(0))
        assert gap >= 0
        if gap > 0 and (min_positive is None or gap < min_positive):
            min_positive = gap
        checks += 1

assert checks == 81 * 44
assert min_positive == Fraction(43, 68630377364883)

print('C0036 ORDER-6 ORBIT/COSSET EXACT SELF-CHECK')
print('Z6_SUBSET_ORBITS=14')
print('Z6_INVARIANT_UPSETS=44')
print('Z6_NONCARDINALITY_UPSETS=36')
print('S3_SUBSET_ORBITS=16')
print('S3_INVARIANT_UPSETS=76')
print('S3_NONCARDINALITY_UPSETS=68')
print('Z6_ADJACENT_IE=', orbit_signature(adj))
print('Z6_DISTANCE2_IE=', orbit_signature(d2))
print('Z6_ANTIPODAL_IE=', orbit_signature(opp))
print('EXACT_SIXTH_POWER_SPECTRA=81')
print('EXACT_INVARIANT_EVENT_CHECKS=3564')
print('NEGATIVE_GAPS=0')
print('SMALLEST_POSITIVE_GAP=', min_positive)
print('ALL_EXACT_CHECKS_PASS')
