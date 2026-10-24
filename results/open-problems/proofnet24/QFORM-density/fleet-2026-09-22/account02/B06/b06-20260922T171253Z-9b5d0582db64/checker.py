from fractions import Fraction
import itertools
import sympy as sp

# Symbolic check for the zero-pivot three-coordinate normal form.
a,b,d,c,e = sp.symbols("a b d c e", real=True)
s2 = a*a+b*b
B = sp.Matrix([[0,a,b],[a,d,c],[b,c,e]])
S = sp.Matrix([[1,0,0],
               [0,a/s2,-b/s2],
               [0,b/s2, a/s2]])  # (x,u,v) -> (x,y,z)
Bt = sp.simplify(S.T*B*S)
assert sp.simplify(Bt[0,0]) == 0
assert sp.simplify(Bt[0,1]-1) == 0
assert sp.simplify(Bt[0,2]) == 0
assert sp.simplify(Bt.det()-B.det()/s2**2) == 0
assert sp.simplify(Bt[2,2] + B.det()/s2**2) == 0

# Exact delocalized heavy-isotropic frame adversary, m=8.
m = 8
u  = sp.Matrix([[sp.sqrt(6)/4, 0, sp.sqrt(6)/4]])
c1 = sp.Matrix([[sp.Rational(3,4),0,sp.Rational(-1,4)]])
c2 = sp.Matrix([[0,1,0]])
c3 = sp.Matrix([[sp.Rational(-1,4),0,sp.Rational(3,4)]])
rows = [u] + [c1/sp.sqrt(m) for _ in range(m)] \
           + [c2/sp.sqrt(m) for _ in range(m)] \
           + [c3/sp.sqrt(m) for _ in range(m)]
R = sp.Matrix.vstack(*rows)
Lam = sp.diag(1,1,-1)
A = sp.simplify(R*Lam*R.T)

assert sp.simplify(R.T*R-sp.eye(3)) == sp.zeros(3)
ell0 = sp.simplify(sum(x*x for x in R.row(0)))
assert ell0 == sp.Rational(3,4)
assert sp.simplify(A[0,0]) == 0
assert sp.simplify(A*R-R*Lam) == sp.zeros(1+3*m,3)

vals=[]
for k,l in itertools.combinations(range(1,1+3*m),2):
    det = sp.simplify(A.extract([0,k,l],[0,k,l]).det())
    vals.append(abs(det))
nz=[v for v in vals if v != 0]
assert len(nz) == 2*m*m
assert all(v == sp.Rational(3,8*m*m) for v in nz)
assert max(vals) == sp.Rational(3,8*m*m)
assert sp.simplify(sum(vals)) == sp.Rational(3,4)

print("PASS")
print("zero_pivot_transform_gamma =", sp.simplify(Bt[2,2]))
print("m =", m)
print("n =", 1+3*m)
print("heavy_leverage =", ell0)
print("A_00 =", A[0,0])
print("nonzero_triples_containing_0 =", len(nz))
print("max_abs_principal_3det_containing_0 =", max(vals))
print("sum_abs_principal_3det_containing_0 =", sp.simplify(sum(vals)))
print("nonzero_spectrum =", [1,1,-1])
