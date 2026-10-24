from fractions import Fraction

# Special N=2 block K_2 = C3 * C3 * Z, plus one involution.
p = Fraction(21, 100)
muC = 2 * (p + p*p - p**3)
muZ = 2*p / (1-p)
branch_margin = muC * (1 + 2*muZ) - 1
sqrt2_up = Fraction(99, 70)
A_up = 3 + 2*sqrt2_up
z = Fraction(50, 11)
root_margin = z + Fraction(6, 1)/z - A_up
gap = Fraction(11, 50) - Fraction(21, 100)

print('SPECIAL_N2')
print('mu_C(21/100)=', muC)
print('mu_Z(21/100)=', muZ)
print('branch_margin=', branch_margin, float(branch_margin))
print('sqrt2_upper=', sqrt2_up, 'square_margin=', sqrt2_up**2 - 2)
print('A_total_upper=', A_up)
print('z=', z, 'z2_minus_Q=', z*z - 6)
print('root_margin=', root_margin, float(root_margin))
print('certified_gap=', gap, float(gap))
assert branch_margin > 0
assert sqrt2_up**2 > 2
assert z*z > 6
assert root_margin > 0
assert gap == Fraction(1, 100)

# General finite symmetric supplement B of cardinality b.
# For N >= b+6, pc < 1/(2N-3) and pu > 1/(2N-4).
print('\nGENERAL_N_GE_B_PLUS_6')
for b in range(0, 101):
    for N in range(b+6, b+40):
        p0 = Fraction(1, 2*N - 3)
        branch_lb = (N-1) * 2*p0  # mu_C(p0) > 2p0
        assert branch_lb > 1
        D = 2*N + 2 + b
        Q = D - 1
        A = Fraction(N + b + 3, 1)
        z = Fraction(2*N - 4, 1)
        assert z*z > Q
        assert z + Fraction(Q, 1)/z > A
        g = Fraction(1, 2*N-4) - Fraction(1, 2*N-3)
        assert g == Fraction(1, (2*N-4)*(2*N-3))
print('verified exact inequalities for 0<=b<=100 and b+6<=N<b+40')

b, N = 1, 7
D = 2*N + 2 + b
print('\nB1_N7_COROLLARY')
print('degree=', D)
print('pc<', Fraction(1, 2*N-3))
print('pu>', Fraction(1, 2*N-4))
print('gap>', Fraction(1, (2*N-4)*(2*N-3)), float(Fraction(1, (2*N-4)*(2*N-3))))
print('ALL_EXACT_CHECKS_PASS')
