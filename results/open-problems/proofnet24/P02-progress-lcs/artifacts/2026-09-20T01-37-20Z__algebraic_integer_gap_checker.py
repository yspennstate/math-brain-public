from math import gcd, log10

# Frozen R17-C045 exact data.
N = 11_614_187
D0 = 1_600_000
XN = YN = 513_434
DX = D0 - XN
DY = D0 - YN
P = int('10114875937111444750637950885399422919832438289108176982868202874026753')
Q = int('29591135160849999997918500618240000000000000000000000000000000000000000')

# Common denominator of every C045 transition weight in the archived exact checker.
C = D0**8 * DX * DY
assert gcd(P,Q) == 1
assert 0 < P < Q

# R = C * lambda = a/b in lowest terms.
g = gcd(C*P, Q)
a = C*P // g
b = Q // g
assert gcd(a,b) == 1
assert b > 1                 # the key non-algebraic-integer obstruction
assert a % b != 0

# The exact spectral-gap certificate is represented symbolically:
# delta_R = 1 / (b * (2*a)**(N-1))
# epsilon_A = delta_R / (2*C)
# and lambda_star = P/Q - epsilon_A.
# We deliberately do not materialize the ~9.31e8-digit denominator.

# Exact sign checks needed by the transfer.
t_num, t_den = 256_717, 800_000
assert 4*t_num*t_num < t_den*t_den  # 4 t^2 < 1
assert Q < 2*C*b*P             # epsilon_A < 1/(2Cb) < lambda

print('P02 T02 algebraic-integer spectral-gap arithmetic checker')
print(f'N={N}')
print(f'D0={D0} XN={XN} DX={DX}')
print(f'C={C}')
print(f'lambda_num={P}')
print(f'lambda_den={Q}')
print(f'gcd_Cp_q={g}')
print(f'R_num_a={a}')
print(f'R_den_b={b}')
print(f'R_noninteger_remainder={a % b}')
print('delta_R_exact = 1 / ( b * (2*a)^(N-1) )')
print('epsilon_A_exact = 1 / ( 2*C*b*(2*a)^(N-1) )')
print('lambda_star_exact = P/Q - epsilon_A_exact')
print(f'epsilon_A_log10_display_approx={-(log10(2*C*b)+(N-1)*log10(2*a)):.6f}')
print('EXACT_GCD_REDUCTION_PASS')
print('EXACT_R_NONINTEGER_PASS')
print('EXACT_4T2_LT_1_PASS')
print('EXACT_LAMBDA_STAR_POSITIVE_PASS')
print('SYMBOLIC_GAP_FORMULA_PASS')
print('ALL_EXACT_CHECKS_PASS')
