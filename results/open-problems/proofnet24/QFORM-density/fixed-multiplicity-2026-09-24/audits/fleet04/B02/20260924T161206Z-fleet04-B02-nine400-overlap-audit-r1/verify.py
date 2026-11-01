from fractions import Fraction

kappa = Fraction(4, 625)
offdiag_sq = 9 * kappa
diag_sq = 2 - offdiag_sq
assert offdiag_sq == Fraction(36, 625)
assert Fraction(6, 25) ** 2 == offdiag_sq
assert diag_sq == Fraction(1214, 625)
assert float(diag_sq) == 1.9424
print("kappa =", kappa)
print("9*kappa =", offdiag_sq)
print("sqrt(9*kappa) = 6/25")
print("2-9*kappa =", diag_sq, "=", float(diag_sq))
