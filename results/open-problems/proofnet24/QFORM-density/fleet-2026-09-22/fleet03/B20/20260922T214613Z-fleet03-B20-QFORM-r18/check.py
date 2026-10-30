from fractions import Fraction

m = Fraction(3501, 8000)

# Triple-determinant branch: 128*(m^2*3/256)^(-1/4) < 589.
assert Fraction(128**4, 1) < Fraction(589**4, 1) * m * m * Fraction(3, 256)

# Sequential-two-pivot branch: elementary inequalities used for the safe <96 bound.
assert m > Fraction(7, 16)
assert Fraction(2, 7) < Fraction(15, 28)**2       # sqrt(2/7) < 15/28
assert Fraction(25, 8) < Fraction(81, 25)         # 5/(2sqrt(2)) < 9/5

print("QFORM_B20_R18_CHECK_PASS")
