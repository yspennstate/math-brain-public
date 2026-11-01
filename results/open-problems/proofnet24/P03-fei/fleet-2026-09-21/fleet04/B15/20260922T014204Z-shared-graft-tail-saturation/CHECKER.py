from fractions import Fraction as F
from decimal import Decimal, getcontext

# Exact tail checker for the fleet03/B15 iterated shared-core recurrence.
# It consumes the certified F2 exact influence and F6 ratio interval from
# fleet03/B15/20260922T012556Z-iterated-shared-graft.

getcontext().prec = 100
ALPHA = F(9, 256)
ISRC = F(261, 128)
B = F(257, 256)
KMAX = F(153, 16)  # H_core <= 9 and alpha*16 = 9/16.

I = F(784028312243315011737, 295147905179352825856)  # I(F2), exact.
for idx in range(3, 7):
    I = ISRC + ALPHA * (I**4 - 1)
I6 = I
assert I6 > 10**8

# Denominator of the F6 -> F7 ratio increment.
D6 = ALPHA * I6**4 + B

# For all later rounds, I >= 16/3 implies I_next >= I^2, hence the
# successive increment denominators grow by at least a factor 2.
# The positive part of any increment is <= KMAX / D_r. Therefore the
# total possible future increase after F6 is <= 2*KMAX/D6.
TAIL = (2 * KMAX) / D6
assert TAIL < F(5213, 10**33)  # < 5.213e-30

R6_LO = F('6.521850949550448184840160538860511501288648868305895469222543106356953492372764166124613916792207343')
R6_HI = F('6.521850949550448184840160538860511501288648871643878248179449753729219561943695052658106144512794690')
FAMILY_SUP_UPPER = R6_HI + TAIL
assert FAMILY_SUP_UPPER < F('6.5218509495504481848401605388657245013')

C0 = F('6.4548')
MARGIN_FLOOR = 4 * (R6_LO - C0)


def dec(q: F, digits: int = 90) -> str:
    getcontext().prec = digits + 15
    return format(Decimal(q.numerator) / Decimal(q.denominator), f'.{digits}g')


print('PASS')
print('I6_gt_1e8=True')
print('D6=' + dec(D6))
print('future_positive_tail_upper=' + dec(TAIL))
print('fixed_family_sup_lower=' + dec(R6_LO))
print('fixed_family_sup_upper=' + dec(FAMILY_SUP_UPPER))
print('old_reference_scalar_margin_floor=' + dec(MARGIN_FLOOR))
print('full_FEI_status=OPEN')
