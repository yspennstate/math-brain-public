import sympy as sp
from math import e

# Target spectrum used in Sections 4, 6, 7.
B1 = sp.Matrix([[1, 2], [2, 0]])
B2 = sp.Matrix([[1, 2], [2, 1]])
print('B1_eigenvalues=', sorted([sp.N(x, 15) for x in B1.eigenvals().keys()], key=float))
print('B2_eigenvalues=', sorted([sp.N(x, 15) for x in B2.eigenvals().keys()], key=float))

# Section 8: first Cauchy--Schwarz doubled low-rank matrix.
S = 2 * sp.eye(2)
R = sp.diag(0, 1)
O = sp.zeros(2)
M6 = sp.Matrix.vstack(
    sp.Matrix.hstack(O, S, -S),
    sp.Matrix.hstack(S.T, R, O),
    sp.Matrix.hstack(-S.T, O, -R),
)
print('M6_rank=', M6.rank())
print('M6_eigenvalues=', sorted([sp.N(x, 15) for x in M6.eigenvals().keys()], key=float))

# Explicit constants.
C_H = 3 * 2 ** (2/3)
C_partner_tau1 = 3 * 2 ** (1/6)
print('C_H=', format(C_H, '.12f'))
print('C_partner_tau1=', format(C_partner_tau1, '.12f'))

for m in (4, 8, 16, 32):
    rho = (1 - 1/m) ** 2
    C_grouped = 3 * e * (4 * rho) ** (-1/3)
    print(f'm={m} rho={rho:.12f} C_grouped={C_grouped:.12f}')

print('C_grouped_limit=', format(3 * e * 4 ** (-1/3), '.12f'))
print('PASS')
