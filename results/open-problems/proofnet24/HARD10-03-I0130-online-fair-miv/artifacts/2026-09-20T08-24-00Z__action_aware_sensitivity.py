from fractions import Fraction as F

S = 202391574968484000000000
Q = 4870886400
P1 = 21454951
G1 = F(2320006002124622963165232172483642250245228391, 105941779200)

# Certified exact continuous actions from the preceding immutable report.
b_root = F(462779651166897045103043986972930783,
           463474350810274668871680000000000000)
b_inner = F(57956185151311377325530313,
            58148415346982400000000000)

# After the exact-MIV prefix, a longest nested path has at most:
# root + inner + 416 generated + 612 old654 = 1030 reward-bearing goods.
# The two explicit continuous goods have exact |d reward/dP| = 76800*S*b,
# while each remaining structural/old654 good has max(a,b) <= 1 and hence
# |d reward/dP| <= 76800*S. The physical threshold derivative is 230400*S.
C_old = F(79334400, 1)
C_new = F(230400, 1) + F(76800, 1) * (F(1028, 1) + b_root + b_inner)
assert C_new < C_old

eta_old = G1 / (F(S, 1) * C_old)
eta_new = G1 / (F(S, 1) * C_new)
assert eta_new > eta_old

U_old = F(9,10) - (F(P1,1) + eta_old) / F(Q,1)
U_new = F(9,10) - (F(P1,1) + eta_new) / F(Q,1)
W_new = U_new - F(19,30)
assert U_new < U_old

# Cross-check inherited endpoint exactly.
U_old_expected = F(
22974092575376445790975264528190846585875386237683,
25652323754312700812535643741618176000000000000000)
assert U_old == U_old_expected

print('I0130_ACTION_AWARE_SENSITIVITY_PASS')
for k,v in [
    ('b_root', b_root), ('b_inner', b_inner),
    ('C_old', C_old), ('C_new', C_new),
    ('eta_old', eta_old), ('eta_new', eta_new),
    ('U_old', U_old), ('U_new', U_new), ('W_new', W_new),
    ('U_improvement', U_old-U_new)]:
    print(f'{k}={v.numerator}/{v.denominator}')
print('eta_new_decimal=%.18f' % float(eta_new))
print('U_new_decimal=%.18f' % float(U_new))
print('W_new_decimal=%.18f' % float(W_new))
print('U_improvement_decimal=%.18e' % float(U_old-U_new))
