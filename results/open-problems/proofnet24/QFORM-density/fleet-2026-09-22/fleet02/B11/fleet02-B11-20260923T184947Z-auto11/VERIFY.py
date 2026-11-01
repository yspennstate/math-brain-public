from decimal import Decimal, getcontext, ROUND_CEILING

# Conservative decimal envelopes used only to verify the displayed C_* < 13.
# pi < 3.141593, pi > 3.141592, log(2) < 0.693148,
# 2^(-1/2) < 0.707107.
getcontext().prec = 50
getcontext().rounding = ROUND_CEILING
pi_u = Decimal('3.141593')
pi_l = Decimal('3.141592')
log2_u = Decimal('0.693148')
r_u = Decimal('0.707107')
A = Decimal(2) + pi_u
B = Decimal(2) * pi_u * log2_u
N = 30
bump = Decimal('1e-45')
partial = Decimal(0)
for j in range(N):
    partial += (r_u ** j) * ((A + B * Decimal(j)).sqrt() + bump)

# For j=N+k, sqrt(A+B(N+k)) <= sqrt(A+BN)+sqrt(B) k, k>=0.
# Sum the resulting geometric and arithmetico-geometric tails.
C = (A + B * Decimal(N)).sqrt() + bump
sqrtB = B.sqrt() + bump
tail = (r_u ** N) * (C / (Decimal(1)-r_u)
        + sqrtB * r_u / (Decimal(1)-r_u) ** 2)
Cstar_upper = Decimal(1) / pi_l + partial + tail
pair_constant = Decimal(8) * (Decimal(2).sqrt().sqrt())
print('partial_upper_30 =', partial)
print('tail_upper =', tail)
print('Cstar_upper =', Cstar_upper)
print('pair_constant =', pair_constant)
assert Cstar_upper < Decimal(13)
assert pair_constant < Decimal('9.514')
print('QFORM_B11_RESIDUAL_SHEAR_CHECK_PASS')
