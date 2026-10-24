from fractions import Fraction as Q

# Exact-arithmetic self-check for R09 / G0013.
# This verifies the rational finite core of the D4/one-dimensional-relaxation
# obstruction in the accompanying report.  It is a SELF-CHECK ONLY, not an
# independent audit and not a copula/Brenier-map construction.

c = Q(8, 3)
m_star = Q(5, 12)

# For A(t)=c*m(t), m(t)=min(t,1-t), the one-sided scalar box obstacle has
# h_min=(a-2m)^3/[12(6m-a)] = m^2/135 up to m=5/12.
h_one_coeff = (c - 2) ** 3 / (12 * (6 - c))
assert h_one_coeff == Q(1, 135)
assert h_one_coeff < Q(1, 40)

# On the two-sided tail m in [5/12,1/2], proving h_min <= m^2/40 reduces,
# after a positive square, to P(m)>=0, where
# P(m)=20/3-12m-m(6-(1747/180)m)^2.
# Its derivative is exactly -(1747m-720)^2/10800 <= 0, so the minimum is
# P(1/2)=2231/259200>0.
d = Q(1747, 180)
P = [Q(20, 3), Q(-48), Q(12) * d, -d * d]  # ascending coefficients
Pprime = [P[i] * i for i in range(1, len(P))]
derivative_square = [
    -Q(720 * 720, 10800),
    Q(2 * 1747 * 720, 10800),
    -Q(1747 * 1747, 10800),
]
assert Pprime == derivative_square

def peval(coeffs, x):
    out = Q(0)
    for a in reversed(coeffs):
        out = out * x + a
    return out

assert peval(P, Q(1, 2)) == Q(2231, 259200) > 0

# Exact integrals for the symmetric two-family relaxation witness
# A_1=A_2=(8/3)m(t), h_1=h_2=m(t)^2/40.
# int m = 1/4 and int m^2 = 1/12 on [0,1].
int_m = Q(1, 4)
int_m2 = Q(1, 12)
H = int_m2 / 40
I = (c * c / 12) * int_m2 + H
rho = c * int_m
S = 2 * I

assert H == Q(1, 480)
assert I == Q(667, 12960)
assert rho == Q(2, 3)
assert S == Q(667, 6480)

# Both inherited Jacobi inequalities coincide for the symmetric witness.
jacobi_lhs = 3 * I + 4 * H
jacobi_margin = Q(1, 6) - jacobi_lhs
assert jacobi_lhs == Q(703, 4320)
assert jacobi_margin == Q(17, 4320) > 0

# Strengthened D4 budget: |rho_1|+|rho_2|+6S <= 2.
d4_lhs = 2 * rho + 6 * S
d4_margin = Q(2) - d4_lhs
assert d4_lhs == Q(2107, 1080)
assert d4_margin == Q(53, 1080) > 0

# Yet the relaxation witness lies strictly above the conjectured source value.
source_gap = S - Q(1, 10)
assert source_gap == Q(19, 6480) > 0

# Pointwise variance stays below the Bernoulli variance m(1-m):
# Var = (667/1080)m^2, and it suffices to check m=1/2.
var_coeff = Q(667, 1080)
assert var_coeff * Q(1, 2) < Q(1, 2)

print('h_one_coeff =', h_one_coeff)
print('tail_P_half =', peval(P, Q(1, 2)))
print('H =', H, float(H))
print('I_each =', I, float(I))
print('rho_each =', rho, float(rho))
print('S_relax =', S, float(S))
print('S_relax_minus_1/10 =', source_gap, float(source_gap))
print('jacobi_lhs =', jacobi_lhs, 'margin =', jacobi_margin)
print('D4_lhs =', d4_lhs, 'margin =', d4_margin)
print('SELF_CHECK_ONLY / PASS')
