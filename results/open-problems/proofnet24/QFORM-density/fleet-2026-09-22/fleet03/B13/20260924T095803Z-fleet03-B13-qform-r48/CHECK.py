from fractions import Fraction
from math import e, sqrt

pivot = Fraction(1024, 1) / (Fraction(2, 3) * Fraction(7, 8) * Fraction(6144, 1))
assert pivot == Fraction(2, 7)

cancel = Fraction(7, 8) - Fraction(2, 7) - Fraction(1, 8)
assert cancel == Fraction(13, 28)

offdiag = cancel - Fraction(1, 16)
assert offdiag == Fraction(45, 112)

detgap = offdiag**2 - Fraction(2, 7)**2
assert detgap == Fraction(1001, 12544)

sigmagap = offdiag - Fraction(2, 7)
assert sigmagap == Fraction(13, 112)

H = sqrt(1536 * e**2)
sqrtH = sqrt(H)
rho0 = 8 * sqrtH
ultra = sqrt(6144 * e**2)

print('QFORM_B13_R48_INDEFPAIR_CHECK_PASS')
print('pivot=', pivot)
print('cancel=', cancel)
print('offdiag=', offdiag)
print('detgap=', detgap, float(detgap))
print('sigmagap=', sigmagap, float(sigmagap))
print('sqrtH=', format(sqrtH, '.15f'))
print('rho0=', format(rho0, '.15f'))
print('ultra_lambda2_const=', format(ultra, '.15f'))
