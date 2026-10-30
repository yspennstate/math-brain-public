from fractions import Fraction
import math

c = math.log(1.5)
near = 128 * (c**3 + 1.5*c**2 + 1.5*c + 0.75)
tail = 32.0
H3 = near + tail
Hnorm = H3 ** (1/3)
C0 = 2 ** (1/3) * Hnorm

assert H3 < 246
assert Hnorm < 6.266
assert C0 < 7.90

for b in (-3, -2, -1, 1, 2, 3):
    for d in (-2, -1, 0, 1, 2):
        for e in (-2, -1, 0, 1, 2):
            for c0 in (-3, -1, 0, 2, 4):
                kappa = Fraction(c0, 1) - Fraction(2*d*e, b)
                det = -b*b*c0 + 2*b*d*e
                assert Fraction(det, 1) == -Fraction(b*b, 1) * kappa

print(f"c={c:.15f}")
print(f"near_bound={near:.15f}")
print(f"tail_bound={tail:.15f}")
print(f"H3_bound={H3:.15f}")
print(f"Hnorm_bound={Hnorm:.15f}")
print(f"C0_bound={C0:.15f}")
print("determinant_identity_grid=PASS")
