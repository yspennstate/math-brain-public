import math

CT = 759375.0/2.0
H0SQ = 1536.0*math.e**2
C5 = 2.0*math.sqrt(30.0*math.pi)
eta = 2.0/7.0
gap = 1.0 - 1.0/3.0 - 2.0*eta  # = 2/21
Ktau = CT/(H0SQ*gap**2)
B = 2.0*C5/3.0
a = 10.3
low = math.sqrt(a)
W = math.sqrt(Ktau/a**2 + B/a)
high = math.sqrt(eta)*W
frob = math.sqrt(1.0 + W**2)

assert abs(gap - 2.0/21.0) < 1e-15
assert Ktau < 3688.288
assert low < 3.21
assert high < 3.21
assert W < 6.002
assert frob < 6.085
assert C5 < 19.417

print('C5=', C5)
print('Ktau=', Ktau)
print('low_line_constant=', low)
print('high_line_constant=', high)
print('high_bank_frobenius_constant=', W)
print('small_residual_branch_constant=', frob)
print('QFORM_B13_R42_DIAG_TWOLINE_CHECK_PASS')
