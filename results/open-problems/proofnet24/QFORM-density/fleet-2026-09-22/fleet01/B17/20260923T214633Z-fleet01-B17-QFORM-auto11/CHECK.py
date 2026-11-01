import sympy as sp

R = sp.Matrix([[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]])/2
k = sp.Matrix([1,-1,-1,1])/2
n = sp.Matrix([7,18,18])/sp.sqrt(697)
B = sp.eye(3)-2*n*n.T
A = sp.simplify(R*B*R.T)
P = sp.simplify(R*R.T)
A_expected = sp.Matrix([
[-1607,95,95,1797],
[95,1993,-795,1103],
[95,-795,1993,1103],
[1797,1103,1103,409]])/2788
P_expected = sp.Matrix([
[3,1,1,-1],[1,3,-1,1],[1,-1,3,1],[-1,1,1,3]])/4
assert R.T*R == sp.eye(3)
assert R.T*k == sp.zeros(3,1)
assert (k.T*k)[0] == 1
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert sp.trace(B)==1 and sp.det(B)==-1
assert A == A_expected
assert P == P_expected
assert all(A[i,j] != 0 for i in range(4) for j in range(4))
assert sp.simplify(A**3-A) == sp.zeros(4)
assert A.rank()==3 and sp.trace(A)==1 and sp.trace(A*A)==3

# For m>=7, all entries of A_m^0 +/- m^-2(I-P_m) stay nonzero.
assert sp.Rational(95)*7**2 > sp.Rational(3,4)*2788
assert 409*7 > 2788

# Partner concrete two-fragment application: Delta=120/sqrt(2)=60sqrt(2)>84.
assert 7200 > 84**2
assert 140**2 < 18*33**2

sigma2 = sp.Rational(1,12)
p0 = sp.simplify(1/(2*sp.sqrt(2)*sigma2))
assert p0 == 3*sp.sqrt(2)
print('QFORM_B17_FULLRANK_ESCAPED_SUPPORT_CHECK_PASS')
print('Astar=', A)
print('Pstar=', P)
print('gaussian_peak=', p0)
