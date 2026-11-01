import sympy as sp

# Generic four-coordinate map determinants.
a11,a12,a13,a14,a22,a23,a24,a33,a34,a44,s=sp.symbols(
    'a11 a12 a13 a14 a22 a23 a24 a33 a34 a44 s')
B=sp.Matrix([[a11,a12,a13,a14],
             [a12,a22,a23,a24],
             [a13,a23,a33,a34],
             [a14,a24,a34,a44]])
C=B.extract([0,1],[2,3])
T12=sp.Matrix([
    [1,0,0,0],
    [s*a11,s*a12,s*a13,s*a14],
    [0,1,0,0],
    [s*a12,s*a22,s*a23,s*a24],
])
T34=sp.Matrix([
    [0,0,1,0],
    [s*a13,s*a23,s*a33,s*a34],
    [0,0,0,1],
    [s*a14,s*a24,s*a34,s*a44],
])
assert sp.simplify(T12.det()+s**2*C.det())==0
assert sp.simplify(T34.det()+s**2*C.det())==0

# The naive three-map L2 BL kernels are always dependent for symmetric B.
b12,b13,b23=sp.symbols('b12 b13 b23')
k1=sp.Matrix([0,-b13,b12])
k2=sp.Matrix([b23,0,-b12])
k3=sp.Matrix([-b23,b13,0])
assert k1+k2+k3==sp.zeros(3,1)

# Exact fleet02/B03 Walsh target family.
t=sp.symbols('t', positive=True)
H2=sp.Matrix([[1,1],[1,-1]])
H8=sp.kronecker_product(sp.kronecker_product(H2,H2),H2)
R=H8[:,0:3]/sp.sqrt(8)
P=sp.simplify(R*R.T)
A=sp.simplify(t*sp.eye(8)+(1-t)*P)
d=sp.factor(A[0,0])
idx=list(range(1,8))
v=A.extract(idx,[0])
S=sp.simplify(A.extract(idx,idx)-(v*v.T)/d)
# one-based residual I={2,3}, J={4,6}: local [0,1] and [2,4]
delta_signed=sp.factor(S.extract([0,1],[2,4]).det())
expected=-(1-t)**2*(1+t)/(4*(5*t+3))
assert sp.simplify(delta_signed-expected)==0
D3=sp.factor(d*delta_signed)
assert sp.simplify(D3+(1-t)**2*(1+t)/32)==0

# Exact endpoint constant on 0<t<=1/2.
Delta=-delta_signed
F=sp.simplify(4*sp.sqrt(2)*d**(-sp.Rational(1,2))*Delta**(-sp.Rational(1,4)))
root=(-7+sp.sqrt(89))/20
assert 0 < float(root) < 0.5
F0=sp.simplify(F.subs(t,0))
Fhalf=sp.simplify(F.subs(t,sp.Rational(1,2)))
assert sp.N(Fhalf-F0)>0
expected_half=32*sp.sqrt(2)/33**sp.Rational(1,4)
assert sp.simplify(Fhalf-expected_half)==0

print('generic_map_det_ratio_T12 =', sp.simplify(T12.det()/(s**2*C.det())))
print('generic_map_det_ratio_T34 =', sp.simplify(T34.det()/(s**2*C.det())))
print('three_kernel_sum =', list(k1+k2+k3))
print('walsh_pivot_d =', d)
print('walsh_residual_cross_det =', delta_signed)
print('walsh_overlap_one_3minor =', D3)
print('critical_root =', root, float(root))
print('bound_at_t0 =', sp.simplify(F0), float(F0))
print('bound_at_t1_2 =', Fhalf, float(Fhalf))
print('QFORM_B03_UNNORMALIZED_SLICE_PASS')
