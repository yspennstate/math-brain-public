import sympy as sp

# 1. Two-dimensional congruence invariant used in the partner-theorem pullback.
x,y,z,w = sp.symbols('x y z w')
a,b,c = sp.symbols('a b c')
p1,p2 = sp.symbols('p1 p2')
L = sp.Matrix([[x,y],[z,w]])
A = sp.Matrix([[a,b],[b,c]])
p = sp.Matrix([p1,p2])
J = sp.Matrix([[0,-1],[1,0]])
v = L.T*p
Ap = L.T*A*L
assert sp.factor((J*v).dot(Ap*(J*v)) - L.det()**2*(J*p).dot(A*(J*p))) == 0

# 2. Selector-shear coefficient-volume determinant.
hs1,hs2,hr1,hr2 = sp.symbols('hs1 hs2 hr1 hr2')
T = sp.Matrix([
    [1,0,0,0],
    [hs1,hr1,1,0],
    [hs2,hr2,0,1],
])
assert sp.factor((T*T.T).det() - (1+hr1**2+hr2**2)) == 0

# 3. Affine range cancellation after Schur completion.
A11,A12,A22 = sp.symbols('A11 A12 A22')
C11,C12,C21,C22 = sp.symbols('C11 C12 C21 C22')
B11,B12,B22 = sp.symbols('B11 B12 B22')
w01,w02,v01,v02 = sp.symbols('w01 w02 v01 v02')
A2 = sp.Matrix([[A11,A12],[A12,A22]])
C2 = sp.Matrix([[C11,C12],[C21,C22]])
B2 = sp.Matrix([[B11,B12],[B12,B22]])
w0 = sp.Matrix([w01,w02])
v0 = sp.Matrix([v01,v02])
ell_w = A2*w0 + C2*v0
ell_v = C2.T*w0 + B2*v0
lhs = sp.simplify(ell_w - C2*B2.inv()*ell_v)
rhs = sp.simplify((A2-C2*B2.inv()*C2.T)*w0)
assert sp.simplify(lhs-rhs) == sp.zeros(2,1)

print('PASS')
print('congruence_invariant=det(L)^2 on quadratic factor, hence det(L)^4 after multiplying det N')
print('selector_gram_det=1+||h_R||^2')
print('affine_residual=Schur*w0')
