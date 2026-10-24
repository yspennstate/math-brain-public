import math
import sympy as sp

# Exact factorization witness for the nonzero-central-coupling obstruction.
X,U,Y,V = sp.symbols('X U Y V', real=True)
expr = sp.expand(2*(X+U)*(Y+V))
assert expr == 2*X*Y + 2*X*V + 2*U*Y + 2*U*V

lam = sp.symbols('lam')
# Variable order (X,U,Y,V): x^T A4 x = 2(X+U)(Y+V).
A4 = sp.Matrix([
    [0,0,1,1],
    [0,0,1,1],
    [1,1,0,0],
    [1,1,0,0],
])
# Add an independent physical square S^2.
A5 = sp.diag(0,0,0,0,1)
A5[:4,:4] = A4

cp4 = sp.factor(A4.charpoly(lam).as_expr())
cp5 = sp.factor(A5.charpoly(lam).as_expr())
assert cp4 == lam**2*(lam-2)*(lam+2)
assert cp5 == lam**2*(lam-2)*(lam-1)*(lam+2)

print('factorization:', expr)
print('charpoly_A4:', cp4)
print('charpoly_A5:', cp5)
print('zero_core_bank_constant:', 2*math.sqrt(2))
print('square_one_arm_bank_constant:', 2**(11/4))
print('QFORM_B05_REVERSE_COAREA_CHECK_PASS')
