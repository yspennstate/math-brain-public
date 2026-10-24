import itertools
import sympy as sp

M = sp.symbols('M', positive=True)
v = sp.Matrix([sp.Rational(1,2)]*4)
w = sp.Matrix([sp.Rational(1,2), sp.Rational(1,2), -sp.Rational(1,2), -sp.Rational(1,2)])
A = sp.eye(4) - (M+1)*(v*v.T) - sp.Rational(3,2)*(w*w.T)

u1 = sp.Matrix([1,-1,0,0])
u2 = sp.Matrix([0,0,1,-1])
assert A*v == -M*v
assert A*w == -sp.Rational(1,2)*w
assert A*u1 == u1
assert A*u2 == u2

d = sp.factor(A[0,0])
s = sp.factor(A[0,1])
o = sp.factor(A[0,2])
assert sp.factor(d-s) == 1
assert sp.factor(d+s) == -(2*M+1)/4
assert sp.factor(d-o) == sp.Rational(1,4)
assert sp.factor(d+o) == (1-M)/2

B = A.extract([0,1,2],[0,1,2])
lam = sp.symbols('lambda')
cp = sp.factor(B.charpoly(lam).as_expr())
assert cp == sp.factor((lam-1)*(8*lam**2+(6*M-1)*lam-1)/8)
assert sp.factor(B.det()) == -sp.Rational(1,8)

M2 = sp.Integer(0)
M3 = sp.Integer(0)
minor_counts = {}
for I in itertools.combinations(range(4),3):
    for J in itertools.combinations(range(4),3):
        det = sp.factor(A.extract(I,J).det())
        r = len(set(I)&set(J))
        minor_counts[(r,det)] = minor_counts.get((r,det),0)+1
        if r == 2:
            M2 += det**2
        elif r == 3:
            M3 += det**2

M2 = sp.factor(M2)
M3 = sp.factor(M3)
eigs = [sp.Integer(1), sp.Integer(1), -sp.Rational(1,2), -M]
e3A2 = sp.factor(sum((a*b*c)**2 for a,b,c in itertools.combinations(eigs,3)))
assert M3 == sp.Rational(1,16)
assert M2 == sp.factor(3*(8*M**2+1)/16)
assert sp.factor(M2+M3-e3A2) == 0
assert minor_counts[(3,-sp.Rational(1,8))] == 4
assert minor_counts[(2,(4*M+1)/8)] == 4
assert minor_counts[(2,(2*M-1)/8)] == 4
assert minor_counts[(2,-(2*M-1)/8)] == 4

rho = sp.simplify(2/(sp.sqrt((6*M-1)**2+32)+(6*M-1)))
print('PASS')
print('charpoly=', cp)
print('rho=', rho)
print('M3=', M3)
print('M2=', M2)
print('e3(A^2)=', e3A2)
