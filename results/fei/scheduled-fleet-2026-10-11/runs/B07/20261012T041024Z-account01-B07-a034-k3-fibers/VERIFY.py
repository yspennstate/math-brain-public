#!/usr/bin/env python3
"""Exact census for the B07 K3 fiber classification.

All arithmetic is integral.  A truth table is a vector f on F_2^3 with
entries +/-1.  We store a_T = (1/2) sum_y f(y)(-1)^{T.y}, so g_T=a_T/4.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


PTS = list(product((0, 1), repeat=3))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) & 1


def wt(a):
    return sum(a)


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def rank_f2(vectors):
    rows = [sum(bit << i for i, bit in enumerate(v)) for v in vectors]
    rank = 0
    for col in range(3):
        pivot = next((j for j in range(rank, len(rows)) if (rows[j] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for j in range(len(rows)):
            if j != rank and ((rows[j] >> col) & 1):
                rows[j] ^= rows[rank]
        rank += 1
    return rank


def affine_plane(supp):
    if len(supp) != 4:
        return False
    base = supp[0]
    diffs = {xor(x, base) for x in supp}
    # A four-point set is an affine 2-flat iff its translate is a
    # two-dimensional linear subspace, equivalently it is xor-closed.
    return len(diffs) == 4 and rank_f2(list(diffs)) == 2 and all(
        xor(u, v) in diffs for u in diffs for v in diffs
    )


def walsh_numerators(f):
    return [sum(f[i] * (-1 if dot(T, y) else 1) for i, y in enumerate(PTS)) // 2 for T in PTS]


counts = Counter()
plane_weight_sums = Counter()
major_counts = Counter()

for bits in product((-1, 1), repeat=8):
    a = walsh_numerators(bits)
    assert sum(x*x for x in a) == 16
    parities = {x & 1 for x in a}
    assert len(parities) == 1
    mags = tuple(sorted((abs(x) for x in a), reverse=True))
    if mags == (4,0,0,0,0,0,0,0):
        typ = "character"
        major = PTS[next(i for i,x in enumerate(a) if abs(x)==4)]
        # J_A = sum |T| g_T^2 = |major|.
        assert sum(wt(T)*a[i]*a[i] for i,T in enumerate(PTS)) == 16*wt(major)
    elif mags == (3,1,1,1,1,1,1,1):
        typ = "point_defect"
        major = PTS[next(i for i,x in enumerate(a) if abs(x)==3)]
        major_counts[wt(major)] += 1
        # 16 J_A = 12 + 8|major|.
        assert sum(wt(T)*a[i]*a[i] for i,T in enumerate(PTS)) == 12 + 8*wt(major)
    elif mags == (2,2,2,2,0,0,0,0):
        typ = "semibent"
        supp = [PTS[i] for i,x in enumerate(a) if x]
        assert affine_plane(supp)
        assert __import__('math').prod(a[i] // 2 for i,x in enumerate(a) if x) == -1
        sw = sum(wt(T) for T in supp)
        assert sw in (4,6,8)
        plane_weight_sums[sw] += 1
        # 16 J_A = 4 sum_{T in supp}|T|.
        assert sum(wt(T)*a[i]*a[i] for i,T in enumerate(PTS)) == 4*sw
    else:
        raise AssertionError((bits, a, mags))
    counts[typ] += 1

assert counts == Counter(character=16, point_defect=128, semibent=112)
assert sum(plane_weight_sums.values()) == 112
assert sum(major_counts.values()) == 128

# Exact check of the general-k point-defect address charge (equation (5))
# for k <= 8, every major character and a fixed flipped point.  Translation
# of the flipped point changes phases but not squared coefficients.
general_k_checks = 0
for k in range(1, 9):
    cube = list(product((0, 1), repeat=k))
    for D in cube:
        vals = [(-1 if dot(D, y) else 1) for y in cube]
        vals[0] *= -1
        coeff = []
        for T in cube:
            coeff.append(Fraction(sum(vals[i] * (-1 if dot(T, y) else 1)
                                      for i, y in enumerate(cube)), 2**k))
        energy = sum(Fraction(sum(T)) * c*c for T, c in zip(cube, coeff))
        target = Fraction(k, 2**(k-1)) + (1-Fraction(1, 2**(k-2))) * sum(D) if k >= 2 else Fraction(k, 1)
        # For k=1 the correction coefficient is -1 and the flipped character
        # is another character; use the direct general formula as written.
        if k == 1:
            target = Fraction(k, 2**(k-1)) + (1-Fraction(4, 2**k))*sum(D)
        assert energy == target, (k, D, energy, target)
        general_k_checks += 1

print("K3_FIBER_CENSUS_PASS")
print("type_counts", dict(counts))
print("semibent_support_weight_sums", dict(sorted(plane_weight_sums.items())))
print("point_defect_major_weight_counts", dict(sorted(major_counts.items())))
print("checked_truth_tables", 256)
print("general_k_point_defect_energy_checks", general_k_checks, "for k=1..8")
print("all_integer_parseval_parity_affine_support_energy_checks_passed", True)
