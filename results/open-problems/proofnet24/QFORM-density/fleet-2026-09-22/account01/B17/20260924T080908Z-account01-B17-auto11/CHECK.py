import sympy as sp
from mpmath import mp

mp.dps = 50
R0 = sp.Matrix([
    [1,1,1],
    [1,-1,1],
    [1,1,-1],
    [1,-1,-1],
]) / 2
n = sp.Matrix([1,2,3]) / sp.sqrt(14)
B = sp.eye(3) - 2*n*n.T
M = sp.simplify(R0*B*R0.T)

assert sp.simplify(R0.T*R0) == sp.eye(3)
assert sp.simplify(B*B) == sp.eye(3)
lam = sp.symbols('lambda')
assert sp.factor(B.charpoly(lam).as_expr()) == (lam-1)**2*(lam+1)
assert all(x != 0 for x in M)
assert max(abs(x) for x in M) == sp.Rational(3,4)
assert all(sp.simplify((R0.row(i)*R0.row(i).T)[0]) == sp.Rational(3,4) for i in range(4))

# The tetrahedral Poisson jump law has minimum nonzero norm sqrt(3)/2:
# every row has first coordinate 1/2.  One jump has norm sqrt(3)/2;
# two or more jumps have first coordinate >=1.
row_norm_sq = sp.simplify((R0.row(0)*R0.row(0).T)[0])
assert row_norm_sq == sp.Rational(3,4)

C0 = 3*mp.sqrt(2)
C1 = 12*mp.e**(-mp.mpf('0.5'))/mp.sqrt(2*mp.pi)
C9 = mp.e**(-mp.mpf('4.5'))*C0 + (1-mp.e**(-mp.mpf('4.5')))*C1
Ctet = mp.e**(-4)*C0 + (1-mp.e**(-4))*C9
assert Ctet < mp.pi < C0

print('QFORM_B17_INF_TARRAY_MIXED_FRAME_CHECK_PASS')
print('R0BR0T =', M)
print('C0 =', mp.nstr(C0, 40))
print('C1 =', mp.nstr(C1, 40))
print('C9 =', mp.nstr(C9, 40))
print('Ctet =', mp.nstr(Ctet, 40))
