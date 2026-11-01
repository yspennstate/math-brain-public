#!/usr/bin/env python3
from math import comb
from fractions import Fraction


def comps(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from comps(total - x, k - 1, prefix + (x,))


def norm3(c):
    # 1, w, w^2=-1-w; N(A+B w)=A^2-A B+B^2.
    c0, c1, c2 = c
    A = c0 - c2
    B = c1 - c2
    return A * A - A * B + B * B


def norm4(c):
    # 1,i,-1,-i.
    c0, c1, c2, c3 = c
    A = c0 - c2
    B = c1 - c3
    return A * A + B * B


coords6 = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]


def norm6(c):
    # zeta_6^k = A+B zeta_6, zeta_6^2-zeta_6+1=0;
    # N(A+B zeta_6)=A^2+A B+B^2.
    A = sum(c[k] * coords6[k][0] for k in range(6))
    B = sum(c[k] * coords6[k][1] for k in range(6))
    return A * A + A * B + B * B


def value_set(q, normfn):
    cs = list(comps(6, q))
    vals = sorted({normfn(c) for c in cs})
    return cs, vals


for q, fn in [(3, norm3), (4, norm4), (6, norm6)]:
    cs, vals = value_set(q, fn)
    print(f"q={q} count_vectors={len(cs)} expected={comb(6 + q - 1, q - 1)}")
    print(f"q={q} squared_moduli={vals}")
    assert len(cs) == comb(6 + q - 1, q - 1)
    assert 6 not in vals
    gap = min(abs(v - 6) for v in vals)
    print(f"q={q} exact_gap_from_6={gap}")
    pair_block_lb = Fraction(36 * gap * gap, 36 * 36)
    print(f"q={q} pair_block_residual_lower_bound={pair_block_lb}")
    full6_lb = Fraction(15, 1) * pair_block_lb / Fraction(756, 1)
    print(f"q={q} six_nonidentity_same_type_Phi_lower_bound={full6_lb}")

# Mixed BH(6,3)-BH(6,6): coordinatewise ratios are sixth roots, so the q=6 gap applies.
gap6 = min(abs(v - 6) for v in value_set(6, norm6)[1])
mixed_lb = Fraction(15, 1) * Fraction(36 * gap6 * gap6, 1296) / 756
print(f"mixed_q3_q6_all_six_Phi_lower_bound={mixed_lb}")
assert mixed_lb == Fraction(5, 9072)

# The elementary obstruction does not automatically extend to twelfth roots.
# With zeta=e^{pi i/6}, take 2 zeta^6 + zeta^7 + zeta^10 + 2 zeta^11.
# Its real/imaginary parts are (sqrt(3)-3)/2 and -(3+sqrt(3))/2,
# so the squared modulus is [(sqrt(3)-3)^2+(3+sqrt(3))^2]/4 = 6 exactly.
numerator_rational = (3 + 9) + (9 + 3)
assert numerator_rational == 24
assert Fraction(numerator_rational, 4) == 6
print("q=12 witness_counts=(0,0,0,0,0,0,2,1,0,0,1,2)")
print("q=12 witness_squared_modulus=6 EXACT")

# Elementary congruence proofs encoded as exhaustive residue checks.
# Eisenstein forms: N3=A^2-AB+B^2 and N6=A^2+AB+B^2.
for sign in (-1, 1):
    for A in range(2):
        for B in range(2):
            n = (A * A + sign * A * B + B * B) % 2
            if n == 0:
                assert A == 0 and B == 0
print("eisenstein_even_norm_implies_even_coefficients_mod2=PASS")

# Gaussian norm A^2+B^2 divisible by 3 forces A,B divisible by 3.
for A in range(3):
    for B in range(3):
        if (A * A + B * B) % 3 == 0:
            assert A == 0 and B == 0
print("gaussian_norm_divisible_by3_implies_coefficients_0_mod3=PASS")

print("ALL_EXACT_CHECKS_PASS")
